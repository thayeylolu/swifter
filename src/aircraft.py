import re
import pandas as pd


KEY_LIST = [
    "Program",
    "Aircraft Name",
    "Aircraft Country",
    "Aircraft Operator",
    "Aircraft Manufacture Date",
    "Aircraft Model",
    "Additional Sanctions Information",
    "MSN",
    "Aircraft Construction Number",
    "Aircraft Serial Identification",
    "Nationality of Registration",
    "Aircraft Mode S Transponder Code",
    "Aircraft Tail Number",
    "Secondary sanctions risk",
    "Transactions Prohibited For Persons Owned or Controlled By U.S. Financial Institutions",
    "Remark"
]
 
# regular expresion to match the strings
# in the text file 

REGEX_LIST = [
    r'\[.*\]',
    r'ObjCountry',
    r'ObjName',
    r'Aircraft\s?Operator',
    r'Aircraft Manufacture Date',
    r'Aircraft\s?Model',
    r'Additional\s?Sanctions\s?Information',
    r"Aircraft\s?Manufacturer's\s?Serial Number\s?(MSN)",
    r'Aircraft\s?Construction\s?Number',
    r'Aircraft\s?Serial\s?Identification',
    r'Nationality\s?of\s?Registration',
    r'Aircraft\s?Mode\s?S\s?Transponder\s?Code',
    r'Aircraft\s?Tail\s?Number',
    r'Secondary\s?sanctions\s?risk',
    r'Transactions\s?Prohibited\s?For\s?Persons\s?Owned\s?or\s?Controlled\s?By\s?U.S.\s?Financial\s?Institutions\s?',
    r'Linked\s?To\s?:'
]

# read text file

with open('data/aircraft.txt') as f:
    data = f.readlines()

# stop words to find values and column names

STOPPER_LIST  = ["(aircraft)", ';', ")." ]

ALL_COLUMNS = []
checker = []
program_list = []
storage = {}

# get unique column names and replace [SDT] etc 
# with program_type

for line in data:
    for pattern in REGEX_LIST:
        matches = re.findall(pattern, line)
        if matches:
            ALL_COLUMNS.append(matches[0])

SET_COLUMNS = set(["program_type" if '[' in column_name else column_name for column_name in ALL_COLUMNS ])

# search for column names in every line
# of text file. If enclosed in [] saves 
# in a new list called program list
for line in data:
    for column_name in SET_COLUMNS:
        if column_name == 'program_type':
            square_brackets = re.findall(r'\[.*\]', line)
            program_list.append(square_brackets)

        # if column name is in line
        # gets the stop words and include 
        # the other stopwords longet than one character

        if column_name in line:
            checker = [index for index, stopper in enumerate(line) if stopper in STOPPER_LIST]
            if ")." in line:
                checker.append(line.index(').'))
            if "(aircraft)" in line:
                checker.append(line.index('(aircraft)'))

            checker.sort()
            min_stopper = min(checker)
            col_index = line.index(column_name)

            # compares index of column name in the
            # line with that of the first stop word
            # it finds. 
            # while true, it continues to check for
            # the stop word with lesser than the col
            # index 

            while col_index > min_stopper:
                try:
                    checker = checker[1:]
                    iterator_checker = iter(checker)
                    min_stopper = next(iterator_checker)  
                except StopIteration:
                    checker = [index for index, stopper in enumerate(line) if stopper in STOPPER_LIST]
                    if ")." in line:
                        checker.append(line.index(').'))
                    if "(aircraft)" in line:
                        checker.append(line.index('(aircraft)'))
                    checker.sort()

            # get the value. replace the column-name
            # and value with '' for easier search

            value_ = line[line.index(column_name) + len(column_name) : min_stopper]
            line = line.replace(line[line.index(column_name): min_stopper], '')

            # ensures that if a column name does not exist
            # it value is replaced with None. 
            # this would make it easy to convert 
            # the stored dictionary to a CSV file

            if column_name in storage:
                storage[column_name].append(value_)
            else:
                storage[column_name] = [value_]
        else:
            if column_name in storage:
                storage[column_name].append(None)
            else:
                storage[column_name] = [None]
    checker = []

# store the program_list 
# in the storage object
storage["program_type"] = program_list


output = pd.DataFrame(storage)
output.to_csv('./data/aircraft.csv', index=False)
