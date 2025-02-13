import os

current_directory =  os.getcwd()
folder_path = current_directory + '\Result'
subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]
for subfolder in subfolders:
    count = 0 
    count_f = 0
    sub_subfolders = [f.path for f in os.scandir(subfolder) if f.is_dir()]
    for sub_subfolder in sub_subfolders:
        sub_sub_subfolders = [f.path for f in os.scandir(sub_subfolder) if f.is_dir()]
        for sub_sub_subfolder in sub_sub_subfolders:
            res_files = [f.path for f in os.scandir(sub_sub_subfolder) if f.is_file()]
            for file in res_files:
                count_f += 1
                with open(file, 'r') as result:
                    lines = result.readlines()
                    for line in lines:
                        if line.startswith("Time:"):
                            time_str = line.split(":")[1].strip().replace('s', '')
                            time_taken = float(time_str)
                            if time_taken < 180.0:
                                count += 1
                            break
    print('Test group:', os.path.basename(os.path.dirname(sub_subfolder)))                        
    print("Total result files:", count_f)
    print("Number of result files optimal:", count)
    print("Ratio of result files optimal:", count/count_f)
    print('-'*20)
