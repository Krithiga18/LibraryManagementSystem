from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from datetime import date,timedelta

root4=Tk()
root4.title("Login System")
root4.geometry("2000x1000")
root4.attributes('-fullscreen',True)

#Database connectivity
con=pymysql.connect(host="localhost",user="root",password='kitty',database='Project')
cur=con.cursor()

#BG image
frame=Frame(root4,bg='black')
frame.place(relwidth=1,relheight=1)
load=Image.open("LIB IMG 6.jpg")
bg=ImageTk.PhotoImage(load)
bglabel=Label(frame,image=bg)
bglabel.image=bg
bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)

#Login frame
lf=Frame(root4,bg='white')
lf.place(x=100,y=350,height=360,width=500)

title=Label(lf,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=50,y=20)
desc=Label(lf,text="Librarian Login Area",font=("Goudy Old Style",17,"bold"),fg="#d25d17",bg="white").place(x=50,y=75)

#Username
user=Label(lf,text="Username",font=("Goudy Old Style",20,"bold"),fg="steelblue",bg="white").place(x=50,y=110)
usertxt=Entry(lf,font=("Times New Roman",18),bd=5,bg="lightgray")
usertxt.place(x=50,y=150,width=350,height=35)

#Password
pwd=Label(lf,text="Password",font=("Goudy Old Style",20,"bold"),fg="steelblue",bg="white").place(x=50,y=190)
pwdtxt=Entry(lf,font=("Times New Roman",18),bd=5,show="*",bg="lightgray")
pwdtxt.place(x=50,y=230,width=350,height=35)

#Table Names assigned to variables
issueTable="books_issued" 
bookTable="books"
memTable="members"

allBid=[] #List to store all Book IDs
allauthor=[] #List to store all author names
alltitle=[] #List to store all Book Title

def searchBook(): 
    global bookInfo6,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame,labelFrame1,lb1,root1
    root1.destroy()
    
    root=Tk()
    root.title("Search")
    root.geometry("2000x1000")
    root.attributes('-fullscreen',True)

    frame=Frame(root,bg='black')
    frame.place(relwidth=1,relheight=1)
    load=Image.open("LIB IMG 5.jpg")
    bg=ImageTk.PhotoImage(load)
    bglabel=Label(frame,image=bg)
    bglabel.image=bg
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
        
    headingFrame1=Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.3,rely=0.05,relwidth=0.4,relheight=0.13)
    
    headingLabel=Label(headingFrame1,text="D.A.V SR SECONDARY SCHOOL\nSearch Book",bg='black',fg='white',font=('Lucida Bright',25,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    labelFrame=Frame(root,bg='black')
    labelFrame.place(relx=0.3,rely=0.22,relwidth=0.4,relheight=0.1)
    
    # Author/BookID to search
    lb1=Label(labelFrame,text="Author/BookTitle: ",bg='black',fg='white',font=('Cardinal',22))
    lb1.place(relx=0.05,rely=0.1)
        
    bookInfo6=Entry(labelFrame,font=("Times New Roman",18))
    bookInfo6.place(relx=0.3,rely=0.5,relwidth=0.64,relheight=0.33)

    labelFrame1=Frame(root,bg='black')
    labelFrame1.place(relx=0.23,rely=0.35,relwidth=0.55,relheight=0.5)
    Label(labelFrame1, text=" %-20s%-23s%-25s%-25s%-5s"%('BID','TITLE','AUTHOR','STATUS','ISSUEDTO'),font=('Lucida Bright',15),
    bg='black',fg='white').place(relx=0.05,rely=0.1)
    Label(labelFrame1,text="*******************************************************************************************************************************************************************************"
          ,bg='black',font=('Lucida Bright',15),fg='white').place (relx=0.03,rely=0.2)

    #Search by author
    SubmitBtn=Button(root,text="SEARCH BY AUTHOR",bg='#d1ccc0',fg='black',command=search_a,font=('Times New Roman',18),bd=5)
    SubmitBtn.place(relx=0.22,rely=0.9,relwidth=0.18,relheight=0.08)

    #Search by title
    SubmitBtn=Button(root,text="SEARCH BY TITLE",bg='#d1ccc0',fg='black',command=search_t,font=('Times New Roman',18),bd=5)
    SubmitBtn.place(relx=0.62,rely=0.9,relwidth=0.18,relheight=0.08)
    
    #Quit Button
    quitBtn=Button(root,text="BACK",bg='#f7f1e3',fg='black',command=quit,font=('Times New Roman',18),bd=5)
    quitBtn.place(relx=0.42,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def search_a():
    author_title=bookInfo6.get()
    
    extract="SELECT AName FROM "+bookTable
    cur.execute(extract)
    con.commit()
    for i in cur:
        allauthor.append(i[0])
        
    if author_title=='':
        messagebox.showinfo('Error',"Entry box not filled up")
    elif author_title in allauthor:
        query="SELECT * FROM "+bookTable+" WHERE AName='"+author_title+"'"
        cur.execute(query)
        con.commit()
        y=0.25
        for i in cur:
            Label(labelFrame1,text="%-13s%-22s%-34s%-32s%-5s"%(i[0],i[1],i[2],i[3],i[4]),font=('Lucida Bright',14)
                  ,bg='black', fg='white').place(relx=0.02,rely=y)
            y+=0.07
        for i in rows:
            print("\t\t\t",i[0],"\t\t",i[1],"\t\t   ",i[2],"\t\t",i[3],"\t          ",i[4])
    else:
        allauthor.clear()
        messagebox.showinfo('Error',"Failed to fetch data from the database")
        
    quit()
    
def search_t():
    author_title=bookInfo6.get()
    
    extract="SELECT BookTitle FROM "+bookTable
    cur.execute(extract)
    con.commit()
    for i in cur:
        alltitle.append(i[0])
        
    if author_title=='':
        messagebox.showinfo('Error',"Entry box not filled up")
    elif author_title in alltitle:
        query1="SELECT * FROM "+bookTable+" WHERE BookTitle='"+author_title+"'"
        cur.execute(query1)
        con.commit()
        y=0.25
        for i in cur:
            Label(labelFrame1,text="%-13s%-22s%-34s%-32s%-5s"%(i[0],i[1],i[2],i[3],i[4]),font=('Lucida Bright',14)
                  ,bg='black', fg='white').place(relx=0.02,rely=y)
            y+=0.1
        for i in rows:
            print("\t\t\t",i[0],"\t\t",i[1],"\t\t   ",i[2],"\t\t\t",i[3],"\t          ",i[4])
    else:
        alltitle.clear()
        messagebox.showinfo('Error',"Failed to fetch data from the database")
        
    quit()

m='DAVREF'
extract1="SELECT COUNT(*) FROM "+bookTable
cur.execute(extract1)
for r in cur.fetchone():
    print(r)

def bookRegister():
    global r,m
    bid=m+str(r+1)
    title=bookInfo3.get()
    author=bookInfo4.get()
    status='Avail'
    issueto='--'

    insertBooks="INSERT INTO "+bookTable+" VALUES ('"+bid+"','"+title+"','"+author+"','"+status+"','"+'--'+"')"

    try:
        if title=='' or author=='':
            messagebox.showinfo('Error',"Entry box not filled up")
        else:
            cur.execute(insertBooks)
            con.commit()
            r+=1
            print("BOOKID:",bid)
            print("BOOKTITLE:",title)
            print("AUTHOR:",author)
            print("STATUS:",status)
            print("ISSUED TO :",issueto)
            print("")
            messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    quit()

def addBook():
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,bookInfo5,Canvas1,con,cur,bookTable,issueTable,root,root1,r
    root1.destroy()
    
    root=Tk()
    root.title("Add Books")
    root.geometry("2000x1000")
    root.attributes('-fullscreen',True)
    
    con=pymysql.connect( host="localhost",user="root",password='kitty',database='Project')
    cur=con.cursor()
    
    frame=Frame(root,bg='black')
    frame.place(relwidth=1,relheight=1)
    load=Image.open("LIB IMG 5.jpg")
    bg=ImageTk.PhotoImage(load)
    bglabel=Label(frame,image=bg)
    bglabel.image=bg
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
        
    headingFrame1=Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.13)
    
    headingLabel=Label(headingFrame1,text="D.A.V SR SECONDARY SCHOOL\nAdd Books",bg='black',fg='white',font=('Lucida Bright',25,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    labelFrame=Frame(root,bg='black')
    labelFrame.place(relx=0.25,rely=0.35,relwidth=0.5,relheight=0.45)

    #BookID
    lb1=Label(labelFrame,text="Book ID           :",bg='black',fg='white',font=('Cardinal',22))
    lb1.place(relx=0.05,rely=0.15,relheight=0.07)
        
    bookInfo1=Label(labelFrame,text=m+str(r+1),font=("Times New Roman",18),anchor=W)
    bookInfo1.place(relx=0.34,rely=0.15,relwidth=0.6,relheight=0.1)
    
    #BookTitle
    lb2=Label(labelFrame,text="Book Title        :", bg='black', fg='white',font=('Cardinal',20))
    lb2.place(relx=0.05,rely=0.35)

    bookInfo3=Entry(labelFrame,font=("Times New Roman",18))
    bookInfo3.place(relx=0.34,rely=0.35, relwidth=0.6,relheight=0.1)

    #AName
    lb3=Label(labelFrame,text="Author             :", bg='black', fg='white',font=('Cardinal',20))
    lb3.place(relx=0.05,rely=0.55)
        
    bookInfo4=Entry(labelFrame,font=("Times New Roman",18))
    bookInfo4.place(relx=0.34,rely=0.55, relwidth=0.6,relheight=0.1)

    #Status
    lb4=Label(labelFrame,text="Status             :",bg='black', fg='white',font=('Cardinal',20))
    lb4.place(relx=0.05,rely=0.75)
        
    bookInfo5=Label(labelFrame,text='Avail',font=("Times New Roman",18),anchor=W)
    bookInfo5.place(relx=0.34,rely=0.75,relwidth=0.6,relheight=0.1)
        
    #ADD Button
    SubmitBtn=Button(root,text="ADD",bg='#d1ccc0',fg='black',command=bookRegister,font=('Times New Roman',22),bd=5)
    SubmitBtn.place(relx=0.28,rely=0.9,relwidth=0.18,relheight=0.08)
    
    #Quit Button
    quitBtn=Button(root,text="BACK",bg='#f7f1e3',fg='black',command=quit,font=('Times New Roman',22),bd=5)
    quitBtn.place(relx=0.53,rely=0.9,relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def show():
    global labelFrame,bookInfo2,bookInfo3,bookInfo4,bookInfo5
    bid=bookInfo1.get()
    
    query1="SELECT * FROM "+bookTable+" WHERE BookID='"+bid+"'"
    cur.execute(query1)
    con.commit()
    for i in cur:
        a=i[1]
        b=i[2]
        c=i[3]
        d=i[4]
        
    #Title
    bookInfo2=Label(labelFrame,text=a,font=("Times New Roman",18),anchor=W)
    bookInfo2.place(relx=0.33,rely=0.32,relwidth=0.62,relheight=0.07)
        
    #Book Author
    bookInfo3=Label(labelFrame,text=b,font=("Times New Roman",18),anchor=W)
    bookInfo3.place(relx=0.33,rely=0.47,relwidth=0.62,relheight=0.07)
        
    #Book Status
    bookInfo4=Label(labelFrame,text=c,font=("Times New Roman",18),anchor=W)
    bookInfo4.place(relx=0.33,rely=0.67,relwidth=0.62,relheight=0.07)

    #Issued To
    bookInfo5=Label(labelFrame,text=d,font=("Times New Roman",18),anchor=W)
    bookInfo5.place(relx=0.33,rely=0.85,relwidth=0.62,relheight=0.07)

def deleteBook():
    global labelFrame,r
    bid=bookInfo1.get()
    
    deleteSql="DELETE FROM "+bookTable+" WHERE BookID='"+bid+"'"
    deleteIssue="DELETE FROM "+issueTable+" WHERE BookID='"+bid+"'"
    extractbid="SELECT BookID FROM "+bookTable
    
    try:
        cur.execute(extractbid)
        for i in cur:
            allBid.append(i[0])
    except:
        messagebox.showinfo('Error',"Can't fetch Book IDs")

    if bid=='':
        messagebox.showinfo('Error',"Entry box not filled up")
    elif bid in allBid:
        ans=messagebox.askquestion('Confirm',"Do you really want to delete?")
        if ans=='yes':
            messagebox.showinfo('Success',"Book Record Deleted Successfully")
            cur.execute(deleteSql)
            con.commit()
            cur.execute(deleteIssue)
            con.commit()
            extract1="SELECT COUNT(*) FROM "+bookTable
            cur.execute(extract1)
            for r in cur.fetchone():
                print(r)
            print("DELETED BOOKID :",bid)
            print("")
    else:
        messagebox.showinfo('Error',"Please check Book ID")
    quit()

def delete(): 
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root,labelFrame,root1,r
    root1.destroy()
    
    root = Tk()
    root.title("Delete Books")
    root.geometry("2000x1000")
    root.attributes('-fullscreen',True)
    
    frame=Frame(root,bg='black')
    frame.place(relwidth=1,relheight=1)
    load=Image.open("LIB IMG 5.jpg")
    bg=ImageTk.PhotoImage(load)
    bglabel=Label(frame,image=bg)
    bglabel.image=bg
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
        
    headingFrame1=Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.31,rely=0.08,relwidth=0.4,relheight=0.13)
    
    headingLabel=Label(headingFrame1,text="D.A.V SR SECONDARY SCHOOL\nDelete Book", bg='black', fg='white', font=('Lucida Bright',25,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    labelFrame=Frame(root,bg='black')
    labelFrame.place(relx=0.26,rely=0.35,relwidth=0.5,relheight=0.45)

    query="SELECT BookID FROM "+bookTable
    cur.execute(query)
    ids=cur.fetchall()
    opts=StringVar()
        
    # Book ID to Delete
    lb2=Label(labelFrame,text="Book ID          :",bg='black',fg='white',font=('Cardinal',22))
    lb2.place(relx=0.05,rely=0.15,relheight=0.07)

    bookInfo1=ttk.Combobox(labelFrame,textvariable=opts,font=("Times New Roman",18))
    bookInfo1['values']=ids
    bookInfo1.place(relx=0.33,rely=0.15,relwidth=0.62,relheight=0.09)
    bookInfo1.current(0)

    #Title
    lb2=Label(labelFrame,text="Book Title       :",bg='black',fg='white',font=('Cardinal',22))
    lb2.place(relx=0.05,rely=0.32,relheight=0.07)
        
    bookInfo2=Label(labelFrame,font=("Times New Roman",18),anchor=W)
    bookInfo2.place(relx=0.33,rely=0.32,relwidth=0.62,relheight=0.09)
        
    #Book Author
    lb3=Label(labelFrame,text="Author            :",bg='black',fg='white',font=('Cardinal',22))
    lb3.place(relx=0.05,rely=0.47,relheight=0.07)
        
    bookInfo3=Label(labelFrame,font=("Times New Roman",18),anchor=W)
    bookInfo3.place(relx=0.33,rely=0.47,relwidth=0.62,relheight=0.09)
        
    #Book Status
    lb4=Label(labelFrame,text="Status            :",bg='black',fg='white',font=('Cardinal',22))
    lb4.place(relx=0.05,rely=0.55,relheight=0.3)
        
    bookInfo4=Label(labelFrame,font=("Times New Roman",18),anchor=W)
    bookInfo4.place(relx=0.33,rely=0.67,relwidth=0.62,relheight=0.09)

    #Issued To
    lb5=Label(labelFrame,text="Issued To      :",bg='black',fg='white',font=('Cardinal',22))
    lb5.place(relx=0.05,rely=0.85,relheight=0.07)
        
    bookInfo5=Label(labelFrame,font=("Times New Roman",18),anchor=W)
    bookInfo5.place(relx=0.33,rely=0.85,relwidth=0.62,relheight=0.09)

    #Delete button
    SubmitBtn=Button(root,text="DELETE",bg='#d1ccc0',fg='black',command=deleteBook,font=('Times New Roman',20),bd=5)
    SubmitBtn.place(relx=0.22,rely=0.9, relwidth=0.18,relheight=0.08)

    #Quit btn
    SubmitBtn=Button(root,text="BACK",bg='#f7f1e3',fg='black',command=quit,font=('Times New Roman',20),bd=5)
    SubmitBtn.place(relx=0.42,rely=0.9, relwidth=0.18,relheight=0.08)
    
    #Show info
    quitBtn=Button(root,text="SHOW INFO",bg='#d1ccc0',fg='black',command=show,font=('Times New Roman',20),bd=5)
    quitBtn.place(relx=0.62,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def AView():
    global root,root2
    root.destroy()

    root2=Tk()
    root2.title("View Avail Books")
    root2.geometry("2000x1000")
    root2.attributes('-fullscreen',True)
    
    Canvas1=Canvas(root2) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1=Frame(root2,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.3,rely=0.05,relwidth=0.4,relheight=0.13)
    headingLabel=Label(headingFrame1,text="D.A.V SR SECONDARY SCHOOL\nBooks in Stock", bg='black', fg='white', font = ('Lucida Bright',25,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1, relheight=1)
    
    labelFrame=Frame(root2,bg='#12a4d9')
    labelFrame.place(relx=0,rely=0.2,relwidth=1,relheight=1)

    #Styles for Treeview widget
    s=ttk.Style()
    s.configure('mystyle.Treeview',font=('Lucida Bright',20,'bold'),rowheight=35)
    s.configure('mystyle.Treeview.Heading',font=('Ms serif',30,'bold','underline'))

    #Adding a scrollbar
    sb=ttk.Scrollbar(labelFrame)
    sb.pack(side=RIGHT,fill=Y)

    #Treeview Widget-for alligning properly
    mt=ttk.Treeview(labelFrame,columns=('BOOKID','BOOKTITLE','AUTHOR','STATUS'),style='mystyle.Treeview'
                    ,yscrollcommand=sb.set)
    mt.pack()
    sb.config(command=mt.yview)
    
    mt['columns']=('BOOKID','BOOKTITLE','AUTHOR','STATUS')
    mt.column('BOOKID',anchor=W)
    mt.heading('BOOKTITLE',anchor=W)
    mt.column('AUTHOR',anchor=W)
    mt.column('STATUS',anchor=W)

    mt.heading('BOOKID',text='BOOKID',anchor=W)
    mt.heading('BOOKTITLE',text='BOOKTITLE',anchor=W)
    mt.heading('AUTHOR',text='AUTHOR',anchor=W)
    mt.heading('STATUS',text='STATUS',anchor=W)
    mt.pack(fill=BOTH,expand=1)

    getBooks="SELECT BookID,BookTitle,AName,Status FROM "+bookTable+" WHERE Status LIKE '_vail' "
    cur.execute(getBooks)
    rows=cur.fetchall()
    for i in rows:
        mt.insert('','end',values='')
        mt.insert('','end',values=i)

    #Quit Button
    quitBtn=Button(root2,text="BACK",bg='#d1ccc0', fg='black',command=quit1,font=('Times New Roman',22),bd=5)
    quitBtn.place(relx=0.42,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
    
def IView():
    global root,root2
    root.destroy()

    root2=Tk()
    root2.title("View Issued Books")
    root2.geometry("2000x1000")
    root2.attributes('-fullscreen',True)
    
    Canvas1=Canvas(root2) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1=Frame(root2,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.3,rely=0.05,relwidth=0.4,relheight=0.13)
    headingLabel=Label(headingFrame1, text="D.A.V SR SECONDARY SCHOOL\n Issued Books", bg='black', fg='white', font = ('Lucida Bright',25,'bold'))
    
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame=Frame(root2,bg='#12a4d9')
    labelFrame.place(relx=0,rely=0.2,relwidth=1,relheight=1)

    #Styles for Treeview widget
    s=ttk.Style()
    s.configure('mystyle.Treeview',font=('Lucida Bright',20,'bold'),rowheight=35)
    s.configure('mystyle.Treeview.Heading',font=('Ms serif',30,'bold','underline'))

    #Adding a scrollbar
    sb=ttk.Scrollbar(labelFrame)
    sb.pack(side=RIGHT,fill=Y)

    #Treeview Widget-for alligning properly
    mt=ttk.Treeview(labelFrame,columns=('BOOKID','BOOKTITLE','AUTHOR','STATUS','ISSUED TO'),style='mystyle.Treeview'
                    ,yscrollcommand=sb.set)
    mt.pack()
    sb.config(command=mt.yview)
    
    mt['columns']=('BOOKID','BOOKTITLE','AUTHOR','STATUS','ISSUED TO')
    mt.column('BOOKID',anchor=W)
    mt.heading('BOOKTITLE',anchor=W)
    mt.column('AUTHOR',anchor=W)
    mt.column('STATUS',anchor=W)
    mt.column('ISSUED TO',anchor=W)

    mt.heading('BOOKID',text='BOOKID',anchor=W)
    mt.heading('BOOKTITLE',text='BOOKTITLE',anchor=W)
    mt.heading('AUTHOR',text='AUTHOR',anchor=W)
    mt.heading('STATUS',text='STATUS',anchor=W)
    mt.heading('ISSUED TO',text='ISSUED TO',anchor=W)
    mt.pack(fill=BOTH,expand=1)

    getBooks="SELECT * FROM "+bookTable+" WHERE Status LIKE '_ssued' "
    cur.execute(getBooks)
    rows=cur.fetchall()
    for i in rows:
        mt.insert('','end',values='')
        mt.insert('','end',values=i)

    #Quit Button
    quitBtn=Button(root2,text="BACK",bg='#d1ccc0', fg='black',command=quit1,font=('Times New Roman',22),bd=5)
    quitBtn.place(relx=0.42,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def quit1():
    global root,root2
    root2.destroy()

    root=Tk()
    root.title("View Booklist")
    root.geometry("2000x1000")
    root.attributes('-fullscreen',True)
    
    Canvas1=Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1=Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.3,rely=0.05,relwidth=0.4,relheight=0.13)
    
    headingLabel=Label(headingFrame1,text="D.A.V SR SECONDARY SCHOOL\nList of Books", bg='black', fg='white', font = ('Lucida Bright',25,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame=Frame(root,bg='#12a4d9')
    labelFrame.place(relx=0,rely=0.2,relwidth=1,relheight=0.8)
    
    #Styles for Treeview widget
    s=ttk.Style()
    s.configure('mystyle.Treeview',font=('Lucida Bright',20,'bold'),rowheight=35)
    s.configure('mystyle.Treeview.Heading',font=('Ms serif',30,'bold','underline'))

    #Adding a scrollbar
    sb=ttk.Scrollbar(labelFrame)
    sb.pack(side=RIGHT,fill=Y)

    #Treeview Widget-for alligning properly
    mt=ttk.Treeview(labelFrame,columns=('BOOKID','BOOKTITLE','AUTHOR','STATUS','ISSUED TO'),style='mystyle.Treeview'
                    ,yscrollcommand=sb.set)
    mt.pack()
    sb.config(command=mt.yview)
    
    mt['columns']=('BOOKID','BOOKTITLE','AUTHOR','STATUS','ISSUED TO')
    mt.column('BOOKID',anchor=W)
    mt.heading('BOOKTITLE',anchor=W)
    mt.column('AUTHOR',anchor=W)
    mt.column('STATUS',anchor=W)
    mt.column('ISSUED TO',anchor=W)

    mt.heading('BOOKID',text='BOOKID',anchor=W)
    mt.heading('BOOKTITLE',text='BOOKTITLE',anchor=W)
    mt.heading('AUTHOR',text='AUTHOR',anchor=W)
    mt.heading('STATUS',text='STATUS',anchor=W)
    mt.heading('ISSUED TO',text='ISSUED TO',anchor=W)
    mt.pack(fill=BOTH,expand=1)

    getBooks="SELECT * FROM "+bookTable
    cur.execute(getBooks)
    rows=cur.fetchall()
    for i in rows:
        mt.insert('','end',values='')
        mt.insert('','end',values=i)
    
    #View Issued books
    SubmitBtn=Button(root,text="ISSUED BOOKS",bg='#d1ccc0',fg='black',command=IView,font=('Times New Roman',18),bd=5)
    SubmitBtn.place(relx=0.8,rely=0.12,relwidth=0.14,relheight=0.06)

    #View Avail books
    SubmitBtn=Button(root,text="AVAIL BOOKS",bg='#d1ccc0',fg='black',command=AView,font=('Times New Roman',18),bd=5)
    SubmitBtn.place(relx=0.8,rely=0.045, relwidth=0.14,relheight=0.06)

    #Quit Button
    quitBtn=Button(root,text="BACK",bg='#f7f1e3',fg='black',command=quit,font=('Times New Roman',18),bd=5)
    quitBtn.place(relx=0.1,rely=0.08, relwidth=0.14,relheight=0.07)
    
    root.mainloop()

def View():
    global root,root1
    root1.destroy()
    
    root=Tk()
    root.title("View Booklist")
    root.geometry("2000x1000")
    root.attributes('-fullscreen',True)
    
    Canvas1=Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1=Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.3,rely=0.05,relwidth=0.4,relheight=0.13)
    
    headingLabel=Label(headingFrame1,text="D.A.V SR SECONDARY SCHOOL\nList of Books", bg='black', fg='white', font = ('Lucida Bright',25,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    labelFrame=Frame(root,bg='#12a4d9')
    labelFrame.place(relx=0,rely=0.2,relwidth=1,relheight=0.8)

    #Styles for Treeview widget
    s=ttk.Style()
    s.configure('mystyle.Treeview',font=('Lucida Bright',20,'bold'),rowheight=35)
    s.configure('mystyle.Treeview.Heading',font=('Ms serif',30,'underline','bold'))

    #Adding a scrollbar
    sb=ttk.Scrollbar(labelFrame)
    sb.pack(side=RIGHT,fill=Y)

    #Treeview Widget-for alligning properly
    mt=ttk.Treeview(labelFrame,columns=('BOOKID','BOOKTITLE','AUTHOR','STATUS','ISSUED TO'),style='mystyle.Treeview'
                    ,yscrollcommand=sb.set)
    mt.pack()
    sb.config(command=mt.yview)
    
    mt['columns']=('BOOKID','BOOKTITLE','AUTHOR','STATUS','ISSUED TO')
    mt.column('BOOKID',anchor=W)
    mt.heading('BOOKTITLE',anchor=W)
    mt.column('AUTHOR',anchor=W)
    mt.column('STATUS',anchor=W)
    mt.column('ISSUED TO',anchor=W)

    mt.heading('BOOKID',text='BOOKID',anchor=W)
    mt.heading('BOOKTITLE',text='BOOKTITLE',anchor=W)
    mt.heading('AUTHOR',text='AUTHOR',anchor=W)
    mt.heading('STATUS',text='STATUS',anchor=W)
    mt.heading('ISSUED TO',text='ISSUED TO',anchor=W)
    mt.pack(fill=BOTH,expand=1)

    getBooks="SELECT * FROM "+bookTable
    cur.execute(getBooks)
    rows=cur.fetchall()
    for i in rows:
        mt.insert('','end',values='')
        mt.insert('','end',values=i)
    
    #View Issued books
    SubmitBtn=Button(root,text="ISSUED BOOKS",bg='#d1ccc0',fg='black',command=IView,font=('Times New Roman',18),bd=5)
    SubmitBtn.place(relx=0.8,rely=0.12,relwidth=0.14,relheight=0.06)

    #View Avail books
    SubmitBtn=Button(root,text="AVAIL BOOKS",bg='#d1ccc0',fg='black',command=AView,font=('Times New Roman',18),bd=5)
    SubmitBtn.place(relx=0.8,rely=0.045, relwidth=0.14,relheight=0.06)

    #Quit Button
    quitBtn=Button(root,text="BACK",bg='#f7f1e3',fg='black',command=quit,font=('Times New Roman',18),bd=5)
    quitBtn.place(relx=0.1,rely=0.08, relwidth=0.14,relheight=0.07)
    
    root.mainloop()

def returnn():
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status,issueto,lb2,inf2,lb4,inf4
    
    bid=bookInfo1.get()
    extractBid="SELECT BookID FROM "+issueTable
    query="SELECT duedate FROM "+issueTable+" WHERE BookID='"+bid+"'"
    
    try:
        cur.execute(query)
        row=cur.fetchone()
        for i in row:
            d=i
        days=(date.today()-d).days
        if days>7:
            fine=(days)*2
        else:
            fine=0
    except:
        messagebox.showinfo('Error',"Please check the BookID")
    
    try:
        cur.execute(extractBid)
        for i in cur:
            allBid.append(i[0])
        if bid in allBid:
            checkAvail="SELECT Status FROM "+bookTable+" WHERE BookID='"+bid+"'"
            cur.execute(checkAvail)
            for i in cur:
                check=i[0]
            if check in ['issued','Issued']:
                status=True
            else:
                status=False
    except:
        messagebox.showinfo('Error',"Can't fetch Book IDs")
        
    try:
        if bid in allBid and status==True:
            issueSql="DELETE FROM "+issueTable+" WHERE BookID='"+bid+"'"
            cur.execute(issueSql)
            con.commit()
            updateStatus1="UPDATE "+bookTable+" SET Status='Avail' WHERE BookID='"+bid+"'"
            cur.execute(updateStatus1)
            con.commit()
            updateStatus2="UPDATE "+bookTable+" SET IssuedTo='--' WHERE Status='Avail'"
            cur.execute(updateStatus2)
            con.commit()
            print("BookID that is returned:",bid)
            print("DUE DATE:",d)
            print("RETURN DATE:",date.today())
            print("FINE:",fine)
            print("")
            messagebox.showinfo('Success',"Book Returned Successfully")
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    allBid.clear()
    quit()
    
def show1():
    global inf3,inf4,labelFrame
    bid=bookInfo1.get()
    
    query="SELECT duedate FROM "+issueTable+" WHERE BookID='"+bid+"'"
    cur.execute(query)
    row=cur.fetchone()
    for i in row:
        d=i
    con.commit()
    days=(date.today()-d).days
    if days>0:
        fine=(days)*2
    else:
        fine=0
    print(fine)

    #Due date
    inf3=Label(labelFrame,text=d,font=("Times New Roman",18),anchor=W)
    inf3.place(relx=0.35,rely=0.55, relwidth=0.6,relheight=0.1)

    #Fine
    inf4=Label(labelFrame,text=fine,font=("Times New Roman",18),anchor=W)
    inf4.place(relx=0.35,rely=0.8,relwidth=0.6,relheight=0.1)

def returnBook(): 
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame,lb1,lb2,inf2lb3,inf3
    root1.destroy()
    
    root=Tk()
    root.title("Return Book")
    root.geometry("2000x1000")
    root.attributes('-fullscreen',True)

    frame=Frame(root,bg='black')
    frame.place(relwidth=1,relheight=1)
    load=Image.open("LIB IMG 5.jpg")
    bg=ImageTk.PhotoImage(load)
    bglabel=Label(frame,image=bg)
    bglabel.image=bg
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
        
    headingFrame1=Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.32,rely=0.07,relwidth=0.4,relheight=0.13)
    
    headingLabel=Label(headingFrame1,text="D.A.V SR SECONDARY SCHOOL\nReturn Book", bg='black', fg='white', font=('Lucida Bright',25,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1, relheight=1)
    
    labelFrame=Frame(root,bg='black')
    labelFrame.place(relx=0.26,rely=0.35,relwidth=0.5,relheight=0.4)

    query="SELECT BookID FROM "+bookTable+" WHERE Status LIKE '_ssued' "
    cur.execute(query)
    ids=cur.fetchall()
    opts=StringVar()
        
    # Book ID
    lb1=Label(labelFrame,text="Book ID            :", bg='black', fg='white',font=('Cardinal',22))
    lb1.place(relx=0.05,rely=0.15)

    bookInfo1=ttk.Combobox(labelFrame,textvariable=opts,font=("Times New Roman",18))
    bookInfo1['values']=ids
    bookInfo1.place(relx=0.35,rely=0.15, relwidth=0.6,relheight=0.1)
    bookInfo1.current(0)
    
    #Return date 
    lb2=Label(labelFrame,text="Return date      :", bg='black', fg='white',font=('Cardinal',22))
    lb2.place(relx=0.05,rely=0.35)

    inf2=Label(labelFrame,text=date.today(),font=("Times New Roman",18),anchor=W)
    inf2.place(relx=0.35,rely=0.35, relwidth=0.6,relheight=0.1)

    #Due date
    lb3=Label(labelFrame,text="Due Date          :", bg='black', fg='white',font=('Cardinal',22))
    lb3.place(relx=0.05,rely=0.55)
        
    inf3=Label(labelFrame,font=("Times New Roman",18),anchor=W)
    inf3.place(relx=0.35,rely=0.55, relwidth=0.6,relheight=0.1)

    #Fine
    lb4=Label(labelFrame,text="Fine                 :",bg='black', fg='white',font=('Cardinal',22))
    lb4.place(relx=0.05,rely=0.8)
        
    inf4=Label(labelFrame,font=("Times New Roman",18),anchor=W)
    inf4.place(relx=0.35,rely=0.8,relwidth=0.6,relheight=0.1)
    
    #Return button
    SubmitBtn=Button(root,text="RETURN",bg='#d1ccc0',fg='black',command=returnn,font=('Times New Roman',20),bd=5)
    SubmitBtn.place(relx=0.22,rely=0.9, relwidth=0.18,relheight=0.08)

    #Quit btn
    SubmitBtn=Button(root,text="BACK",bg='#f7f1e3',fg='black',command=quit,font=('Times New Roman',20),bd=5)
    SubmitBtn.place(relx=0.42,rely=0.9, relwidth=0.18,relheight=0.08)
    
    #Show info
    quitBtn=Button(root,text="SHOW INFO",bg='#d1ccc0',fg='black',command=show1,font=('Times New Roman',20),bd=5)
    quitBtn.place(relx=0.62,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()
 
def issue():
    global issueBtn,labelFrame,lb1,bookInfo1,inf2,quitBtn,root,Canvas1,status
    
    bid=bookInfo1.get()
    issueto=inf2.get()
    borroweddate=date.today()
    duedate=borroweddate+timedelta(7)

    extractBid="SELECT BookID FROM "+bookTable

    try:
        cur.execute(extractBid)
        for i in cur:
            allBid.append(i[0])
        if bid in allBid:
            checkAvail="SELECT Status FROM "+bookTable+" WHERE BookID='"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check=i[0]
            if check in ['avail','Avail']:
                status=True
            else:
                status=False
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    issueSql="INSERT INTO "+issueTable+" VALUES ('"+bid+"','"+issueto+"','"+str(borroweddate)+"','"+str(duedate)+"')"
    updateStatus="UPDATE "+bookTable+" SET Status='Issued' WHERE BookID='"+bid+"'"
    updateStatus2="UPDATE "+bookTable+" SET IssuedTo='"+issueto+"'WHERE BookID='"+bid+"'"
    
    if bid in allBid and status==True:
        cur.execute(issueSql)
        con.commit()
        cur.execute(updateStatus)
        con.commit()
        cur.execute(updateStatus2)
        con.commit()
        print("BOOKID :",bid)
        print("ISSUED TO :",issueto)
        print("BORROWED DATE:",borroweddate)
        print("DUE DATE:",duedate)
        print("")
        messagebox.showinfo('Success',"Book Issued Successfully\n        Fine:Rs.2/day\nif returned late")
    elif bid in allBid and status==False:
        messagebox.showinfo('Message',"Book Already Issued")
    else:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    allBid.clear()
    quit()
    
def issueBook(): 
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,root1,status,lb2,lb3,lb4,inf3,inf4,bookInfo1
    root1.destroy()
    
    root=Tk()
    root.title("Issue Books")
    root.geometry("2000x1000")
    root.attributes('-fullscreen',True)

    frame=Frame(root,bg='black')
    frame.place(relwidth=1,relheight=1)
    load=Image.open("LIB IMG 5.jpg")
    bg=ImageTk.PhotoImage(load)
    bglabel=Label(frame,image=bg)
    bglabel.image=bg
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    headingFrame1=Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.13)
    
    headingLabel=Label(headingFrame1,text="D.A.V SR SECONDARY SCHOOL\nIssue Book", bg='black', fg='white', font=('Lucida Bright',25,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1, relheight=1)
    
    labelFrame=Frame(root,bg='black')
    labelFrame.place(relx=0.25,rely=0.35,relwidth=0.5,relheight=0.4)

    query="SELECT BookID FROM "+bookTable+" WHERE Status LIKE '_vail' "
    cur.execute(query)
    ids=cur.fetchall()
    query1="SELECT RefID FROM "+memTable
    cur.execute(query1)
    mem=cur.fetchall()
    opts=StringVar()
    opts1=StringVar()
        
    # Book ID
    lb1=Label(labelFrame,text="Book ID           :", bg='black', fg='white',font=('Cardinal',22))
    lb1.place(relx=0.05,rely=0.15)

    bookInfo1=ttk.Combobox(labelFrame,textvariable=opts,font=("Times New Roman",18))
    bookInfo1['values']=ids
    bookInfo1.place(relx=0.35,rely=0.15, relwidth=0.6,relheight=0.1)
    bookInfo1.current(0)
    
    # Issued To 
    lb2=Label(labelFrame,text="Issued To        :", bg='black', fg='white',font=('Cardinal',22))
    lb2.place(relx=0.05,rely=0.35)

    inf2=ttk.Combobox(labelFrame,textvariable=opts1,font=("Times New Roman",18))
    inf2['values']=mem
    inf2.place(relx=0.35,rely=0.35, relwidth=0.6,relheight=0.1)
    inf2.current(0)

    #Issued date
    lb3=Label(labelFrame,text="Issued Date     :", bg='black', fg='white',font=('Cardinal',22))
    lb3.place(relx=0.05,rely=0.55)
        
    inf3=Label(labelFrame,text=date.today(),font=("Times New Roman",18),anchor=W)
    inf3.place(relx=0.35,rely=0.55, relwidth=0.6,relheight=0.1)

    #Due date
    lb4=Label(labelFrame,text="Due Date         :",bg='black', fg='white',font=('Cardinal',22))
    lb4.place(relx=0.05,rely=0.8)
        
    inf4=Label(labelFrame,text=date.today()+timedelta(7),font=("Times New Roman",18),anchor=W)
    inf4.place(relx=0.35,rely=0.8,relwidth=0.6,relheight=0.1)
    
    #Issue Button
    issueBtn=Button(root,text="ISSUE",bg='#d1ccc0', fg='black',command=issue,font=('Times New Roman',22),bd=5)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    #Quit Button
    quitBtn=Button(root,text="BACK",bg='#f7f1e3', fg='black',command=quit,font=('Times New Roman',22),bd=5)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def quit():
    global root1,root
    root.destroy()
    
    root1=Tk()
    root1.title("Book Details")
    root1.geometry("2000x1000")
    root1.attributes('-fullscreen',True)

    frame=Frame(root1,bg='black')
    frame.place(relwidth=1,relheight=1)
    load=Image.open("LIB IMG 4.jpg")
    bg=ImageTk.PhotoImage(load)
    bglabel=Label(frame,image=bg)
    bglabel.image=bg
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    headingFrame1=Frame(root1,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.28,rely=0.1,relwidth=0.45,relheight=0.16)
    headingLabel=Label(headingFrame1,text="D.A.V SR SECONDARY SCHOOL\nBook Details",bg='black',fg='white',font=('Lucida Bright',25,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1, relheight=1)

    btn3=Button(root1,text="ADD BOOKS",bg='black',fg='white',font=("Courier",22),bd=5,command=addBook)
    btn3.place(relx=0.34,rely=0.35,relwidth=0.32,relheight=0.08)
        
    btn4=Button(root1,text="ISSUE BOOK",bg='black',fg='white',font=("Courier",22),bd=5,command=issueBook)
    btn4.place(relx=0.34,rely=0.43,relwidth=0.32,relheight=0.08)
        
    btn5=Button(root1,text="RETURN BOOK",bg='black',fg='white',font=("Courier",22),bd=5,command=returnBook)
    btn5.place(relx=0.34,rely=0.51,relwidth=0.32,relheight=0.08)

    btn5=Button(root1,text="DELETE BOOK",bg='black',fg='white',font=("Courier",22),bd=5,command=delete)
    btn5.place(relx=0.34,rely=0.59,relwidth=0.32,relheight=0.08)

    btn6=Button(root1,text="VIEW BOOKLIST",bg='black',fg='white',font=("Courier",22),bd=5,command=View)
    btn6.place(relx=0.34,rely=0.67,relwidth=0.32,relheight=0.08)

    btn7=Button(root1,text="SEARCH BOOK",bg='black',fg='white',font=("Courier",22),bd=5,command=searchBook)
    btn7.place(relx=0.34,rely=0.75,relwidth=0.32,relheight=0.08)

    btn7=Button(root1,text="BACK",bg='black',fg='white',font=("Courier",22),bd=5,command=quit3)
    btn7.place(relx=0.34,rely=0.83,relwidth=0.32,relheight=0.08)

    root1.mainloop()
    
def bookdetails():
    global root1,root,root3
    root3.destroy()
    
    root1=Tk()
    root1.title("Book Details")
    root1.geometry("2000x1000")
    root1.attributes('-fullscreen',True)

    frame=Frame(root1,bg='black')
    frame.place(relwidth=1,relheight=1)
    load=Image.open("LIB IMG 4.jpg")
    bg=ImageTk.PhotoImage(load)
    bglabel=Label(frame,image=bg)
    bglabel.image=bg
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    headingFrame1=Frame(root1,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.28,rely=0.1,relwidth=0.45,relheight=0.16)
    
    headingLabel=Label(headingFrame1,text="D.A.V SR SECONDARY SCHOOL\nBook Details",bg='black',fg='white',font=('Lucida Bright',25,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1, relheight=1)

    btn3=Button(root1,text="ADD BOOKS",bg='black',fg='white',font=("Courier",22),bd=5,command=addBook)
    btn3.place(relx=0.34,rely=0.35,relwidth=0.32,relheight=0.08)
        
    btn4=Button(root1,text="ISSUE BOOK",bg='black',fg='white',font=("Courier",22),bd=5,command=issueBook)
    btn4.place(relx=0.34,rely=0.43,relwidth=0.32,relheight=0.08)
        
    btn5=Button(root1,text="RETURN BOOK",bg='black',fg='white',font=("Courier",22),bd=5,command=returnBook)
    btn5.place(relx=0.34,rely=0.51,relwidth=0.32,relheight=0.08)
    btn5=Button(root1,text="DELETE BOOK",bg='black',fg='white',font=("Courier",22),bd=5,command=delete)
    btn5.place(relx=0.34,rely=0.59,relwidth=0.32,relheight=0.08)

    btn6=Button(root1,text="VIEW BOOKLIST",bg='black',fg='white',font=("Courier",22),bd=5,command=View)
    btn6.place(relx=0.34,rely=0.67,relwidth=0.32,relheight=0.08)

    btn7=Button(root1,text="SEARCH BOOK",bg='black',fg='white',font=("Courier",22),bd=5,command=searchBook)
    btn7.place(relx=0.34,rely=0.75,relwidth=0.32,relheight=0.08)

    btn7=Button(root1,text="BACK",bg='black',fg='white',font=("Courier",22),bd=5,command=quit3)
    btn7.place(relx=0.34,rely=0.83,relwidth=0.32,relheight=0.08)

    root1.mainloop()

n='MG'
extract2="SELECT COUNT(*) FROM "+memTable
cur.execute(extract2)
for p in cur.fetchone():
    print(p)
    
def memRegister():
    global p,n
    Mtype=bookInfo3.get()
    Ref=n+str(p+1)
    name=bookInfo2.get()
    doj=date.today()
    
    insertmem="INSERT INTO "+memTable+" VALUES ('"+Ref+"','"+name+"','"+Mtype+"','"+str(doj)+"')"
    
    try:
        if name=='':
            messagebox.showinfo("Error","Entry box not filled up")
        elif Mtype!='' and name!='':
            cur.execute(insertmem)
            con.commit()
            p+=1
            print("MEMBERTYPE :",Mtype)
            print("REFERENCE ID :",Ref)
            print("NAME :",name)
            print("DOJ:",doj)
            print("")
            messagebox.showinfo('Success',"Member added successfully")
    except:
        messagebox.showinfo("Error","Can't add Member into Database")
    
    quit2()

def addmem():
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas2,con,cur,memTable,root,p,lb1,lb2,lb3,lb4,root3
    root3.destroy()
    
    root=Tk()
    root.title("Library")
    root.title("Add Members")
    root.geometry("2000x1000")
    root.attributes('-fullscreen',True)
    
    frame=Frame(root,bg='black')
    frame.place(relwidth=1,relheight=1)
    load=Image.open("LIB IMG 7.jpg")
    bg=ImageTk.PhotoImage(load)
    bglabel=Label(frame,image=bg)
    bglabel.image=bg
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)
        
    headingFrame1=Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.13)
    
    headingLabel=Label(headingFrame1,text="D.A.V SR SECONDARY SCHOOL\nAdd Members", bg='black', fg='white', font=('Lucida Bright',25,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    labelFrame=Frame(root,bg='black')
    labelFrame.place(relx=0.25,rely=0.38,relwidth=0.5,relheight=0.37)
        
    #Refid
    lb1=Label(labelFrame,text="Reference ID    :", bg='black', fg='white',font=('Cardinal',20))
    lb1.place(relx=0.05,rely=0.15)
        
    bookInfo1=Label(labelFrame,text=n+str(p+1),font=("Times New Roman",18),anchor=W)
    bookInfo1.place(relx=0.33,rely=0.16, relwidth=0.6, relheight=0.1)
        
    #Name
    lb2=Label(labelFrame,text="Name               :", bg='black', fg='white',font=('Cardinal',20))
    lb2.place(relx=0.05,rely=0.35)
        
    bookInfo2=Entry(labelFrame,font=("Times New Roman",18))
    bookInfo2.place(relx=0.33,rely=0.36, relwidth=0.6, relheight=0.1)

    opts=StringVar()
        
    #MemberType
    lb3=Label(labelFrame,text="MemberType    :",bg='black',fg='white',font=('Cardinal',20))
    lb3.place(relx=0.05,rely=0.55)

    bookInfo3=ttk.Combobox(labelFrame,textvariable=opts,font=("Times New Roman",18))
    bookInfo3['values']=['Student','Staff']
    bookInfo3.place(relx=0.33,rely=0.56,relwidth=0.6,relheight=0.1)
    bookInfo3.current(0)

    #Date of Joining
    lb4=Label(labelFrame,text="DOJ                 :",bg='black',fg='white',font=('Cardinal',20))
    lb4.place(relx=0.05,rely=0.8)
        
    bookInfo4=Label(labelFrame,text=date.today(),font=("Times New Roman",18),anchor=W)
    bookInfo4.place(relx=0.33,rely=0.81,relwidth=0.6,relheight=0.1)

    #Add Button
    SubmitBtn=Button(root,text="SAVE",bg='#d1ccc0', fg='black',command=memRegister,font=('Times New Roman',22),bd=5)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    #Quit Button
    quitBtn=Button(root,text="BACK",bg='#f7f1e3', fg='black',command=quit2,font=('Times New Roman',22),bd=5)
    quitBtn.place(relx=0.53,rely=0.9,relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def Viewmem():
    global root3,root
    root3.destroy()
    
    root=Tk()
    root.title("View MembersList")
    root.geometry("2000x1000")
    root.attributes('-fullscreen',True)
    
    Canvas1=Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1=Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.3,rely=0.05,relwidth=0.4,relheight=0.13)
    
    headingLabel=Label(headingFrame1,text="D.A.V SR SECONDARY SCHOOL\nView Members",bg='black',fg='white',font=('Lucida Bright',25,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    labelFrame=Frame(root,bg='#12a4d9')
    labelFrame.place(relx=0,rely=0.2,relwidth=1,relheight=0.8)

    #Styles for Treeview widget
    s=ttk.Style()
    s.configure('mystyle.Treeview',font=('Lucida Bright',20,'bold'),rowheight=35)
    s.configure('mystyle.Treeview.Heading',font=('Ms serif',30,'bold','underline'))

    #Adding a scrollbar
    sb=ttk.Scrollbar(labelFrame)
    sb.pack(side=RIGHT,fill=Y)

    #Treeview Widget-for alligning properly
    mt=ttk.Treeview(labelFrame,columns=('REFID','NAME','MEMBERTYPE','DOJ'),style='mystyle.Treeview'
                    ,yscrollcommand=sb.set)
    mt.pack()
    sb.config(command=mt.yview)
    
    mt['columns']=('REFID','NAME','MEMBERTYPE','DOJ')
    mt.column('REFID',width=200,anchor=W)
    mt.column('NAME',width=200,anchor=W)
    mt.column('MEMBERTYPE',width=200,anchor=W)
    mt.column('DOJ',width=200,anchor=W)

    mt.heading('REFID',text='REFID',anchor=W)
    mt.heading('NAME',text='NAME',anchor=W)
    mt.heading('MEMBERTYPE',text='MEMBERTYPE',anchor=W)
    mt.heading('DOJ',text='DOJ',anchor=W)
    mt.pack(fill=BOTH,expand=1)

    getBooks="SELECT * FROM "+memTable
    cur.execute(getBooks)
    rows=cur.fetchall()
    for i in rows:
        mt.insert('','end',values='')
        mt.insert('','end',values=i)
    
    #Quit Button
    quitBtn=Button(root,text="BACK",bg='#d1ccc0', fg='black',command=quit2,font=('Times New Roman',22),bd=5)
    quitBtn.place(relx=0.42,rely=0.9,relwidth=0.14,relheight=0.07)

    root.mainloop()

def quit3():
    global root3,root,root1
    root1.destroy()
    
    root3=Tk()
    root3.title("Library Management System")
    root3.geometry("2000x1000")
    root3.attributes('-fullscreen',True)

    con=pymysql.connect(host="localhost",user="root",password='kitty',database='Project')
    cur=con.cursor()

    frame=Frame(root3,bg='black')
    frame.place(relwidth=1,relheight=1)
    load=Image.open("LIB IMG 7.jpg")
    bg=ImageTk.PhotoImage(load)
    bglabel=Label(frame,image=bg)
    bglabel.image=bg
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    headingFrame1=Frame(root3,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    
    headingLabel=Label(headingFrame1,text="D.A.V SR SECONDARY SCHOOL\nLibrary Management System",bg='black',fg='white',font=('Lucida Bright',25,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    headingFrame=Frame(root3,bg="#FFBB00",bd=5)
    headingFrame.place(relx=0.7,rely=0.85,relwidth=0.27,relheight=0.1)
    
    headingLabel1=Label(headingFrame,text="BY:Krithiga R & Kaavya Sree SK",bg='black',fg='white',font=('Lucida Bright',18,'bold'))
    headingLabel1.place(relx=0,rely=0,relwidth=1,relheight=1)

    btn1=Button(root3,text="VIEW MEMBERS LIST",bg='black',bd=5,fg='white',font=("Courier",22),command=Viewmem)
    btn1.place(relx=0.34,rely=0.4,relwidth=0.32,relheight=0.1)
        
    btn2=Button(root3,text="ADD MEMBERS",bg='black',bd=5,fg='white',font=("Courier",22),command=addmem)
    btn2.place(relx=0.34,rely=0.5,relwidth=0.32,relheight=0.1)

    btn3=Button(root3,text="BOOK DETAILS",bg='black',bd=5,fg='white',font=("Courier",22),command=bookdetails)
    btn3.place(relx=0.34,rely=0.6,relwidth=0.32,relheight=0.1)

    btn4=Button(root3,text="QUIT",bg='black',bd=5,fg='white',font=("Courier",22),command=root3.destroy)
    btn4.place(relx=0.34,rely=0.7,relwidth=0.32,relheight=0.1)

    root3.mainloop()

def quit2():
    global root3,root,root1
    root.destroy()
    
    root3=Tk()
    root3.title("Library Management System")
    root3.geometry("2000x1000")
    root3.attributes('-fullscreen',True)

    con=pymysql.connect(host="localhost",user="root",password='kitty',database='Project')
    cur=con.cursor()

    frame=Frame(root3,bg='black')
    frame.place(relwidth=1,relheight=1)
    load=Image.open("LIB IMG 7.jpg")
    bg=ImageTk.PhotoImage(load)
    bglabel=Label(frame,image=bg)
    bglabel.image=bg
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    headingFrame1=Frame(root3,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    
    headingLabel=Label(headingFrame1,text="D.A.V SR SECONDARY SCHOOL\nLibrary Management System",bg='black',fg='white',font=('Lucida Bright',25,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    headingFrame=Frame(root3,bg="#FFBB00",bd=5)
    headingFrame.place(relx=0.7,rely=0.85,relwidth=0.27,relheight=0.1)
    
    headingLabel1=Label(headingFrame,text="BY:Krithiga R & Kaavya Sree SK",bg='black',fg='white',font=('Lucida Bright',18,'bold'))
    headingLabel1.place(relx=0,rely=0,relwidth=1,relheight=1)

    btn1=Button(root3,text="VIEW MEMBERS LIST",bg='black',bd=5,fg='white',font=("Courier",22),command=Viewmem)
    btn1.place(relx=0.34,rely=0.4,relwidth=0.32,relheight=0.1)
        
    btn2=Button(root3,text="ADD MEMBERS",bg='black',bd=5,fg='white',font=("Courier",22),command=addmem)
    btn2.place(relx=0.34,rely=0.5,relwidth=0.32,relheight=0.1)

    btn3=Button(root3,text="BOOK DETAILS",bg='black',bd=5,fg='white',font=("Courier",22),command=bookdetails)
    btn3.place(relx=0.34,rely=0.6,relwidth=0.32,relheight=0.1)

    btn4=Button(root3,text="QUIT",bg='black',bd=5,fg='white',font=("Courier",22),command=root3.destroy)
    btn4.place(relx=0.34,rely=0.7,relwidth=0.32,relheight=0.1)

    root3.mainloop()
        
def login():
    n='Kaavyakrithiga'
    if usertxt.get()=="" or pwdtxt.get()=="":
        messagebox.showinfo('Error',"Entry box not filled up")
    elif usertxt.get()!="Kaavyakrithiga" or pwdtxt.get()!="1234":
        messagebox.showinfo('Error',"Invalid Username/Password")
    else:
        screen()

lb=Button(root4,text="LOGIN",fg="white",bg="#d77337",command=login,bd=5,font=("Times New Roman",20,"bold")).place(x=130,y=680,width=180,height=45)
lb=Button(root4,text="EXIT",fg="white",bg="#d77337",command=root4.destroy,bd=5,font=("Times New Roman",20,"bold")).place(x=370,y=680,width=180,height=45)

def screen():
    global root4,root3
    root4.destroy()
    
    root3=Tk()
    root3.title("Library Management System")
    root3.geometry("2000x1000")
    root3.attributes('-fullscreen',True)

    con=pymysql.connect(host="localhost",user="root",password='kitty',database='Project')
    cur=con.cursor()

    frame=Frame(root3,bg='black')
    frame.place(relwidth=1,relheight=1)
    load=Image.open("LIB IMG 7.jpg")
    bg=ImageTk.PhotoImage(load)
    bglabel=Label(frame,image=bg)
    bglabel.image=bg
    bglabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    headingFrame1=Frame(root3,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    
    headingLabel=Label(headingFrame1,text="D.A.V SR SECONDARY SCHOOL\nLibrary Management System",bg='black',fg='white',font=('Lucida Bright',25,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    headingFrame=Frame(root3,bg="#FFBB00",bd=5)
    headingFrame.place(relx=0.7,rely=0.85,relwidth=0.27,relheight=0.1)
    
    headingLabel1=Label(headingFrame,text="BY:Krithiga R & Kaavya Sree SK",bg='black',fg='white',font=('Lucida Bright',18,'bold'))
    headingLabel1.place(relx=0,rely=0,relwidth=1,relheight=1)

    btn1=Button(root3,text="VIEW MEMBERS LIST",bg='black',bd=5,fg='white',font=("Courier",22),command=Viewmem)
    btn1.place(relx=0.34,rely=0.4,relwidth=0.32,relheight=0.1)
        
    btn2=Button(root3,text="ADD MEMBERS",bg='black',bd=5,fg='white',font=("Courier",22),command=addmem)
    btn2.place(relx=0.34,rely=0.5,relwidth=0.32,relheight=0.1)

    btn3=Button(root3,text="BOOK DETAILS",bg='black',bd=5,fg='white',font=("Courier",22),command=bookdetails)
    btn3.place(relx=0.34,rely=0.6,relwidth=0.32,relheight=0.1)

    btn4=Button(root3,text="QUIT",bg='black',bd=5,fg='white',font=("Courier",22),command=root3.destroy)
    btn4.place(relx=0.34,rely=0.7,relwidth=0.32,relheight=0.1)

    root3.mainloop()
    
root4.mainloop()
