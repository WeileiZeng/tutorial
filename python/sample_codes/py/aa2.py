# -*- coding:utf-8 -*-
import threading
from time import sleep, ctime
threading
loops = [4,2]

def loop(nloop, nsec):
    print 'start loop ',nloop,' at time: ', ctime()
    sleep(nsec)
    print 'done loop ',nloop,' at time: ', ctime()
    
if __name__=='__main__':
    print 'starting program at time: ', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        print 1
        t = threading.Thread(target=loop, args=(i,loops[i]))
        threads.append(t)

    for i in nloops:
        print 2
        threads[i].start()

    for i in nloops:
        print 3
        threads[i].join()
        
    print 'done program at time: ', ctime()
