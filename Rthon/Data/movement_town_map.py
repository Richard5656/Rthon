import game_engine as ge
import town_map as tm
import os 




map = tm.town_map

player = ge.character(10,1,"Male","Jimmy")

player.x = 10
player.y = 10
player.max_lim = 48

def display():
    for i in range(len(map)):
        
        if(i % 48 == 0):
            print("")
        print(map[i],end="")
    print("\n")
os.system("clear")
k = 0

while(map[player.x + (player.y*player.max_lim)] != " "):
    player.x-=1

    

map[player.x + (player.y*48)] = "@"
display()
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
        
    
    
    
    

    if map[player.x + (player.y*player.max_lim)] != " ":
    
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
        
        display();
        print(f"X: {player.x}")
        print(f"Y: {player.y}")
