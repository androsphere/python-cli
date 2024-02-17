from models.__init__ import CURSOR, CONN


class Character:
    all = {}

    def __init__(self, name, species, character_class , id = None ):
        self.id = id
        self.name = name
        self.species = species
        self.character_class = character_class
        
        
    def __repr__(self):
        return f"<Character {self.id}: {self.name},{self.species}, {self.character_class}>"
    
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
    def species(self):
        return self._species

    @species.setter
    def species(self, species):
        if isinstance(species, str) and len(species):
            self._species = species
        else:
            raise ValueError("Species must be a non-empty string")
    
    @property
    def character_class(self):
        return self._character_class

    @character_class.setter
    def character_class(self, character_class):
        if isinstance(character_class, str) and len(character_class):
            self._character_class = character_class
        else:
            raise ValueError("Class must be a non-empty string")
        
    
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Character instances """
        sql = """
            CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY,
            name TEXT,
            species TEXT,
            character_class TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Character instances """
        sql = """
            DROP TABLE IF EXISTS characters;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def get_all(cls):
        """Return a list containing a character object per row in the table"""
        sql = """
            SELECT *
            FROM characters
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]


    @classmethod
    def instance_from_db(cls, row):
        """Return a character object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        character = cls.all.get(row[0])
        if character:
            # ensure attributes match row values in case local instance was modified
            character.name = row[1]
            character.species = row[2]
            character.character_class = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            character = cls(row[1], row[2], row [3])
            character.id = row[0]
            cls.all[character.id] = character
        return character
    
    def save(self):
        """ Insert a new row with the name and location values of the current Department instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO characters (name, species, character_class)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.species, self.character_class))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls, name, species, character_class):
        """ Initialize a new Character instance and save the object to the database """
        character = cls(name, species, character_class)
        character.save()
        return character

    def items(self):
        """Return list of items associated with current character"""
        from models.item import Item
        sql = """
            SELECT * FROM items
            WHERE character_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Item.instance_from_db(row) for row in rows
        ]

    def total_item_weight(self, cursor):
        """Calculate and return the total weight of items associated with the character."""
        from models.item import Item
        sql = """
            SELECT weight FROM items
            WHERE character_id = ?
        """
        cursor.execute(sql, (self.id,))
        rows = cursor.fetchall()
        
        total_weight = sum(row[0] for row in rows)
        return total_weight
    
    @classmethod
    def find_by_name(cls, name):
        """Return Character object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM characters
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def delete(self):


        sql = """
            DELETE FROM characters
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None