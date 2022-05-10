import os
import re

# NOT NEEDED : this file is not useful

# seperate the aircraft based on the 
# number of columns they have

semi_colon_counter = [i for i in range(1,51)]
index = 0
country_dict = {}
s = []
# chop off ever occurence before afghanistan

with open('data/vessel.txt') as f:
    data = f.readlines()


# store all lisitngs associated with each country

# for line in data:
#     if line.count(";") < 1:
#         continue
#     s.append(line.count(";"))
#     #print(f'{index} is : and semi-colon occurened {line.count(";")} times')
#     index += 1
# print(max(s))

# split according to the number of semi colons
# since i know all the countries here are undetermined
# I will skip it

for line in data:
    for number in semi_colon_counter:
        if line.count(";") < 1:
            continue
        if line.count(";") == number:
            with open(f'data/{number}_ent.txt', 'a') as new_file:
                new_file.write(line)
        index += 1
