from tkinter import *
from tkinter import messagebox
from db import database
# db2 = database(r'C:\Users\Pc44\Desktop\exam.py\course.db')

win = Tk()
win.geometry('700x500')
win.config(bg='#C9A3E8')
#func======
def clear():
    ent_password.delete(0,END)
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_course.delete(0,END)
def exit():
    result = messagebox.showerror('exit','r u sure to exit?')
    if result == 'ok':
        win.destroy()
def insert():
    fname = ent_fname.get()
    lname = ent_lname.get()
    course = ent_course.get()
    password = ent_password.get()
    db2.insert(fname,lname,course,password)
    messagebox.showinfo('insert','record inserted')
def show():
    lst_show.delete(0,END)
    users = db2.select_record()
    for user in users:
        lst_show.insert(END,user)
def delete():
    index = lst_show.curselection()
    records = lst_show.get(index)
    re = messagebox.askquestion('exit','r u sure?')
    if re == 'yes':
        db2.delete(records[0])
    show()
def open_wellcome():
    new_win = Toplevel(win)
    new_win.title('wellcome')
    new_win.geometry('300x300')
    lable1 = Label(new_win , text='wellcome back')
    lable1.pack(pady=30)
def sign_in():
    password=ent_password2.get()
    users = db2.find(password)
    if users:
        open_wellcome()
    else:
        messagebox.showerror('error','usere not find or wrong password')
#widget========
lbl_fname = Label(win,text='Fname:',background="#C9A3E8",font='romantic 17')
lbl_fname.place(x=10,y=10)
ent_fname =Entry(win,width=20)
ent_fname.place(x=100,y=14)
lbl_sn = Label(win,text='*',bg='#C9A3E8',fg='red',font=17)
lbl_sn.place(x=90,y=10)

lbl_lname = Label(win,text='Lname:',background="#C9A3E8",font='romantic 17')
lbl_lname.place(x=10,y=60)
ent_lname =Entry(win,width=20)
ent_lname.place(x=100,y=64)
lbl_sl = Label(win,text='*',bg='#C9A3E8',fg='red',font=17)
lbl_sl.place(x=90,y=64)

lbl_course = Label(win,text='course name:',background="#C9A3E8",font='romantic 17')
lbl_course.place(x=230,y=10)
ent_course =Entry(win,width=20)
ent_course.place(x=390,y=14)

lbl_password = Label(win,text='password:',background="#C9A3E8",font='romantic 17')
lbl_password.place(x=230,y=60)
ent_password =Entry(win,width=20,show='*')
ent_password.place(x=390,y=64)
lbl_sp = Label(win,text='*',bg='#C9A3E8',fg='red',font=17)
lbl_sp.place(x=380,y=64)

btn_show = Button(win,text='show',width=20,command=show)
btn_show.place(x=500,y=95)

lst_show = Listbox(win, width=60)
lst_show.place(x=100, y=130)

btn_add = Button(win, text='Insert',width=20,command=insert)
btn_add.place(x=500, y=130)

btn_delete = Button(win, text='Delete',width=20,command=delete)
btn_delete.place(x=500, y=200)

btn_clear = Button(win, text='Clear',width=20,command=clear)
btn_clear.place(x=500, y=165)

btn_exit = Button(win, text='Exit',width=20,command=exit)
btn_exit.place(x=500, y=235)

btn_login = Button(win,text='login',width=20,command=sign_in)
btn_login.place(x=500,y=265)
lbl_password2 = Label(win,text='password:',background="#C9A3E8",font='romantic 17')
lbl_password2.place(x=50,y=340)
ent_password2 =Entry(win,width=70)
ent_password2.place(x=180,y=345)
win.mainloop()