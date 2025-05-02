import boto3
import json 
import os
import pandas as pd
import glob 
import csv

directory = '/Users/Ishan/data-engineering-practice-IS/Exercises/Exercise-4/data'
pattern = '**/*.json'
search_path = os.path.join(directory, pattern)
_files = glob.glob(search_path, recursive=True)
# print(_files)

def main():
    # your code here
    # All files ending with '.txt'
    try:
        for files in _files:
            with open(files,'r') as f:
                contents = json.loads(f.read())
                # print(contents)
                df = pd.json_normalize(contents)
                print(df)
                print(f'this is the file name:{files}')
                with open(files, 'w',newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerows(df)
            # print(df)

            # with open(files, 'r') as f:
            #     contents = json.loads(f)
            #     print(contents)
        # for dirpath,dirname,filename in os.walk(directory):
        #     for files in filename:
        #         with open(files, 'r') as f:
        #             contents = json.loads(f)
        #             print(contents)
        #             print(pd.json_normalize(files))
    except:
        pass


    # try:
    #     for dirpath, dirnames, filenames in os.walk('/Users/Ishan/data-engineering-practice-IS/Exercises/Exercise-4/data'):
    #         for files in filenames:
    #             # file_path = os.path.join(folder_path, files)
    #             with open(files,'r') as f:
    #                 contents = json.load(f)
                
    #             df = pd.json_normalize(contents)
    #             print(df)
                # x = pd.json_normalize(files)
                # print(x)
            # if os.path.isfile(file_path):
            #     with open(file_path, 'r') as file:
            #         content = file.read()
            #         print(content)
    # except:
    #     pass


if __name__ == "__main__":
    main()
