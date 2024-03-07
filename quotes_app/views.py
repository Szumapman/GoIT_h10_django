from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Author, Quote, Tag
from .forms import AuthorForm, TagForm, QuoteForm

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