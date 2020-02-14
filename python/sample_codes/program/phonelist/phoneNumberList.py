#phoneNumberList.py
'''

##add_record
##delete_record
##display_all_record
##query_by_name
##modify_record
##add_from_a_txt_file
##write_to_a_text_file
##sort
##Quit
the imformation of all clients is saved in the file 'phone_number_list.txt'.
The imformation of each client occupies one line in the file, from serial
number, name, family number, mobilephone number, email and address. For example,

15 Mike 2657897 13768687373 hello@126.com No.800 Dongchuan Road, Shanghai

if some of these terms are unknown, they will be filled by ***

for convenience, I write it as
0 serialnumber
1 name
2 family number
3 mobilephone number
4 email
5 address.

Once the program runs, These imformation will be recorded in the dictionary
named all_records, family_number_records, mobilephone_number_records and
email_records. In all_records, the key is each client'
name, and its value is a list assigned by all of his imformation. Whereas in
mobilephone_number_records, the key is still the name of each client, its value is only
his mobilephone number. So do the remained two dictionaries.


'''

import string


all_records={}
mobilephone_number_records={}
family_number_records={}
email_records={}


class client:
    def __init__(self,imformation_list):
        self.No=imformation_list[0]
        self.name=imformation_list[1]
        self.family_number=imformation_list[2]
        self.mobilephone_number=imformation_list[3]
        self.address=imformation_list[4]
        self.email=imformation_list[5]
        



    
def interface():
    print 'System of Phone Number List'
    print '1. add_record'
    print '2. delete_record'
    print '3. display_all_record'
    print '4. query_by_name'
    print '5. modify_record'
    print '6. add_from_a_txt_file'
    print '7. write_to_a_text_file'
    print '8. sort'
    print '9. quit'
    print 'Please choose <1--9>'

def getInput():
    return input('enter: ')

def getRecord():
    record_file=open('phone_number_list.txt','r')
    file_content=record_file.readlines()
    record_file.close()

    if len(file_content)<5:
        print 'there is no record before.'
        
        return all_records,family_number_records,mobilephone_number_records,email_records
    else:
        for item in file_content[3:]:
            imformation_list=string.split(item)
            name=imformation_list[1]
            mobilephone_number_records[name]=imformation_list[3]
            family_number_records[name]=imformation_list[2]
            email_records[name]=imformation_list[4]
            all_records[name]=imformation_list
def clearFile():
    IP_file=open('phone_number_list.txt','w')
    IP_file.close()

def saveInformation():
    clearFile()
    IP_file=open('phone_number_list.txt','w')
    IP_file.writelines('PhoneNumberList\nTotal number is\n'+str(len(all_records))+'\n')
    IP_file.writelines('No\tname\tfamily number\tmobile phone\temail\taddress\n')
    names=all_records.keys()
    names.sort()
    No=1
    for name in names:
        information_list=all_records[name]
        IP_file.writelines(str(No)+'\t'+information_list[1]+'\t'+information_list[2]+'\t'+information_list[3]+'\t'+information_list[4]+'\t'+information_list[5]+'\n')
        print str(No)+'\t'+information_list[1]+'\t'+information_list[2]+'\t'+information_list[3]+'\t'+information_list[4]+'\t'+information_list[5]+'\n'
        No+=1
    IP_file.close()    
def saveCopy():
    
def displayAllRecord():
    print 'No\tname\tfamily number\tmobile phone\temail\taddress\n'
    for item in all_records:
        print all_records[item]
def add_record_interface():
    print ''
def addRecordInterface():
    print 'Please input the imformation successively, and press enter directly if you don\'t know the item'
    
    
    name=raw_input('name: ')
    if name=='':
        name='***'
    family_number=raw_input('family_number: ')
    if family_number=='':
        family_number='***'
    mobilephone_number=raw_input('mobilephone_number: ')
    if mobilephone_number=='':
        mobilephone_number='***'
    email=raw_input('email: ')
    if email=='':
        email='***'
    address=raw_input('address: ')
    if address=='':
        address='***'
    
    imformation_list=[0,name, family_number, mobilephone_number, email, address]
    print imformation_list
    return imformation_list
def addRecord(imformation_list):

    name=imformation_list[1]
    mobilephone_number_records[name]=imformation_list[3]
    family_number_records[name]=imformation_list[2]
    email_records[name]=imformation_list[4]
    all_records[name]=imformation_list

##def delete_record
##def display_all_record
##def query_by_name
##def modify_record
##def add_from_a_txt_file
##def write_to_a_text_file
##def sort
##def Quit

#interface()
#getInput()
#getRecord()    

def run(order):
    if order ==1:
        addRecord(addRecordInterface())

    

def main():
    getRecord()
    interface()
    run(getInput())
    saveInformation()

    displayAllRecord()
main()
    


