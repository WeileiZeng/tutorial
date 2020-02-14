import thread
import time
import threading

def write(start):
    for i in range(5):
        print start+i
        time.sleep(1)
def main():
    a=threading.Thread(target=write,args=1)
    b=threading.Thread(target=write,args=10)
    for i in range(5):
        print 100+i
        time.sleep(0.001)
    time.sleep(0.1)
    a.start()
    time.sleep(0.1)
    b.start()
    print 'the main program end'
def main2():
    print 'start loop 1'
    thread.start_new_thread(write,(1,2))
    print 'start loop 2'
    thread.start_new_thread(write,10)
    
main()
