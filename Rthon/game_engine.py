
class item:
    desc = "not described"
    def __init__(self,name, tier):
       self.name = name
       self.tier = tier
    def usage():
        #function to use item
        print(f"{self.name}")

class character:
    gold=5
    inventory =[]
    mainslot = item("empty",0)
    def __init__(self,hp,level,gender,name):
        self.hp = hp
        self.level = level
        self.gender = gender
        self.name = name
       
    def display_inventory(self):
        print(f"{self.name}'s inventory:")
        for i,v in enumerate(self.inventory):
            print(f"Index: {i},Item: {v.tier} {v.name}")
        print("\n")
    def additem(self,item_p):
       self.inventory.append(item_p)
      
    def useitem(self):
        self.mainslot.usage()
       
    def equip_item(self,index):
        self.mainslot = self.inventory[index]
        
    def print_main_slot(self):
        print("Main Slot: "+self.mainslot.name,end="\n\n")

class enemy:
    def __init__(self,hp,name,level,attack_power, description):
        self.hp = hp
        self.name = name
        self.level = level
        self.attack_power = attack_power
        self.description = description

class map:
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

    def display(self):
        for i in range(0,len(self._map)):
            if i%10 == 0:
                print()
            print(self._map[i],end=" ")
        print("\n")
