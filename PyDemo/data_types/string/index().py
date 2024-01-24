"""

  str.index(
    substring : str,
    start : Optional[int] = 0,
    end : Optional[int]
  )

  Find the index of the first occurenece of an existing substring  inside a given string

  ======================================================================================

  Parameters :

  substring : str = strubg to be searched for

  start : Optional[int] = the position from where the search starts ; defaults to 0

  end : Optional[int] = the position from where the search has to end ; defaults to the length of string

  ======================================================================================================

  Exceptions :

  ValueError : the argument is not found or index is out of range

"""

string : str = "welcome to pydemo"
print(
  string.index("pydemo")
)

# Output :
# 11

# ==================
#
# Case : SUBSTRING does not exist in STRING :

print(
  string.index("hola")
)

# Output :
# ValueError: substring not found