import requests
import os 
import zipfile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

path_to_folder = '/Users/Ishan/data-engineering-practice-IS/Exercises/Exercise-1/downloads'
os.makedirs(path_to_folder, exist_ok=True)

files = []
print(files)

def main():
    # your code here
    try:
        for url in download_uris:
            param = url.split('/')[-1]
            x = url.replace(param,'')
            response = requests.get(url)
            if response.status_code == 200:
                param = url.split('/')[-1]
                x = url.replace(param,'')
                with zipfile.ZipFile(response) as zip_ref:
                    for file_info in zip_ref.infolist():
                        extracted_filepath = os.path.join(path_to_folder,param)
                # param = url.split('/')[-1]
                # x = url.replace(param,'')
    except requests.exceptions.HTTPError as errh:
        print("error")
    
    # for 
        # response = requests.get(url)
        # print(response)
    # try:
    #     response = requests.get("https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip")
    #     print(response)
    # except 


if __name__ == "__main__":
    main()
