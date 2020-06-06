# CSV File handling examples
# --------------------------

import csv

# Using csv.reader - normal
# -------------------------

with open("swannie-csv01.txt") as csv0101:
    file01 = csv.reader(csv0101, delimiter=',')
    line_Cnt = 0
    for row in file01:
        if line_Cnt == 0:
            print(f"Column names are {'  -  '.join(row)}")
            line_Cnt += 1
        else:
            print(f"\t{row[0] + ' ' + row[1]} of age {row[2]} lives in {row[3]} and is a {row[4]}")
            line_Cnt += 1
    print(f"We have processed {line_Cnt} lines")

# Using csv.DictReader - DictReader
# ---------------------------------

with open("swannie-csv01.txt") as csv0102:
    file02 = csv.DictReader(csv0102, delimiter=',')
    line_Cnt2 = 0
    for row in file02:
        if line_Cnt2 == 0:
            print(f"Column names are {'  -  '.join(row)}")
            line_Cnt2 += 1
        print(f"\t{row['Name'] + ' ' + row['Surname']} of age {row['Age']} lives in {row['Location']} and is a {row['Career']}")
        line_Cnt2 += 1
    print(f"We have processed {line_Cnt2} lines")

# Using csv.reader - with quotechar
# ---------------------------------

with open("swannie-csv02.txt") as csv02:
    file03 = csv.reader(csv02, delimiter=',', quotechar='"')
    line_Cnt3 = 0
    for row in file03:
        if line_Cnt3 == 0:
            print(f"Column names are {'  -  '.join(row)}")
            line_Cnt3 +=1
        else:
            print(f"\t{row[0]} of age {row[2]} lives at {row[1]} and id no is {row[3]}")
            line_Cnt3 += 1
    print(f"The number of records are {line_Cnt3}")

# Using csv.reader - with escapechar
# ----------------------------------

with open("swannie-csv03.txt") as csv03:
    file04 = csv.reader(csv03, delimiter=',', escapechar='|')
    line_Cnt4 = 0
    for row in file04:
        if line_Cnt4 == 0:
            print(f"Column Names are {'  -  '.join(row)}")
            line_Cnt4 += 1
        else:
            print(f"\t{row[0]} at address {row[1]} is {row[2]} years old")
            line_Cnt4 += 1
    print(f"We have now processed {line_Cnt4} reocrds")

# Using csv.writer - write row by row
# -----------------------------------

with open('swannie-csv04.csv', 'w', newline='') as csv04:
    writer1 = csv.writer(csv04)
    writer1.writerow(['ID', 'fullname', 'age'])
    writer1.writerow([109315, 'Luke Sheehan', 29])
    writer1.writerow([107532, 'James Mower', 51])
    writer1.writerow([108614, 'Richard Adams', 33])
    writer1.writerow([107996, 'Peter Pumpkineater', 41])

# Using csv.writer - write multiple rows at once
# ----------------------------------------------

rec1 = [['ID', 'fullname', 'age'],
        [109315, 'Luke Sheehan', 29],
        [107532, 'James Mower', 51],
        [108614, 'Richard Adams', 33],
        [107996, 'Peter Pumpkineater', 41]]

with open('swannie-csv05.csv', 'w', newline='') as csv05:
    writer2 = csv.writer(csv05)
    writer2.writerows(rec1)

# Using csv.writer - write multiple rows and add the quotes to non numeric fields
# -------------------------------------------------------------------------------

with open('swannie-csv06.csv', 'w', newline='') as csv06:
    writer3 = csv.writer(csv06, quoting=csv.QUOTE_NONNUMERIC, delimiter=';', quotechar='"')
    writer3.writerows(rec1)

# csv.QUOTE_ALL will add quotes around all entries
# csv.QUOTE_MINIMAL will add quotes only around special characters
# csv.QUOTE_NONE will ensure that none of the entries will have quotes around them

# Using csv.writer - write multiple rows and custom quoting
# ---------------------------------------------------------

with open('swannie-csv07.csv', 'w', newline='') as csv07:
    writer4 = csv.writer(csv07, quoting=csv.QUOTE_ALL, delimiter=';', quotechar='*')
    writer4.writerows(rec1)

# Using csv.writer - write multiple rows and use dialect to group together a formatting pattern
# ---------------------------------------------------------------------------------------------

csv.register_dialect('dialectOne',
                     delimiter='|',
                     quoting=csv.QUOTE_ALL,
                     quotechar='%')

with open('swannie-csv08.csv', 'w', newline='') as csv08:
    writer5 = csv.writer(csv08, dialect='dialectOne')
    writer5.writerows(rec1)

# Using csv.DictWriter - write row by row
# ---------------------------------------

with open('swannie-csv09.csv', 'w', newline='') as csv09:
    fieldNames = ['fullname', 'age', 'location', 'career']
    writer = csv.DictWriter(csv09, fieldnames=fieldNames)
    writer.writeheader()
    writer.writerow({'fullname': 'Terry Proops',
                     'age': 58,
                     'location': 'Wellington',
                     'career': 'Mainframe Storage Management Specialist'})
    writer.writerow({'fullname': 'Alex kimi',
                     'age': 56,
                     'location': 'Auckland',
                     'career': 'Reporting Analyst'})
    writer.writerow({'fullname': 'Gustav Ponelis',
                     'age': 57,
                     'location': 'Johannesburg',
                     'career': 'Senior Solutions Architect'})

# Using csv.DictWriter - write multiple rows at once
# --------------------------------------------------

rec2 = [{'fullname': 'Terry Proops',
         'age': 58,
         'location': 'Wellington',
         'career': 'Mainframe Storage Management Specialist'},
        {'fullname': 'Alex kimi',
         'age': 56,
         'location': 'Auckland',
         'career': 'Reporting Analyst'},
        {'fullname': 'Gustav Ponelis',
         'age': 57,
         'location': 'Johannesburg',
         'career': 'Senior Solutions Architect'}]


with open('swannie-csv10.csv', 'w', newline='') as csv10:
    fieldNames2 = ['fullname', 'age', 'location', 'career']
    writer = csv.DictWriter(csv10, fieldnames=fieldNames2)
    writer.writeheader()
    writer.writerows(rec2)
