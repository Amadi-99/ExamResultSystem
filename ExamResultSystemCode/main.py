import tkinter as tk
from tkinter import *
import databse
import tkinter.messagebox









class MainWindow:

    def Image(self):
        self.Photo =PhotoImage(file="jpg.png")
        return self.Photo

    def __init__(self, master):


        StudentID = StringVar()
        StudentName = StringVar()


        self.master = master
        self.master.title("Exam Result system")

        # Main Text
        self.frameTitleMainText = tk.Frame(self.master)
        self.frameTitleMainText.place(relx=0.7, rely=0.05, relwidth=0.85, relheight=0.25, anchor='n')

        self.labelTitleTextMain = tk.Label(self.frameTitleMainText, text="Exam Result System", font="Times 30 bold")
        self.labelTitleTextMain.place(relwidth=1, relheigh=1)

        self.framePhoto = tk.Frame(self.master)
        self.framePhoto.place(relx=0.25, rely=0.09, relwidth=0.35, relheight=0.35, anchor='n')

        self.labelPhoto = tk.Label(self.framePhoto, image=self.Image())
        self.labelPhoto.place(relwidth=1, relheigh=0.5)

        # Student Id
        self.frameStuID = tk.Frame(self.master, bg='#9494b8', bd=5)
        self.frameStuID.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.1, anchor='n')

        self.labelStuID = tk.Label(self.frameStuID, text="Student ID", font="Times 20 bold")
        self.labelStuID.place(relwidth=0.4, relheight=1)

        self.entryStuID = tk.Entry(self.frameStuID, textvariable=StudentID)
        self.entryStuID.place(relx=0.45, relwidth=0.55, relheight=1)
        # Student Name
        self.frameStuName = tk.Frame(self.master, bg='#9494b8', bd=5)
        self.frameStuName.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.1, anchor='n')

        self.labelStuName = tk.Label(self.frameStuName, text="Student Name", font="Times 20 bold")
        self.labelStuName.place(relwidth=0.4, relheight=1)

        self.entryStuName = tk.Entry(self.frameStuName, textvariable=StudentName)
        self.entryStuName.place(relx=0.45, relwidth=0.55, relheight=1)

        # Buttons (Primary,Ordinary,Advance)
        self.frameButtonMain = tk.Frame(self.master, bg='#9494b8', bd=5)
        self.frameButtonMain.place(relx=0.5, rely=0.65, relwidth=0.75, relheight=0.3, anchor='n')

        self.buttonPrimary = tk.Button(self.frameButtonMain, text="Primary Level", font=40,
                                       command=lambda: self.Login_System_Primary())
        self.buttonPrimary.place(relheight=0.3, relwidth=1)

        self.buttonOrdinary = tk.Button(self.frameButtonMain, text="Ordinary Level", font=40,
                                        command=lambda: self.Login_System_Ordinary())
        self.buttonOrdinary.place(rely=0.35, relheight=0.3, relwidth=1)

        self.buttonAdvanced = tk.Button(self.frameButtonMain, text="Advanced Level", font=40,
                                        command=lambda: self.Login_System_Advance())
        self.buttonAdvanced.place(rely=0.7, relheight=0.3, relwidth=1)




    #check login Details
    def Login_System_Primary(self):
        stu_id = int(self.entryStuID.get())
        if stu_id >= 10000 and stu_id <= 20000:
            self.newWindow = tk.Toplevel(self.master)
            self.newWindow.geometry('800x700')
            self.app = windowPrimary(self.newWindow, self.entryStuID.get(), self.entryStuName.get())
        else:
            tkinter.messagebox.askokcancel("Login_System_Primary", " Invalid Login Details. \n Please enter your correct Student ID Number.")


    def Login_System_Ordinary(self):
        stu_id = int(self.entryStuID.get())
        if stu_id >= 20001 and stu_id <= 50000:
            self.newWindow = tk.Toplevel(self.master)
            self.newWindow.geometry('800x700')
            self.app = windowOdinary(self.newWindow, self.entryStuID.get(), self.entryStuName.get())
        else:
            tkinter.messagebox.askokcancel("Login_System_Primary", " Invalid Login Details. \n Please enter your correct Student ID Number.")


    def Login_System_Advance(self):
        stu_id = int(self.entryStuID.get())
        if stu_id >= 50001 and stu_id <= 100000:
            self.newWindow = tk.Toplevel(self.master)
            self.newWindow.geometry('800x700')
            self.app = windowAdvance(self.newWindow, self.entryStuID.get(), self.entryStuName.get())
        else:
            tkinter.messagebox.askokcancel("Login_System_Primary", " Invalid Login Details. \n Please enter your correct Student ID Number.")






    def loadWindowPrimary(self):

        #StudentID = IntVar()
        #if StudentID in range(1000, 5000):
        print(self.entryStuID.get())
        print(self.entryStuName.get())
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('800x700')
        self.app = windowPrimary(self.newWindow, self.entryStuID.get(), self.entryStuName.get())


    def loadWindowOrdinary(self):
        print(self.entryStuID.get())
        print(self.entryStuName.get())
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('800x700')
        self.app = windowOdinary(self.newWindow,  self.entryStuID.get(), self.entryStuName.get())

    def loadWindowAdvance(self):
        print(self.entryStuID.get())
        print(self.entryStuName.get())
        self.newWindow = tk.Toplevel(self.master)
        self.newWindow.geometry('800x700')
        self.app = windowAdvance(self.newWindow,  self.entryStuID.get(), self.entryStuName.get())


class windowPrimary:

    def CalculateTotal(self):
        sum = int(self.entrySubject1.get()) + int(self.entrySubject2.get()) + int(self.entrySubject3.get()) + \
              int(self.entrySubject4.get()) + int(self.entrySubject5.get()) + int(self.entrySubject6.get())
        return sum

    def CalculateAverage(self):
        average = self.CalculateTotal()/6
        return average


    def analyseData(self):
        print("Total =", self.CalculateTotal())
        print("Average = ", self.CalculateAverage())
        self.textTotal.set(self.CalculateTotal())
        self.textAverage.set(self.CalculateAverage())
        databse.InsertPrimaryData(self.StudentID, self.StudentName, int(self.entrySubject1.get()), \
                                    int(self.entrySubject2.get()), int(self.entrySubject3.get()), \
                                    int(self.entrySubject4.get()), int(self.entrySubject5.get()), \
                                    int(self.entrySubject6.get()), self.CalculateTotal(), self.CalculateAverage())



    def __init__(self, master, StudentID, StudentName):
        self.master = master

        self.textTotal = StringVar()
        self.textAverage = StringVar()

        self.StudentID = StudentID
        self.StudentName = StudentName

        # Primary Title
        self.frameTitleText = tk.Frame(self.master)
        self.frameTitleText.place(relx=0.5, rely=0.01, relwidth=0.65, relheight=0.15, anchor='n')

        self.labelTitleText = tk.Label(self.frameTitleText, text="Primary Level", font="Times 24 bold")

        self.labelTitleText.place(relwidth=1, relheigh=1)

        # subjects
        self.frameSubject1 = tk.Frame(self.master)
        self.frameSubject1.place(relx=0.3, rely=0.20, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject1 = tk.Label(self.frameSubject1, text="Mathematics")
        self.labelSubject1.place(relwidth=0.4, relheight=1)

        self.entrySubject1 = tk.Entry(self.frameSubject1)
        self.entrySubject1.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameSubject2 = tk.Frame(self.master)
        self.frameSubject2.place(relx=0.3, rely=0.30, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject2 = tk.Label(self.frameSubject2, text="Buddhism")
        self.labelSubject2.place(relwidth=0.4, relheight=1)

        self.entrySubject2 = tk.Entry(self.frameSubject2)
        self.entrySubject2.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameSubject3 = tk.Frame(self.master)
        self.frameSubject3.place(relx=0.3, rely=0.40, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject3 = tk.Label(self.frameSubject3, text="Sinhala")
        self.labelSubject3.place(relwidth=0.4, relheight=1)

        self.entrySubject3 = tk.Entry(self.frameSubject3)
        self.entrySubject3.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameSubject4 = tk.Frame(self.master)
        self.frameSubject4.place(relx=0.6, rely=0.20, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject4 = tk.Label(self.frameSubject4, text="Environment")
        self.labelSubject4.place(relwidth=0.4, relheight=1)

        self.entrySubject4 = tk.Entry(self.frameSubject4)
        self.entrySubject4.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameSubject5 = tk.Frame(self.master)
        self.frameSubject5.place(relx=0.6, rely=0.30, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject5 = tk.Label(self.frameSubject5, text="English")
        self.labelSubject5.place(relwidth=0.4, relheight=1)

        self.entrySubject5 = tk.Entry(self.frameSubject5)
        self.entrySubject5.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameSubject6 = tk.Frame(self.master)
        self.frameSubject6.place(relx=0.6, rely=0.40, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject6 = tk.Label(self.frameSubject6, text="Tamil")
        self.labelSubject6.place(relwidth=0.4, relheight=1)

        self.entrySubject6 = tk.Entry(self.frameSubject6)
        self.entrySubject6.place(relx=0.45, relwidth=0.55, relheight=1)

        # Button Analyze
        self.frameButtonAnalyze = tk.Frame(self.master, bg='#9494b8', bd=2)
        self.frameButtonAnalyze.place(relx=0.5, rely=0.70, relwidth=0.25, relheight=0.05, anchor='n')

        self.buttonPrimaryWinAna = tk.Button(self.frameButtonAnalyze, text="Analyze Result ", font=20,
                                             command=lambda: self.analyseData())
        self.buttonPrimaryWinAna.place(relheight=1, relwidth=1)


        # Total and average
        self.frameTotal = tk.Frame(self.master)
        self.frameTotal.place(relx=0.3, rely=0.80, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelTotal = tk.Label(self.frameTotal, text="Total")
        self.labelTotal.place(relwidth=0.4, relheight=1)

        self.labelEntryTotal = tk.Label(self.frameTotal, textvariable=self.textTotal)
        self.labelEntryTotal.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameAverage = tk.Frame(self.master)
        self.frameAverage.place(relx=0.3, rely=0.90, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelAverage = tk.Label(self.frameAverage, text="Average")
        self.labelAverage.place(relwidth=0.4, relheight=1)

        self.labelEntryAverage = tk.Label(self.frameAverage, textvariable=self.textAverage)
        self.labelEntryAverage.place(relx=0.45, relwidth=0.55, relheight=1)


class windowOdinary:

    def CalculateTotal(self):
        sum = int(self.entrySubject1.get()) + int(self.entrySubject2.get()) + int(self.entrySubject3.get()) + \
              int(self.entrySubject4.get()) + int(self.entrySubject5.get()) + int(self.entrySubject6.get()) + \
              int(self.entrySubject7.get()) +int(self.entrySubject8.get()) + int(self.entrySubject9.get())
        return sum

    def CalculateAverage(self):
        average = self.CalculateTotal() / 9
        return average

    def analyseData(self):
        print("Total =", self.CalculateTotal())
        print("Average = ", self.CalculateAverage())
        self.textTotal.set(self.CalculateTotal())
        self.textAverage.set(self.CalculateAverage())
        databse.InsertOrdinaryData(self.StudentID, self.StudentName, int(self.entrySubject1.get()), \
                                    int(self.entrySubject2.get()), int(self.entrySubject3.get()), \
                                    int(self.entrySubject4.get()), int(self.entrySubject5.get()), \
                                    int(self.entrySubject6.get()), int(self.entrySubject7.get()),
                                    int(self.entrySubject8.get()), int(self.entrySubject9.get()),\
                                    self.CalculateTotal(), self.CalculateAverage())



    def __init__(self, master, StudentID, StudentName):
        self.master = master

        self.textTotal = StringVar()
        self.textAverage = StringVar()

        self.StudentID = StudentID
        self.StudentName = StudentName


        # Ordinary Title
        self.frameTitleText = tk.Frame(self.master)
        self.frameTitleText.place(relx=0.5, rely=0.01, relwidth=0.65, relheight=0.15, anchor='n')

        self.labelTitleText = tk.Label(self.frameTitleText, text="Ordinary Level", font="Times 24 bold")
        self.labelTitleText.place(relwidth=1, relheigh=1)

        # subjects
        self.frameSubject1 = tk.Frame(self.master)
        self.frameSubject1.place(relx=0.3, rely=0.20, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject1 = tk.Label(self.frameSubject1, text="Mathematics")
        self.labelSubject1.place(relwidth=0.4, relheight=1)

        self.entrySubject1 = tk.Entry(self.frameSubject1)
        self.entrySubject1.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameSubject2 = tk.Frame(self.master)
        self.frameSubject2.place(relx=0.3, rely=0.30, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject2 = tk.Label(self.frameSubject2, text="Buddhism")
        self.labelSubject2.place(relwidth=0.4, relheight=1)

        self.entrySubject2 = tk.Entry(self.frameSubject2)
        self.entrySubject2.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameSubject3 = tk.Frame(self.master)
        self.frameSubject3.place(relx=0.3, rely=0.40, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject3 = tk.Label(self.frameSubject3, text="Sinhala")
        self.labelSubject3.place(relwidth=0.4, relheight=1)

        self.entrySubject3 = tk.Entry(self.frameSubject3)
        self.entrySubject3.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameSubject4 = tk.Frame(self.master)
        self.frameSubject4.place(relx=0.3, rely=0.50, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject4 = tk.Label(self.frameSubject4, text="Science")
        self.labelSubject4.place(relwidth=0.4, relheight=1)

        self.entrySubject4 = tk.Entry(self.frameSubject4)
        self.entrySubject4.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameSubject5 = tk.Frame(self.master)
        self.frameSubject5.place(relx=0.3, rely=0.60, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject5 = tk.Label(self.frameSubject5, text="History")
        self.labelSubject5.place(relwidth=0.4, relheight=1)

        self.entrySubject5 = tk.Entry(self.frameSubject5)
        self.entrySubject5.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameSubject6 = tk.Frame(self.master)
        self.frameSubject6.place(relx=0.6, rely=0.20, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject6 = tk.Label(self.frameSubject6, text="English")
        self.labelSubject6.place(relwidth=0.4, relheight=1)

        self.entrySubject6 = tk.Entry(self.frameSubject6)
        self.entrySubject6.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameSubject7 = tk.Frame(self.master)
        self.frameSubject7.place(relx=0.6, rely=0.30, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject7 = tk.Label(self.frameSubject7, text="Bucket 01")
        self.labelSubject7.place(relwidth=0.4, relheight=1)

        self.entrySubject7 = tk.Entry(self.frameSubject7)
        self.entrySubject7.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameSubject8 = tk.Frame(self.master)
        self.frameSubject8.place(relx=0.6, rely=0.40, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject8 = tk.Label(self.frameSubject8, text="Bucket 02")
        self.labelSubject8.place(relwidth=0.4, relheight=1)

        self.entrySubject8 = tk.Entry(self.frameSubject8)
        self.entrySubject8.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameSubject9 = tk.Frame(self.master)
        self.frameSubject9.place(relx=0.6, rely=0.50, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject9 = tk.Label(self.frameSubject9, text="Bucket 03")
        self.labelSubject9.place(relwidth=0.4, relheight=1)

        self.entrySubject9 = tk.Entry(self.frameSubject9)
        self.entrySubject9.place(relx=0.45, relwidth=0.55, relheight=1)

        # Button Analyze
        self.frameButtonAnalyze = tk.Frame(self.master, bg='#9494b8', bd=2)
        self.frameButtonAnalyze.place(relx=0.5, rely=0.70, relwidth=0.25, relheight=0.05, anchor='n')

        self.buttonPrimaryWin = tk.Button(self.frameButtonAnalyze, text="Analyze Result ", font=20,
                                          command=lambda: self.analyseData())
        self.buttonPrimaryWin.place(relheight=1, relwidth=1)

        # Total and average
        self.frameTotal = tk.Frame(self.master)
        self.frameTotal.place(relx=0.3, rely=0.80, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelTotal = tk.Label(self.frameTotal, text="Total")
        self.labelTotal.place(relwidth=0.4, relheight=1)

        self.labelEntryTotal = tk.Label(self.frameTotal,textvariable=self.textTotal)
        self.labelEntryTotal.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameAverage = tk.Frame(self.master)
        self.frameAverage.place(relx=0.3, rely=0.90, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelAverage = tk.Label(self.frameAverage, text="Average")
        self.labelAverage.place(relwidth=0.4, relheight=1)

        self.labelEntryAverage = tk.Label(self.frameAverage,textvariable=self.textAverage)
        self.labelEntryAverage.place(relx=0.45, relwidth=0.55, relheight=1)


class windowAdvance:

    def CalculateTotal(self):
        sum = int(self.entrySubject1.get()) + int(self.entrySubject2.get()) + int(self.entrySubject3.get())
        return sum

    def CalculateAverage(self):
        average = self.CalculateTotal() / 3
        return average

    def analyseData(self):
        print("Total =", self.CalculateTotal())
        print("Average = ", self.CalculateAverage())
        self.textTotal.set(self.CalculateTotal())
        self.textAverage.set(self.CalculateAverage())
        databse.InsertAdvancedData(self.StudentID, self.StudentName, self.entrySubStream.get(), \
                                   int(self.entrySubject1.get()), int(self.entrySubject2.get()), \
                                   int(self.entrySubject3.get()), self.CalculateTotal(), self.CalculateAverage())


    def __init__(self, master, StudentID, StudentName):
        self.master = master

        self.textTotal = StringVar()
        self.textAverage = StringVar()

        self.StudentID = StudentID
        self.StudentName = StudentName

        # Advance Title
        self.frameTitleText = tk.Frame(self.master)
        self.frameTitleText.place(relx=0.5, rely=0.01, relwidth=0.65, relheight=0.15, anchor='n')

        self.labelTitleText = tk.Label(self.frameTitleText, text="Advance Level", font="Times 24 bold")
        self.labelTitleText.place(relwidth=1, relheigh=1)

        self.frameSubStream = tk.Frame(self.master)
        self.frameSubStream.place(relx=0.4, rely=0.20, relwidth=0.55, relheight=0.05, anchor='n')

        self.labelSubStream = tk.Label(self.frameSubStream, text="Subject Stream")
        self.labelSubStream.place(relwidth=0.3, relheight=1)

        self.entrySubStream = tk.Entry(self.frameSubStream, textvariable=StudentName)
        self.entrySubStream.place(relx=0.30, relwidth=0.55, relheight=1)

        # subjects
        self.frameSubject1 = tk.Frame(self.master)
        self.frameSubject1.place(relx=0.3, rely=0.30, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject1 = tk.Label(self.frameSubject1, text="Subject 01")
        self.labelSubject1.place(relwidth=0.4, relheight=1)

        self.entrySubject1 = tk.Entry(self.frameSubject1)
        self.entrySubject1.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameSubject2 = tk.Frame(self.master)
        self.frameSubject2.place(relx=0.3, rely=0.40, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject2 = tk.Label(self.frameSubject2, text="Subject 02")
        self.labelSubject2.place(relwidth=0.4, relheight=1)

        self.entrySubject2 = tk.Entry(self.frameSubject2)
        self.entrySubject2.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameSubject3 = tk.Frame(self.master)
        self.frameSubject3.place(relx=0.3, rely=0.50, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelSubject3 = tk.Label(self.frameSubject3, text="Subject 03")
        self.labelSubject3.place(relwidth=0.4, relheight=1)

        self.entrySubject3 = tk.Entry(self.frameSubject3)
        self.entrySubject3.place(relx=0.45, relwidth=0.55, relheight=1)

        # Button Analyze

        self.frameButtonAnalyze = tk.Frame(self.master, bg='#9494b8', bd=2)
        self.frameButtonAnalyze.place(relx=0.5, rely=0.70, relwidth=0.25, relheight=0.05, anchor='n')

        self.buttonPrimaryWin = tk.Button(self.frameButtonAnalyze, text="Analyze Result ", font=20,
                                          command=lambda: self.analyseData())
        self.buttonPrimaryWin.place(relheight=1, relwidth=1)

        # Total and Average
        self.frameTotal = tk.Frame(self.master)
        self.frameTotal.place(relx=0.3, rely=0.80, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelTotal = tk.Label(self.frameTotal, text="Total")
        self.labelTotal.place(relwidth=0.4, relheight=1)

        self.labelEntryTotal = tk.Label(self.frameTotal, textvariable=self.textTotal)
        self.labelEntryTotal.place(relx=0.45, relwidth=0.55, relheight=1)

        self.frameAverage = tk.Frame(self.master)
        self.frameAverage.place(relx=0.3, rely=0.90, relwidth=0.25, relheight=0.05, anchor='n')

        self.labelAverage = tk.Label(self.frameAverage, text="Average")
        self.labelAverage.place(relwidth=0.4, relheight=1)

        self.labelEntryAverage = tk.Label(self.frameAverage, textvariable=self.textAverage)
        self.labelEntryAverage.place(relx=0.45, relwidth=0.55, relheight=1)


root = tk.Tk()

root.geometry('700x700')
app = MainWindow(root)
root.mainloop()


