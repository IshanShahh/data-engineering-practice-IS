import requests
import pandas
from bs4 import BeautifulSoup
import os 

file = '2024-01-19 10:27'
path_to_folder = '/Users/Ishan/data-engineering-practice-IS/Exercises/Exercise-2/downloads'
os.makedirs(path_to_folder, exist_ok=True)

def main():
    # your code here
    response = requests.get("https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/")
    soup_data = BeautifulSoup(response.text,'html.parser')
    table_row = soup_data.find_all('tr')
    # print(table_row)
    
    for data in table_row:
        x = data.find_all('td')
        if len(x) > 1:
            dates = x[1].text.strip()
            if dates == '2024-01-19 10:27':
                file_link = x[0].find('a')
                file_name = file_link['href']
                file_api = requests.get(response.url + file_name)
                if file_api.status_code == 200:
                    file_path = os.path.join(path_to_folder,file_name)
                    with open(file_path, 'wb') as f:
                        f.write(file_api.content)
                    print(f"Saved {file_name} to downloads")
                else:
                    print('Did not work')

df = pandas.read_csv("/Users/Ishan/data-engineering-practice-IS/Exercises/Exercise-2/downloads/01023199999.csv")
print(max(df['HourlyDryBulbTemperature']))

        # z = x.find_all('<td')
        # print
        # date_column = x[1]
        # print(date_column)

if __name__ == "__main__":
    main()
