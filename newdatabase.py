# from tkinter import *
# import sqlite3
# from tkinter import messagebox

# root=Tk()
# root.geometry("1200x1200")

# # conn=sqlite3.connect("facebook.db")
# # c=conn.cursor()
# # c.execute("""CREATE TABLE user(
# #     first_name text,
# #     last_name text,
# #     address text,
# #     age text,
# #     password text,
# #     father_name text,
# #     city text,
# #     zip_code integer)""")
# # conn.commit()
# # conn.close()

# #function to insert records
# def insert():
#     conn=sqlite3.connect("facebook.db")
#     c=conn.cursor()
#     c.execute("INSERT INTO user VALUES(:f_name,:l_name,:address,:age,:password,:father_name,:city,:zip_code)",{
#         'f_name':first_nameE.get(),
#         'l_name':last_nameE.get(),
#         'address':addressE.get(),
#         'age':ageE.get(),
#         'password':passwordE.get(),
#         'father_name':father_nameE.get(),
#         'city':cityE.get(),
#         'zip_code':zip_codeE.get()
#     }) 
#     messagebox.showinfo("user","success")
#     conn.commit()
#     conn.close()


# #function to show record
# def show_records():
#     conn=sqlite3.connect('facebook.db')
#     c=conn.cursor()
#     c.execute("SELECT *, oid from user")
#     records=c.fetchall()
#     print(records)
#     print_record=""
#     for record in records:
#         print_record+=str(record[0])+' '+str(record[1])+' '+str(record[6])+"\n"
#     show_records_label=Label(root,text=print_record)
#     show_records_label.grid(row=9, column=3)
#     conn.commit()
#     conn.close()

# #function to edit records
# def edit():
#     global editor
#     editor=Tk()
#     editor.title("Update data")
#     editor.geometry('500x500')
#     conn=sqlite3.connect('facebook.db')
#     c=conn.cursor()
#     record_id= deleteE.get()
#     c.execute("SELECT * from user WHERE oid="+ record_id)
#     records=c.fetchall()
#     #creating global variable for entry
#     global first_nameN
#     global last_nameN
#     global addressN
#     global ageN
#     global passwordN
#     global father_nameN
#     global cityN
#     global zipcodeN

#     #defining entries for new window
#     first_nameN=Entry(editor)
#     last_nameN=Entry(editor)
#     addressN=Entry(editor)
#     ageN=Entry(editor)
#     passwordN=Entry(editor)
#     father_nameN=Entry(editor)
#     cityN=Entry(editor)
#     zipcodeN=Entry(editor)

#    #placing the new entries
#     first_nameN.grid(row=1,column=4)
#     last_nameN.grid(row=2,column=4)
#     addressN.grid(row=3,column=4)
#     ageN.grid(row=4,column=4)
#     passwordN.grid(row=5,column=4)
#     father_nameN.grid(row=6,column=4)
#     cityN.grid(row=7,column=4)
#     zipcodeN.grid(row=8,column=4)

#     #defining new labels
#     first_nameLN=Label(editor,text="First_name")
#     last_nameLN=Label(editor,text="last_name")
#     addressLN=Label(editor,text="address")
#     ageLN=Label(editor,text="age")
#     passwordLN=Label(editor,text="password")
#     father_nameLN=Label(editor,text="father_name")
#     cityLN=Label(editor,text="city")
#     zip_codeLN=Label(editor,text="zip_code")
#     deleteLN=Label(editor,text="Delete")

#     #placing new labels
#     first_nameLN.grid(row=1,column=0)
#     last_nameLN.grid(row=2,column=0)
#     addressLN.grid(row=3,column=0)
#     ageLN.grid(row=4,column=0)
#     passwordLN.grid(row=5,column=0)
#     father_nameLN.grid(row=6,column=0)
#     cityLN.grid(row=7,column=0)
#     zip_codeLN.grid(row=8,column=0)
#     deleteLN.grid(row=9,column=0)

    
#     for record in records:
#         first_nameN.insert(0,record[0])
#         last_nameN.insert(0,record[1])
#         addressN.insert(0,record[2])
#         ageN.insert(0,record[3])
#         passwordN.insert(0,record[4])
#         father_nameN.insert(0,record[5])
#         cityN.insert(0,record[6])
#         zipcodeN.insert(0,record[7])
    
#     # making update button
#     updateN=Button(editor,text="Update",command=update)
#     updateN.grid(row=9,column=0)

# # function to insert updated records
# def update():
#     conn=sqlite3.connect('facebook.db')
#     c=conn.cursor()
#     record_id=deleteE.get()
    
#     c.execute(""" UPDATE user SET
#         first_name = :first,
#         last_name= :last,
#         address= :address,
#         age= :age,
#         password= :password,
#         father_name = :father,
#         city= :city,
#         zip_code= :zip
#         WHERE oid = :oid""",
#         {'first': first_nameN.get(),
#         'last' :last_nameN.get(),
#         'address':addressN.get(),
#         'age':ageN.get(),
#         'password':passwordN.get(),
#         'father':father_nameN.get(),
#         'city':cityN.get(),
#         'zip':zipcodeN.get(),
#         'oid': record_id
#         }
#     )
#     conn.commit()
#     conn.close()
#     editor.destroy()

# #function to delete everything
# def deleteall():
#     conn=sqlite3.connect("facebook.db")
#     c=conn.cursor()
#     c.execute("DELETE from user")
#     conn.commit()
#     conn.close()

# def delete():
#     conn=sqlite3.connect("facebook.db")
#     c=conn.cursor()
#     c.execute("DELETE from user WHERE oid ="+deleteE.get())
#     conn.commit()
#     conn.close()

# #defining entries
# first_nameE=Entry(root)
# last_nameE=Entry(root)
# addressE=Entry(root)
# ageE=Entry(root)
# passwordE=Entry(root)
# father_nameE=Entry(root)
# cityE=Entry(root)
# zip_codeE=Entry(root)
# deleteE=Entry(root)

# #placing entries
# first_nameE.grid(row=1,column=3,pady=10)
# last_nameE.grid(row=2,column=3,pady=10)
# addressE.grid(row=3,column=3,pady=10)
# ageE.grid(row=4,column=3,pady=10)
# passwordE.grid(row=5,column=3,pady=10)
# father_nameE.grid(row=6,column=3,pady=10)
# cityE.grid(row=7,column=3,pady=10)
# zip_codeE.grid(row=8,column=3,pady=10)
# deleteE.grid(row=1,column=12,pady=10)


# #defining labels
# first_nameL=Label(root,text="First_name")
# last_nameL=Label(root,text="last_name")
# addressL=Label(root,text="address")
# ageL=Label(root,text="age")
# passwordL=Label(root,text="password")
# father_nameL=Label(root,text="father_name")
# cityL=Label(root,text="city")
# zip_codeL=Label(root,text="zip_code")
# deleteL=Label(root,text="Delete")

# #placing labels
# first_nameL.grid(row=1,column=0)
# last_nameL.grid(row=2,column=0)
# addressL.grid(row=3,column=0)
# ageL.grid(row=4,column=0)
# passwordL.grid(row=5,column=0)
# father_nameL.grid(row=6,column=0)
# cityL.grid(row=7,column=0)
# zip_codeL.grid(row=8,column=0)
# deleteL.grid(row=1,column=8)

# #defining button
# add=Button(root,text="Add",command=insert)
# delete=Button(root,text="Delete",command=delete)
# show=Button(root,text="Show Records",command=show_records)
# edit=Button(root,text="Edit",command=edit)
# delete_all=Button(root,text="Delete all",command=deleteall)


# #placing button
# add.grid(row=9,column=0,pady=10)
# delete.grid(row=10,column=0,pady=10)
# show.grid(row=11,column=0,pady=10)
# edit.grid(row=12,column=0,pady=10)
# delete_all.grid(row=13,column=0,pady=10)
# root.mainloop()

from tkinter import*
from tkinter import messagebox

root=Tk()
root.title('login')
root.geometry('1280x800')
root.configure(bg='#fff')
root.resizable(False,False)




img=PhotoImage(file='logen.png')
Label(root,image=img,bg='white').pack()

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading=Label(frame,text='Sign In',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0,END)

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')



user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

def on_enter(e):
    code.delete(0,END)

def on_leave(e):
    name=user.get()
    if name=='':
        code.insert(0,'Password')


code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

def signin():
    username=user.get
    password=code.get

    if username=='admin' and password=='1234':
        # print('Inventory Management Setup')
        screen=Toplevel(root)
        screen.title('APP')
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen,text='Welcome!',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)

        screen.mainloop()

Button(frame,width=39,pady=7,text='Sign In',bg='royal blue',fg='white',command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='royal blue')
sign_up.place(x=215,y=270)


root.mainloop()