# pylint: skip-file
import errno
import os
import types

from app._compat import import_string
from app._compat import iteritems
from app._compat import string_types
from etc.config import ROOT

# avoid use os.getcwd(), because process may cd different working directory
STATIC_ROOT = os.path.join(ROOT, "misc/static")
ENV = os.environ.get('ENV', 'local')
CONF_DIR = os.path.join(ROOT, 'settings')


class Config(dict):
    """Works exactly like a dict but provides ways to fill it from files
    or special dictionaries.  There are two common patterns to populate the
    config.

    Either you can fill the config from a config file::

        config.from_pyfile('yourconfig.cfg')

    Or alternatively you can define the configuration options in the
    module that calls :meth:`from_object` or provide an import path to
    a module that should be loaded.  It is also possible to tell it to
    use the same module and with that provide the configuration values
    just before the call::

        DEBUG = True
        SECRET_KEY = 'development key'
        config.from_object(__name__)

    In both cases (loading from any Python file or loading from modules),
    only uppercase keys are added to the config.  This makes it possible to use
    lowercase values in the config file for temporary values that are not added
    to the config or to define the config keys in the same file that implements
    the application.

    :param root_path: path to which files are read relative from.  When the
                      config object is created by the application.
    :param defaults: an optional dictionary of default values
    """

    def __init__(self, root_path, defaults=None):
        dict.__init__(self, defaults or {})
        self.root_path = root_path

    def from_pyfile(self, filename, silent=False):
        """Updates the values in the config from a Python file.  This function
        behaves as if the file was imported as module with the
        :meth:`from_object` function.

        :param filename: the filename of the config.  This can either be an
                         absolute filename or a filename relative to the
                         root path.
        :param silent: set to ``True`` if you want silent failure for missing
                       files.
        """
        filename = os.path.join(self.root_path, filename)
        d = types.ModuleType("config")
        d.__file__ = filename
        try:
            with open(filename, mode="rb") as config_file:
                exec(compile(config_file.read(), filename, "exec"), d.__dict__)
        except IOError as e:
            if silent and e.errno in (errno.ENOENT, errno.EISDIR, errno.ENOTDIR):
                return False
            e.strerror = "Unable to load configuration file (%s)" % e.strerror
            raise
        self.from_object(d)
        return True

    def from_object(self, obj):
        """Updates the values from the given object.  An object can be of one
        of the following two types:

        -   a string: in this case the object with that name will be imported
        -   an actual object reference: that object is used directly

        Objects are usually either modules or classes. :meth:`from_object`
        loads only the uppercase attributes of the module/class. A ``dict``
        object will not work with :meth:`from_object` because the keys of a
        ``dict`` are not attributes of the ``dict`` class.

        Example of module-based configuration::

            config.from_object('yourapplication.default_config')
            from yourapplication import default_config
            config.from_object(default_config)

        Nothing is done to the object before loading. If the object is a
        class and has ``@property`` attributes, it needs to be
        instantiated before being passed to this method.

        You should not use this function to load the actual configuration but
        rather configuration defaults.  The actual config should be loaded
        with :meth:`from_pyfile` and ideally from a location not within the
        package because the package might be installed system wide.

        See :ref:`config-dev-prod` for an example of class-based configuration
        using :meth:`from_object`.

        :param obj: an import name or object
        """
        if isinstance(obj, string_types):
            obj = import_string(obj)
        for key in dir(obj):
            if key.isupper():
                self[key] = getattr(obj, key)

    def get_namespace(self, namespace, lowercase=True, trim_namespace=True):
        """Returns a dictionary containing a subset of configuration options
        that match the specified namespace/prefix. Example usage::

            config['IMAGE_STORE_TYPE'] = 'fs'
            config['IMAGE_STORE_PATH'] = '/var/app/images'
            config['IMAGE_STORE_BASE_URL'] = 'http://img.website.com'
            image_store_config = config.get_namespace('IMAGE_STORE_')

        The resulting dictionary `image_store_config` would look like::

            {
                'type': 'fs',
                'path': '/var/app/images',
                'base_url': 'http://img.website.com'
            }

        This is often useful when configuration options map directly to
        keyword arguments in functions or class constructors.

        :param namespace: a configuration namespace
        :param lowercase: a flag indicating if the keys of the resulting
                          dictionary should be lowercase
        :param trim_namespace: a flag indicating if the keys of the resulting
                          dictionary should not include the namespace

        .. versionadded:: 0.11
        """
        rv = {}
        for k, v in iteritems(self):
            if not k.startswith(namespace):
                continue
            if trim_namespace:
                key = k[len(namespace):]
            else:
                key = k
            if lowercase:
                key = key.lower()
            rv[key] = v
        return rv

    def __repr__(self):
        return "<%s %s>" % (self.__class__.__name__, dict.__repr__(self))


def _conf_init_app(conf):

    es_url = "http://{}:{}@{}:{}".format(
        conf["ES_USER"], conf["ES_PASS"],
        conf["ES_HOST"], conf["ES_PORT"],
    )
    conf["ES_URL"] = es_url
    redis_url = 'redis://:{}@{}:{}/{}'.format(
        conf['REDIS_PWD'], conf['REDIS_HOST'],
        conf['REDIS_PORT'], conf['REDIS_DB']
    )
    conf['REDIS_URL'] = redis_url
    db_uri = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
        conf["DB_USER"], conf["DB_PASS"],
        conf["DB_HOST"], conf["DB_PORT"], conf["DB_NAME"],
    )
    conf['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    conf['SQLALCHEMY_DATABASE_URI'] = db_uri
    # conf['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False
    traffic_db_uri = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
        conf["TFC_DB_USER"], conf["TFC_DB_PASS"],
        conf["TFC_DB_HOST"], conf["TFC_DB_PORT"], conf["TFC_DB_NAME"],
    )
    conf['SQLALCHEMY_BINDS'] = {
        'traffic': traffic_db_uri,
    }
    conf["DB_URI"] = db_uri

    conf["CUSTOMIZE_ENGINE_PATH"] = os.path.join(
        conf["CUSTOMIZE_BATH_PATH"],
        conf["CUSTOMIZE_ENGINE_DIR"]
    )
    conf["CUSTOMIZE_DEPENDENT_PATH"] = os.path.join(
        conf["CUSTOMIZE_BATH_PATH"],
        conf["CUSTOMIZE_ENGINE_DIR"],
        conf["CUSTOMIZE_DEPENDENT"]
    )

    conf["CONF_CHECK_REPORT_PATH"] = os.path.join(conf["CONF_CHECK_DATA"], "report")
    conf["CONF_CHECK_SRC_PATH"] = os.path.join(conf["CONF_CHECK_DATA"], "src")
    conf["CONF_CHECK_NATIVE_MAP"] = conf["CONF_CHECK_APP_MAPPING"].keys()
    conf['ROOT'] = ROOT

    for i in [conf["FILE_TEMP_PATH"], conf["WIFI_WORK_PATH"], conf["CONF_CHECK_REMOTE_TEMP"]]:
        if not os.path.exists(i):
            os.makedirs(i)


class Conf(Config):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Conf, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        super(Conf, self).__init__(CONF_DIR)
        self.from_pyfile('{}.py'.format(ENV))
        _conf_init_app(self)


conf = Conf()
