"""

str.count(
  substring : str,
  start : Optional[int] = 0,
  end : Optional[int] = ...
)

Returns the number of occurences of a substring within a string


Parameters :

substring : substring whose count is to be found

start : starting index ; defaults to 0

end : ending index ; defaults to length of string

"""

string : str = "sample string"
substring = "s"
print(
  string.count(
    substring
  )
)

# Output :
# 2