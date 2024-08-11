from django.db import models
from django import forms

class Author(models.Model):
    name = models.CharField(max_length=20)
    books = models.CharField(max_length=50)

class AuthorForms(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["id", "name", "books"]

class Authors():
    def __init__(self, name, book) -> None:
        self.name = name
        self.book = book
        

    def add_author(self, name, book):
        addAuthor = Author.objects.create(name=name, book=book)
        addAuthor.save()

    def add_book(self):
        pass

    def del_author(self):
        delAuthor = Author.objects.get(id=id)
        delAuthor.delete()

    def del_book(self):
        pass