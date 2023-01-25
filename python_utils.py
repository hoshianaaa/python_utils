import os,sys

# input: string list (ex. ["aaa","bbb","ccc"])
# output: string (ex. "aaa,bbb,ccc"
def list2string(list):
  ret = ""
  for l in list:
    ret = ret + l + ","
  return ret[:-1]

# https://softhints.com/python-change-directory-parent/
def getud_name():
  return os.path.abspath(os.curdir).split("/")[-2]
