"""
Atualiza o banco com a lista oficial de heróis
"""
import datetime
import hashlib
import os
from django.core.exceptions import ObjectDoesNotExist
import requests
import json
from django.core.management.base import BaseCommand
from app.models import Hero


class Command(BaseCommand):
    help = 'Connect to official Marvel API and update the database list'

    def handle(self, *args, **options):

        try:
            ts = str(int(datetime.datetime.now().timestamp()))
            private = os.environ.get('MARVEL_PRIVATE_KEY')
            public = os.environ.get('MARVEL_PUBLIC_KEY')

            concatenated_string = ts + private + public

            # Calculando o hash MD5 da string concatenada
            hash_md5 = hashlib.md5(concatenated_string.encode()).hexdigest()

            offset = 0

            while True:
                api_url = (f"http://gateway.marvel.com/v1/public/characters?ts={ts}&apikey={public}&hash={hash_md5}"
                           f"&offset={offset}")
                response = requests.get(api_url)
                if response.status_code >= 300:
                    self.stdout.write(self.style.ERROR(f'Error to access url marvel. Details: {response.text}'))
                    break
                data = json.loads(response.text)['data']
                total = int(data['total'])
                items = data['results']
                for item in items:
                    id_ = int(item['id'])
                    try:
                        Hero.objects.get(heroe_id=id_)
                    except ObjectDoesNotExist:
                        hero = Hero(heroe_id=id_, name=item['name'])
                        hero.save()
                if offset > total:
                    break
                offset += 20
                break  # for tests purposes

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error to update data from Marvel API: {e}'))
