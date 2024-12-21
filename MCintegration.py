import shutil
from os.path import join
import os
import time
import sys
import subprocess
from playsound import playsound



def server_command(cmd):
    os.system('screen -S  -X stuff "{}\015"'.format(cmd))

print("started")
minecraft_dir = ('server.jar')
world_dir = ('C:/Users/noahl/OneDrive/Desktop/MC Fun w Friends')

# Start the server process
process = subprocess.Popen('java -Xmx1024M -Xms1024M -jar server.jar', stdin=subprocess.PIPE, shell=True)
lastcommand = None
global keepinventory
keepinventory = False
commandsLength = 0
global tickspeed
tickspeed = 20
frozenTime = False
while True:
    with open("commands.txt", "r") as connector:
        current_command = connector.readlines()  # Read the whole file content and strip any extra whitespace
        
        

        actualLength = len(current_command)
        if commandsLength < actualLength:
            focused_command = current_command[commandsLength]
            focused_command = focused_command.strip()
            print(current_command)
            if focused_command == "kill": 
                killcommand = "/kill @e[type=!player]\n"
                process.stdin.write(killcommand.encode())  # Encode the command to bytes
                process.stdin.flush()
            
            elif focused_command == "tp":
                killcommand = "/execute as glexal at glexal run tp @a ~ ~200 ~\n"
                process.stdin.write(killcommand.encode())  # Encode the command to bytes
                process.stdin.flush()
            
            elif focused_command == "stone":
                killcommand = "/execute as glexal at glexal run fill ~15 ~15 ~15 ~-15 ~-15 ~-15 air replace stone\n"
                process.stdin.write(killcommand.encode())  # Encode the command to bytes
                process.stdin.flush()
            
            elif focused_command == "water":
                print("water ran")
                killcommand = "/execute as glexal at glexal run fill ~5 ~5 ~5 ~-5 ~-5 ~-5 water replace air\n"
                process.stdin.write(killcommand.encode())  # Encode the command to bytes
                process.stdin.flush()

            elif focused_command == "tnt":
                killcommand = "/execute as glexal at glexal run summon minecraft:tnt ~ ~ ~ {fuse:40}\n"
                process.stdin.write(killcommand.encode())  # Encode the command to bytes
                process.stdin.flush()
            
            elif focused_command == "kick":
                killcommand = "/kick @a\n"
                process.stdin.write(killcommand.encode())  # Encode the command to bytes
                process.stdin.flush()
            
            elif focused_command == "hole":
                killcommand = "/execute as glexal at glexal run fill ~ ~ ~ ~ ~-100 ~ air\n"
                killcommand2 = "/execute as glexal at glexal run fill ~ ~-99 ~ ~ ~-49 ~ water\n"
                process.stdin.write(killcommand.encode())  # Encode the command to bytes
                process.stdin.write(killcommand2.encode())
                process.stdin.flush()
            
            elif focused_command == "fling":
                killcommand = '/execute as glexal at glexal run summon wind_charge ~ ~1.5 ~1 {Motion:[0d,0d,-10d],Passengers:[{id:wind_charge,Motion:[0d,0d,-10d],Passengers:[{id:wind_charge,Motion:[0d,0d,-10d],Passengers:[{id:wind_charge,Motion:[0d,0d,-10d],Passengers:[{id:wind_charge}]}]}]}]}\n'
                killcommand2 = '/execute as glexal at glexal run summon wind_charge ~ ~1.5 ~1 {Motion:[0d,0d,-10d],Passengers:[{id:wind_charge,Motion:[0d,0d,-10d],Passengers:[{id:wind_charge,Motion:[0d,0d,-10d],Passengers:[{id:wind_charge,Motion:[0d,0d,-10d],Passengers:[{id:wind_charge}]}]}]}]}\n'
                process.stdin.write(killcommand.encode())  # Encode the command to bytes
                process.stdin.write(killcommand2.encode())
                process.stdin.flush()

            elif focused_command == "keepinventory":
                if keepinventory:
                    killcommand = "/gamerule keepInventory false\n"
                    keepinventory = False
                else:
                    killcommand = "/gamerule keepInventory true\n"
                    keepinventory = True
                process.stdin.write(killcommand.encode())  # Encode the command to bytes
                process.stdin.flush()
            elif focused_command == "tick":
                tickspeed += 1
                killcommand = f"/tick rate {tickspeed}\n"
                process.stdin.write(killcommand.encode())  # Encode the command to bytes
                process.stdin.flush()
            elif focused_command == "world":
                if frozenTime == False:
                    killcommand = f"/tick freeze\n"
                    frozenTime = True
                else:
                    killcommand = f"/tick unfreeze\n"
                    frozenTime = False
                killcommand2 = f"/execute as glexal at glexal run effect give @a minecraft:blindness 2 225 true\n"
                killcommand3 = f"/execute as glexal at glexal run effect give @a minecraft:slowness 2 225 true\n"
                process.stdin.write(killcommand2.encode())
                process.stdin.write(killcommand.encode())  # Encode the command to bytes
                process.stdin.flush()
                if frozenTime == True:
                    playsound("SFX/za-warudo-effect-green-screen_160k-1.mp3")
                else:
                    playsound("SFX/toki-wa-ugoki-desu.mp3")
            commandsLength += 1
    
    time.sleep(1)  # Sleep for a short period to avoid high CPU usage
