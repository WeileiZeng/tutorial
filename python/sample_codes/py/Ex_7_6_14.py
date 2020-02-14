# Ex_7_6_14.py  
import string
def date_split(date):   # return list (like [mm,dd,yy])
    datelists=string.split(date,'/')
    mm=int(datelists[0])
    dd=int(datelists[1])
    yy=int(datelists[2])
    return[mm,dd,yy]

def IS_leap_year(yy):   # return True or False
    if yy%4==0:
        if yy%100==0:
            return 'false'
        else:
            return 'ture'
    else:
        return 'false'

def IS_valid_date(ll):  # return True or False
    mm=ll[0]
    dd=ll[1]
    yy=ll[2]
    if mm in [1,3,5,7,8,10,12]:
        if dd<32 and dd>0:
            return 'ture'
        else:
            return 'false'
    elif mm in [4,6,9,11]:
        if dd<31 and dd>0:
            return 'ture'
        else:
            return 'false'
    elif mm==2:
        if dd<29 and dd>0:
            return 'ture'
        else:
            if IS_leap_year(yy)=='ture' and  dd ==29:
                return 'ture'
            else:
                                return 'false'
    else:
                return 'false'

def main():
    date_s = raw_input('enter the date in the form month/day/year: ')
    ll = date_split(date_s)

    y = IS_valid_date(ll)
    return y
    print y

main()      
        


        
