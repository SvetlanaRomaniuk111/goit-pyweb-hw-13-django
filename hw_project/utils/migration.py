import os
import django
from pymongo import MongoClient
from bson.objectid import ObjectId

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_project.settings")
django.setup()

from quotes.models import Quote, Tag, Author  # noqa

client = MongoClient("mongodb://localhost")

db = client.hw_django

authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    )

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)


    exist_quotes = bool(len(Quote.objects.filter(quote=quote['quote'])))

    if not exist_quotes:
        author = db.authors.find_one({'_id': ObjectId(quote['author'])})
        a = Author.objects.get(fullname=author['fullname'])
        q = Quote.objects.create(
            author=a,
            quote=quote['quote']
        )
        for tag in tags:
            q.tags.add(tag)
