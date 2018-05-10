#!/usr/bin/python3
import requests
import sys
import time

def main():

    count = 0
    for line in sys.stdin:
        response = ""
        line = line.rstrip("\n")
        line = line.split("_|_")
        url = line[0]
        mmsid = line[1]
        delim = "	"
        try:
            count += 1
            response = requests.head(url, timeout=5)
        except requests.exceptions.RequestException as e:
            sys.stderr.write(str(e) + "\n")
            print("Check " + str(url) + delim + "in " + str(mmsid))
            continue
        if response:
            status = response.status_code
#            print(status)
#            print(response)
            if status > 400:
                print("Check " + str(url) + delim + "in " + str(mmsid))
            else:
                continue
        else:
            continue
    print(str(count) + " Urls processed")
#    print(time.asctime(time.localtime()))

if __name__=="__main__":
    sys.exit(main())
