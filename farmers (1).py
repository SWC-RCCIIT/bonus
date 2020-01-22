from tkinter import *
from farmersbackend import *
from tkinter import messagebox

class farmerGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Web Portal")
        self.root.maxsize(600,600)
        self.root['bg']='Light Green'
        self.farmersbackend = farmers()

        lblWelcome = Label(self.root,width=30,height=3, font=('Arial',15),bg='Green',
                                  text="WELCOME TO KISAN-E-KIRAN").grid(row=0,column=0)

        lblWelcome = Label(self.root, width=30, height=3, font=('Arial', 15), bg='Orange',
                           text="For Farmer").grid(row=1, column=0)

        btnLogin1 = Button(self.root,bg='SkyBlue', width=10, height=2, text="SIGN IN",
                               command=lambda: self.loginWindowfarmer()).grid(row=2, column=0)

        btnRegister1 = Button(self.root,bg='SkyBlue', width=10, height=2, text="REGISTER",
                             command=lambda: self.registerWindowfarmer()).grid(row=3, column=0)

        lblWelcome = Label(self.root, width=30, height=3, font=('Arial', 15), bg='Orange',
                           text="For Consumer").grid(row=4, column=0)

        btnLogin2 = Button(self.root, bg='SkyBlue', width=10, height=2, text="SIGN IN",
                          command=lambda: self.loginWindowconsumer()).grid(row=5, column=0)

        btnRegister2 = Button(self.root, bg='SkyBlue', width=10, height=2, text="REGISTER",
                             command=lambda: self.registerWindowconsumer()).grid(row=6, column=0)

        lblWelcome = Label(self.root, width=30, height=3, font=('Arial', 15), bg='Orange',
                           text="contact us:xxxxxxxxxx").grid(row=7, column=0)

        btnExit = Button(self.root,bg='SkyBlue', width=10, height=2, text="EXIT",
                          command=lambda: self.root.destroy()).grid(row=8, column=0)

        self.root.mainloop()

    def loginWindowfarmer(self):
        if self.farmersbackend.currentUserId !=0:
            self.showfarmerMenu()
        else:
            child = Toplevel(self.root)
            child.title("Login Screen")
            child.maxsize(500,500)
        lblLogin = Label(child,text="contact details:",width=10,height=2,
                         font=('Arial',15)).grid(row=0,column=0)
        entcontactdetails = Entry(child,width=30,font=('Arial',14))
        entcontactdetails.grid(row=0,column=1)

        lblpassword = Label(child, text="Password::", width=10, height=2,
                         font=('Arial', 15)).grid(row=1, column=0)
        entpassword = Entry(child, width=30, font=('Arial', 14))
        entpassword.grid(row=1, column=1)

        btnLogin = Button(child,text="Sign In",width=10,height=2,bg='Yellow',
                          font=('Arial',15),command=lambda :self.validatefarmer(child,entcontactdetails.get(),entpassword.get()))
        btnLogin.grid(row=2,column=1)

    def loginWindowconsumer(self):
        if self.farmersbackend.currentUserId !=0:
            self.showconsumerMenu()
        else:
            child = Toplevel(self.root)
            child.title("Login Screen")
            child.maxsize(500,500)
        lblLogin = Label(child,text="contact details:",width=10,height=2,
                         font=('Arial',15)).grid(row=0,column=0)
        entcontactdetails = Entry(child,width=30,font=('Arial',14))
        entcontactdetails.grid(row=0,column=1)

        lblpassword = Label(child, text="Password::", width=10, height=2,
                         font=('Arial', 15)).grid(row=1, column=0)
        entpassword = Entry(child, width=30, font=('Arial', 14))
        entpassword.grid(row=1, column=1)

        btnLogin = Button(child,text="Sign In",width=10,height=2,bg='Yellow',
                          font=('Arial',15),command=lambda :self.validateconsumer(child,entcontactdetails.get(),entpassword.get()))
        btnLogin.grid(row=2,column=1)

    def validatefarmer(self,child,contactdetails,password):
        result = self.farmersbackend.farmerLogin(contactdetails,password)

        if result:
            self.showfarmerMenu()
            child.destroy()

        else:
            messagebox.showinfo('error','invalide error')



    def validateconsumer(self,child,contactdetails,password):
        result = self.farmersbackend.consumerLogin(contactdetails,password)

        if result:
            self.showconsumerMenu()
            child.destroy()

        else:
            messagebox.showinfo('error','invalide error')

    def registerWindowfarmer(self):
        child = Toplevel(self.root)
        child.title("Register Screen")
        child.maxsize(600,600)

        self.Name = Label(child, text="Name", width=10, height=2).grid(row=0, column=0)
        entName = Entry(child, width=50)
        entName.grid(row=0, column=1)

        self.products = Label(child, text="products", width=10, height=2).grid(row=1, column=0)
        entproducts = Entry(child,width=50)
        entproducts.grid(row=1, column=1)

        self.rate = Label(child, text="rate", width=10, height=2).grid(row=2, column=0)
        entrate = Entry(child, width=50)
        entrate.grid(row=2, column=1)

        self.addressandcity = Label(child, text="address and city", width=20, height=2).grid(row=3, column=0)
        entaddressandcity = Entry(child, width=50)
        entaddressandcity.grid(row=3, column=1)

        self.contactdetails = Label(child, text="contact details", width=10, height=2).grid(row=4, column=0)
        entcontactdetails = Entry(child, width=50)
        entcontactdetails.grid(row=4, column=1)

        self.password = Label(child, text="password", width=10, height=2).grid(row=5, column=0)
        entpassword= Entry(child, width=50, show='*')
        entpassword.grid(row=5, column=1)

        btnRegister = Button(child, text="Register", width=7, height=2,
                             command=lambda :self.addUserf(child,entName.get(),entproducts.get(),entrate.get(),entaddressandcity.get(),entcontactdetails.get(),entpassword.get())
                             ).grid(row=6,column=1)

    def addUserf(self,child,Name,products,rate,addressandcity,contactdetails,password):
        self.farmersbackend.farmerRegister(Name,products,rate,addressandcity,contactdetails,password)
        messagebox.showinfo('Success','Registeration Successful')
        child.destroy()


    def registerWindowconsumer(self):
        child = Toplevel(self.root)
        child.title("Register Screen")
        child.maxsize(600,600)

        self.Name = Label(child, text="Name", width=10, height=2).grid(row=0, column=0)
        entName = Entry(child, width=50)
        entName.grid(row=0, column=1)

        self.address = Label(child, text="address", width=10, height=2).grid(row=1, column=0)
        entaddress = Entry(child,width=50)
        entaddress.grid(row=1, column=1)

        self.contactdetails = Label(child, text="contact details", width=10, height=2).grid(row=2, column=0)
        entcontactdetails = Entry(child, width=50)
        entcontactdetails.grid(row=2, column=1)

        self.password = Label(child, text="password", width=10, height=2).grid(row=3, column=0)
        entpassword = Entry(child, width=50)
        entpassword.grid(row=3, column=1)

        btnRegister = Button(child, text="Register", width=7, height=2,
                             command=lambda :self.addUserc(child,entName.get(),entaddress.get(),entcontactdetails.get(),entpassword.get())
                             ).grid(row=6,column=1)

    def addUserc(self,child,Name,address,contactdetails,password):
        self.farmersbackend.consumerRegister(Name,address,contactdetails,password)
        messagebox.showinfo('Success','Registeration Successful')
        child.destroy()



    def showfarmerMenu(self):
        child = Toplevel(self.root)
        child.title("farmer Menu")
        child.maxsize(600, 600)

        uname = self.farmersbackend.fetchUserNamef()

        lblWelcome = Label(child,text="Welcome %s"%(uname[0][0]),width=30,height=3,font=("courier",16),bg='Red').grid(row=0,column=0)
        btnAll=Button(child,text="View all orders",width=20,height=2,bg='Pink',font=("Courier",15),
                      command=lambda :self.vieworder()).grid(row=1,column=0,pady=10)
        btnExit = Button(child, text="exit", width=20, height=2, bg='Pink', font=("Courier", 15),
                         command=lambda :self.logout(child)).grid(row=5,column=0,pady=10)

    def showconsumerMenu(self):
        child = Toplevel(self.root)
        child.title("consumer Menu")
        child.maxsize(600, 600)

        uname = self.farmersbackend.fetchUserNamec()

        lblWelcome = Label(child,text="Welcome %s"%(uname[0][0]),width=30,height=3,font=("courier",16),bg='Red').grid(row=0,column=0)

        btnAll=Button(child,text="View all farmers",width=20,height=2,bg='Pink',font=("Courier",15),
                      command=lambda :self.showfarmer()).grid(row=1,column=0,pady=10)

        btnsent = Button(child, text="View sent orders", width=20, height=2, bg='Pink', font=("Courier", 15),
                        command=lambda: self.viewSent()).grid(row=2, column=0, pady=10)

        btnExit = Button(child, text="exit", width=20, height=2, bg='Pink', font=("Courier", 15),
                         command=lambda :self.logout(child)).grid(row=3,column=0,pady=10)


    def showfarmer(self):
        child = Toplevel(self.root)
        child.title("farmer List")
        child.maxsize(2000, 2000)
        child['bg']='Light Green'
        userList = self.farmersbackend.viewAllfarmers()
        i=1
        lWelcome=Label(child,text="Farmers List",width=100,height=3,bg='Green',
                       font=('Courier',16,'bold')).grid(row=0,column=0,columnspan=4)
        k=0
        for user in userList:

            lName=Label(child,text=user[1],width=15,height=2,font=('Arial',10)
                        ).grid(row=i,column=0)
            lproduct = Label(child, text=user[2], width=30, height=2, font=('Arial', 10)
                          ).grid(row=i, column=1)

            lrate = Label(child, text=user[3], width=10, height=2, font=('Arial', 10)
                             ).grid(row=i, column=2)

            laddressandcity = Label(child, text=user[4], width=55, height=2, font=('Arial', 10)
                             ).grid(row=i, column=3)

            lcontactdetails = Label(child, text=user[5], width=10, height=2, font=('Arial', 10)
                             ).grid(row=i, column=4)

            btnorder = Button(child, text="click to proceed", width=12, height=2,
                                       font=('Arial', 10), bg='Red',
                                       command=lambda k=i: self.sendorder(userList[k - 1][0])).grid(row=i, column=5)
            i = i + 1


    def sendorder(self,Userid):
        self.farmersbackend.order(Userid)
        messagebox.showinfo('Sent','order sent. wait for approval!')

    def viewSent(self):
        child = Toplevel(self.root)
        child.title("farmers List sent orders")
        child.maxsize(1500, 1500)
        child['bg'] = 'Light Green'
        userList = self.farmersbackend.viewSentorders()
        i = 1
        lWelcome = Label(child, text="view orders sent", width=100, height=3, bg='Red',
                         font=('Courier', 16, 'bold')).grid(row=0, column=0, columnspan=6)
        for user in userList:
            lName = Label(child, text=user[4], width=20, height=2, font=('Arial', 10)
                          ).grid(row=i, column=1)
            lproducts = Label(child, text=user[5], width=20, height=2, font=('Arial', 10)
                              ).grid(row=i, column=2)
            lrate = Label(child, text=user[6], width=10, height=2, font=('Arial', 10)
                          ).grid(row=i, column=3)
            laddressandcity = Label(child, text=user[7], width=50, height=2, font=('Arial', 10)
                                    ).grid(row=i, column=4)
            lcontactdetails = Label(child, text=user[8], width=10, height=2, font=('Arial', 10)
                                    ).grid(row=i, column=5)
            i = i + 1

    def vieworder(self):
        child = Toplevel(self.root)
        child.title("orders received")
        child.maxsize(2000, 2000)
        child['bg'] = 'Light Green'
        userList = self.farmersbackend.viewReceivedorders()
        i = 1
        lWelcome = Label(child, text="order List", width=100, height=3, bg='Orange',
                         font=('Courier', 16, 'bold')).grid(row=0, column=0, columnspan=4)
        for user in userList:
            lName = Label(child, text=user[4], width=20, height=2, font=('Arial', 10)
                          ).grid(row=i, column=1)

            laddressandcity = Label(child, text=user[5], width=100, height=2, font=('Arial', 10)
                          ).grid(row=i, column=2)
            lcontactdetails = Label(child, text=user[6], width=10, height=2, font=('Arial', 10)
                                    ).grid(row=i, column=3)
            i = i + 1


    def logout(self,child):
        messagebox.showinfo('thanks','thanks for visiting!')
        child.destroy()


obj = farmerGUI()
