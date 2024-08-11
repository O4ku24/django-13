from models import Author

person = Author.objects.get(id=7)
person.delete()
