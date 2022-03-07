dictionary = {
              "cat": "chat",
              "dog": "chien",
              "horse": "cheval"
              }

dictionary['cat'] = 'minou' # update
dictionary['swan'] = 'cygne' # add
dictionary.update({"horse": "canard"}) # add-update
del dictionary['dog'] # remove item
# dictionary.clear()   # removes all the items
# del dictionary    # removes the dictionary
dictionary.popitem() # remove last

copy_dictionary = dictionary.copy()
print(dictionary)