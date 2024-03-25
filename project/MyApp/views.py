from django.shortcuts import render , redirect
from .models import *
from .forms import *

# Create your views here.

def Home(request):

    Books = Book.objects.all()

    Book_count = Books.count()

    Book_Available , Book_Rented , Book_Sold = 0 , 0 , 0

    Salarey_Rented = []
    Salarey_Sold = []


    for x in Books:
        if x.States == 'Available':
            Book_Available +=1
        if x.States == 'Rented':
            Book_Rented +=1
        if x.States == 'Sold':
            Book_Sold +=1
        # =================
        if x.States == 'Sold':
            if x.Price != None:
                Salarey_Sold.append(x.Price)
        if x.States == 'Rented':
            if x.Price != None:
                Salarey_Rented.append(x.Price)
    

    context = {
        'Books': Books,
        'Book_Add': Book_Add(),
        'Cat': Category.objects.all(),
        'Cat_Add': Cat_Add(),
        'Count': Book_count,
        'Book_Av': Book_Available,
        'Book_Rn': Book_Rented,
        'Book_Sl': Book_Sold,
        'Salary_Sl': sum(Salarey_Sold),
        'Salary_Rn': sum(Salarey_Rented),
        'Salary_all': sum(Salarey_Rented)+sum(Salarey_Sold),
    }

    if request.method == 'POST':

        data = Book_Add(request.POST, request.FILES)
        if data.is_valid():
            data.save()

    if request.method == 'POST':
        add_cat = Cat_Add(request.POST)
        if add_cat.is_valid():
            add_cat.save()

    return render(request , 'pages/Home.html' , context)

def Books(request):
    All_Book = Book.objects.all()

    title = None

    if 'category' in request.GET:
        title = request.GET['category']
        All_Book = All_Book.filter(category= title)


    if 'Book_St' in request.GET:
        title = request.GET['Book_St']
        All_Book = All_Book.filter(States = title)


    if 'search_name' in request.GET:
        title = request.GET['search_name']
        All_Book = All_Book.filter(Title__icontains = title)

    context = {
        'Books': All_Book,
        'Cat': Category.objects.all(),
        'Cat_Add': Cat_Add(),
    }

    if request.method == 'POST':
        add_cat = Cat_Add(request.POST)
        if add_cat.is_valid():
            add_cat.save()

    return render(request , 'pages/Books.html' , context)



def Update(request , id):
    Book_Id = Book.objects.get(id = id)

    if request.method == 'POST':
        Book_Save = Book_Add(request.POST , request.FILES , instance= Book_Id)
        if Book_Save.is_valid():
            Book_Save.save()
            return redirect("/")
        
    else:
       Book_Save = Book_Add(instance= Book_Id)

    contex = {
        'Book': Book_Save,
    } 

    return render(request , 'pages/Update.html' , contex)

def Delete(request , id):
    Book_Id = Book.objects.get(id = id)

    if request.method == 'POST':
        Book_Id.delete()
        return redirect("/")

    return render(request , 'pages/Delete.html')

