from pyspark.sql import SparkSession
import os 
import zipfile 

path = '/Users/Ishan/data-engineering-practice-IS/Exercises/Exercise-6/data'
files = os.listdir(path)
def main():
    spark = SparkSession.builder.appName("Exercise6").enableHiveSupport().getOrCreate()
    # your code here
    for file in files:
        print(file)
        # df = spark.read.csv(file)
        # print(df)
        full_path = os.path.join(path,file)
        with zipfile.ZipFile(full_path,'r') as f:
            content = f.namelist()
            # print(content)
            for _ in content:
                if _.endswith('.csv'):
                    with f.open(_,'r') as w:
                        data = spark.read.csv(w)
                        print(data)

                # read = f.read(_['start_time'])
                # print(read)
            # for _ in content:
            #     print(_)
                    
    


if __name__ == "__main__":
    main()
