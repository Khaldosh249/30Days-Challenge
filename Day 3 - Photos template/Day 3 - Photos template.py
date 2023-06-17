from PIL import Image
import os



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


tem_name = 'tem.png' # Template Name

c = 1 

try:
    os.mkdir(os.getcwd() + "\Done")
except FileExistsError:
    pass

tem = Image.open(tem_name)
width, height = tem.size


for x in os.listdir():

    if x[-4:] == ".jpg" and not x == tem_name:
        try:
            saved_path = 'Done/' + str(c) + ".jpg"  # save dir
            pic = Image.open(x)
            pic = Image.Image.resize(pic,(width, height))
            pic.paste(tem, (0, 0) , tem)
            pic.save(saved_path)
            c = c + 1
            pic.close()
        except:
            pass 



readme = open("readme.txt" , "w+")

readme.writelines(f"""
{c-1} photos were placed in the template

  ____          _  ___           _ _     _   _____           _               _ 
 |  _ \        | |/ / |         | (_)   | | |  __ \         | |             | |
 | |_) |_   _  | ' /| |__   __ _| |_  __| | | |__) |__ _ ___| |__   __ _  __| |
 |  _ <| | | | |  < | '_ \ / _` | | |/ _` | |  _  // _` / __| '_ \ / _` |/ _` |
 | |_) | |_| | | . \| | | | (_| | | | (_| | | | \ \ (_| \__ \ | | | (_| | (_| |
 |____/ \__, | |_|\_\_| |_|\__,_|_|_|\__,_| |_|  \_\__,_|___/_| |_|\__,_|\__,_|
         __/ |                                                                 
        |___/                                                                  


Khalid's social media links:
https://www.linkedin.com/in/khalid-rashad-6560b7202
https://www.facebook.com/khaldosh

ELTECH's social media links:
https://www.facebook.com/ELTECH.sd

""")


readme.close()
print("Finished")
