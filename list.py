import sys
import os

def main(argv):
    if len(argv) != 2:
        print "invalid argument"
        return		
    all_list = open(argv[1], "rb").read().replace("\r\n", "\n").split("\n")
    li = {}.fromkeys(all_list).keys()
    for ele in li:
        if ele:
            print ele			
	
if __name__ == '__main__':
    main(sys.argv)