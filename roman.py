# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def two(no):
    
    dict19 = {'1':'I','2':'II','3':'III','4':'IV','5':'V','6':'VI','7':'VII','8':'VIII','9':'IX'}
    dict10 = {'10':'X','20':'XX','30':'XXX','40':'XL','50':'L','60':'LX','70':'LXX','80':'LXXX','90':'XC'}
    wnum, ext, ext1 = '','',''    
    
    if no[0] == '0':
        no = 2*int(no)//2
    if str(no) in dict19:
        wnum = dict19.get(str(no))
    elif str(no) in dict10:
        wnum = dict10.get(str(no))
    else:
        ext = str(no[0])+'0'
        ext1 = int(no)-int(ext)
        wnum = dict10[ext] + dict19[str(ext1)]
    return wnum   

def three(no):
    
    dict100 = {'100':'C','200':'CC','300':'CCC','400':'CD','500':'D','600':'DC','700':'DCC','800':'DCCC','900':'CM','1000':'M'}   
    wnum, ext, ext1 = '','','' 

    if no[0] == '0':
        no = str(2*int(no)//2)
    if len(no)<3:
        two(str(no))
    elif str(no) in dict100:
        wnum = dict100.get(str(no))
    else:
        ext = str(no[0])+'00'
        ext1 = str(int(no)-int(ext))
        wnum = dict100[ext] + two(ext1)
    return wnum


arabic = input("Enter an Arabic numeral upto 1000: ")
if(len(arabic)<3):
    print(f"{arabic} in Roman is",two(arabic))
elif(len(arabic)==3 or arabic=='1000'):
    print(f"{arabic} in Roman is",three(arabic))
else:
    print("Number should be less than or equal to 1000.")