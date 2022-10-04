import os
#チェックするパスの入力

# def check_subfolder():
    


directory_path = input('input folder path(e.g. ./my_folder): ')
valid_path = False


#入力データの検証
while not valid_path:
    try:
        files = os.listdir(directory_path)
    except (FileNotFoundError):
        print (f"'{directory_path}' is invalid path")
        directory_path = input('input folder path(e.g. ./my_folder): ')
    else:
        valid_path = True
        
        
        
        files = [f for f in files if os.path.isfile(os.path.join(directory_path, f))]
        remove_list = []




for file_name in files:
    if "(1)" in file_name:
        remove_list.append(file_name)




if not remove_list == []:
    check = str
    valid_input = False
    [print(name) for name in remove_list]
    
    while not valid_input:
        check = input("do you want to remove these files? y/n: ")
        
        if check == 'y' or check == 'Y':
            valid_input = True
            for file_name in remove_list:
                os.remove(f"{directory_path}/{file_name}")
            print ('successed to remove files')
            
        elif check == 'n' or check == 'N':
            valid_input = True
            print ('canceled')
            
        else:
            print ('invalid input')
            