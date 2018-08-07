import pathlib
import shutil
import os

def makedir(input_path, name):
    splitted_name = name.split(".")



    try:
        if splitted_name[len(splitted_name)-1] == '':
            if not os.path.exists(input_path+"/unamed"):
                os.mkdir(input_path + "/unamed")
                print("Making Directory 'unamed'")
                print(shutil.copy(input_path +"/"+name, input_path + "/unamed"))
                os.remove(input_path + "/" + name)
            else:
                print(shutil.copy(input_path +"/"+name, input_path + "/unamed"))
                os.remove(input_path + "/" + name)
        else:
            if not os.path.exists(input_path+"/"+splitted_name[len(splitted_name)-1]):
                os.mkdir(input_path+"/"+splitted_name[len(splitted_name)-1])
                print(shutil.copy(input_path+"/"+name,input_path+"/"+splitted_name[len(splitted_name)-1]))
                os.remove(input_path + "/" + name)
            else:
                print(shutil.copy(input_path + "/" + name, input_path + "/" + splitted_name[len(splitted_name) - 1]))
                os.remove(input_path + "/" + name)

    except Exception as e:
        print(e)



input_path = "/home/suraj"

list_of_name = os.listdir(input_path)

for name in list_of_name:

    if os.path.isfile(input_path+"/"+name):
        makedir(input_path, name)