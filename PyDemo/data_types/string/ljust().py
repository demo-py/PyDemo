"""

  str.ljust(
    length : int,
    fillchar : Optional[str] = " "
  )

  Returns a new string of given length after substituting a given character in right side of original string

  ==========================================================================================================

  Parameters :

  length : int = length of the modified string

  fillchar : Optional[str] = characters which needs to be padded ; defaults to SPACE

"""

string : str = "pydemo"
print(string.ljust(10, "-"))

# Output :
# pydemo----

# =====================================================================================================
#
# Case : LENGTH is less than or equal to the length of the string, the original string then is return :

string : str = "pydemo"
print(string.ljust(5, "#"))

# Output :
# pydemo