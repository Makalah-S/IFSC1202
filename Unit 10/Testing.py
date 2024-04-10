class character ():
    def __init__(self, name="", race="", classType=""):
        self.classType = classType
        self.name = name
        self.race = race

paladin = character("Igneous", "F. Genasi", "Paladin") ##Devotion
druid = character("Amaryllis", "Fae", "Druid" ) ##Wildfire
bard = character("Celestia", "Elf", "Bard") ##Glamour
cleric = character("Giovanni", "Human", "Cleric") ##War
rouge = character("Graveyard", "E. Genasi", "Rouge") ##Grave
wizard = character("Brook", "Human", "Wizard") ##Diviation

party = [paladin, druid, bard, cleric, rouge, wizard]

for i in range(len(party)):
    print(party[i].name, party[i].race, party[i].classType)

def nameChange(self):
    self.name = input("Enter New Name: ")
    return self.name
