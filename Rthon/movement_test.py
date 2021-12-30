import game_engine as ge
import os


seed = 1
player = ge.character(10,1,"Male","Jimmy")
map = ge.map(seed)



os.system("clear")
while(map._map[player.x + (player.y*10)] != " "):
    player.x+=1
map._map[player.x + (player.y*10)] = "@"
map.display();

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
        
    
    
    
    

    if map._map[player.x + (player.y*10)] != " ":
        print("Invalid move will cause collision")
        if move == "W" or move == "S":
            player.y = player.y_buf
        if move == "A" or move == "D":
            player.x = player.x_buf
    else:
    
        os.system("clear")
        map = ge.map(seed)
        map._map[player.x + (player.y*10)] = "@"
        map.display();
        print(f"X: {player.x}")
        print(f"Y: {player.y}")
