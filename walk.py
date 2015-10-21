import sys
import os
import hashlib
from hashlib import md5

def fast_md5(fpath):
    ha=md5()
    with open(fpath,"rb") as ff:
        data=ff.read(512*1024)
        while data:
            ha.update(data)
            data=ff.read(512*1024)
    return ha.hexdigest().lower()

class SamplePusher:
    
    def push(self, src):
        if os.path.getsize(src) > 10*1024*1024:
            return          
        m = fast_md5(src)
        #sha1 = hashlib.sha1(stream).hexdigest().lower()
        #md5 = hashlib.md5(stream).hexdigest().lower()
        print m
        pass
    

def main(argv):
    if len(argv) != 2:
        print "invalid argument"
        return
    pusher = SamplePusher()
    src = argv[1]
    if not os.path.exists(src):
        print "path does not exist"
        return -1
    
    if os.path.isdir(src):
        for root, dirnames, filenames in os.walk(src):
            for fn in filenames:
                _src = os.path.join(root, fn)
                pusher.push(_src)
        pass
    elif os.path.isfile(src):
        pusher.push(src)
        pass
    else:
        print "invalid input type"
        return -1
    pass

if __name__ == '__main__':
    main(sys.argv)
