import csv

from django.core.management import BaseCommand
from django.conf import settings

from main.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = settings.CSV_FILE_PATH
        with open(file_path) as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                Category.objects.create(**row)
                # Category.objects.create(name=row['name'], slug=row['slug'])
