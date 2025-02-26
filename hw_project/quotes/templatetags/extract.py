from bson.objectid import ObjectId
from django import template
from ..utils import get_mongodb

register = template.Library()

def get_author(id_):
    db = get_mongodb()
    author = db.authors.find_one({'_id': ObjectId(id_)})
    if author:  # Перевірка, чи автор знайдений
        return author['fullname']
    return 'Unknown Author'


register.filter('author', get_author)
