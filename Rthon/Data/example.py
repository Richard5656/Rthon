import game_engine as ge
#tutorial for game engine 



#how to create a chracter

#name = ge.chracter(hp,level,gender,name)
kyle = ge.character(100,1,"Male","Kyle") # kyle has 100 hp # is level 1 # is a boy # is named kyle 

#items
#to create an item you must use classes but don't worry its going to be simple

"""
simpily put it like this

class itemname(ge.item):
    def usage():
            #function to show that the item has been used
    pass
"""

class pickaxe(ge.item):
    def usage(self):
        print("pickaxe used")
    pass

class sword(ge.item):
    def usage(self):
        print("Sword used")
    pass
#create a list of items so we can id them
#btw when calling pickaxe as a function or any other item you must also include the tier the item is in so like this pickaxe(name,tier)
#the tier can be any string you want you want


items = [pickaxe("Pickaxe","Weak"),sword("Sword","Weak")]
#items have id's so this pickaxe has the ID of 0 and the sword has the ID of 1 when it is setup
#to access the item do like so 
"""
items[0] #acesses the pickaxe
items[1] #acesses the sword 
"""

#to give an item to a chracter you must call the additem on the chracter varible
#the add item takes in an item so it can be like this 
kyle.additem(pickaxe("Pickaxe","Weak"))

#or it can be like this with the ID's
kyle.additem(items[0])

#to list the player's inventory you must call display_inventory()
#currently there are 2 items in the inventory and they are both pickaxes
kyle.display_inventory();

#for the player to use the item they must equip it into their main slot

#the display inventory displays the items and their location within the inventory 
#using their location which is the index 
#we can equip the item by calling name.equip_item(index)
#Note we can only equip one item at a time
#Armour may be added

kyle.equip_item(0);

#now we can check if this item is equiped by callling this function 

kyle.print_main_slot()

#if it prints empty the equip_item did not work

#now we can call use item and the function usage inside the class for the item is called

kyle.useitem()


#map generation
#so our current map generation relys on seeds
# we create a map varible like so map = ge.map(seed)
# so I have only allowed seeds 1-100 and each map will be 10 ascii chracters wide by 10
#I added the X's as mineable areas not sure where we are going with this so yeah
#I am open to any ways you want me to change the map

map = ge.map(0)

#to show the map just call display() 
map.display();
