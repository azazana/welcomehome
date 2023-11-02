import time

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from mysqlx import OperationalError as MysqlError


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        self.stdout.write('Wait for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True

            except (MysqlError, OperationalError):
                self.stdout.write('Database is not available')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database is ready!'))
