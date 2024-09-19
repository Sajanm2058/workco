from tkinter import *   # to import all the classes and methods present in tkiner which helps to greating in grapical user interface 
from tkinter import messagebox  # to display message boxes
from PIL import ImageTk   # to import python image library helps to import jpg image for png file no pil is required



def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get() == 'sajan' and passwordEntry.get() =='1234':
        messagebox.showinfo('success','welcome')
        window.destroy()
        import stdmng2
    else:
        messagebox.showerror('Error','Invalid Username or Password')
        



      
window = Tk()


window.geometry("1280x700+0+0")
window.title('Login system of Student management system')

window.resizable(False,False)

backgroundImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(window,image = backgroundImage)  # just created a new label

bgLabel.place(x=0,y=0) # to place the background


loginFrame = Frame(window,bg='white')  # the frame inside which we contain the logo and login user input.
loginFrame.place(x=400,y=150)

logoImage = PhotoImage(file='logo.png')

logoLabel = Label(loginFrame,image = logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

# username entry
usernameImage = PhotoImage(file='user.png')
usernameLabel = Label(loginFrame,image=usernameImage,text="Username",compound=LEFT
                      ,font = ('times new Roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)


usernameEntry = Entry(loginFrame,font = ('times new Roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

# password entry
passwordImage = PhotoImage(file='password.png')
passwordLabel = Label(loginFrame,image=passwordImage,text='Password',compound=LEFT
                      ,font=('times new Roman',20,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

passwordEntry = Entry(loginFrame,font = ('times new Roman',20,'bold'),bd=5,fg='royalblue',show='*')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

# login button


loginButton = Button(loginFrame,text='Login',font = ('times new Roman',14,'bold'),width=15,bg='cornflowerblue',fg='white'
                     ,activebackground='cornflowerblue',activeforeground='white'
                     ,cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)

# register button



window.mainloop()  # this is the main loop of the program

