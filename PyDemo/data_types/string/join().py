"""

  str.join(
    iterable : Iterable
  )

  Concatenates elements of the sequence separated by a string operator

  ========================================================================================================================================

  Parameters :

  iterable : Iterable = objects capable of returning their members one at a time ; examples are : LIST, TUPLE, STRING, DICTIONARY, and SET

  ========================================================================================================================================

  Exceptions :

  TypeError : if the iterable contains any non-string values

  ==========================================================

"""

string : str = "#".join("hello world")
print(string)

# Output :
# h#e#l#l#o# #w#o#r#l#d

# ================================
#
# Case : LISTs :

string : str = "".join(["p", "y"])
print(string)

# Output :
# py

# ================================
#
# Case : TUPLEs :

sample_tuple : tuple = ("1", "25", "24")
string : str = "-".join(sample_tuple)
print(string)

# Output :
# 1-25-24

# ===================================
#
# Case : DICTs

dictionary : dict = {
  "py": 1,
  "demo": 2
}
string : str = "".join(dictionary)
print(string)

# Output :
# pydemo