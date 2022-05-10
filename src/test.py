# import os
# import re

# # dis seperates country from entity, vessel, aircraft and individual

# TYPE_NAMES = {'vessel': '(vessel)',
#                 'aircraft':'(aircraft)',
#                  'individual':'(individual)'
#                 }


# #  'entities': r'([aA-zZ]+\s\[)'
# # splits data if its surrounded by empty lines and replace empty
# # lines with ''

# with open('data/test.txt') as f:
#     lines = f.read()
#     data = re.sub('\n(?!\n)', '', lines).split('\n')

# for chunk in data:
#     flag = False
#     for key, _  in TYPE_NAMES.items():
#         if _ in chunk:
#             flag = True
#             with open(f'data/{key}.txt', 'a') as new_file:
#                 new_file.write(chunk)
#                 new_file.write('\n')
#     if flag is False:
#         with open('data/entity.txt', 'a') as new_file:
#             new_file.write(chunk)
#             new_file.write('\n')


# print(data)


data = ['s', 'a 1', 'b', 'c', 'd', 'e 1','f', 'g 1','h','i 2']
country_list = ['s', 'c', 'd', 'f', 'h']
index = 1
country_dict = {}
TYPE_NAMES = {'1': '1', '2':'2'}

for chunk in data:
    if index <= len(country_list) - 1:
        compare=  country_list[index]
        if chunk == compare:
            country_dict[country_list[index - 1]] = data[:data.index(chunk)]
            data =  data[data.index(chunk):]
            index +=1
    country_dict[country_list[-1]] = data[data.index('h'):]


for key, _  in TYPE_NAMES.items():
    for country,value in country_dict.items():
        with open(f'data/{key}.txt', 'a') as new_file:
            new_file.write(country)
            #new_file.write(chunk)
            new_file.write('\n')
        for chunk in value:
            flag = False
            if _ in chunk:
                flag = True
                with open(f'data/{key}.txt', 'a') as new_file:
                    #new_file.write(country)
                    new_file.write(chunk)
                    new_file.write('\n')
            
        # if flag is False:
        #     with open('data/y.txt', 'a') as new_file:
        #         new_file.write(chunk)
        #         new_file.write('\n')
print(country_dict)