#Frontend

from tkinter import*
import tkinter.messagebox
import stdDatabase

class Student:

    def __init__(self, root):
        self.root =root
        self.root.title("Student Database Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")

        StdID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Dob = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        #========================================frames=================================
        Mainframe = Frame(self.root, bg="cadet blue")
        Mainframe.grid()

        Titframe = Frame(Mainframe, bd=2, padx=54, pady=8,bg="Ghost White", relief = RIDGE)
        Titframe.pack(side=TOP)

        self.lblTit = Label(Titframe, font=('arial', 47, 'bold'),text="Student Database Management Systems",bg="Ghost White")
        self.lblTit.grid()

        Buttonframe = Frame(Mainframe, bd=2, width=1350, height=70, padx=18,pady=10, bg="Ghost White", relief = RIDGE)
        Buttonframe.pack(side=BOTTOM)

        Dataframe = Frame(Mainframe, bd=1, width=1300, height=400, padx=20,pady=20, bg="cadet blue", relief = RIDGE)
        Dataframe.pack(side=BOTTOM)

        DataframeLEFT = LabelFrame(Dataframe, bd=1, width=1000, height=600, padx=20, bg="Ghost White", relief = RIDGE,
                              font=('arial', 20, 'bold'), text="Student Info\n")
        DataframeLEFT.pack(side=LEFT)

        DataframeRIGHT = LabelFrame(Dataframe, bd=1, width=450, height=300, padx=31,pady=3, bg="Ghost White", relief = RIDGE,
                                    font=('arial', 20, 'bold'), text="Student Details\n")
        DataframeRIGHT.pack(side=RIGHT)

         #========================================Label and Entry Widget=================================

        self.lblStdID = Label(DataframeLEFT, font=('arial', 20, 'bold'),text="Student ID:", padx=2,pady=2,bg="Ghost White")
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(DataframeLEFT, font=('arial', 20, 'bold'),textvariable=StdID, width=39)
        self.txtStdID.grid(row=0, column=1)

        self.lblfna = Label(DataframeLEFT, font=('arial', 20, 'bold'),text="Firstname:", padx=2,pady=2,bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataframeLEFT, font=('arial', 20, 'bold'),textvariable=StdID, width=39)
        self.txtfna.grid(row=1, column=1)

        self.lblSna = Label(DataframeLEFT, font=('arial', 20, 'bold'),text="Surname:", padx=2,pady=2,bg="Ghost White")
        self.lblSna.grid(row=2, column=0, sticky=W)
        self.txtSna = Entry(DataframeLEFT, font=('arial', 20, 'bold'),textvariable=StdID, width=39)
        self.txtSna.grid(row=2, column=1)

        self.lblStdID = Label(DataframeLEFT, font=('arial', 20, 'bold'),text="Date of Birth:", padx=2,pady=3,bg="Ghost White")
        self.lblStdID.grid(row=3, column=0, sticky=W)
        self.txtStdID = Entry(DataframeLEFT, font=('arial', 20, 'bold'),textvariable=StdID, width=39)
        self.txtStdID.grid(row=3, column=1)

        self.lblfna = Label(DataframeLEFT, font=('arial', 20, 'bold'),text="Age:", padx=2,pady=3,bg="Ghost White")
        self.lblfna.grid(row=4, column=0, sticky=W)
        self.txtfna = Entry(DataframeLEFT, font=('arial', 20, 'bold'),textvariable=StdID, width=39)
        self.txtfna.grid(row=4, column=1)

        self.lblSna = Label(DataframeLEFT, font=('arial', 20, 'bold'),text="Gender:", padx=2,pady=3,bg="Ghost White")
        self.lblSna.grid(row=5, column=0, sticky=W)
        self.txtSna = Entry(DataframeLEFT, font=('arial', 20, 'bold'),textvariable=StdID, width=39)
        self.txtSna.grid(row=5, column=1)

        self.lblfna = Label(DataframeLEFT, font=('arial', 20, 'bold'),text="Address", padx=2,pady=3,bg="Ghost White")
        self.lblfna.grid(row=6, column=0, sticky=W)
        self.txtfna = Entry(DataframeLEFT, font=('arial', 20, 'bold'),textvariable=StdID, width=39)
        self.txtfna.grid(row=6, column=1)

        self.lblSna = Label(DataframeLEFT, font=('arial', 20, 'bold'),text="Mobile", padx=2,pady=3,bg="Ghost White")
        self.lblSna.grid(row=7, column=0, sticky=W)
        self.txtSna = Entry(DataframeLEFT, font=('arial', 20, 'bold'),textvariable=StdID, width=39)
        self.txtSna.grid(row=7, column=1)

        #========================================Listbox & Scrollbar Widget=================================

        scrollbar = Scrollbar (DataframeRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        Studentlist = Listbox (DataframeRIGHT, width=41, height=16, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        Studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command = Studentlist.yview)

        #========================================Button Widget=============================================
        self.btnAddDate = Button(Buttonframe, text="Add new",font=('arial', 20, 'bold'),height= 1,width=10, bd=4)
        self.btnAddDate.grid(row=0,column=0)
        self.btnAddDate = Button(Buttonframe, text='Display',font=('arial', 20, 'bold'),height= 1,width=10, bd=4)
        self.btnAddDate.grid(row=0,column=1)
        self.btnAddDate = Button(Buttonframe, text='Clear',font=('arial', 20, 'bold'),height= 1,width=10, bd=4)
        self.btnAddDate.grid(row=0,column=2)
        self.btnAddDate = Button(Buttonframe, text='Delete',font=('arial', 20, 'bold'),height= 1,width=10, bd=4)
        self.btnAddDate.grid(row=0,column=3)
        self.btnAddDate = Button(Buttonframe, text='Search',font=('arial', 20, 'bold'),height= 1,width=10, bd=4)
        self.btnAddDate.grid(row=0,column=4)
        self.btnAddDate = Button(Buttonframe, text='Update',font=('arial', 20, 'bold'),height= 1,width=10, bd=4)
        self.btnAddDate.grid(row=0,column=5)
        self.btnAddDate = Button(Buttonframe, text='Exit',font=('arial', 20, 'bold'),height= 1,width=10, bd=4)
        self.btnAddDate.grid(row=0,column=6)

if __name__ == '__main__':
    root=Tk()
    application = Student(root)
    root.mainloop()