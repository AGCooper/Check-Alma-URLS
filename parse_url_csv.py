#!/usr/bin/python3
import sys

#input: Portfolio,53271685970002486,https://proxy.library.emory.edu/login?url=http://infoweb.newsbank.com/?db=NEMB
#output: http://pid.emory.edu/dpp5j_|_990032702130302486_|_1

def main():

   delim = "_|_"
   for line in sys.stdin:
       line = line.rstrip("\n")
       line = line.split(",")
       sys.stdout.write(line[2] + delim + line[1] + "\n")

if __name__=="__main__":
    sys.exit(main())
