#my_contacts_list.py
import py
from graphics import *
import button
class Contact:
    def __init__(self,contact_content):
        #contact_content is a dictionary including name, mobilephone,
        #office_phone, email, address. If any of them doesn't be input, it should
        #be set as None
        self.name=contact_content['name']
        self.mobilephone=contact_content['mobilephone']
        self.office_phone=contact_content['office_phone']
        self.email=contact_content['email']
        self.address=contact_content['address']
    def display(self,win):
        pass
class Contact_list:
    def __init__(self):
        self.list={}
    def add_contact(self,contact_name,contact_content):
        self.list[name]=contact_content
    def delete_contact(self,name):
        del self.list[name]

def set_entry(win):
    Text(Point(8,12),'name:').draw(win)
    namein=Entry(Point(12,12),10)
    namein.draw(win)
    Text(Point(8,10),'mobile:').draw(win)
    mobilein=Entry(Point(12,10),15)
    mobilein.draw(win)
    Text(Point(8,8),'office phone:').draw(win)
    officein=Entry(Point(12,8),15)
    officein.draw(win)
    Text(Point(8,6),'email:').draw(win)
    emailin=Entry(Point(12,6),22)
    emailin.draw(win)
    Text(Point(8,4),'address:').draw(win)
    addressin=Entry(Point(12,4),22)
    addressin.draw(win)
def set_button(win):
    add=button.button(win,Point(8,2.5),1.5,0.8,'add')
    dispaly_all=button.button(win,Point(2,1),2.5,0.8,'display all')
    menu=button.button(win,Point(5,1),1.5,0.8,'menu')
    next_=button.button(win,Point(4,2.5),1.5,0.8,'next')
    last=button.button(win,Point(1.5,2.5),1.5,0.8,'last')
def draw_contacts(win):
    tt=Text(Point(2,13.5),'CONTACTS:')
    tt.draw(win)
    
    tt.setSize(12)
    
def main():
    win=GraphWin('contact list',500,500)
    win.setCoords(0,0,15,15)
    set_entry(win)
    set_button(win)
    draw_contacts(win)
main()
