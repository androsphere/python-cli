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
    def type(self, character_class):
        if isinstance(type, str) and len(type):
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
