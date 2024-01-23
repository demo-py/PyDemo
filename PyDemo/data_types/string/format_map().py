"""

  str.format_map(
    dictionary : dict
  )

  Used to return a dictionary key's value

  ==================================================

  Parameters :

  dictionary : dict = a dictionary of values of keys

  ==================================================

"""

dictionary : dict = {
  "name": "demo",
  "age": 18,
  "hobby": None
}
string : str = """Name : {name}
Age : {age}
Hobby : {hobby}"""
print(string.format_map(dictionary))

# Output :
# Name : demo
# Age : 18
# Hobby : None