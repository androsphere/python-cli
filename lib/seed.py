from models.__init__ import CONN, CURSOR
from models.character import Character
from models.item import Item

def seed_database():
    Character.drop_table()
    Item.drop_table()
    Character.create_table()
    Item.create_table()

    # Create seed data
    Andy = Character.create("Andy", "Human", "Paladin")
    Harper = Character.create("Harper", "Elf", "Druid")
    Item.create("Longsword", 3 , Andy.id)
    Item.create("Shield", 6, Andy.id)
    Item.create("Chainmail", 55, Andy.id)
    Item.create("Quarterstaff", 4, Harper.id)
    Item.create("Bag of Holding", 15, Harper.id)
    Item.create("pipe", 1, Harper.id)


seed_database()
print("Seeded database")