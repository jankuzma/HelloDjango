import random

from django.shortcuts import render, redirect

from hello.models import Person


# Create your views here.


def hello(request):
    return render(request, 'hello.html')


def name(request):
    return render(request, 'name.html')


def losowy_napis(request):
    napisy = [
        'Sławek Bo',
        'Gosia Pe',
        'Piotrek de'
    ]
    napis = napisy[random.randint(0, len(napisy) - 1)]
    return render(request, 'ln.html', {'n': napis})


def losuj(request):
    liczba = random.randint(1, 100)
    return render(request, 'ln.html', {'n': liczba})


def kosci(request):
    k1 = random.randint(1, 100)
    k2 = random.randint(1, 100)
    k3 = random.randint(1, 100)
    return render(request, 'kosci.html', {'k1': k1, 'k2': k2, 'k3': k3})


def lottek(request):
    lst = list(range(1, 49))
    random.shuffle(lst)
    wylosowane = lst[:6]
    wylosowane.sort()
    return render(request, 'lotek.html', {'liczby': wylosowane})


def ll2(request, a, b):
    liczba = random.randint(a, b)
    return render(request, 'ln.html', {'n': liczba})


def rzut(request, ilosc, kosc):
    lst = []
    for _ in range(ilosc):
        lst.append(random.randint(1, kosc))
    return render(request, 'kosci2.html', {'wyniki': lst, 'ilosc': ilosc, 'kosc': kosc})



def PersonView(request):
    persons = Person.objects.all()
    return render(request, 'persons.html', {'persons':persons})


def add_person_view(request):
    if request.method == 'GET':
        return render(request, 'form_add_person.html')
    imie = request.POST.get('first_name')
    nazwisko = request.POST.get('last_name')
    p = Person()
    p.first_name = imie
    p.last_name = nazwisko
    p.save()
    return redirect('/persons/')


