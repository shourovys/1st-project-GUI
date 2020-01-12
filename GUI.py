import tkinter as tk
from tkinter import ttk 
win = tk.Tk()
win.title("GUI")
#create label
name_label=ttk.Label(win, text= "Enter your name : ")
name_label.grid(row=0,column=0,sticky= tk.W)
email_label=ttk.Label(win,text='Enter your email : ')
email_label.grid(row=1,column=0,sticky=tk.W)

age_label=ttk.Label(win,text="Enter your age : ")
age_label.grid(row=2,column=0,sticky=tk.W)

gander_lable=ttk.Label(win,text="Enter your gender : ")
gander_lable.grid(row=3,column=0,sticky=tk.W)
#create entry box
name_ver=tk.StringVar()
name_enterbox=ttk.Entry(win,width=16,textvariable=name_ver)
name_enterbox.grid(row=0,column=1)
name_enterbox.focus()

email_ver=tk.StringVar()
email_enterbox=ttk.Entry(win,width=16,textvariable=email_ver)
email_enterbox.grid(row=1,column=1)

age_ver=tk.StringVar()
age_enterbox=ttk.Entry(win,width=16,textvariable=age_ver)
age_enterbox.grid(row=2,column=1)



#create combobox
gander_var=tk.StringVar()
gander_combobox= ttk.Combobox(win,width=13,textvariable=gander_var,state="readonly")
gander_combobox['values'] = ('Male','Female','Other')
gander_combobox.current(0)
gander_combobox.grid(row=3,column=1)

#radio button
user_type=tk.StringVar()
rediobt1 = ttk.Radiobutton(win,text='Student',value='Student',variable=user_type)
rediobt1.grid(row=4,column=1,sticky=tk.W)
rediobt2 = ttk.Radiobutton(win,text="Teachet",value="Teacher",variable=user_type)
rediobt2.grid(row=4,column=0,sticky=tk.W)

#check button
checkbtn_ver=tk.IntVar()
checkbtn=ttk.Checkbutton(win,text='check if you went to sub',variable=checkbtn_ver)
checkbtn.grid(row=5,columnspan=3,sticky=tk.W)

#submit\creat button
def action():
    username = name_ver.get()
    userEmail = email_ver.get()   
    userage = age_ver.get()
    usergander = gander_var.get()
    usertype = user_type.get()
    if checkbtn_ver.get() == 0:
        sub="No"
    else:
        sub="yes"
    print(username,userEmail,userage,usergander,usertype,sub)

    with open('file.txt','a') as f:
        f.write(f'{username},{userEmail},{userage},{usergander},{usertype},{sub}\n')
        name_enterbox.delete(0,tk.END)
        age_enterbox.delete(0,tk.END)
        email_enterbox.delete(0,tk.END)

        name_label.configure(foreground="Blue")

submit_button=ttk.Button(win,text='Submit',command=action)
submit_button.grid(row=6,column=3)


win.mainloop()