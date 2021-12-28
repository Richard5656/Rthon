import os, subprocess, time


def help():
    print("Multiplayer will come soon!")
    time.sleep(4)
    print("You can select options by using numbers!")
    time.sleep(4)
    print('To go back type "back" to go right back to the menu')
    helptype = input(">>>: ")
    if helptype == 'back':
        mainmenu()


def mainmenu():
    print("Rthon!")
    time.sleep(2)
    print('###########Beta###########################')
    print('##########Rthon###########################')
    print('##        -Play Story                   ##')
    print('##        -Play multiplayer Coming soon!##')
    print('##        -help                         ##')
    print('##        -quit                         ##')
    print('##########################################')
    menu = input("<<>>: ")
    if menu == 'play':
        subprocess.call("python introduction.py", shell=True)

    if menu == 'help':
        help()

# Start the main menu Once this file has been launched.
mainmenu()
