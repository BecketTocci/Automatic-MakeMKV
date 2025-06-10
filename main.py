from makemkv import *
from os import getcwd,mkdir

final_name=str()
name=str()
save_dir=str()


m=MakeMKV(0)

def con():
    conin=input("The final name is "+final_name + ". Do you want to continue, or change the name? (y/n) : ")
    if conin=="y":
        return
    elif conin=="n":
        get_input()
    else:
        print("Sorry, I didn't understand that. Please try again.")
        con()

def get_input():
    global final_name
    global name
    global save_dir
    name=input("What is the name of this media? ")
    year=input("What year was this media made in? ")
    save_dir=input("Where would you like it to be stored? (Defaults to current directory)")
    if save_dir=="":
        save_dir=getcwd()+"/RippedMedia"
    final_name=name + " (" + year + ")"
    con()

get_input()
print("Getting title count...")
info=m.info()
print("Title count is "+ str(info["title_count"]))

try: mkdir(save_dir+"/"+final_name)
except:print("Directory already found. Warning that if you don't delete already ripped tracks in there it will try to overwrite them and error.")
for i in range(info["title_count"]):
    print("Ripping title " + str(i))
    m.mkv(i,save_dir+"/"+final_name)
print("...Ripping done.")
