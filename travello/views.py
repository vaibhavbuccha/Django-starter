from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.id = 1
    dest1.name = 'Mumbai'
    dest1.desc = '''A city that never sleep's.'''
    dest1.price = 700
    dest1.image = 'destination_1.jpg'
    dest1.offer = True
    dest2 = Destination()
    dest2.id = 1
    dest2.name = 'Rajasthan'
    dest2.desc = '''A city Of traditions.'''
    dest2.price = 500
    dest2.image = 'destination_2.jpg'
    dest2.offer = False
    dest3 = Destination()
    dest3.id = 1
    dest3.name = 'kolkata'
    dest3.desc = '''A city Of joy.'''
    dest3.price = 650
    dest3.image = 'destination_3.jpg'
    dest3.offer = True
    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests': dests})