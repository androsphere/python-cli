# Andy's Dungeons n' Dragons inventory manager

This is my character/item inventory CLI! It uses ORM
 to allow the user to create DnD characters, add
 items to their inventories, and persist that to a
 database. It also keeps track of the collective weight of items in a character's inventory

Run lib/cli.py to access the interface.
From the main menu you can:
    -List the current characters in the database
    -Add an character to the database
    -add an item to the database

When you list the characters, you may also see the
items in their inventory, edit/delete characters, 
and edit/delete items.

The seed.py file creates some example characters and
items.
