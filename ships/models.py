from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import random

crewSize = {"Sloop": 20, "Schooner": 30, "Brig": 40, "Galleon": 80, "Man-O-War": 100}

class Ship(models.Model):
    name = models.CharField(max_length=50, unique=True)
    SHIPS = ((0, "Sloop"), (2, "Schooner"), (2, "Brig"), (3, "Galleon"), (4, "Man-O-War")) 
    type = models.IntegerField(choices=SHIPS, default=0)

    #Returns Ship object name
    def __str__(self):
        return self.name

class Character(models.Model):
        name = models.CharField(max_length=50, unique=False)
        GENDERS = ((0, "Male"), (1, "Female"), (2, "Other"))
        gender = models.IntegerField(choices=GENDERS, default=0)
        SPECIES = ((0, "Human"), (1, "Dragonborn"), (2, "Dwarf"), (3, "Elf"), (4, "Gnome"), (5, "Goliath"), (6, "HalfOrc"), (7, "Halfling"), (8, "Vampire"))
        species = models.IntegerField(choices=SPECIES, default=0)
    

#Extends Character class
class CrewMember(Character):
        role = models.CharField(max_length=30, unique=False, default="Crew")
        co = models.CharField(max_length=30, unique=False)
        ship = models.ForeignKey(Ship, models.SET_NULL, null=True, blank=True)
        important = models.BooleanField(default=False)

        def promoteToOfficer(self, role):
            self.role = role
        
        def generateCrewMember(self):
            self.name = self.genName()
            self.species = self.genSpecies()
            self.gender = self.genGender()

        #Temporary function
        def genName(self):
            return random.choice(["Name1", "Name2", "Name3", "Name4", "Name5"])

        #Temporary function
        def genSpecies(self):
            return random.choice([0,1,2,3,4,5,6,7,8])

        #Temporary function
        def genGender(self) :
            return random.choice([0,1,2])

        #Returns object attribute, value pairs in following format. Name, Species, Gender, Role, CO.
        def getVars(self):
            return {"name": self.name, "species": self.get_species_display(), "gender": self.get_gender_display(), "role":self.role, "co":self.co}


@receiver(post_save, sender=Ship)
def genNewShipCrew(sender, instance, created, **kwargs): 
    """Post Save method which generates a crew for any newly generated ship

    Args:
        sender (Ship Class): Django internal argument to ensure function only executes when Ship Class is saved to DB. 
        instance (Object Instance): Object instance of the Ship saved to the database 
        created (Boolean): True if object is newly created. False otherwise
    """
    if created:
        #Generates a CrewMember object can assigns the role to Captain.
        chr = CrewMember(role="Captain", co="Self", ship=instance)
        chr.generateCrewMember()
        CrewMember.save(chr)
        
        #Generates a officer for each item in officers array.
        officers = ["First Mate", "Boatswain", "Master Gunner", "Surgeon", "Navigator", "Spellcaster"]
        for i in officers:
            chr = CrewMember(role=i, co="Captain", ship=instance)
            chr.generateCrewMember()
            CrewMember.save(chr)
        
        #Generates n CrewMember objects where n is the crewsize of the saved Ship Object. 
        crewSize = {"Sloop": 20, "Schooner": 30, "Brig": 40, "Galleon": 80, "Man-O-War": 100}
        for _ in range(crewSize[instance.get_type_display()]):
            chr = CrewMember(co=random.choice(officers), ship=instance)
            chr.generateCrewMember()
            CrewMember.save(chr)