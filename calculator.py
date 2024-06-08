from tkinter import *

root = Tk()
root.title('Calculator Of Professor')

entry=Entry(root,width=35,border=7)
entry.grid(row=0,column=0,columnspan=3)
# entry.pack()

def add(num):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(num))
    return

def buttons(tex,r,c,n):
    button= Button(root,text=tex,padx=40,pady=20,command=lambda: add(n))
    button.grid(row=r,column=c)
    # button.pack()
    
def clean():
    entry.delete(0,END)
def clear(tex,r,c):
    button= Button(root,text=tex,padx=83,pady=20,command=clean)
    button.grid(row=r,column=c,columnspan=2)

def addi():
    firstnum = entry.get()
    global fnum
    global math
    math = '+'
    fnum = int(firstnum)
    entry.delete(0,END)
def subs():
    firstnum = entry.get()
    global fnum
    global math
    math = '-'
    fnum = int(firstnum)
    entry.delete(0,END)
def multi():
    firstnum = entry.get()
    global fnum
    global math
    math = '*'
    fnum = int(firstnum)
    entry.delete(0,END)
def divi():
    firstnum = entry.get()
    global fnum
    global math
    math = '/'
    fnum = int(firstnum)
    entry.delete(0,END)
        
def addit(tex,r,c):
    button= Button(root,text=tex,padx=40,pady=20,command=addi)
    button.grid(row=r,column=c)
        
def su(tex,r,c):
    button= Button(root,text=tex,padx=40,pady=20,command=subs)
    button.grid(row=r,column=c)
        
def mu(tex,r,c):
    button= Button(root,text=tex,padx=40,pady=20,command=multi)
    button.grid(row=r,column=c)
        
def di(tex,r,c):
    button= Button(root,text=tex,padx=40,pady=20,command=divi)
    button.grid(row=r,column=c)
    
def equp():
    secnum = entry.get()
    entry.delete(0,END)

    if math == '+':
        entry.insert(0,int(fnum)+int(secnum))
    if math == '-':
        entry.insert(0,int(fnum)-int(secnum))
    if math == '*':
        entry.insert(0,int(fnum)*int(secnum))
    if math == '/':
        entry.insert(0,float(fnum)/float(secnum))
                
    
    
    
def equ(tex,r,c):
    button= Button(root,text=tex,padx=83,pady=20,command=equp)
    button.grid(row=r,column=c,columnspan=2)
    # button.pack()
    

    
buttons('7',1,0,7)
buttons('8',1,1,8)
buttons('9',1,2,9)
buttons('4',2,0,4)
buttons('5',2,1,5)
buttons('6',2,2,6)
buttons('1',3,0,1)
buttons('2',3,1,2)
buttons('3',3,2,3)
buttons('0',4,0,0)
su('-',5,0)
mu('*',5,1)
di('/',5,2)
clear('AC',6,1)
addit('+',6,0)
equ('=',4,1)









# button1= Button(root,text='1',padx=40,pady=20,command=add)
# button2= Button(root,text='2',padx=40,pady=20,command=add)
# button3= Button(root,text='3',padx=40,pady=20,command=add)
# button4= Button(root,text='4',padx=40,pady=20,command=add)
# button5= Button(root,text='5',padx=40,pady=20,command=add)
# button6= Button(root,text='6',padx=40,pady=20,command=add)
# button7= Button(root,text='7',padx=40,pady=20,command=add)
# button8= Button(root,text='8',padx=40,pady=20,command=add)
# button9= Button(root,text='9',padx=40,pady=20,command=add)
# button10= Button(root,text='0',padx=40,pady=20,command=add)
# button11= Button(root,text='Clear',padx=40,pady=20,command=add)
# button12= Button(root,text='+',padx=40,pady=20,command=add)

# button1.grid(row=3,column=0)
# button2.grid(row=3,column=1)
# button3.grid(row=3,column=2)
# button4.grid(row=2,column=0)
# button5.grid(row=2,column=1)
# button6.grid(row=2,column=2)
# button7.grid(row=1,column=0)
# button8.grid(row=1,column=1)
# button9.grid(row=1,column=2)
# button10.grid(row=4,column=1)
# button11.grid(row=4,column=2)
# button12.grid(row=4,column=0)


root.mainloop()