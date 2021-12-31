import game_engine as ge
import town_map as tm
import os 




os.system("clear")
shop_menu_flag = 0
def display_town_map():
    for i in range(len(map)):
        
        if(i % 48 == 0):
            print("")
        print(map[i],end="")
    print("\n")


def shop_menu():
    global shop_menu_flag
    os.system("clear")
    
    while True:
        buy = 0
        print(f"You have {player.gold} pieces of gold")
        for i in range(len(ge.items)):
            print(f"[{i}] {ge.items[i].name} Tier {ge.items[i].tier}, Price: {ge.items[i].price}")
        print("\n\n")
        print("Press e to exit")
        print("\n\n")
        buy = input(">> ").upper()
        
        if(buy == "E"):
            break;
        else:
            buy = int(buy)
            if(ge.items[buy].price < player.gold):
                player.gold -= ge.items[buy].price
                print(f"You bought a {ge.items[i].name} Tier {ge.items[i].tier}")
                player.additem(ge.items[buy])
            else:
                print("Cannot_buy")
    shop_menu_flag  = 1
    res_map()


def clear_map():
    for i in range(len(map)):
        if(map[i] == "@"):
            map[i] = " "


def res_map():
    global shop_menu_flag
    os.system("clear")
    clear_map()
    if shop_menu_flag == 1:
        player.x+=1
        shop_menu_flag =0
    #only reprints maps after menu's
    map[player.x + (player.y*48)] = "@"
    display_town_map()
    print("Press O to open menu")
    print(f"X: {player.x}")
    print(f"Y: {player.y}")





def open_menu():
    
    os.system("clear")
    while True:

        select = 0
        print("[1] Inventory")
        print("[2] Show Main slot")
        print("[3] Settings(coming soon)")
        print("Press e to exit")
        select = input(">>")
        if(select == "1"):
            os.system("clear")
            player.display_inventory()
            print("Press e to exit")
            select = input("Equip into main slot:")
            if select == "e":
                print("OK")
                os.system("clear")
            else:
                player.equip_item(int(select))

        elif(select == "2"):
            os.system("clear")
            player.print_main_slot()
        elif(select == "e"):
            os.system("clear")
            break;
    res_map()

print("[1] Load Game")
print("[2] Start New Game\n\n\n\n\n")

menu = input(">>> ")

if menu == '1':
    print("feaure not added")
elif menu == '2':
    print("Are you a boy or a girl?\n\n\n\n\n")
    gender = input(">>> ")
    print("Your name is? \n\n\n\n\n")
    name = input(">>> ")
    player = ge.character(10,1,gender, name)


player.x = 46
player.y = 9
player.max_lim = 48
map = tm.town_map

map[player.x + (player.y*48)] = "@"
display_town_map()




print(f"{player.name}, you have been brought to this world to defeat a being known as Kars")
print("Nearly 100 years ago Kars ravenged the earth in and effort to wipe out humanity and become the ultimate lifeform")
print("Kars had succeded in becoming the ultimate lifeform")
print("But was able to be traped in a shell of ice which was sent to space.")
print("Now he has returned and plans to take over the earth.")
print("Your goal is to defeat Kars.")
print("Kars has 4 genarals bellow him you must beat first")
print("Go to town first to make preperations.")
print("Move to make this text disapear ^^^\n\n\n\n")
print("Press O to open menu")
print(f"X: {player.x}")
print(f"Y: {player.y}")


while True:
    
    move = input(">> ").upper()
    how_much = 1
    
    if move == "W":
        player.move_up(how_much)
    if move == "S":
        player.move_down(how_much)
    if move == "A":
        player.move_left(how_much)
    if move == "D":
        player.move_right(how_much)
    if move == "O":
        open_menu()
    if move == "F":
        player.useitem()
    
    
    

    if map[player.x + (player.y*player.max_lim)] != " ":
        if(map[player.x + (player.y*player.max_lim)] == "S"):
            shop_menu()
            res_map()
        else:
            print("Invalid move will cause collision")
            if move == "W" or move == "S":
                player.y = player.y_buf
            if move == "A" or move == "D":
                player.x = player.x_buf
    else:
    
        os.system("clear")

        for i in range(len(map)):
            if(map[i] == "@"):
                map[i] = " "
                
        map[player.x + (player.y*player.max_lim)] = "@"
        
        display_town_map();

        print("Press O to open menu")
        print("Press F to use main slot")
        print("Walk into the S in shop to enter the shop menu.")
        print(f"X: {player.x}")
        print(f"Y: {player.y}")
