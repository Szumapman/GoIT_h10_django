from datetime import datetime

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Author, Quote, Tag
from .forms import AuthorForm, TagForm, QuoteForm
from .data_scraper import get_data

# Create your views here.
def index(request):
    quotes = Quote.objects.all()
    context = {"quotes": quotes}
    return render(request, "quotes_app/index.html", context)

def author(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {"author": author}
    return render(request, "quotes_app/about.html", context)


@login_required
def new_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            context = {"form": form}
            return render(request, "quotes_app/new_author.html", context)
        
    return render(request, "quotes_app/new_author.html", {"form": AuthorForm()})


@login_required
def new_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            context = {"form": form}
            return render(request, "quotes_app/new_tag.html", context)
    
    return render(request, "quotes_app/new_tag.html", {"form": TagForm()})


@login_required
def new_quote(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()
    
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote_to_save = form.save(commit=False)
            quote_to_save.author = Author.objects.get(name=request.POST["author"])
            quote_to_save.save()
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist("tags"))
            for tag in choice_tags.iterator():
                quote_to_save.tags.add(tag)
            return redirect(to="quotes_app:index")
        else:
            context = {"form": form, "tags": tags, "authors": authors}
            return render(request, "quotes_app/new_quote.html", context)
        
    context = {"form": QuoteForm(), "tags": tags, "authors": authors}
    return render(request, "quotes_app/new_quote.html", context)


@login_required
def scrape_data(request):
    quotes, authors = get_data()
    for author in authors:
        author_object = Author.objects.get_or_create(
            name=author["fullname"], 
            born_date=datetime.strptime(author["born_date"], "%B %d, %Y").date(), 
            born_location=author["born_location"], 
            descryption=author["description"])
        for quote in quotes:
            if quote["author"] == author["fullname"]:
                quote_object = Quote.objects.get_or_create(
                    quote=quote["quote"],
                    author=author_object[0])
                for tag in quote["tags"]:
                    tag_object = Tag.objects.get_or_create(name=tag)
                    quote_object[0].tags.add(tag_object[0])
                quote_object[0].save()
                
    return redirect(to="quotes_app:index")