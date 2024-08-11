from django.shortcuts import render
from .models import Author
from .models import Authors
from django.http import HttpResponse

def home(request):
    return render(request=request, template_name='core/home.html')

def author(request):
    if request.method == 'GET':
        authors = {'authors':{}}
        authors_db = Author.objects.values()
        for author in authors_db:
            authors['authors'][f'{author["name"]}'] = author['id']
        return render(request=request, template_name='core/authors.html', context=authors)
    
            
def author_book(request, name):
    if request.method == 'GET':
        books = Author.objects.filter(name = name).values
        data = {'author':name,'books':books}
        print(data)
        return render(request=request, template_name='core/authorBooks.html', context=data)



def top_books(request):
    data = {'books':[]}
    data_db = Author.objects.values()
    for i in data_db:
        book = i['books']
        print(book)
        data['books']+=[book]
    print(data)   
    return render(request=request, template_name='core/top_books.html', context=data)

def add_author(request):
    if request.method == 'GET':
        return render(request=request, template_name='core/addAuthor.html')
    if request.method == 'POST':
        nameAuthor = request.POST.get("newAuthor")
        newBook = request.POST.get("newbook")
        print(nameAuthor, newBook)
        Author.objects.get_or_create(name = nameAuthor, books = newBook)
        return render(request=request, template_name='core/addAuthor.html')
    
      

