import os
import shutil

x = os.listdir("S:/Games/minecraft/Instances/")

for i in x:
    if not os.path.exists("S:/Games/gitCurseClone/"+i):
        os.mkdir("S:/Games/gitCurseClone/"+i)
    shutil.copy("S:/Games/minecraft/Instances/"+i+"/minecraftinstance.json","S:/Games/gitCurseClone/"+i+"/minecraftinstance.json")