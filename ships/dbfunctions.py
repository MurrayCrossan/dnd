import sqlite3
from . import functions

"""
def saveShipToDB(ship):
    con = sqlite3.connect('dbFiles/testShipsCopy.db')
    c = con.cursor()
    shipInfo = [ship.name, ship.model, ship.weapons, ship.movement]
    c.execute('''CREATE TABLE IF NOT EXISTS Ships 
                    (ShipKey INTEGER PRIMARY KEY AUTOINCREMENT, 
                    Name TEXT, 
                    Model TEXT, 
                    Weapons TEXT, 
                    Movement INTEGER);''')

    #Checks if ship of this name already exists, if it does replaces the ship and assigned the new ship the old primary key
    c.execute(f"SELECT Shipkey FROM Ships where name='{ship.name}';")
    pkey = c.fetchall()

    if pkey == []:
        c.execute('INSERT INTO Ships (Name, Model, Weapons, Movement) VALUES (?,?,?,?);', shipInfo)
    else:
        c.execute(f'DELETE FROM Ships Where ShipKey={pkey[0][0]};')
        c.execute(f'INSERT INTO Ships (Shipkey, Name, Model, Weapons, Movement) VALUES ({pkey[0][0]},?,?,?,?);', shipInfo)

    c.execute(f"SELECT Shipkey FROM Ships WHERE Name='{ship.name}';")
    pkey = c.fetchall()[0][0]

    con.commit()
    con.close()

    saveCrewToDB(ship, pkey)


def saveCrewToDB(ship, pkey):

    con = sqlite3.connect('dbFiles/testShipsCopy.db')
    c = con.cursor()    

    table = (ship.name).replace(" ", "_").replace("\n", "")

    #Creates table for ship. If Ship already exists, deletes previous table and creates a new table with the new data
 
    c.execute(f'''DROP TABLE IF EXISTS {table};''')
    c.execute(f''' CREATE TABLE IF NOT EXISTS {table} (ShipKey INTEGER, Name, Gender, Race, Role, CommandingOfficer);''')

    for i in ship.crew:
        crewMemInfo = [pkey, i.name, i.gender, i.race, i.role, i.commandingOfficer]
        c.execute(f"INSERT INTO {table} VALUES (?,?,?,?,?,?)", crewMemInfo)

    con.commit()
    con.close()
"""

def loadShipFromDB(name):
    con = sqlite3.connect('ships/static/ships/testShipsCopy.db')
    c = con.cursor() 
    name = name.replace("%20", " ")
    ar = []
    c.execute(f'SELECT * FROM Ships where name="{name}";')
    shipInfo = c.fetchall()[0]

    ship = functions.Ship()
    ship.loadShip(shipInfo[1],shipInfo[2],shipInfo[3],shipInfo[4], shipInfo[5])

    ar.append(ship)

    name = name.replace(" ", "_")

    c.execute(f'SELECT * FROM {name};')
    crewInfo = c.fetchall()

    officers = []
    crew = []

    for i in crewInfo:
        char = functions.CrewMember()
        char.loadCrewMember(i[1],i[2],i[3],i[4],i[5])
        
        if char.role != "Crew":
            officers.append(char)
        else:
            crew.append(char)
    
    ar.append(officers)
    ar.append(crew)

    return ar


def getShipListFromDB():
    con = sqlite3.connect('ships/static/ships/testShipsCopy.db')
    #con = sqlite3.connect('http://192.168.0.139/ships.db')
    c = con.cursor() 

    c.execute("SELECT Name FROM Ships")
    names = c.fetchall()
    con.close()
    return names