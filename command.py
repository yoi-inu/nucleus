import sys
from django.core.management import call_command
from nucleus import connection


def run_command():
    """Configures django setup and runs all tests
    """
    args = sys.argv
    args.pop(0)

    command_name = args.pop(0)

    connection.setup()
    call_command(command_name, *args)


if __name__ == '__main__':
    run_command()
