# JSON Examples
# -------------

# Python vs JSON
# --------------

# Python           |   	JSON
# ----------------------------
# dict	           |    object
# list, tuple      |    array
# str	           |    string
# int, long, float |	number
# True	           |    true
# False	           |    false
# None	           |    null

# JSON File Structure
# -------------------

import json
import requests

jsdata = {
            "firstName": "Johannes",
            "lastName": "Swan",
            "hobbies": ["Trumpet", "Gym", "Trailing"],
            "age": 57,
            "Brothers-Sisters": [
            {
                "firstName": "Chris",
                "age": 59
            },
            {
                "firstName": "Richard",
                "age": 56
            },
            {
                "firstName": "Julie",
                "age": 55
            }
        ]
    }

# dumps a record layout
# ---------------------

jsString = json.dumps(jsdata, indent=4)

print(jsString)

# dump(write) and load(read)
# --------------------------

with open("stellie-json01.json", "w") as stellie1_json:
    json.dump(jsdata, stellie1_json)

with open("stellie-json01.json", "r") as read_file:
    data1 = json.load(read_file)

print()
print('data in file :', data1, end='')
print()

# Create a string with record layout
# ----------------------------------

jsString2 = """
{
    "Car Category1": {
        "name": "BMW",
        "series": "3 Series",
        "manufacturers": [
            {
                "name": "BMW South Africa",
                "location": "Mabopane - Rosslyn"
            },
            {
                "name": "BMW Germany",
                "location": "Frankfurt"
            }
        ]
    },
    "Car Category2": {
        "name": "Mercedes Benz",
        "series": "A Class",
        "manufacturers": [
            {
                "name": "Mercedes Benz USA",
                "location": "New York"
            },
            {
                "name": "Mercedes Benz Germany",
                "location": "Berlin"
            }
        ]
    }
}
"""

# loads a string
# --------------

data2 = json.loads(jsString2)

print()
print(data2)
print()

# Send a request to a website and loads the response
# --------------------------------------------------

response = requests.get("https://jsonplaceholder.typicode.com/todos")
toDos = json.loads(response.text)
print('toDos  =  ', toDos)

print(toDos == response.json())
print(type(toDos), '   ', toDos[:1])

# Create dictionary with a count of each user as per user-id
# ----------------------------------------------------------

tbu = {}

for t in toDos:
    if t["completed"]:
        try:
            tbu[t["userId"]] += 1
        except KeyError:
            tbu[t["userId"]] = 1

# Sort the dictionary in the order of the user-id with most counts
# ----------------------------------------------------------------

tu = sorted(tbu.items(), key=lambda x: x[1], reverse=True)
print('The top users are : ', tu)

# Determine which count is the highest of all user-id's
# -----------------------------------------------------

tuc = tu[0][1]
print(tuc)

# Create a list of all user-id's with the highest count
# -----------------------------------------------------

tuIds = []

for uId, IdCnt in tu:
    if IdCnt < tuc:
        break
    tuIds.append(str(uId))

# Print out the top users in two different ways
# ---------------------------------------------

topUsers = " + ".join(tuIds)

print('The top users are :', topUsers)

# OR

s = "s" if len(tuIds) > 1 else ""

print(f"user{s} {topUsers} completed {tuc} todo's")

# Filtering data from the web request JSON File and create a new JSON File
# ------------------------------------------------------------------------

def keep(todo):
    comPleted = todo["completed"]
    topIds = str(todo["userId"]) in tuIds
    return comPleted and topIds

with open("stellie-todos.json", "w") as new_JasonF:
    toDos_New = list(filter(keep, toDos))
    json.dump(toDos_New, new_JasonF, indent=2)

# JSON example with classes
# -------------------------

class cTu:
    def __init__(self, lvl, recs=None):
        self.lvl = lvl
        self.recs = {
            "str": 11, "dex": 32, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        }if recs is None else recs
        self.hp = 10 + self.recs["con"]

ctu = cTu(lvl=4)
r = json.dumps(ctu.recs['dex'] + ctu.recs['cha'])
s = json.dumps(True if (ctu.recs['dex'] / ctu.recs['cha'] > 2) else False)
print(r)
print(s)
