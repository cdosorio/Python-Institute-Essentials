dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
              }

# keys
for item in dictionary:
    print(item) 

# key method             
for key in dictionary.keys():
    print(key, "->", dictionary[key])

# loop through a dictionary's keys and values
for english, french in dictionary.items():
    print(english, "->", french)

#  values() method
for french in dictionary.values():
    print(french)
