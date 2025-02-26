from datetime import datetime, timezone

from bson import ObjectId
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import AuthorForm, QuoteForm
from .models import Author
from .utils import get_mongodb


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html',
                  context={'quotes': quotes_on_page})

def author_list(request):
    author = Author.objects.all()
    return render(request, "quotes/author.html", {"author": author})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author=form.save(commit=False)

            # Додавання автора в MongoDB
            db = get_mongodb()
            mongo_author = db.authors.insert_one({
                'fullname': author.fullname,
                'born_date': author.born_date,
                'born_location': author.born_location,
                'description': author.description,
                'created_at': datetime.now(timezone.utc)
            })
            author.mongo_id = str(mongo_author.inserted_id)
            author.created_at = datetime.now(timezone.utc)
            author.save()
            return redirect(to='quotes:main')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote=form.save(commit=False)

            # Додавання цитати в MongoDB
            db = get_mongodb()
            db.quotes.insert_one({
                'author': ObjectId(quote.author.mongo_id),
                'quote': quote.quote,
                'created_at': datetime.now(timezone.utc)
            })
            quote.created_at = datetime.now(timezone.utc)
            quote.save()
            return redirect(to='quotes:main')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})
