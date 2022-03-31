def unique_set(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False;
print(unique_set([5,1,2,2,4]))
print(unique_set([2,4,5,7,9]))
