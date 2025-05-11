import psycopg2
import os 
import csv
import pandas as pd

path = '/Users/Ishan/data-engineering-practice-IS/Exercises/Exercise-5/data'
files = os.listdir(path)

queries = []

def main():
    # host = "postgres"
    # database = "postgres"
    # user = "postgres"
    # pas = "postgres"
    # conn = psycopg2.connect(host=host, database=database, user=user, password=pas)
    # your code here
    # cur = conn.cursor()
    for dirname, dirpath, name in os.walk(path):
        print(dirname)
        print(dirpath)
        print(name)
        for file in name:
            df = pd.read_csv(dirname + '/' + file)
            print(df)

            

    # for file in files:
    #     content = os.path.join(path, file)
    #     df = pd.read_csv(content)
    #     for key in df.keys():
    #         print(key)
    #         # print(df.dtypes)
    #         print(f"Create Table {file} for \n {key}, {df.dtypes}")

if __name__ == "__main__":
    main()

