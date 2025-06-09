import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exec:
        raise ImportError(
            "Couldn't import django. Are you sure it's installed and available?"
        ) from exec
    execute_from_command_line(sys.argv)