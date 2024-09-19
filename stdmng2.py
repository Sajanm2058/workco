from tkinter import *
import time
import ttkthemes  # for importing themes
from tkinter import ttk, messagebox,filedialog
import pymysql
import pandas
# Fuctionality part

def iexit():
    result = messagebox.askyesno('Confirm','Do you want to exit')
    if result:
        root.destroy()
    else:
        pass

def export_data():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = studentTable.get_children()
    newlist = []
    for index in indexing:
        content = studentTable.item(index)
        datalist = content['values']
        newlist.append(datalist)
    table=pandas.DataFrame(newlist, columns=['Id', 'Name','Mobile','Email','Address','Gender','Dob','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo("Success","Data Exported Successfully")




def toplevel_data(title,button_text,command):

    global idEntry,mobileEntry,nameEntry,emailEntry,addressEntry,genderEntry,dobEntry,screen  
    screen = Toplevel()
    screen.grab_set()
    screen.resizable(0,0)
    screen.title(title)
    idLabel = Label(screen,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry = Entry(screen,font=('times new roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel = Label(screen,text='Name',font=('times new roman',20,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry = Entry(screen,font=('times new roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)

    mobileLabel = Label(screen,text='Mobile',font=('times new roman',20,'bold'))
    mobileLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    mobileEntry = Entry(screen,font=('times new roman',15,'bold'),width=24)
    mobileEntry.grid(row=2,column=1,pady=15,padx=10)

    emailLabel = Label(screen,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry = Entry(screen,font=('times new roman',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,pady=15,padx=10)
    
    addressLabel = Label(screen,text='Address',font=('times new roman',20,'bold'))
    addressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addressEntry = Entry(screen,font=('times new roman',15,'bold'),width=24)
    addressEntry.grid(row=4,column=1,pady=15,padx=10)
    
    genderLabel = Label(screen,text='Gender',font=('times new roman',20,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    genderEntry = Entry(screen,font=('times new roman',15,'bold'),width=24)
    genderEntry.grid(row=5,column=1,pady=15,padx=10)
    
    dobLabel = Label(screen,text='D.O.B',font=('times new roman',20,'bold'))
    dobLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    dobEntry = Entry(screen,font=('times new roman',15,'bold'),width=24)
    dobEntry.grid(row=6,column=1,pady=15,padx=10)

    student_button = ttk.Button(screen,text=button_text,command=command)
    student_button.grid(row=7,columnspan=2,pady=15) 

    if title == 'Update Student':
        indexing = studentTable.focus()

        content = studentTable.item(indexing) 
        listdata = content['values']  
        idEntry.insert(0,listdata[0])
        nameEntry.insert(0,listdata[1])
        mobileEntry.insert(0,listdata[2])
        emailEntry.insert(0,listdata[3])
        addressEntry.insert(0,listdata[4])
        genderEntry.insert(0,listdata[5])
        dobEntry.insert(0,listdata[6])




def update_data():
    query = 'update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id = %s'
    mycursor.execute(query,(nameEntry.get(),mobileEntry.get(),emailEntry.get(),addressEntry.get(),
                            genderEntry.get(),dobEntry.get(),date,currenttime,idEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id {idEntry.get()} Updated Successfully',parent=screen)
    screen.destroy()
    show_student()



  

    




def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)


def delete_student():   # select the that and fetched id and with the help of id delete the records.
    indexing = studentTable.focus()
    print(indexing)
    content = studentTable.item(indexing)
    content_id = content['values'][0]
    query = 'delete from  student where id = %s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'This ID = {content_id} is deleted successfully')
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)
        
        
    



def search_data():

    query = 'select * from student where id = %s or name =%s or email =%s or mobile =%s or address =%s or gender = %s or dob =%s'    
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),mobileEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)








def add_data():
    if idEntry.get() == '' or nameEntry.get() == '' or mobileEntry.get() == '' or emailEntry.get() == '' or addressEntry.get() == '' or genderEntry.get() == '' or dobEntry.get() == '':
        messagebox.showerror('Error','Please fill all the fields',parent=screen)
    else:

        try:
            query = 'insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),mobileEntry.get(),emailEntry.get(),
                                    addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currenttime))
            con.commit()
            result = messagebox.askyesno('Confirm','Data added successfully, Do you want to clean the form?',parent=screen)
            if result == True:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                mobileEntry.delete(0,END)
                emailEntry.delete(0,END)
                addressEntry.delete(0,END)
                genderEntry.delete(0,END)
                dobEntry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror('Error','Id cannot be repeated',parent=screen)
            return 


        query = 'select * from student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()

        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('',END,values = data)
                

    




def connect_database():
    def connect():
        global mycursor,con
        try:
            con = pymysql.connect(host = hostEntry.get(),user=usernameEntry.get(),password=passwordEntry.get())
            mycursor = con.cursor()  # helps in executing commands
        except:
            messagebox.showerror('Error','Invalid Username or Password',parent=connectWindow)
            return
        try:
            query = 'create database studentmanagementsystem'
            mycursor.execute(query)
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
            query = 'create table student(id int not null primary key, name varchar(30),mobile varchar(30), email varchar(30),'\
                'address varchar(100),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50))'
            mycursor.execute(query)
        except:  #if database is already created
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success','Successfully Connected to Database',parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportdataButton.config(state=NORMAL)   
        deletedstudentButton.config(state=NORMAL)             
            

    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+600+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)


    hostnameLabel = Label(connectWindow,text='Host Name',font = ('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry = Entry(connectWindow,font=('roman',15,'bold'),bd = 2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow,text='Username',font = ('arial',20,'bold'))
    usernameLabel.grid(row=1,column=0,padx=20)

    usernameEntry = Entry(connectWindow,font=('roman',15,'bold'),bd = 2)
    usernameEntry.grid(row=1,column=1,padx=40,pady=20)
    
    passwordLabel = Label(connectWindow,text='Password',font = ('arial',20,'bold'))
    passwordLabel.grid(row=2,column=0,padx=20)
    
    passwordEntry = Entry(connectWindow,font=('roman',15,'bold'),bd = 2)
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)
    
    connectButton = ttk.Button(connectWindow,text='Connect',command = connect)
    connectButton.grid(row=3,column=0)
    
    cancelButton = ttk.Button(connectWindow,text='Cancel',command = lambda: connectWindow.destroy())
    cancelButton.grid(row=3,column=1)

    
    
    

def clock():
    global date, currenttime
    date = time.strftime("%d/%m/%Y")
    currenttime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text = f'  Date:{date}\nTime: {currenttime}')   # update datetime
    datetimeLabel.after(1000,clock)  # update every 1 second

count = 0
text = ''
def slider():
    global text,count
    if count == len(s):
        count = 0
        text = ''
    text = text +s[count] #S
    sliderLabel.config(text = text)
    count += 1
    sliderLabel.after(200,slider)



# GUI part

root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')



root.geometry('1174x680+0+0')

root.title('Student Management system')
root.resizable(0,0) # for not changing thw window size


datetimeLabel = Label(root,font = ('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()


s = 'Student Management System'  #s[count] = S when count =0
sliderLabel = Label(root,font= ('arial',20,'italic bold'),width =30)
sliderLabel.place(x=300,y=0)
slider()

# connect button
connectButton = ttk.Button(root,text='Connect to database',command= connect_database)  
connectButton.place(x=980,y=0)


# left frame

leftFrame = Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600,)

#logo image
logo_Image = PhotoImage(file = 'student (1).png')
logo_Label = Label(leftFrame,image=logo_Image)
logo_Label.grid(row=0,column=0)

#student button

addstudentButton = ttk.Button(leftFrame,text='Add student',width=25,state=DISABLED,command=lambda :toplevel_data('Add student','SUBMIT',add_data))
addstudentButton.grid(row=1,column=0,pady=20)

#search student button
searchstudentButton = ttk.Button(leftFrame,text='Search student',width=25,state=DISABLED,command=lambda :toplevel_data('Search student','SEARCH',search_data))
searchstudentButton.grid(row=2,column=0,pady=20)

# deleted student button
deletedstudentButton = ttk.Button(leftFrame,text='Delete student',width=25,state=DISABLED,command=delete_student)
deletedstudentButton.grid(row=3,column=0,pady=20)

# update student buttons
updatestudentButton = ttk.Button(leftFrame,text='Update student',width=25,state=DISABLED,command=lambda:toplevel_data('Update Student','UPDATE',update_data))
updatestudentButton.grid(row=4,column=0,pady=20)

# show student
showstudentButton = ttk.Button(leftFrame,text='Show student',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

#export data
exportdataButton = ttk.Button(leftFrame,text='Export data',width=25,state=DISABLED,command=export_data)
exportdataButton.grid(row=6,column=0,pady=20)

#exit
exitButton = ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitButton.grid(row=7,column=0,pady=20)


# right frame
rightFrame = Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

#scroll bar
scrollBarX = Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame,orient=VERTICAL)


#tree view
studentTable = ttk.Treeview(rightFrame,column=('Id','Name','Mobile No','Email','Address','Gender',
                                               'D.O.B.','Added Date','Added Time'),
                                               xscrollcommand=scrollBarX.set,
                                               yscrollcommand=scrollBarY.set)
scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)


scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)


#student table heading
studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile No',text='Mobile No')
studentTable.heading('Email',text='Email')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B.',text='D.O.B.')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')


studentTable.column('Id',anchor=CENTER,width=50)
studentTable.column('Name',anchor=CENTER,width=200)
studentTable.column('Mobile No',anchor=CENTER,width=200)
studentTable.column('Email',anchor=CENTER,width=200)
studentTable.column('Address',anchor=CENTER,width=200)
studentTable.column('Gender',anchor=CENTER,width=200)
studentTable.column('D.O.B.',anchor=CENTER,width=200)
studentTable.column('Added Date',anchor=CENTER,width=200)
studentTable.column('Added Time',anchor=CENTER,width=200)


style = ttk.Style()
style.configure('Treeview', rowheight= 40,font=('arial',12,'bold'))
style.configure('Treeview.Heading', font=('arial',15,'bold'))


studentTable.config(show='headings')

root.mainloop()