#!/opt/rh/python27/root/usr/bin/python
import sys
import re
r"""
Title: Parse text file for url
Author: Alex Cooper
Date: 04/19/2018
Purpose: Parse text file produced 
by marc_to_txt for urls to check
"""
#001||990032719490302486
#856|41|\puhttp://rstl.royalsocietypublishing.org/content/50.toc

def main():
  state = "init"
  rec_delim = "****"
  count = 0
  delim = "_|_"
  mmsid = ""
  url = ""
  sf_856 = ""
  try:
    for line in sys.stdin:
      line = line.rstrip("\n")
      if state == "init":
        try:
          if line[0:4] == rec_delim:
            try:
              state = "new"
            except:
              sys.stderr.write("could not set state to new" + "\n")
        except:
          sys.stderr.write("could not find delimiter" + "\n")
      elif state == "new":
        if line[0:4] == "001|":
          mmsid = line[5: ]
        elif line[0:5] == "856|4":
          url = re.search(r"\\pu(.*)", line)
          if url:
            url = url.group(1)
            sf_856 = re.search(r"^(.*)\\p", url)
            if sf_856:
              url = sf_856.group(1)
          else:
            continue
          print url + delim + mmsid + delim + "1"
  except:
    sys.stderr.write("could not parse lines" + "\n")

if __name__=="__main__":
  sys.exit(main())
