from makemkv import * # Python wrapper for MakeMKV
from os import getcwd,mkdir # This way we can store the media in their own folders.

final_name=str()
name=str()
save_dir=str()
save_dir_empty=False

m=MakeMKV(0) # Starts a MakeMKV session on disk drive 0.

def con():
    conin=input("The final name is "+final_name + ". Do you want to continue, or change the name? (Y/n) : ")
    if conin=="y" or conin=="":
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
    global save_dir_empty
    name=input("What is the name of this media? ")
    save_dir=input("Where would you like it to be stored? (Defaults to current directory)")
    if save_dir=="":
        save_dir=getcwd()
        save_dir_empty=True
    final_name=name
    con() # Asks to confirm the name.

get_input() # Gets the name and save directory, and confirms the name.
print("Getting title count...")

# Gets the info of the disk, which lets us get title count.
info=m.info()

print("Title count is "+ str(info["title_count"]))

# This will make sure RippedMedia exists, and if it does and errors, just pass.
try: mkdir(save_dir+"/"+"RippedMedia")
except:pass 

# Makes sure the final save directory exists, and if it does and errors, just print it becuase of a potential error.
try: mkdir(save_dir+"/"+"RippedMedia" +"/"+final_name)
except:print("Directory already found. Warning that if you don't delete already ripped tracks in there it will try to overwrite them and error.")

for i in range(info["title_count"]):

    print("Ripping title " + str(i))

    m.mkv(i,save_dir+"/"+"RippedMedia" +"/"+final_name) # Rip title i to MKV.

print("...Ripping done.")