#this program is going to find the IP appearing most frequently among the 100,000,000 ones

import random 
import time
file_lines=int(1e8)

def generateIP():
    return '10.197.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))+'\n'
def clearFile():
    IP_file=open('IP_file.txt','w')
    IP_file.close()


def generateFile():
    IP_file=open('IP_file.txt','a')
    for i in range(file_lines):
        IP_file.write(generateIP())
        
    IP_file.close()

def generateFile2():
    IP_file=open('IP_file.txt','a')
    IP=[]
    for i in range(file_lines):
        IP.append(generateIP())
        
    IP_file.writelines(IP)
    IP_file.close()

def IP_search():
    IP_file=open('IP_file.txt','r')
    IPs={}
    for i in range(file_lines):
        try:
            IPs[IP_file.readline()]+=1
        except:
            IPs[IP_file.readline()]=1
    #print IPs
    IP_file.close()
    return IPs

def sort(adict):
    #adict={'a':1,4:4,5:5,2:2,3:3}
    maxIPtimes=0
    for item in adict:
        if adict[item]>maxIPtimes:
            maxIP=item
    print "the most frequently appeared IP is ",item," , appearing for",adict[item]," times.\n"
    
def main():
    print time.ctime()
    clearFile()
    generateFile()
    IPs=IP_search()
    sort(IPs)
    print time.ctime()


    print "over"
clearFile()
  
    













