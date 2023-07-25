"""
Django command to wait for database to be ready

"""
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """ Django commad to wait for database """

    def handle(self, *args, **options):
        """Entry Point for command"""
        self.stdout.write('waiting for database ....')
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable , waiting for 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database Available !'))



            



