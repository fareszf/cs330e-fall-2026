import json
# Dictionary
# A Python dictionary is created with details about a person,
# including nested objects (address) and arrays (children).
person = { "name": "John Smith", 
           "age": 35, 
           "address": {"street": "5 main St.", "city": "Austin"}, 
           "children": ["Mary", "Abel"], 
           "has_car": None }

# Convert the person dictionary into JSON format 
# and writes it to a file named person_to_json.json.
with open('person_to_json.json', 'w') as fp:
    json.dump(person, fp, indent=4)
# json.dump: Writes a Python object directly to a file
# in JSON format.


# Converts the person dictionary into a JSON string 
# using json.dumps() and assigns it to js.   
js = json.dumps(person) 
#json.dumps
# json.dumps: Converts a Python object 
# into a JSON-formatted string.


  
assert js ==  '{"name": "John Smith", \
"age": 35, \
"address": {"street": "5 main St.", "city": "Austin"}, \
"children": ["Mary", "Abel"], \
"has_car": null}'
                
       
# Defines a function load_json(filename) that reads 
# a JSON file and converts its contents back into 
# a Python dictionary.

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
    return jsn
    
person = load_json('person_to_json.json')

assert person["age"]               == 35
assert person["address"]["street"] == "5 main St."
assert person["address"]["city"]   == "Austin"
assert person["children"][0]       == "Mary"
assert person["children"][1]       == "Abel"
assert person["has_car"]           == None
