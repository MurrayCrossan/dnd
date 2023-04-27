from django.shortcuts import render, get_list_or_404, get_object_or_404
from .functions import generateShip
from .dbfunctions import getShipListFromDB, loadShipFromDB
from .models import Ship

#Temporary function until DB migration complete. Loads ships from DB into an array before returning the Array in the HTML template.
def guiLoad(request):
    ships = getShipListFromDB()
    shipList = []
    for i in ships:
        shipList.append(i[0])
    return render(request, 'ships/guiIndex.html', {'Ships': shipList})


#Temporary function until DB migration complete. Returns new Ship and CrewMember objects in HTML template.
def newShip(request, slug):
    ar = generateShip(slug)
    return render(request, 'ships/guiIndex.html', {'Ship': ar[0], 'Officer': ar[1], 'Crew': ar[2], 'Dir': vars(ar[1][0])})


#Temporary function until DB migration complete. Loads ship specificed by slug argument. Returns requested Ship and CrewMember objects in HTML template.
def loadShip(request, slug):
    ar = loadShipFromDB(slug)
    #Loops through both Officers and CrewMembers, adds species to array if not present. Used to build species dropdown.
    spec = []
    for i in [ar[1], ar[2]]:
        for j in i:
            if j.species not in spec:
                spec.append(j.species)

    spec.sort()
    return render(request, 'ships/guiIndex.html', {'Ship': ar[0], 'Officer': ar[1], 'Crew': ar[2], 'Dir': vars(ar[1][0]), "Species": spec})


#Loads Ship objects from Django DB. Returns Ship objects in HTML template.
def viewShips(request):
    obj = get_list_or_404(Ship)
    return render(request, 'ships/testing.html', {"objects": obj})


#Loads Ship object specified by slug argument. Returns Ship and assosiated CrewMember objects in HTML template.
def testLoad(request, slug):
    obj = get_object_or_404(Ship, name=slug)
    crew = obj.crewmember_set.all()
    spec = []
    print(f"Slug: : {slug}")
    #Loops through CrewMembers objects, adds species to array if not present. Used to build species dropdown.
    for i in crew:
        species = i.get_species_display()
        if species not in spec:
            spec.append(species)

    return render(request, 'ships/testing.html', {"ship": obj, "Species": spec})