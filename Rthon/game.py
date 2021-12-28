import os, time, subprocess

print("""_____  _   _                 
 |  __ \| | | |                
 | |__) | |_| |__   ___  _ __  
 |  _  /| __| '_ \ / _ \| '_ \ 
 | | \ \| |_| | | | (_) | | | |
 |_|  \_\\__|_| |_|\___/|_| |_|""")

print("Welcome to Rthon! A Ascii Text game.")
time.sleep(3)
print("Thank you for downloading!")
time.sleep(3)
os.chdir('Data')
subprocess.call("python menu.py", shell=True)
