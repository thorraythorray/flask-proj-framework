from pylint import lint
from flask.cli import AppGroup, with_appcontext

manager_cli = AppGroup('manager', help='Run manage on Python files')


@manager_cli.command('lint')
@with_appcontext
def lint_pyfile():
    """Run pylint on the codebase."""
    pylint_opts = ["--rcfile", ".pylintrc", 'app', 'common']  # 指定要分析的文件名
    lint.Run(pylint_opts)
