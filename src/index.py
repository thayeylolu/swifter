import os
import re


country_list = []
country_dict = {}

TYPE_NAMES = {'vessel': '(vessel)',
                'aircraft':'(aircraft)',
                 'individual':'(individual)'
                }
index = 0

# chop off  ever occurence before afghanistan

with open('data/original_data.txt') as f:
    lines = f.read()
    data = re.sub('\n(?!\n)', '', lines).split('\n')

del data[: data.index('Afghanistan')]

# check if there is a one word item
# in the list like Afghanistan and
# keep it in a country list

country_list = [ word for word in data if not ' ' in word]

# store all listings associated with each country

for chunk in data:
    if index <= len(country_list) - 1:
        compare=  country_list[index]
        if chunk == compare:
            country_dict[country_list[index - 1]] = data[:data.index(chunk)]
            data =  data[data.index(chunk):]
            index +=1
    country_dict[country_list[-1]] = data[data.index('undetermined'):]

# seperate the data based on 
# the TYPE_NAME. If line
# has no type_name. Name it entity

for country, value in country_dict.items():
    for chunk in value:
        flag = False
        for key, _  in TYPE_NAMES.items():
            if (_ in chunk) :
                flag = True
                with open(f'data/{key}.txt', 'a') as new_file:
                    new_file.write(f'ObjCountry:{country};')
                    new_file.write(f'ObjName:{chunk}')
                    new_file.write('\n')
            
        if flag is False:
            with open('data/entity.txt', 'a') as new_file:
                new_file.write(country)
                new_file.write(chunk)
                new_file.write('\n')



