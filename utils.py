# input: string list (ex. ["aaa","bbb","ccc"])
# output: string (ex. "aaa,bbb,ccc"
def list2string(list):
  ret = ""
  for l in list:
    ret = ret + l + ","
  return ret[:-1]
