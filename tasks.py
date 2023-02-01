from invoke import task


@task
def lint(c):  # pylint: disable=invalid-name
    c.run('pylint --rcfile=.pylintrc app utils common')

# Collection(lint)  # pylint: disable=invalid-name
