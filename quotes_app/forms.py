from django.forms import ModelForm, CharField, DateField, Textarea, TextInput

from .models import Author, Quote, Tag

class AuthorForm(ModelForm):
    name = CharField(max_length=200, required=True, widget=TextInput())
    born_date = DateField()
    born_location = CharField(max_length=200)
    descryption = Textarea()

    class Meta:
        model = Author
        fields = ["name", "born_date", "born_location", "descryption"]
        
class TagForm(ModelForm):
    name = CharField(max_length=200, required=True, widget=TextInput()) # unique=True ?

    class Meta:
        model = Tag
        fields = ["name"]
        

class QuoteForm(ModelForm):
    quote = Textarea()
    

    class Meta:
        model = Quote
        fields = ["quote"]
        exclude = ["author", "tags"]