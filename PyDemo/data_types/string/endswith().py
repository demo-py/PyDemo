"""

  str.endswith(
    suffix : str,
    start : Optional[int],
    end : Optional[int]
  )

  Returns True if a string ends with the given suffix, otherwise returns False

  =====================================================================================================

  Parameters :

  suffix : str = suffix is nothing but a string that needs to be checked

  start : Optional[int] = starting position from where suffix is needed to be checked within the string

  end : Optional[int] = Ending position - 1 from where suffix is needed to be checked within the string

  =====================================================================================================

"""

string = "sample string"
print(
  string.endswith("ing")
)

# Output :
# True