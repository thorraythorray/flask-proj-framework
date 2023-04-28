class Singleton:
    def __new__(cls, *args, **kw):
        if not hasattr(cls, "_instance"):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


def singleton(cls, *args, **kw):  # pylint: disable=unused-argument
    instances = {}

    def _singleton(*_args, **_kw):
        if cls not in instances:
            instances[cls] = cls(*_args, **_kw)
        return instances[cls]
    return _singleton
