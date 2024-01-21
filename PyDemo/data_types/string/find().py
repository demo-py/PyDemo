"""

  str.find(
    substring : str,
    start : Optional[int],
    end : Optional[int]
  )

  Finds the index of a substring within a given string

  =================================================================================================

  Parameters :

  substring : str = substring that needs to be searched in the given string

  start : Optional[int] = starting index where the substringg needs to be checked within the string

  end : Optional[int] = the index of the last value for the specified range.
                        It is excluded while checking

  =================================================================================================

"""

string : str = "sample string"

print(string.find("str"))

# Output :
# 7


# case    : if SUBSTRING is not found in the string
# returns : -1

print(string.find("demo"))

# Output :
# -1