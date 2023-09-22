from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os

#size
root = Tk()
root.title('project management')
root.geometry('950x500+300+100')
root.configure(bg='#fff')
root.resizable(False,False)

def Project_editing():
        def project_editing2():

                code_file = user5_1.get() 
                if code_file == '':
                        messagebox.showerror('ERROR','Code file is None')

                # elif f'{code_file}.txt' not in os.listdir(r'C:\Users\sohei\OneDrive\Desktop\project endly\user') :
                #         messagebox.showerror('ERROR','Your Code File is Wrong')
                #         print('iehfbbirihfbekisuhfbkerhbgf')
                else:          

                        screen5 = Tk()
                        screen5.title('Project Editing')
                        screen5.geometry('950x500+300+100')
                        screen5.configure(bg='#fff')
                        screen5.resizable(False,False)

                        def open_file():
                                text_file = open(f'user/{code_file}.txt','r')
                                stuff = text_file.read()
                                my_text.insert(END, stuff)
                                text_file.close()
                                # screen5.destroy()
                                # messagebox.showerror('ERROR','Your Code File is Wrong')

                        def save_txt():
                                text_file = open(f'user/{code_file}.txt','w')
                                text_file.write(my_text.get(1.0, END))
                                messagebox.showinfo('Savw','Sucessfully !!!')
                                screen5.destroy()

                        my_text = Text(screen5,width=40,bg='#FF7252',height=10,font=('Helvetic',16))
                        my_text.pack(pady=20)

                        btm1 = Button(screen5,text='Open text File',width=28,bg='#FF7252',fg='white',border=0,font=('microsoft YaHei UI light',11,'bold'),command=open_file)
                        btm1.place(x=350,y=300)
                        btm2 = Button(screen5,text='Save File',width=28,bg='#FF7252',fg='white',border=0,font=('microsoft YaHei UI light',11,'bold'),command=save_txt)
                        btm2.place(x=350,y=340)
                        
                        screen5.mainloop()

        root.destroy()
        screen4 = Tk()
        screen4.title('Code File')
        screen4.geometry('950x500+300+100')
        screen4.config(bg='#fff')
        screen4.resizable(False,False)  
        #photo4
        img = PhotoImage(file='Photos/N9.png')
        lib = Label(screen4,image=img,bg='white').place(x=50,y=50)
        frame = Frame(screen4,width=350,height=350,bg='white').place(x=480,y=70)


        #--------heading----
        heading = Label(screen4,text='Code File ',fg='#FF7252',background='white',font=('microsoft YaHei UI light',28,'bold'))
        heading.place(x=610,y=50)   
        #-------user5_1----
        def on_enter(e):
            user5_1.delete(0,'end')

        def on_leave(e):
            name = user5_1.get()
            if name == '':
              user5_1.insert(0,'Enter code')
              
        user5_1 = Entry(screen4,width=25,fg='black',border=0,bg='white',font=('microsoft YaHei UI light',11,'bold'))
        user5_1.place(x=550,y=200)
        user5_1.insert(0,'Enter code')  
        user5_1.bind('<FocusIn>',on_enter)
        user5_1.bind('<FocusOut>',on_leave) 
        Frame(screen4,width=280,height=2,bg='#FF7252').place(x=550,y=225)

        #--------button-----
        Button(screen4,text='Enter',width=28,bg='#FF7252',fg='white',border=0,font=('microsoft YaHei UI light',11,'bold'),command=project_editing2).place(x=550,y=300)

        screen4.mainloop()


def Project_registration():
#     root.destroy()
    screen3 = Toplevel(root)
    screen3.title('New Project')
    screen3.geometry('950x500+300+100')
    screen3.config(bg='#fff')
    screen3.resizable(False,False)
#--------new-def-for-registration----------
    def registration_endly():
        # file2 = open('dataProject.txt','r')
        username4_1 = user4_1.get()
        username4_2 = user4_2.get()
        username4_3 = user4_3.get()
        username4_4 = user4_4.get()
        username4_5 = user4_5.get()
        if   username4_5 == '':
             messagebox.showerror('ERROR','Code file is not number!!!')  
        elif username4_1 == '':
             messagebox.showerror('Invalid','Your project name is none !!!')  
        elif username4_2 == '':
             messagebox.showerror('Invalid','Your compony name is none !!!')  
        elif username4_3 == '':
             messagebox.showerror('Invalid','Fild start datatime is none !!!')                            
        elif username4_4 == '':
             messagebox.showerror('Invalid','Fild end datatime is none !!!') 
        elif username4_5 == 'Your code':
             messagebox.showerror('Invalid','Your Code File is none !!!')                            

        else:     
             f = open(f'user/{username4_5}.txt','a') 
             f.write(username4_1+','+username4_2+','+username4_3+','+username4_4+'\n')
             messagebox.showinfo('project','Sucessfully Sign up project !!!')
             screen3.destroy()

    img = PhotoImage(file='Photos/N7.png')
    lib = Label(screen3,image=img,bg='white').place(x=50,y=50)
    frame = Frame(screen3,width=350,height=350,bg='white').place(x=480,y=70)             

    #portal-lable-heading
    heading3 = Label(screen3,text='New Project',fg='#FF7252',background='white',font=('microsoft YaHei UI light',28,'bold'))
    heading3.place(x=585,y=50)


    #---------entery1---user4_1----nameproject
    def on_enter(e):
            user4_1.delete(0,'end')

    def on_leave(e):
            name = user4_1.get()
            if name == '':
              user4_1.insert(0,'Name project')
              
    user4_1 = Entry(screen3,width=25,fg='black',border=0,bg='white',font=('microsoft YaHei UI light',11,'bold'))
    user4_1.place(x=550,y=150)
    user4_1.insert(0,'Name project')  
    user4_1.bind('<FocusIn>',on_enter)
    user4_1.bind('<FocusOut>',on_leave) 
    Frame(screen3,width=278,height=2,bg='#FF7252').place(x=550,y=175)

    #---------entery2---user4_2----Namecompony
    def on_enter(e):
            user4_2.delete(0,'end')

    def on_leave(e):
            name = user4_2.get()
            if name == '':
              user4_2.insert(0,'Name compony')
              
    user4_2 = Entry(screen3,width=25,fg='black',border=0,bg='white',font=('microsoft YaHei UI light',11,'bold'))
    user4_2.place(x=550,y=200)
    user4_2.insert(0,'Name compony')  
    user4_2.bind('<FocusIn>',on_enter)
    user4_2.bind('<FocusOut>',on_leave) 
    Frame(screen3,width=278,height=2,bg='#FF7252').place(x=550,y=225)

    #---------entery3---user4_3----datetime-start 
    def on_enter(e):
            user4_3.delete(0,'end')

    def on_leave(e):
            name = user4_3.get()
            if name == '':
              user4_3.insert(0,'Start date 00/00/00')
              
    user4_3 = Entry(screen3,width=25,fg='black',border=0,bg='white',font=('microsoft YaHei UI light',11,'bold'))
    user4_3.place(x=550,y=250)
    user4_3.insert(0,'Start date 00/00/00')  
    user4_3.bind('<FocusIn>',on_enter)
    user4_3.bind('<FocusOut>',on_leave) 
    Frame(screen3,width=278,height=2,bg='#FF7252').place(x=550,y=275)
   
    #---------entery4---user4_4----datetime-end
    def on_enter(e):
            user4_4.delete(0,'end')

    def on_leave(e):
            name = user4_4.get()
            if name == '':
              user4_4.insert(0,'End date 00/00/00')
              
    user4_4 = Entry(screen3,width=25,fg='black',border=0,bg='white',font=('microsoft YaHei UI light',11,'bold'))
    user4_4.place(x=550,y=300)
    user4_4.insert(0,'End date 00/00/00')  
    user4_4.bind('<FocusIn>',on_enter)
    user4_4.bind('<FocusOut>',on_leave) 
    Frame(screen3,width=278,height=2,bg='#FF7252').place(x=550,y=325)

    #---------entery5---user4_5----code
    def on_enter(e):
            user4_5.delete(0,'end')

    def on_leave(e):
            name = user4_5.get()
            if name == '':
              user4_5.insert(0,'Your code')
              
    user4_5 = Entry(screen3,width=25,fg='black',border=0,bg='white',font=('microsoft YaHei UI light',11,'bold'))
    user4_5.place(x=550,y=350)
    user4_5.insert(0,'Your code')  
    user4_5.bind('<FocusIn>',on_enter)
    user4_5.bind('<FocusOut>',on_leave) 
    Frame(screen3,width=278,height=2,bg='#FF7252').place(x=550,y=375)

    #---Button--------
    Button(screen3,width=39,pady=7,text='Project editing',bg='#FF7252',fg='white',border=0,command=registration_endly).place(x=550,y=400)



    screen3.mainloop()


def portal_win():
        
        screen = Toplevel(root)
        screen.title('My Portal')
        screen.geometry('950x500+300+100')
        screen.config(bg='#fff')
        screen.resizable(False,False)

        #photo-in-portal
        img2 = PhotoImage(file='Photos/N8.png')
        lib2 = Label(screen,image=img2,bg='white').place(x=50,y=50)
        frame2 = Frame(screen,width=350,height=350,bg='white').place(x=480,y=70)

        #portal-lable-heading
        heading2 = Label(screen,text='My Portal',fg='#FF7252',background='white',font=('microsoft YaHei UI light',28,'bold'))
        heading2.place(x=600,y=50)

        ##portal-button1
        Button(screen,width=39,pady=7,text='Project registration',bg='#FF7252',fg='white',border=0,command=Project_registration).place(x=550,y=200)
        Button(screen,width=39,pady=7,text='Project editing',bg='#FF7252',fg='white',border=0,command=Project_editing).place(x=550,y=260)

        screen.mainloop()

def login():
    f = open('datasheet.txt','r')        
    username = user.get()
    password = user2.get()
    q1 = []
    q2 = []
    for i in f:
        a,b = i.split(',')
        # b = b.strip()
        q1.append(a)
        q2.append(b)
    data = dict(zip(q1,q2))
    q22 = []
    for i in q2:
        w = len(i) - 1
        q22.append(i[:w:])
#-----------------new-pags-open-portal----
    if username in q1 :
        if password in q22:
                portal_win()
        else:
                messagebox.showerror('Invalid','Invalid your password !!!')
    else:
        messagebox.showerror('Invalid','Invalid your name !!!')
#--------------sign-up-----------
def sign__up():

    def sign_up2():
        f = open('datasheet.txt','r')        
        username3_1 = user3_1.get()
        password3_2 = user3_2.get()
        password3_3 = user3_3.get()
        code3_4 = user3_4.get()
        q1 = []
        q2 = []
        for i in f:
                a,b = i.split(',')
                # b = b.strip()
                q1.append(a)
                q2.append(b)
        data = dict(zip(q1,q2))
        if password3_2 != password3_3:
                messagebox.showerror('ERROR','Both password should match')
 
        else:
            if username3_1 in q1:
                    messagebox.showerror('ERROR',f'This is {username3_1} in database !!!, pleas change name')

            elif len(password3_2) <4:
                    messagebox.showerror('ERROR','Your password is short , Pleas more 4 charecter!!!')

            elif 'Username' == username3_1:
                    messagebox.showerror('ERROR','Fild user is none')
            else:
                f = open('datasheet.txt','a') 
                f.write(username3_1+','+password3_2+'\n')
                messagebox.showinfo('Sign un','Sucessfully Sign up')
                opf = str(code3_4) 
                with open(f'user/{opf}.txt','w') as f:
                        pass
                screen2.destroy()
   
    screen2 = Toplevel(root)
    screen2.title('Sign up')
    screen2.geometry('950x500+300+100')
    screen2.config(bg='#fff')
    screen2.resizable(False,False)

    #photo3
    img3 = PhotoImage(file='Photos/N6.png')
    lib3 = Label(screen2,image=img3,bg='white').place(x=50,y=50)
    frame = Frame(screen2,width=350,height=350,bg='white').place(x=480,y=70)

    #sign-in-lable-heading
    heading3 = Label(screen2,text='sign up',fg='#FF7252',background='white',font=('microsoft YaHei UI light',28,'bold'))
    heading3.place(x=635,y=50)
    #user3_1
    def on_enter(e):
         user3_1.delete(0,'end')

    def on_leave(e):
         name = user3_1.get()
         if name == '':
              user3_1.insert(0,'Username')
              
    user3_1 = Entry(screen2,width=25,fg='black',border=0,bg='white',font=('microsoft YaHei UI light',11,'bold'))
    user3_1.place(x=550,y=150)
    user3_1.insert(0,'Username')  
    user3_1.bind('<FocusIn>',on_enter)
    user3_1.bind('<FocusOut>',on_leave) 
    Frame(screen2,width=278,height=2,bg='#FF7252').place(x=550,y=175)
    #user3_2-password
    def on_enter(e):
         user3_2.delete(0,'end')

    def on_leave(e):
         name = user3_2.get()
         if name == '':
              user3_2.insert(0,'Password')
    user3_2 = Entry(screen2,width=25,fg='black',border=0,bg='white',font=('microsoft YaHei UI light',11,'bold'))
    user3_2.place(x=550,y=200)
    user3_2.insert(0,'Password')   
    user3_2.bind('<FocusIn>',on_enter)
    user3_2.bind('<FocusOut>',on_leave)
    Frame(screen2,width=278,height=2,bg='#FF7252').place(x=550,y=225)
    #user3_3-password2
    def on_enter(e):
         user3_3.delete(0,'end')

    def on_leave(e):
         name = user3_3.get()
         if name == '':
              user3_3.insert(0,'Password again')    
    user3_3 = Entry(screen2,width=25,fg='black',border=0,bg='white',font=('microsoft YaHei UI light',11,'bold'))
    user3_3.place(x=550,y=250)
    user3_3.insert(0,'Password again')   
    user3_3.bind('<FocusIn>',on_enter)
    user3_3.bind('<FocusOut>',on_leave)    
    Frame(screen2,width=278,height=2,bg='#FF7252').place(x=550,y=275)

    #user3_4-code-just-number
    def on_enter(e):
         user3_4.delete(0,'end')

    def on_leave(e):
         name = user3_4.get()
         if name == '':
              user3_4.insert(0,'Code file just number')    
    user3_4 = Entry(screen2,width=25,fg='black',border=0,bg='white',font=('microsoft YaHei UI light',11,'bold'))
    user3_4.place(x=550,y=300)
    user3_4.insert(0,'Code file (just number)')   
    user3_4.bind('<FocusIn>',on_enter)
    user3_4.bind('<FocusOut>',on_leave)    
    Frame(screen2,width=278,height=2,bg='#FF7252').place(x=550,y=325)


    ##sign-up-button-----
    Button(screen2,width=39,pady=7,text='sign up',bg='#FF7252',fg='white',border=0,command=sign_up2).place(x=550,y=350)


    screen2.mainloop()

  
#photo
img = PhotoImage(file='Photos/N5.png')
lib = Label(root,image=img,bg='white').place(x=50,y=50)
frame = Frame(root,width=350,height=350,bg='white').place(x=480,y=70)

#log in lable heading
heading = Label(frame,text='log in',fg='#FF7252',background='white',font=('microsoft YaHei UI light',28,'bold'))
heading.place(x=635,y=50)

##user1-------
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0,'Username')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('microsoft YaHei UI light',11,'bold'))
user.place(x=550,y=150)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=278,height=2,bg='#FF7252').place(x=550,y=175)

##user2-------
def on__enter(e):
    user2.delete(0,'end')

def on__leave(e):
    name = user2.get()
    if name == '':
        user2.insert(0,'Password')



user2 = Entry(frame,width=25,fg='black',border=0,bg='white',font=('microsoft YaHei UI light',11,'bold'))
user2.place(x=550,y=200)
user2.insert(0,'Password')
user2.bind('<FocusIn>',on__enter)
user2.bind('<FocusOut>',on__leave)

Frame(frame,width=278,height=2,bg='#FF7252').place(x=550,y=225)

##button-----
Button(frame,width=39,pady=7,text='log in',bg='#FF7252',fg='white',border=0,command=login).place(x=550,y=300)
lable = Label(frame,text="Don't have an account ?",fg='black',bg='white',font=('microsoft YaHei UI light',9))
lable.place(x=580,y=355)

#link-sign-up
sign_up = Button(frame,width=6,text='sign up',border=0,bg='white',cursor='hand2',fg='#FF7252',command=sign__up)
sign_up.place(x=725,y=355)

root.mainloop()