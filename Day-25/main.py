# with open("C:/new/100-Projects-of-Python/Day-25/weather_data.csv") as data_file:
#     list_of_data = data_file.readlines()
#     print(list_of_data)

# import csv
# with open("C:/new/100-Projects-of-Python/Day-25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature=[]
#     i = 0
#     for row in data:
#         if i>0:
#             temp =int(row[1])
#             temperature.append(temp)
#         i+=1
# print(temperature)

import pandas
data = pandas.read_csv("C:/new/100-Projects-of-Python/Day-25/weather_data.csv")
sum_of_temp=0
for temp in data["temp"]:
    sum_of_temp +=temp
answer = sum_of_temp/len(data["temp"])
print(answer)