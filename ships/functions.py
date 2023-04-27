import random
from ships.templatetags.funct import getFlag

shipNames = ["The Aldo","The Planecutter","The Osprey","The Dalia","The Gladiator","The Concorde","The Many Eyes","The Tarrasque","Timats Revenge","The Fame","The Vengeance","The Mad Serpent","The Planar Gate","The Snapdragon","The Antioch","The Ithaca","The Recovery","The Hammerhead","The Scimitar","The Black Dagger","The Vile Delivery","The Fearful Delight","The Mad Howl","The Storm","The Adventure Eel","The Rude Princess"]

class Test:
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.species = ""
        self.role = ""
        self.co = ""

    def gen(self):
        self.name = random.choice(["Liz", "Mark", "Del"])
        self.gender = random.choice(["Male", "Female"])
        self.species = random.choice((["Human","Elf","Dwarf","Orc"]))
        self.role = random.choice(["Crew"])
        self.co = "Captain"
        if self.species == "Dwarf":
            self.color = "Red"
        elif self.species == "Human":
            self.color = "Blue"
        elif self.species == "Orc":
            self.color = "Green"
        else:
            self.color = "Yellow"

    def load(self, name, gender, species, role, co, color):
        pass

class Character:
    def __init__(self):
        self.name = random.choice(["Liz", "Mark", "Del"])
        self.gender = random.choice(["Male", "Female"])
        self.species = random.choice((["Human","Elf","Dwarf","Orc"]))

    def loadCharacter(self, name, gender, species):
        self.name = name
        self.gender = gender
        self.species = species

class CrewMember(Character):
    def newCrewMember(self):
        Character.__init__(self)
        self.role = "Crew"
        self.CO = self.getOfficer()
        #self.color = self.getColor()

    def loadCrewMember(self, name, gender, species, role, co):
        Character.loadCharacter(self, name, gender, species)
        self.role = role
        self.CO = co
        #self.color = self.getColor()

    def getOfficer(self):
        if self.role == "Crew":
            return random.choice(["First Mate", "Boatswain", "Surgeon", "Navigator", "Spellcaster"])
        else:
            return "Captain"

    def getColor(self):
        colors = {"Human": "Black", "Elf": "Yellow", "Dwarf": "Blue", "Orc": "Green", "Halforc": "Green", "Dragonborn": "red", "Halfling": "Brown"}
        if self.species not in colors.keys():
            return colors["Human"]
        return colors[self.species]

    def promoteToOfficer(self, role):
        self.role = role
        if self.role == "Captain":
            self.CO = "Self"
        else: 
            self.CO = "Captain"

class Ship:
    def newShip(self):
        self.name = random.choice(shipNames)
        self.flag = getFlag()


    def shipType(self, model):
        #Placeholder info for ships, should eventually be added to DB and retrived
        if model.lower() == "brig":
            self.model = "Brig"
            self.weapons = "12 8-Pound Guns (4d10), 4 1-Pound Swivel Guns (2d6)"
            self.movement = "45ft"
            #crewnumber does not include officers
            self.crewNumber = 30
            #self.crew = []


    def loadShip(self, name, model, weapons, movement, flag):
        self.name = name
        self.model = model
        self.weapons = weapons
        self.movement = movement
        if flag == None:
            self.flag = getFlag()
        else:
            self.flag = flag

    """
    def getShipOfficers(self):
        ary = []
        for i in self.crew:
            if i.role in ["Captain", "First Mate", "Boatswain", "Surgeon", "Navigator", "Spellcaster"]:
                ary.append(i)
        return ary


    def getShipCrew(self):
        ary = []
        for i in self.crew:
            if i.role not in ["Captain", "First Mate", "Boatswain", "Surgeon", "Navigator", "Spellcaster"]:
                ary.append(i)
        return ary
        """

def generateShip(shipType):

    ar = []

    ship = Ship()
    ship.newShip()
    #ship.shipType("brig")
    ar.append(ship)

    #Generate officers for ship
    ar1 = []
    for i in ["Captain", "First Mate", "Boatswain", "Surgeon", "Navigator", "Spellcaster"]:
        offc = CrewMember()
        offc.newCrewMember()
        offc.promoteToOfficer(i)
        ar1.append(offc)
    ar.append(ar1)

    #Generate crew members
    ar2 = []
    i=0
    if shipType == "Brig":
        num = 40
    elif shipType == "Sloop":
        num = 20

    while i < num:
        memb = CrewMember()
        memb.newCrewMember()
        ar2.append(memb)
        i+=1
    ar.append(ar2)
    
    return ar

