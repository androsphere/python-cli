from character import Character

class Item:
    all = {}
    

    def __init__(self, name, weight,character_id, id=None):
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
    def name(self, weight):
        if isinstance(weight, int):
            self._weight = weight
        else:
            raise ValueError("Weight must be an integer")