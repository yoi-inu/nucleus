from django.core.management import call_command
from nucleus import connection


def runtests():
    """Any kind of pre-test configuration can be performed inside
    this function.
    """
    connection.setup(test=True)
    call_command("test")


if __name__ == '__main__':
    runtests()
