for i in xrange(1,13):  
     for j in xrange(1,32):
       if i==2 and j>28:  
           break 
       elif i in [4,6,9,11] and j>30:  
           break 
       else:  
            strDate = i<10 and '0'+str(i) or str(i)  
            strDate += j<10 and '0'+str(j) or str(j)  

            print strDate[::-1],strDate 
