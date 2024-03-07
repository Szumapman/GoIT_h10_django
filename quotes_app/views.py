from django.shortcuts import render

from .models import Author, Quote, Tag

# Create your views here.
def index(request):
    quotes = Quote.objects.all()
    context = {"quotes": quotes}
    return render(request, "quotes_app/index.html", context)

def author(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {"author": author}
    return render(request, "quotes_app/about.html", context)