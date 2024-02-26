from models.__init__ import CONN, CURSOR
from models.character import Character
from models.item import Item

def seed_database():
    Character.drop_table()
    Item.drop_table()
    Character.create_table()
    Item.create_table()

    # Create seed data
    Andros = Character.create("Andy", "Human", "Paladin")
    Harper = Character.create("Harper", "Elf", "Druid")
    James = Character.create("James", "Elf", "Warlock")
    Kate  = Character.create("Kate", "Half-elf", "Rogue")
    Item.create("Longsword", 3 , Andros.id)
    Item.create("Shield", 6, Andros.id)
    Item.create("Chainmail", 55, Andros.id)
    Item.create("Quarterstaff", 4, Harper.id)
    Item.create("Bag of Holding", 15, Harper.id)
    Item.create("pipe", 1, Harper.id)
    Item.create("Spellbook", 1, James.id)
    Item.create("Rapier", 2, Kate.id)


seed_database()
print("Seeded database")