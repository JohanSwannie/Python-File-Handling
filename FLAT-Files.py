# TXT File handling examples
# --------------------------

# Creating a TXT file
# -------------------

reclst1 = ["Jean", "Louis", "Gert", "Piet", "Derrick", "Johan", "Stephen", "Herman"]
reclst2 = [29, 39, 54, 33, 71, 56, 49, 69]
reclst3 = ["Architect", 'Boiler Maker', 'Teacher', 'Lawyer',
           'CEO', 'Software Developer', 'Professional Golfer', 'Preacher']

txtFile01 = open("swannie-txt01.txt","w+")

for x in range(8):
    rec = reclst1[x] + ' of age ' + str(reclst2[x]) + ' is a ' + reclst3[x] + '\n'
    txtFile01.write(rec)

# Closing a TXT file
# ------------------

txtFile01.close()

# Reading a TXT file
# ------------------

txtFile02 = open("swannie-txt01.txt", 'r')
for recs in txtFile02:
    print(recs, end = ' ')

print('=' *200)

txtFile02.close()

# OR readlines()

with open("swannie-txt01.txt", "r") as txt01:
    recs = txt01.readlines()
    for line in recs:
        print(line)

print('=' *200)

# OR read complete file

with open("swannie-txt01.txt", "r") as txt02:
    recs = txt02.read()
    print(recs)

# OR read only first 50 characters of file

with open("swannie-txt01.txt", "r") as txt03:
    print(txt03.read(50))

# Appending a TXT file
# --------------------

reclst1b = ["Eunice", "Sandra", "Roxanne", "Sharon", "Tasha", "Louise", "Mandy", "Ann"]
reclst2b = [27, 40, 25, 43, 30, 52, 44, 37]
reclst3b = ['Bookkeeper', 'Programmer', 'Photographer', 'Administrator',
            'Manager', 'Software Engineer', 'Advocate', 'Barrister']

with open("swannie-txt01.txt","a+") as txt04:
    for x in range(8):
        rec2 = reclst1b[x] + ' of age ' + str(reclst2b[x]) + ' is a ' + reclst3b[x] + '\n'
        txt04.write(rec2)

# Deleting a TXT file
# -------------------

import os
os.remove('swannie-txt01.txt')



