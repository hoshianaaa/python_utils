import os,sys
import subprocess

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

def run_bash(cmd):
  ret = subprocess.Popen(cmd, shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
  out,err = ret.communicate()
  return out,err

if __name__ == '__main__':
  out,err = run_bash("ls")
  print("*** out ***")
  print(out)
  print("*** error ***")
  print(err)
