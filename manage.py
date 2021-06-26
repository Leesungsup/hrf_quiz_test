#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from crawler import crawler
from quiz.models import Player_info
from csvwriter import csvwriter
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapi.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__=='__main__':
    main()
    #data = crawler()
    #for item in data:
        #Player_info(number = item['number'], name = item['name'], position = item['position'],age=item['age'],nation=item['nation'],team=item['team'],value=item['value'],photo=item['photo']).save()
    #csvwriter()