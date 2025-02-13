import os
import random

current_directory =  os.getcwd()
folder_path = current_directory + '\Result'
subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]
for subfolder in subfolders:
    sub_subfolders = [f.path for f in os.scandir(subfolder) if f.is_dir()]
    random_sub_subfolders = random.sample(sub_subfolders, 4)
    for sub_subfolder in random_sub_subfolders:
        sub_sub_subfolders = [f.path for f in os.scandir(sub_subfolder) if f.is_dir()]
        random_sub_sub_subfolders = random.sample(sub_sub_subfolders, 1)
        for sub_sub_subfolder in sub_sub_subfolders:
            res_files = [f.path for f in os.scandir(sub_sub_subfolder) if f.is_file()]
            random_file = random.sample(res_files, 1)
            for file in random_file:
                with open(file, 'r') as result:
                    file_content = result.readlines()
                    prefix = r"D:\ASUS\Trí_tuệ_nhân_tạo\BT3\Result"
                    path = file[len(prefix) + 1:]
                    index = path.rfind('_res.txt')
                    path = path[:index] + '.kp'
                    print('Path:', path)
                    print(file_content[0],end=' ')
                    print(file_content[2],end=' ')
                    print(file_content[3],end=' ')
                    print(file_content[6],end='')
                    print('-'*10)
