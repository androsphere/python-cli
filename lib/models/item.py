
from models.__init__ import CURSOR, CONN

class Item:
    all = {}
    

    def __init__(self, name, weight, character_id, id=None):
        self.id = id
        self.name = name
        self.weight = weight
        self.character_id = character_id

    def __repr__(self):
        return (
            f"<Item {self.id}: {self.name}, {self.item_type}, {self.weight}, " +
            f"Owner: {self.character_id}>"
        )
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if isinstance(weight, int):
            self._weight = weight
        else:
            raise ValueError("Weight must be an integer")
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of item instances """
        sql = """
            CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT,
            weight INTEGER,
            character_id INTEGER,
            FOREIGN KEY (character_id) REFERENCES characters(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists item instances """
        sql = """
            DROP TABLE IF EXISTS items;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def instance_from_db(cls, row):
        """Return an Item object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        item = cls.all.get(row[0])
        if item:
            # ensure attributes match row values in case local instance was modified
            item.name = row[1]
            item.weight = row[2]
            item.character_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            item = cls(row[1], row[2], row[3])
            item.id = row[0]
            cls.all[item.id] = item
        return item
    
    def save(self):
        
        sql = """
            INSERT INTO items (name, weight, character_id)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.weight, self.character_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, weight, character_id):
        """ Initialize a new Employee instance and save the object to the database """
        item = cls(name, weight, character_id)
        item.save()
        return item