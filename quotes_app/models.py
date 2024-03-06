from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200, null=False)
    born_date = models.DateField()
    born_location = models.CharField(max_length=200)
    descryption = models.TextField()
    
    def __str__(self):
        return f"{self.name}"

    
class Tag(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"
    

class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.quote}"