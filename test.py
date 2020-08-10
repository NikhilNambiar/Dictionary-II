from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
root=Tk()
root.geometry('600x600')
root.configure(background="lawn green");
root.title("Relief Funds")
'''canvas = Canvas(root,width=600,height=600)
canvas.pack()
pilImage = Image.open("background.png")
image = ImageTk.PhotoImage(pilImage)
img= canvas.create_image(0,0,anchor=NW,image=image)''' 
fn=StringVar()

ln=StringVar()
ad=StringVar()
st=StringVar()
rad=IntVar()
em=StringVar()
ph=IntVar()
sld1=0
sld2=0
a=0
b=0
sel=0
sel1=0
minidb=mysql.connector.connect(
     host="localhost",
     user="root",
     passwd="(Hello123)",
     database="Mini"
)

minic=minidb.cursor(buffered=True)

def second_win():
 
    fn1=fn.get();
    ln1=ln.get();
    ad1=ad.get();
    st1=st.get();
    em1=em.get()
    ph1=ph.get();  

    if fn1=="" or ln1=="" or ad1=="" or st1=="" or em1=="" or em1=="" or ph1==0:
        messagebox.showerror("Error","Please Enter your details")

    else:

        minic.execute("INSERT INTO DONOR (FNAME,LNAME,ADDRRESS,STATE,PHONE_NUMBER) VALUES(%s,%s,%s,%s,%s)",(fn1,ln1,ad1,st1,ph1));
        minidb.commit()
    
        window=Tk()
        window.geometry('300x300')
        window.configure(background="lawn green")
        window.title("Relief Funds")
        '''canvas1= Canvas(window,width=300,height=300)
        canvas1.pack()
        pilImage1= Image.open("background.png")
        image1= ImageTk.PhotoImage(pilImage1)
        img1= canvas.create_image(0,0,anchor=NW,image=image1)'''
        hie=IntVar(master=window)
        label_7=Label(window,text="Choose An Option:",width=20,bg="dark green",fg="white",font=("arial",12,"bold")).pack()
        button_2=Radiobutton(window, text="Donation for Soldiers",padx=5,variable=hie,value=1).place(x=10,y=70)
        #print(var)
        button_3=Radiobutton(window, text="Donation for Flood-Affected Victims",padx=5,variable=hie,value=2).place(x=10,y=120)
    #   print(var1) 
        button_4=Radiobutton(window, text="Admin",padx=5,variable=hie,value=3).place(x=10,y=170)
        #print(hie)
        button_5=Button(window, text='Submit',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=lambda:third_win(hie,fn)).place(x=30,y=220)    
        button_6=Button(window, text='Cancel',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=window.destroy).place(x=150,y=220)

def third_win(hie,fn):
    fn1=fn.get()
    print(fn1)
    print("selection:",hie.get())
    global sel
    sel=hie.get()
    if sel==1:
        window2=Tk()
        window2.geometry('550x300')
        window2.configure(background="lawn green")
        window2.title("Relief Funds")
        cb=StringVar(master=window2)
        '''canvas2= Canvas(window2,width=550,height=300)
        canvas2.pack()
        pilImage2= Image.open("background.png")
        image2= ImageTk.PhotoImage(pilImage2)
        img2= canvas.create_image(0,0,anchor=NW,image=image2)'''
        label_8=Label(window2,text="In the dropdown menu below,\n there is a list of soldiers who have sacrificed their life for this nation.\n Choose the name of the soldier you want to donate money to:",width=50,fg="white",bg="dark green",font=("arial",12,"bold")).place(x=20,y=10)
        cb=ttk.Combobox(window2,values=['Karnail Singh','Ravi Paul','Rakesh Singh','Javra Munda','Naiman Kajur','Janrao','SK Vidyarthi','G Sanokhar','Rajesh KR SIngh','B Ghorai','Ashok Kumar Singh','Pankaj Tripathi','Amit Kumar','Maneshwar Basumatari','Sukhjinder Singh','Rohitash Lamba','Subramaniam G','Vijay Soreng','PK Sahoo','TK Prabhakaran'])
        cb.place(x=140,y=110)
        cb.config(width=40)
        cb.current(1)
        print(cb.current(),cb.get())
        button_7=Button(window2, text='Submit',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=lambda:fourth_win(sel,cb,fn)).place(x=120,y=220)
        button_8=Button(window2, text='Cancel',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=window2.destroy).place(x=270,y=220)

        
    elif sel==2:
        window3=Tk()
        window3.geometry('550x300')
        window3.configure(background="lawn green")
        window3.title("Relief Funds")
        label_10=Label(window3,text="In the dropdown menu below,\n are the list of foundations which are helping the flood-affected victims.\n Choose th charitable foundation you \n want to donate to:",width=50,fg="white",bg="dark green",font=("arial",12,"bold")).place(x=20,y=10)
        cb=ttk.Combobox(window3,values=["KARNATAKA'S CHIEF MINISTER'S RELIEF FUND","KERALA'S CHIEF MINISTER'S RELIEF FUND","MAHARASHTRA'S CHIEF MINISTER'S RELIEF FUND","ASSAM'S CHIEF MINISTER'S RELIEF FUND","RAJASTHAN'S CHIEF MINISTER'S RELIEF FUNDS"])
        cb.place(x=140,y=130)
        cb.config(width=40)
        cb.current(1)
        #print(cb.current(),cb.get())
        button_7=Button(window3, text='Submit',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=lambda:fourth_win(sel,cb,fn)).place(x=120,y=220)
        button_8=Button(window3, text='Cancel',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=window3.destroy).place(x=270,y=220)
    elif sel==3:
        window3=Tk()
        window3.geometry('450x330')
        window3.configure(background="lawn green")
        window3.title("Relief Funds")
        var=IntVar(master=window3)
        user=StringVar(master=window3)
        pwd=StringVar(master=window3)
        label_2=Label(window3,text="Enter your details:",width=15,fg="black",bg="yellow",font=("arial",12,"bold")).pack()
        label_1=Label(window3,text="Username:",width=10,bg="dark green",fg="white",font=("arial",12,"bold")).place(x=40,y=80)
        entry_1=Entry(window3,textvar=user).place(x=180,y=80)
        label_2=Label(window3,text="Password:",width=10,bg="dark green",fg="white",font=("arial",12,"bold")).place(x=40,y=130)
        entry_2=Entry(window3,textvar=pwd,show="*").place(x=180,y=130)
        button_5=Button(window3, text='Submit',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=lambda:eighth_win(user,pwd)).place(x=70,y=220)   
        button_6=Button(window3, text='Cancel',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=window3.destroy).place(x=230,y=220)
        '''label_7=Label(window3,text="Choose An Option:",width=20,bg="thistle1",font=("arial",12,"bold")).pack()
        button_2=Radiobutton(window3, text="Soldiers",padx=5, variable=var,value=1).place(x=10,y=70)
        button_3=Radiobutton(window3, text="Goverment Relief Fund",padx=5,variable=var,value=2).place(x=10,y=120)
        button_4=Radiobutton(window3, text="Donor",padx=5,variable=var,value=3).place(x=10,y=170)
        button_5=Button(window3, text='Submit',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=lambda:eighth_win(var)).place(x=30,y=220)    
        button_6=Button(window3, text='Cancel',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=window3.destroy).place(x=150,y=220)'''

def fourth_win(sel,cb,fn):
    fn1=fn.get()
    print(fn1)
    global sld1
    global a
    global b
    window4=Tk()
    window4.geometry('600x600')
    window4.configure(background="lawn green")
    window4.title("Relief Funds")
    nam=StringVar(master=window4)
    amt=IntVar(master=window4)
    acc=StringVar(master=window4)
    date=StringVar(master=window4)
    if sel==1:
        print(cb.get())
        #window4=Tk()
        '''window4.geometry('600x600')
        window4.configure(background="thistle1")
        window4.title("Relief Funds") '''
        sld1=cb.get()
        print(sld1)
        label_1=Label(window4,text="These are the account details of the soldier selected:",width=40,fg="white",bg="dark green",font=("arial",12,"bold")).pack()
        label_12=Label(window4,text="Soldier Name:",bg='dark green',fg='white',font=("arial",10,"bold")).place(x=185,y=30)
        Message(window4,text=sld1,width=100,justify=CENTER,bg='yellow',fg='black',font=("airal",10,"bold")).place(x=295,y=30)
        label_13=Label(window4,text="Bank Name:",bg='dark green',fg='white',font=("arial",10,"bold")).place(x=185,y=70)
        minic.execute("SELECT BANK_NAME FROM soldiers WHERE NAME=(%s)",(sld1,))
        a=minic.fetchall()
        print(a)
        Message(window4,text=a,width=200,justify=CENTER,bg='yellow',fg='black',font=("arial",10,"bold")).place(x=280,y=70)
        label_14=Label(window4,text="Account Number:",bg='dark green',fg='white',font=("arial",10,"bold")).place(x=185,y=110)
        minic.execute("SELECT ACC_NO FROM SOLDIERS WHERE NAME=(%s)",(sld1,))
        b=minic.fetchall()
        Message(window4,text=b,width=200,justify=CENTER,bg='yellow',fg='black',font=("arial",10,"bold")).place(x=310,y=110)
        label_1=Label(window4,text="Enter your bank details:",width=30,fg="white",bg="dark green",font=("arial",12,"bold")).place(x=130,y=150)
        label_2=Label(window4,text="Name:",width=10,bg="dark green",fg="white",font=("arial",12,"bold")).place(x=110,y=210)
        entry_1=Entry(window4,textvar=nam).place(x=250,y=213)
        label_3=Label(window4,text="Email ID:",width=10,bg="dark green",fg="white",font=("arial",12,"bold")).place(x=110,y=250)
        entry_2=Entry(window4,textvar=acc).place(x=250,y=253)
        label_4=Label(window4,text="Amount:",width=10,bg="dark green",fg="white",font=("arial",12,"bold")).place(x=110,y=290)
        entry_3=Entry(window4,textvar=amt).place(x=250,y=293)
        label_5=Label(window4,text="Date:",width=10,bg="dark green",fg="white",font=("arial",12,"bold")).place(x=110,y=330)
        entry_2=Entry(window4,textvar=date).place(x=250,y=333)
        label_6=Label(window4,text="Select the name of the bank:",bg="dark green",fg="white",width=30,font=("arial",12,"bold")).place(x=150,y=370)
        cb1=ttk.Combobox(window4,width=40,values=['Axis Bank','Bank Of Baroda','State Bank Of India','Canara Bank','Indian Overseas Bank','Federal Bank','ICICI Bank'])
        cb1.place(x=170,y=420)
        button_1=Button(window4, text='Submit',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=lambda:fifth_win(sel,cb,cb1,nam,acc,amt,fn)).place(x=140,y=520)    
        button_2=Button(window4, text='Cancel',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=window4.destroy).place(x=330,y=520)
      
        
        
    elif sel==2:
        '''window4=Tk()
        window4.geometry('600x600')
        window4.configure(background="thistle1")
        window4.title("Relief Funds") '''
        label_1=Label(window4,text="The account details are listed below:",width=40,fg="white",bg="dark green",font=("arial",12,"bold")).pack()
        sld1=cb.get()
        print(sld1)
        label_12=Label(window4,text="Governnment Name:",bg='dark green',fg='white',font=("arial",10,"bold")).place(x=115,y=30)
        Message(window4,text=sld1,width=500,justify=CENTER,bg='yellow',fg='black',font=("arial",10,"bold")).place(x=265,y=30)
        label_13=Label(window4,text="Bank Name:",bg='dark green',fg='white',font=("arial",10,"bold")).place(x=115,y=70)
        minic.execute("SELECT BANK_NAME FROM govt_body WHERE GNAME=(%s)",(sld1,))
        a=minic.fetchall()
        print(a)
        #print(b)
        Message(window4,text=a,width=200,justify=CENTER,bg='yellow',fg='black',font=("arial",10,"bold")).place(x=265,y=70)
        label_14=Label(window4,text="Account Number:",bg='dark green',fg='white',font=("arial",10,"bold")).place(x=115,y=110)
        minic.execute("SELECT ACC_NO FROM govt_body WHERE GNAME=(%s)",(sld1,))
        b=minic.fetchall()
        Message(window4,text=b,width=200,justify=CENTER,bg='yellow',fg='black',font=("arial",10,"bold")).place(x=265,y=110)
        label_1=Label(window4,text="Enter your bank details:",width=30,fg="white",bg="dark green",font=("arial",12,"bold")).place(x=130,y=150)
        label_2=Label(window4,text="Name:",width=10,bg="dark green",fg="white",font=("arial",12,"bold")).place(x=110,y=210)
        entry_1=Entry(window4,textvar=nam).place(x=250,y=210)
        label_3=Label(window4,text="Email ID:",width=10,bg="dark green",fg="white",font=("arial",12,"bold")).place(x=110,y=250)
        entry_2=Entry(window4,textvar=acc).place(x=250,y=250)
        label_4=Label(window4,text="Amount:",width=10,bg="dark green",fg="white",font=("arial",12,"bold")).place(x=110,y=290)
        entry_3=Entry(window4,textvar=amt).place(x=250,y=290)
        label_5=Label(window4,text="Date:",width=10,bg="dark green",fg="white",font=("arial",12,"bold")).place(x=110,y=330)
        entry_2=Entry(window4,textvar=date).place(x=250,y=330)
        print(amt)
        label_6=Label(window4,text="Select the name of the bank:",width=30,bg="dark green",fg="white",font=("arial",12,"bold")).place(x=150,y=370)
        cb1=ttk.Combobox(window4,width=40,values=['Axis Bank','Bank Of Baroda','State Bank Of India','Canara Bank','Indian Overseas Bank','Federal Bank','ICICI Bank'])
        cb1.place(x=170,y=420)
        button_1=Button(window4, text='Submit',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=lambda:fifth_win(sel,cb,cb1,nam,acc,amt,fn)).place(x=140,y=520)    
        button_2=Button(window4, text='Cancel',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=window4.destroy).place(x=330,y=520) 
        

def fifth_win(sel,cb,cb1,nam,acc,amt,fn):
    combo=cb1.get()
    print(combo)
    fn1=fn.get()
    print(fn1)
    nam1=nam.get()
    acc1=acc.get()
    amt1=amt.get()
    print(nam.get())
    print(amt.get())
    print(acc.get())
    if nam.get()=="" or acc.get()=="" or amt.get()==0:
        messagebox.showerror("Error","Please Enter the details")
    else:
        window5=Tk()
        window5.geometry('450x330')
        window5.title("Relief Funds")
        window5.configure(background='lawn green')
        us=StringVar(master=window5)
        pas=StringVar(master=window5)
        minic.execute("UPDATE DONOR SET BANK_NAME=(%s) WHERE FNAME=(%s)",(combo,fn1))
        minidb.commit();
        if sel==1:
            minic.execute("INSERT INTO bank_details_soldier (Name,Email,Amount) VALUES(%s,%s,%s)",(nam1,acc1,amt1));
            minidb.commit();
            label_1=Label(window5,text="The bank selected is:",width=30,bg='dark green',fg='white',font=("arial",12,"bold")).pack()
            sel1=cb1.get()
            Message(window5,text=sel1,width=200,justify=CENTER,bg='yellow',fg='black',font=("arial",10,"bold")).pack()
            label_1=Label(window5,text="Username:",width=10,bg="dark green",fg="white",font=("arial",12,"bold")).place(x=40,y=80)
            entry_1=Entry(window5,textvar=us).place(x=180,y=80)
            label_2=Label(window5,text="Password:",width=10,bg="dark green",fg="white",font=("arial",12,"bold")).place(x=40,y=130)
            entry_2=Entry(window5,textvar=pas,show="*").place(x=180,y=130)
            button_5=Button(window5, text='Submit',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=lambda:sixth_win(sel,cb,us,pas,amt,nam,fn)).place(x=70,y=220)   
            button_6=Button(window5, text='Cancel',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=window5.destroy).place(x=230,y=220)

        elif sel==2:
            minic.execute("INSERT INTO bank_details_fav (Name,Email,Amount) VALUES(%s,%s,%s)",(nam1,acc1,amt1));
            minidb.commit();
            '''window5=Tk()
            window5.geometry('450x330')
            window5.title("Relief Funds")
            window5.configure(background='lawn green')'''
            label_1=Label(window5,text="The bank selected is:",width=30,bg='dark green',fg='white',font=("arial",12,"bold")).pack()
            sel1=cb1.get()
            #print(sel)
            Message(window5,text=sel1,width=200,justify=CENTER,bg='yellow',fg='black',font=("arial",10,"bold")).pack()
            label_1=Label(window5,text="Username:",width=10,bg="dark green",fg="white",font=("arial",12,"bold")).place(x=40,y=80)
            entry_1=Entry(window5,textvar=us).place(x=200,y=80)
            label_2=Label(window5,text="Password:",width=10,bg="dark green",fg="white",font=("arial",12,"bold")).place(x=40,y=130)
            entry_2=Entry(window5,textvar=pas,show="*").place(x=200,y=130)
            button_5=Button(window5, text='Submit',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=lambda:sixth_win(sel,cb,us,pas,amt,nam,fn)).place(x=70,y=220)   
            button_6=Button(window5, text='Cancel',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=window5.destroy).place(x=230,y=220)
            


def sixth_win(sel,cb,us,pas,amt,nam,fn):
    fn1=fn.get()
    print(fn1)
    nam2=nam.get()
    amt2=amt.get()
    us2=us.get()
    pas2=pas.get()
    print(us.get())
    print(pas.get())
    if sel==1:
        minic.execute("UPDATE bank_details_soldier SET username=(%s),password=(%s) WHERE Name=(%s)",(us2,pas2,nam2))
        minidb.commit();
        window6=Tk()
        window6.geometry('450x450')
        window6.title("Relief Funds")
        window6.configure(background='lawn green')
        label_1=Label(window6,text="Final display of details:",width=30,bg='dark green',fg='white',font=("arial",12,"bold")).pack()
        label_2=Label(window6,text="Soldier Name:",width=15,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=20,y=60)
        Message(window6,text=sld1,width=250,justify=CENTER,bg='yellow',fg='black',font=("arial",11,"bold")).place(x=170,y=59)
        label_3=Label(window6,text="Bank Name:",width=15,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=20,y=100)
        Message(window6,text=a,width=250,justify=CENTER,bg='yellow',fg='black',font=("arial",11,"bold")).place(x=170,y=99)
        label_4=Label(window6,text="Account NO:",width=15,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=20,y=140)
        Message(window6,text=b,width=250,justify=CENTER,bg='yellow',fg='black',font=("arial",11,"bold")).place(x=170,y=139)
        label_2=Label(window6,text="Amount:",width=15,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=20,y=180)
        Message(window6,text=amt2,width=250,justify=CENTER,bg='yellow',fg='black',font=("arial",11,"bold")).place(x=170,y=179)
        button_1=Button(window6, text='Proceed',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=lambda:seventh_win(sel,cb,amt,fn)).place(x=50,y=280)   
        button_2=Button(window6, text='Cancel',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=window6.destroy).place(x=190,y=280)

    elif sel==2:
        minic.execute("UPDATE bank_details_fav SET username=(%s),password=(%s) WHERE Name=(%s)",(us2,pas2,nam2));
        minidb.commit();
        window6=Tk()
        window6.geometry('550x400')
        window6.title("Relief Funds")
        window6.configure(background='lawn green')
        label_1=Label(window6,text="Final display of details:",width=30,bg='dark green',fg='white',font=("arial",12,"bold")).pack()
        label_2=Label(window6,text="Fund Name:",width=15,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=20,y=60)
        Message(window6,text=sld1,width=400,justify=CENTER,bg='yellow',fg='black',font=("arial",11,"bold")).place(x=170,y=59)
        label_3=Label(window6,text="Bank Name:",width=15,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=20,y=100)
        Message(window6,text=a,width=250,justify=CENTER,bg='yellow',fg='black',font=("arial",11,"bold")).place(x=170,y=99)
        label_4=Label(window6,text="Account NO:",width=15,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=20,y=140)
        Message(window6,text=b,width=250,justify=CENTER,bg='yellow',fg='black',font=("arial",11,"bold")).place(x=170,y=139)
        label_2=Label(window6,text="Amount:",width=15,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=20,y=180)
        Message(window6,text=amt2,width=250,justify=CENTER,bg='yellow',fg='black',font=("arial",11,"bold")).place(x=170,y=179)
        button_1=Button(window6, text='Proceed',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=lambda:seventh_win(sel,cb,amt,fn)).place(x=100,y=280)   
        button_2=Button(window6, text='Cancel',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=window6.destroy).place(x=240,y=280)


        


def seventh_win(sel,cb,amt,fn):
    fn1=fn.get()
    print(fn1)
    amt1=amt.get()
    #sld3=sld1.get()
    if sel==1:
        minic.execute("SELECT DID FROM DONOR where FNAME=(%s)",(fn1,))
        sdid=minic.fetchone()
        did=sdid[0]
        print(did)
        minic.execute("CREATE TRIGGER T1 BEFORE UPDATE ON soldiers FOR EACH ROW SET NEW.TOTAL_COLLECTION=OLD.TOTAL_COLLECTION+NEW.TOTAL_COLLECTION;")
        minic.execute("UPDATE soldiers SET TOTAL_COLLECTION=(%s),SDID=(%s) WHERE NAME=(%s)",(amt1,did,sld1))
        minic.execute("DROP TRIGGER T1;")
        minidb.commit()
        messagebox.showinfo("Success","Amount has been transferred to the soldier's account!")
    elif sel==2:
        #minic.execute("DELIMITER /")
        minic.execute("CREATE TRIGGER T1 BEFORE UPDATE ON govt_body FOR EACH ROW SET NEW.TOTAL_COLLECTION=OLD.TOTAL_COLLECTION+NEW.TOTAL_COLLECTION;")
        minic.execute("UPDATE govt_body SET TOTAL_COLLECTION=(%s) WHERE GNAME=(%s)",(amt1,sld1))
        minic.execute("DROP TRIGGER T1;")
        minic.execute("SELECT DID FROM DONOR WHERE FNAME=(%s)",(fn1,))
        sdid=minic.fetchone()
        did=sdid[0]
        print(did)
        minic.execute("SELECT GID FROM GOVT_BODY WHERE GNAME=(%s)",(sld1,))
        gdid=minic.fetchone()
        gid=gdid[0]
        print(gid)
        minic.execute("INSERT INTO donor_govt VALUES(%s,%s)",(did,gid))
        minidb.commit()
        messagebox.showinfo("Success","Amount has been transferred to the Government's's Relief Fund!")


def eighth_win(user,pwd):
    us=user.get()
    pas=pwd.get()
    minic.execute("SELECT US FROM ADMIN")
    username=minic.fetchall()
    print(username)
    #us1=username
    minic.execute("SELECT PAS FROM ADMIN")
    password=minic.fetchall()
    print(password)
    #pas1=password
    if username!=[(us,)] or password!=[(pas,)]:
        messagebox.showerror("Error","Please enter valid username and password.")
    else:
        window10=Tk()
        window10.geometry('300x300')
        window10.configure(background="lawn green")
        window10.title("Relief Funds")
        var=IntVar(master=window10)
        label_7=Label(window10,text="Choose An Option:",width=20,bg="yellow",fg="black",font=("arial",12,"bold")).pack()
        button_2=Radiobutton(window10, text="Soldiers",padx=5, variable=var,value=1).place(x=10,y=70)
        button_3=Radiobutton(window10, text="Goverment Relief Fund",padx=5,variable=var,value=2).place(x=10,y=150)
        button_5=Button(window10, text='Submit',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=lambda:ninth_win(var)).place(x=30,y=220)    
        button_6=Button(window10, text='Cancel',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=window10.destroy).place(x=150,y=220)



def ninth_win(var):
    global sel1
    sel1=var.get()
    print(sel1)
    if sel1==1:
        window8=Tk()
        window8.geometry('550x300')
        window8.configure(background="lawn green")
        window8.title("Relief Funds")
        label_10=Label(window8,text="In the dropdown menu below,\n are the list of foundations which are helping the flood-affected victims.\n Choose th charitable foundation you \n want to donate to:",width=50,fg="white",bg="dark green",font=("arial",12,"bold")).place(x=20,y=10)
        cb1=ttk.Combobox(window8,values=['Karnail Singh','Ravi Paul','Rakesh Singh','Javra Munda','Naiman Kajur','Janrao','SK Vidyarthi','G Sanokhar','Rajesh KR SIngh','B Ghorai','Ashok Kumar Singh','Pankaj Tripathi','Amit Kumar','Maneshwar Basumatari','Sukhjinder Singh','Rohitash Lamba','Subramaniam G','Vijay Soreng','PK Sahoo','TK Prabhakaran'])
        cb1.place(x=140,y=130)
        cb1.config(width=40)
        cb1.current(1)
            #print(cb.current(),cb.get())
        button_7=Button(window8, text='Submit',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=lambda:tenth_win(sel1,cb1)).place(x=120,y=220)

        button_8=Button(window8, text='Cancel',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=window8.destroy).place(x=270,y=220)

    elif sel1==2:
        window8=Tk()
        window8.geometry('550x300')
        window8.configure(background="lawn green")
        window8.title("Relief Funds")
        label_10=Label(window8,text="In the dropdown menu below,\n are the list of foundations which are helping the flood-affected victims.\n Choose th charitable foundation you \n want to donate to:",width=50,fg="white",bg="dark green",font=("arial",12,"bold")).place(x=20,y=10)
        cb1=ttk.Combobox(window8,values=["KARNATAKA'S CHIEF MINISTER'S RELIEF FUND","KERALA'S CHIEF MINISTER'S RELIEF FUND","MAHARASHTRA'S CHIEF MINISTER'S RELIEF FUND","ASSAM'S CHIEF MINISTER'S RELIEF FUND","RAJASTHAN'S CHIEF MINISTER'S RELIEF FUNDS"])
        cb1.place(x=140,y=130)
        cb1.config(width=40)
        cb1.current(1)
            #print(cb.current(),cb.get())
        button_7=Button(window8, text='Submit',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=lambda:tenth_win(sel1,cb1)).place(x=120,y=220)
        button_8=Button(window8, text='Cancel',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=window8.destroy).place(x=270,y=220)

    #elif sel==3:

def tenth_win(sel1,cb1):
    global sld2
    sld2=cb1.get()
    if sel1==1:
        window9=Tk()
        window9.geometry('550x400')
        window9.title("Relief Funds")
        window9.configure(background='lawn green')
        label_1=Label(window9,text="The details of the soldier are as follows:",width=30,bg='dark green',fg='white',font=("arial",12,"bold")).pack()
        label_2=Label(window9,text="Soldier Name:",width=15,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=20,y=60)
        Message(window9,text=sld2,width=400,justify=CENTER,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=170,y=59)
        label_3=Label(window9,text="Designation:",width=15,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=20,y=100)
        minic.execute("SELECT DESGN FROM SOLDIERS WHERE NAME=(%s)",(sld2,))
        c=minic.fetchall()
        Message(window9,text=c,width=250,justify=CENTER,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=170,y=99)
        label_13=Label(window9,text="Bank Name:",bg='dark green',fg='white',font=("arial",10,"bold")).place(x=20,y=140)
        minic.execute("SELECT BANK_NAME FROM soldiers WHERE NAME=(%s)",(sld2,))
        a=minic.fetchall()
        print(a)
        Message(window9,text=a,width=200,justify=CENTER,bg='yellow',fg='black',font=("arial",10,"bold")).place(x=170,y=139)
        label_14=Label(window9,text="Account Number:",bg='dark green',fg='white',font=("arial",10,"bold")).place(x=20,y=180)
        minic.execute("SELECT ACC_NO FROM SOLDIERS WHERE NAME=(%s)",(sld2,))
        b=minic.fetchall()
        Message(window9,text=b,width=200,justify=CENTER,bg='yellow',fg='black',font=("arial",10,"bold")).place(x=170,y=179)
        label_4=Label(window9,text="Total Collection:",width=15,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=20,y=220)
        minic.execute("SELECT TOTAL_COLLECTION FROM SOLDIERS WHERE NAME=(%s)",(sld2,))
        d=minic.fetchall()
        Message(window9,text=d,width=250,justify=CENTER,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=170,y=219)
        #label_2=Label(window9,text="Amount:",width=15,bg='purple',fg='white',font=("arial",11,"bold")).place(x=20,y=180)
        #Message(window9,textvariable=amt1,width=250,justify=CENTER,bg='blue',fg='white',font=("arial",11,"bold")).place(x=170,y=179)
        button_1=Button(window9, text='Proceed',width=10,bg='brown',fg='white',font=("arial",12,"bold")).place(x=100,y=300)   
        button_2=Button(window9, text='Cancel',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=window9.destroy).place(x=240,y=300)

    if sel1==2:
        window9=Tk()
        window9.geometry('550x400')
        window9.title("Relief Funds")
        window9.configure(background='lawn green')
        label_1=Label(window9,text="Final display of details:",width=30,bg='dark green',fg='white',font=("arial",12,"bold")).pack()
        label_2=Label(window9,text="Fund Name:",width=15,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=20,y=60)
        Message(window9,text=sld2,width=400,justify=CENTER,bg='yellow',fg='black',font=("arial",11,"bold")).place(x=170,y=59)
        label_3=Label(window9,text="Bank Name:",width=15,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=20,y=100)
        minic.execute("SELECT BANK_NAME FROM govt_body WHERE GNAME=(%s)",(sld2,))
        c=minic.fetchall()
        Message(window9,text=c,width=250,justify=CENTER,bg='yellow',fg='black',font=("arial",11,"bold")).place(x=170,y=99)
        label_4=Label(window9,text="Account NO:",width=15,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=20,y=140)
        minic.execute("SELECT ACC_NO FROM govt_body WHERE GNAME=(%s)",(sld2,))
        d=minic.fetchall()
        Message(window9,text=d,width=250,justify=CENTER,bg='yellow',fg='black',font=("arial",11,"bold")).place(x=170,y=139)
        label_4=Label(window9,text="Total Collection:",width=15,bg='dark green',fg='white',font=("arial",11,"bold")).place(x=20,y=180)
        minic.execute("SELECT TOTAL_COLLECTION FROM govt_body WHERE GNAME=(%s)",(sld2,))
        e=minic.fetchall()
        Message(window9,text=e,width=250,justify=CENTER,bg='yellow',fg='black',font=("arial",11,"bold")).place(x=170,y=179)
        #label_2=Label(window9,text="Amount:",width=15,bg='purple',fg='white',font=("arial",11,"bold")).place(x=20,y=180)
        #Message(window9,textvariable=amt1,width=250,justify=CENTER,bg='blue',fg='white',font=("arial",11,"bold")).place(x=170,y=179)
        button_1=Button(window9, text='Proceed',width=10,bg='brown',fg='white',font=("arial",12,"bold")).place(x=100,y=280)   
        button_2=Button(window9, text='Cancel',width=10,bg='brown',fg='white',font=("arial",12,"bold"),command=window9.destroy).place(x=240,y=280)
                
        
    
    

label_1=Label(root,text="WELCOME USER",width=40,fg="white",bg="dark green",font=("arial",12,"bold")).place(x=90,y=20)
label_1=Label(root,text="WE THANK YOU FOR TAKING THIS INIATIVE",width=40,fg="white",bg="dark green",font=("arial",12,"bold")).place(x=90,y=45)
label_2=Label(root,text="Enter your details:",width=15,fg="white",bg="dark green",font=("arial",12,"bold")).place(x=10,y=80)
label_3=Label(root,text="First Name:",width=15,fg="white",bg="dark green",font=("arial",11,"bold")).place(x=10,y=120)
entry_1=Entry(root,textvar=fn).place(x=175,y=120)
label_4=Label(root,text="Last Name:",width=15,fg="white",bg="dark green",font=("arial",11,"bold")).place(x=10,y=170)
entry_2=Entry(root,textvar=ln).place(x=175,y=170)

label_5=Label(root,text="Address:",width=15,fg="white",bg="dark green",font=("arial",11,"bold")).place(x=10,y=220)
entry_3=Entry(root,textvar=ad).place(x=175,y=220)
label_6=Label(root,text="State:",width=15,fg="white",bg="dark green",font=("arial",11,"bold")).place(x=10,y=270)
entry_4=Entry(root,textvar=st).place(x=175,y=270)
label_5=Label(root,text="E-Mail:",width=15,fg="white",bg="dark green",font=("arial",11,"bold")).place(x=10,y=320)
entry_5=Entry(root,textvar=em).place(x=175,y=320)
label_6=Label(root,text="Phone No:",width=15,fg="white",bg="dark green",font=("arial",11,"bold")).place(x=10,y=370)
entry_6=Entry(root,textvar=ph).place(x=175,y=370)
button_1=Button(root, text='Submit',width=20,bg='brown',fg='white',font=("arial",12,"bold"),command=second_win).place(x=170,y=470)

root.mainloop()
