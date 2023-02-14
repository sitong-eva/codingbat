def monkey_trouble(a_smile, b_smile):
  """
  This is a function to see if we are in trouble.
  """
  if a_smile== True and b_smile==True:
    return True
  if a_smile == False and b_smile == False:
    return True
  else:
    return False