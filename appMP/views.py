from django.shortcuts import render
from .models import MissingPerson

# Create your views here.
def MissingPersonsTable (request):
    MissingList = MissingPerson.objects.all()
    context = {
        'persons' : MissingList
    }
    
    return render(request, 'appMP/index.html', context)

# def MissingPersonsTable(request):
#     return render(request, 'appMP/index.html')


def personView (request,personId) :
    data = MissingPerson.objects.get(
        id=personId
    )
    context = {
        'person':data
    }
    return render(request, 'appMP/person.html', context)
    
    """data = MissingPerson.objects.filter(
        id=personId
    ).get()
    context = {
        'person': data
    }
    """