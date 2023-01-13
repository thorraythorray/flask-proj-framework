from invoke import task, Collection


@task
def lint(c):  # pylint: disable=invalid-name
    c.run('pylint --rcfile=.pylintrc app')


# Collection(lint)  # pylint: disable=invalid-name