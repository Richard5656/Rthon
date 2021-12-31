import __main__ #allows me to use varibles from main_game.py
import time

class item: #item class used for the creation of items
    desc = "not described"
    def __init__(self,name, tier,price, power):
       self.name = name   #items name
       self.tier = tier   #items tier
       self.price = price #items price
       self.power = power #items power

    def usage(self):
        #function to use item
        print(f"{self.name}")

class character: #chracter class used for the creation of characters
    dungeon_floor = 1
    x = 0   #x position of player
    y = 0   #y position of player
    x_buf = 0 #stores the previous x position of player will be removed
    y_buf = 0 #stores the previous x position of player will be removed
    gold=5  #stores the ammount of gold the player has #player starts with 5 gold 
    attack = 3 #attack power #player starts with 3 atk
    
    min_lim = 0 #map dependant #multiplication to keep the coordinates ok
    max_lim =10 #map dependant #multiplication to keep the coordinates ok
    
    inventory =[] # inventory is a list of items, items can be added here with additem()
    mainslot = item("No item in Main",0,0,0) # this is the main slot where an item will be stored. It is the main item that can be used.




    def __init__(self,hp,level,gender,name): #function sets up player like their hp,level,gender,name
        self.hp = hp
        self.level = level
        self.gender = gender
        self.name = name



    # these functions move the player 
    def move_up(self,how_many_to_move_by):
        self.y_buf = self.y
        self.y-= how_many_to_move_by
        self.limit_movement(0,self.max_lim)
        
    def move_down(self,how_many_to_move_by):
         self.y_buf = self.y
         self.y+= how_many_to_move_by
         self.limit_movement(0,self.max_lim)
         
    def move_left(self,how_many_to_move_by):
         self.x_buf = self.x
         self.x-= how_many_to_move_by
         self.limit_movement(0,self.max_lim)
         
    def move_right(self,how_many_to_move_by):
         self.x_buf = self.x
         self.x+= how_many_to_move_by
         self.limit_movement(0,self.max_lim)
         
    def limit_movement(self,min_lim_,max_lim_): # this function is hit detecion
        while self.x > max_lim_:
            self.x-=1
        while self.y > max_lim_:
            self.y-=1
            
        while self.x < min_lim_:
            self.x+=1
        while self.y < min_lim_:
            self.y+=1
#end of movement functions 
    
    def display_inventory(self): # displays inventory
        print(f"{self.name}'s inventory:")
        for i,v in enumerate(self.inventory):
            print(f"Index: {i},Item: {v.tier} {v.name}")
        print("\n")

    def additem(self,item_p): # adds item to inventory
       self.inventory.append(item_p)
      
    def useitem(self): #uses the item in the main slot
        self.mainslot.usage()
       
    def equip_item(self,index): #equips item in to main slot
        self.mainslot = self.inventory[index]
        
    def print_main_slot(self): # prints the item in the main slot
        print("Main Slot: "+self.mainslot.name,end="\n\n")

class enemy: # creates enemy (coming soon)
    def __init__(self,hp,name,level,attack_power, description):
        self.hp = hp
        self.name = name
        self.level = level
        self.attack_power = attack_power
        self.description = description



class map: # creates map, I used the lcg algorithm which is just multplication subtraction addition and getting the remainder from a division
    def __init__(self,seed):
        x=seed
        m= 418837
        c= 1452457
        a= 1067711
        self._map =[]

        for i in range(0,100):
            x=((x*a)+c)%m
            
            if (x%2) == 0:
                self._map.append("X")
            else:
                self._map.append(" ")
    def create_ep(self):
        self._map[int(time.time()) % len(self._map)] = "O"
        
    def display(self):
        self.create_ep()
        for i in range(0,len(self._map)):
            if i%10 == 0:
                print()
            print(self._map[i],end=" ")
        print("\n")
    
class pickaxe(item): # creates pickaxe item
    def usage(self):
        #AudioTore I need you to program a way for a pickaxe to break multiple blocks forward
        #This task should helpwith the understanding of the game engine 
        if(__main__.map[__main__.player.x + ((__main__.player.y-1)*48)] == "X"):
            __main__.map[__main__.player.x + ((__main__.player.y-1)*48)] = " "
        __main__.res_map()
    pass

class sword(item): # creates sword item
    def usage(self):
        print("sword")
    pass


class potion(item): # creates potion item
    def usage(self):
        print("potion")
    pass


class regular_rock(item): # creates rock item
    def usage():
        print("rock")
    pass

items =[pickaxe("Pickaxe",1,3,1),sword("Sword",1,3,1)] # items with id's

   
