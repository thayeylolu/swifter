
# # find 
# # 1. AircraftOperator| Aircraft Operator | AircraftOperatorA 
# # 2. Aircraft Manufacture Date| AircraftManufacture Date | Aircraft ManufactureDate | Aircraft Manufacture DateA
# # 3. Aircraft Model | AircraftModel | Aircraft ModelA
# # 4. AdditionalSanctions Information |Additional Sanctions Information| Additional SanctionsInformation 
# # 5. Aircraft Manufacturer's Serial Number (MSN) | AircraftManufacturer's Serial Number (MSN) | Aircraft Manufacturer'sSerial Number (MSN)
# # 6. Aircraft Construction Number| AircraftConstruction Number| Aircraft ConstructionNumber |Aircraft Construction NumberA
# # 7. Aircraft Serial Identification|Aircraft Serial IdentificationA | AircraftSerial Identification |Aircraft SerialIdentification
# # 8. Nationality of Registration | Nationality ofRegistration | Nationality of RegistrationA
# # 9. Aircraft Mode S Transponder Code | Aircraft Mode STransponder Code |Aircraft Mode S Transponder CodeA
# # 10. Aircraft Tail Number | AircraftTail Number |Aircraft TailNumber | Aircraft Tail NumberA
# # 11. Secondary sanctions risk |Secondarysanctions risk |Secondary sanctionsrisk |Secondary sanctions riskA
# # 12. Transactions Prohibited For Persons Owned or Controlled ByU.S. Financial Institutions | Transactions Prohibited For Persons Owned or Controlled By U.S. Financial Institutions
# # 13. 


# # s1: Aircraft\s?Operator
# # S2  Aircraft Manufacture Date
# # s3  Aircraft\s?Model
# # s4  Additional\s?Sanctions\s?Information
# # s5. (MSN)
# # s6. Aircraft\s?Construction\s?Number
# # s7. Aircraft\s?Serial\s?Identification
# # s8. Nationality\s?of\s?Registration
# # s9. Aircraft\s?Mode\s?S\s?Transponder\s?Code
# # s10. Aircraft\s?Tail\s?Number
# # s11. Secondary\s?sanctions\s?risk
# # s12. Transactions\s?Prohibited\s?For\s?Persons\s?Owned\s?or\s?Controlled\s?By\s?U.S.\s?Financial\s?Institutions

from os import replace
import re
sample  = ['pipe cat 2 3 !s  app cat dara 100 ; shine cat 2 . [3][a]' ,
                'sendappcat 2 ;sandcat 3 .[2][s] raincat 4!s',
                '[1][d] raincat nine ; pipecat red . ! shinecat 2 !s', ]

items= [r'app\s?cat', r'sand\s?cat', r'rain\s?cat', r'pipe\s?cat', r'shine\s?cat', r'\[.*\]']
stoppers = {';', '.', '!s'}
storage = {}
new_item = []
program_list = []

# matching all items 
for sales in sample:
    for item in items:
        matches = re.findall(item, sales)
        if matches:
            new_item.append(matches[0])
            
set_item = set(new_item)
set_item = set(["program_type" if '[' in item else item for item in set_item  ])
print(set_item)

for sales in sample:
    for item in set_item:
        if item == 'program_type':
            square_brackets = re.findall(r'\[.*\]', sales)
            program_list.append(square_brackets)
        if item in sales:
            checker = [index for index, stopper in enumerate(sales) if stopper in stoppers]
            if '!s' in sales:
                checker.append(sales.index('!s'))
                checker.sort()
            min_stopper = min(checker)
            index_item = sales.index(item)
            while sales.index(item) > min_stopper:
                try:
                    checker = checker[1:]
                    iterator_checker = iter(checker)
                    min_stopper = next(iterator_checker)  
                except StopIteration:
                    checker = [index for index, stopper in enumerate(sales) if stopper in stoppers]
                    if '!s' in sales:
                        checker.append(sales.index('!s'))
                        checker.sort()

            gets = sales[sales.index(item) + len(item) : min_stopper]
            sales = sales.replace(sales[sales.index(item): min_stopper], '')
            #sales = sales[min_stopper+1:]
            if item in storage:
                storage[item].append(gets)
            else:
                storage[item] = [gets]
        else:
            if item in storage:
                storage[item].append(None)
            else:
                storage[item] = [None]

    checker = []

storage["program_type"] = program_list
print(storage)
