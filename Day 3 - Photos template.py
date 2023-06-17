from PIL import Image, ImageDraw, ImageFont

import os

##############################################################################################

print("""
  ______ _   _______ ______ _____ _    _ 
 |  ____| | |__   __|  ____/ ____| |  | |
 | |__  | |    | |  | |__ | |    | |__| |
 |  __| | |    | |  |  __|| |    |  __  |
 | |____| |____| |  | |___| |____| |  | |
 |______|______|_|  |______\_____|_|  |_| 
""")

print("\n","\n","\n","\n","\n")

print("""
  ____          _  ___           _ _     _   _____           _               _ 
 |  _ \        | |/ / |         | (_)   | | |  __ \         | |             | |
 | |_) |_   _  | ' /| |__   __ _| |_  __| | | |__) |__ _ ___| |__   __ _  __| |
 |  _ <| | | | |  < | '_ \ / _` | | |/ _` | |  _  // _` / __| '_ \ / _` |/ _` |
 | |_) | |_| | | . \| | | | (_| | | | (_| | | | \ \ (_| \__ \ | | | (_| | (_| |
 |____/ \__, | |_|\_\_| |_|\__,_|_|_|\__,_| |_|  \_\__,_|___/_| |_|\__,_|\__,_|
         __/ |                                                                 
        |___/                                                                  
""")
temd = 'tem.png' # Template
c = 1

try:
    os.mkdir(os.getcwd() + "\Done")
except FileExistsError:
    pass

tem = Image.open(temd)
width2, height2 = tem.size

for x in os.listdir():

    if x[-4:] == ".jpg" and not x == temd:

        qrimg = 'Done/' + str(c) + ".jpg"  # save dir
        pic = Image.open(x)
        
        pic = Image.Image.resize(pic,(width2, height2))
        pic.paste(tem, (0, 0) , tem)
        pic.save(qrimg)
        c = c + 1

        pic.close()


print("Finished")