import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk as ttk
import sqlite3
 
class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)
  
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings
  
        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)
  
        for row in rows:
            table.insert('', tk.END, values=tuple(row))
  
        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)
         

class App:
    def __init__(self, root):
        #setting title
        root.title("Client")
        #setting window size
        width=600
        height=345
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_996=tk.Button(root)
        GButton_996["bg"] = "#39d50a"
        ft = tkFont.Font(family='Times',size=30)
        GButton_996["font"] = ft
        GButton_996["fg"] = "#000000"
        GButton_996["justify"] = "center"
        GButton_996["text"] = "Запуск приложения"
        GButton_996.place(x=40,y=60,width=520,height=75)
        GButton_996["command"] = self.GButton_996_command

        GButton_920=tk.Button(root)
        GButton_920["bg"] = "#400707"
        ft = tkFont.Font(family='Times',size=25)
        GButton_920["font"] = ft
        GButton_920["fg"] = "#ffffff"
        GButton_920["justify"] = "center"
        GButton_920["text"] = "Выбор данных для отображения"
        GButton_920.place(x=40,y=150,width=520,height=75)
        GButton_920["command"] = self.GButton_920_command

        GButton_20=tk.Button(root)
        GButton_20["bg"] = "#400707"
        ft = tkFont.Font(family='Times',size=25)
        GButton_20["font"] = ft
        GButton_20["fg"] = "#ffffff"
        GButton_20["justify"] = "center"
        GButton_20["text"] = "Натройки приложения"
        GButton_20.place(x=40,y=240,width=520,height=75)
        GButton_20["command"] = self.GButton_20_command

        GLabel_562=tk.Label(root)
        ft = tkFont.Font(family='ansi',size=30)
        GLabel_562["font"] = ft
        GLabel_562["fg"] = "#333333"
        GLabel_562["justify"] = "center"
        GLabel_562["text"] = "Главное меню"
        GLabel_562.place(x=40,y=18,width=520,height=30)
        


                 
        def hotR(self):
            Ravt = tk.Tk()
            #setting title
            Ravt.title("Авторизация")
            #setting window size
            width=300
            height=250
            screenwidth = Ravt.winfo_screenwidth()
            screenheight = Ravt.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            Ravt.geometry(alignstr)
            Ravt.resizable(width=False, height=False)

            GLabel_853=tk.Label(Ravt)
            ft = tkFont.Font(family='Times',size=24)
            GLabel_853["font"] = ft
            GLabel_853["fg"] = "#333333"
            GLabel_853["justify"] = "center"
            GLabel_853["text"] = "Авторизация"
            GLabel_853.place(x=30,y=20,width=250,height=40)

            GLabel_204=tk.Label(Ravt)
            ft = tkFont.Font(family='Times',size=16)
            GLabel_204["font"] = ft
            GLabel_204["fg"] = "#333333"
            GLabel_204["justify"] = "center"
            GLabel_204["text"] = "Логин"
            GLabel_204.place(x=0,y=50,width=77,height=32)

            GLabel_752=tk.Label(Ravt)
            ft = tkFont.Font(family='Times',size=16)
            GLabel_752["font"] = ft
            GLabel_752["fg"] = "#333333"
            GLabel_752["justify"] = "center"
            GLabel_752["text"] = "Пароль"
            GLabel_752.place(x=10,y=110,width=73,height=30)

            GLineEdit_603=tk.Entry(Ravt)
            GLineEdit_603["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times',size=10)
            GLineEdit_603["font"] = ft
            GLineEdit_603["fg"] = "#333333"
            GLineEdit_603["justify"] = "center"
            GLineEdit_603["text"] = "Entry"
            GLineEdit_603.place(x=10,y=80,width=264,height=30)

            GLineEdit_711=tk.Entry(Ravt)
            GLineEdit_711["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times',size=10)
            GLineEdit_711["font"] = ft
            GLineEdit_711["fg"] = "#333333"
            GLineEdit_711["justify"] = "center"
            GLineEdit_711["text"] = "Entry"
            GLineEdit_711.place(x=10,y=150,width=268,height=30)


            GButton_874=tk.Button(Ravt)
            GButton_874["bg"] = "#d4d0c8"
            ft = tkFont.Font(family='Times',size=10)
            GButton_874["font"] = ft
            GButton_874["fg"] = "#000000"
            GButton_874["justify"] = "center"
            GButton_874["text"] = "Войти"
            GButton_874.place(x=10,y=200,width=266,height=30)
            GButton_874["command"] = self.GButton_874_command
            
        def GButton_874_command(self):
            avt = tk.Tk()
            #setting title
            avt.title("Авторизация")
            #setting window size
            width=300
            height=250
            screenwidth = avt.winfo_screenwidth()
            screenheight = avt.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            avt.geometry(alignstr)
            avt.resizable(width=False, height=False)

            GLabel_853=tk.Label(avt)
            ft = tkFont.Font(family='Times',size=24)
            GLabel_853["font"] = ft
            GLabel_853["fg"] = "#333333"
            GLabel_853["justify"] = "center"
            GLabel_853["text"] = "Авторизация"
            GLabel_853.place(x=30,y=20,width=250,height=40)

            GLabel_204=tk.Label(avt)
            ft = tkFont.Font(family='Times',size=16)
            GLabel_204["font"] = ft
            GLabel_204["fg"] = "#333333"
            GLabel_204["justify"] = "center"
            GLabel_204["text"] = "Логин"
            GLabel_204.place(x=0,y=50,width=77,height=32)

            GLabel_752=tk.Label(avt)
            ft = tkFont.Font(family='Times',size=16)
            GLabel_752["font"] = ft
            GLabel_752["fg"] = "#333333"
            GLabel_752["justify"] = "center"
            GLabel_752["text"] = "Пароль"
            GLabel_752.place(x=10,y=110,width=73,height=30)

            GLineEdit_603=tk.Entry(avt)
            GLineEdit_603["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times',size=10)
            GLineEdit_603["font"] = ft
            GLineEdit_603["fg"] = "#333333"
            GLineEdit_603["justify"] = "center"
            GLineEdit_603["text"] = "Entry"
            GLineEdit_603.place(x=10,y=80,width=264,height=30)

            GLineEdit_711=tk.Entry(avt)
            GLineEdit_711["borderwidth"] = "1px"
            ft = tkFont.Font(family='Times',size=10)
            GLineEdit_711["font"] = ft
            GLineEdit_711["fg"] = "#333333"
            GLineEdit_711["justify"] = "center"
            GLineEdit_711["text"] = "Entry"
            GLineEdit_711.place(x=10,y=150,width=268,height=30)


            GButton_874=tk.Button(avt)
            GButton_874["bg"] = "#d4d0c8"
            ft = tkFont.Font(family='Times',size=10)
            GButton_874["font"] = ft
            GButton_874["fg"] = "#000000"
            GButton_874["justify"] = "center"
            GButton_874["text"] = "Войти"
            GButton_874.place(x=10,y=200,width=266,height=30)
            GButton_874["command"] = self.GButton_874_command
            
        def hotA(self):
            print("hot")

            
        root.bind('<Control-r>', hotR)
        root.bind('<Control-a>', hotA)



        


    
    def GButton_996_command(self):
        main = tk.Tk()
        main.title("Основное приложение")
        main.geometry("700x100") 
         
        # создаем набор вкладок
        notebook = ttk.Notebook(main)
        notebook.pack(expand=True, fill='both')
         
        # создаем пару фреймвов
        frame1 = ttk.Frame(notebook)
        frame2 = ttk.Frame(notebook)
        frame3 = ttk.Frame(notebook)
        frame4 = ttk.Frame(notebook)
        frame5 = ttk.Frame(notebook)
        frame6 = ttk.Frame(notebook)
         
        frame1.pack(fill='both', expand=True)
        frame2.pack(fill='both', expand=True)
        frame3.pack(fill='both', expand=True)
        frame4.pack(fill='both', expand=True)
        frame5.pack(fill='both', expand=True)
        frame6.pack(fill='both', expand=True)
         
        # добавляем фреймы в качестве вкладок
        notebook.add(frame1, text="Банк Канады")
        notebook.add(frame2, text="Центральный банк России")
        notebook.add(frame3, text="Европейский центральный банк")
        notebook.add(frame4, text="Национльный банк Грузии")
        notebook.add(frame5, text="Национальный банк республики Беларусь")
        notebook.add(frame6, text="Швейцарский национальный банк")

        
        data1 = ()
        with sqlite3.connect('currencies.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM BOCData")
            data1 = (row for row in cursor.fetchall())
        table1 = Table(frame1, headings=('Код', 'Значение', 'Время обновления'), rows=data1)
        table1.pack(expand=tk.YES, fill=tk.BOTH)
        
        data2 = ()
        with sqlite3.connect('currencies.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT CharCode,Value,UpdateDate FROM CBRData")
            data2 = (row for row in cursor.fetchall())
        table2 = Table(frame2, headings=('Код', 'Значение', 'Время обновления'), rows=data2)
        table2.pack(expand=tk.YES, fill=tk.BOTH)
        
        data3 = ()
        with sqlite3.connect('currencies.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM ECBData")
            data3 = (row for row in cursor.fetchall())
        table3 = Table(frame3, headings=('Код', 'Значение', 'Время обновления'), rows=data3)
        table3.pack(expand=tk.YES, fill=tk.BOTH)
        
        data4 = ()
        with sqlite3.connect('currencies.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM NBGData")
            data4 = (row for row in cursor.fetchall())
        table4 = Table(frame4, headings=('Код', 'Значение', 'Время обновления'), rows=data4)
        table4.pack(expand=tk.YES, fill=tk.BOTH)
        
        data5 = ()
        with sqlite3.connect('currencies.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM NBRBData")
            data5 = (row for row in cursor.fetchall())
        table5 = Table(frame5, headings=('Код', 'Значение', 'Время обновления'), rows=data5)
        table5.pack(expand=tk.YES, fill=tk.BOTH)
        
        data6 = ()
        with sqlite3.connect('currencies.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM SNBData")
            data6 = (row for row in cursor.fetchall())
        table6 = Table(frame6, headings=('Код', 'Значение', 'Время обновления'), rows=data6)
        table6.pack(expand=tk.YES, fill=tk.BOTH)      


     
    
        
    def SaveButton_command(self): 
        print("test")

    def GButton_920_command(self):
        Conf = tk.Tk()
        #setting title
        Conf.title("Меню настроек")
        #setting window size
        width=420
        height=245
        screenwidth = Conf.winfo_screenwidth()
        screenheight = Conf.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        Conf.geometry(alignstr)
        Conf.resizable(width=False, height=False)

        GCheckBox_494= tk.Checkbutton(Conf)
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_494["font"] = ft
        GCheckBox_494["fg"] = "#333333"
        GCheckBox_494["justify"] = "center"
        GCheckBox_494["text"] = "Центральный банк\nРоссии"
        GCheckBox_494.place(x=10,y=10,width=200,height=50)
        GCheckBox_494["offvalue"] = "0"
        GCheckBox_494["onvalue"] = "1"
        GCheckBox_494["command"] = self.GCheckBox_494_command

        GCheckBox_687=tk.Checkbutton(Conf)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_687["font"] = ft
        GCheckBox_687["fg"] = "#333333"
        GCheckBox_687["justify"] = "center"
        GCheckBox_687["text"] = "Центральный банк\nКанады"
        GCheckBox_687.place(x=10,y=70,width=200,height=45)
        GCheckBox_687["offvalue"] = "0"
        GCheckBox_687["onvalue"] = "1"
        GCheckBox_687["command"] = self.GCheckBox_687_command

        GCheckBox_409=tk.Checkbutton(Conf)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_409["font"] = ft
        GCheckBox_409["fg"] = "#333333"
        GCheckBox_409["justify"] = "center"
        GCheckBox_409["text"] = "Европейский\nцентральный банк"
        GCheckBox_409.place(x=10,y=120,width=200,height=50)
        GCheckBox_409["offvalue"] = "0"
        GCheckBox_409["onvalue"] = "1"
        GCheckBox_409["command"] = self.GCheckBox_409_command

        GCheckBox_174=tk.Checkbutton(Conf)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_174["font"] = ft
        GCheckBox_174["fg"] = "#333333"
        GCheckBox_174["justify"] = "center"
        GCheckBox_174["text"] = "Наиональный банк\nГрузии"
        GCheckBox_174.place(x=220,y=10,width=185,height=50)
        GCheckBox_174["offvalue"] = "0"
        GCheckBox_174["onvalue"] = "1"
        GCheckBox_174["command"] = self.GCheckBox_174_command

        GCheckBox_816=tk.Checkbutton(Conf)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_816["font"] = ft
        GCheckBox_816["fg"] = "#333333"
        GCheckBox_816["justify"] = "center"
        GCheckBox_816["text"] = "Национальный банк\nреспублики Беларусь"
        GCheckBox_816.place(x=220,y=70,width=200,height=50)
        GCheckBox_816["offvalue"] = "0"
        GCheckBox_816["onvalue"] = "1"
        GCheckBox_816["command"] = self.GCheckBox_816_command

        GCheckBox_490=tk.Checkbutton(Conf)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_490["font"] = ft
        GCheckBox_490["fg"] = "#333333"
        GCheckBox_490["justify"] = "center"
        GCheckBox_490["text"] = "Швейцарский\nнациональный банк"
        GCheckBox_490.place(x=220,y=120,width=185,height=50)
        GCheckBox_490["offvalue"] = "0"
        GCheckBox_490["onvalue"] = "1"
        GCheckBox_490["command"] = self.GCheckBox_490_command

        SaveButton=tk.Button(Conf)
        SaveButton["bg"] = "#400707"
        ft = tkFont.Font(family='Times',size=10)
        SaveButton["font"] = ft
        SaveButton["fg"] = "#ffffff"
        SaveButton["justify"] = "center"
        SaveButton["text"] = "Сохранить настройки"
        SaveButton.place(x=50,y=180,width=300,height=50)
        SaveButton["command"] = self.SaveButton_command


        
    def GCheckBox_494_command(self):
        print()


    def GCheckBox_687_command(self):
        print("command")


    def GCheckBox_409_command(self):
        print("command")


    def GCheckBox_754_command(self):
        print("command")


    def GCheckBox_592_command(self):
        print("command")


    def GCheckBox_174_command(self):
        print("command")


    def GCheckBox_816_command(self):
        print("command")


    def GCheckBox_490_command(self):
        print("command")


    def GCheckBox_577_command(self):
        print("command")


    def GCheckBox_166_command(self):
        print("commddd")




    def GButton_20_command(self):
        Sets = tk.Tk()
        #setting title
        Sets.title("Настройки")
        #setting window size
        width=600
        height=250
        screenwidth = Sets.winfo_screenwidth()
        screenheight = Sets.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        Sets.geometry(alignstr)
        Sets.resizable(width=False, height=False)

        GButton_142=tk.Button(Sets)
        GButton_142["bg"] = "#d4d0c8"
        ft = tkFont.Font(family='Times',size=10)
        GButton_142["font"] = ft
        GButton_142["fg"] = "#000000"
        GButton_142["justify"] = "center"
        GButton_142["text"] = "Назад"
        GButton_142.place(x=40,y=160,width=520,height=60)
        GButton_142["command"] = self.GButton_142_command

        GButton_918=tk.Button(Sets)
        GButton_918["bg"] = "#ff0000"
        ft = tkFont.Font(family='Times',size=10)
        GButton_918["font"] = ft
        GButton_918["fg"] = "#000000"
        GButton_918["justify"] = "center"
        GButton_918["text"] = "Выйти из аккаунта"
        GButton_918.place(x=40,y=90,width=520,height=60)
        GButton_918["command"] = self.GButton_918_command

        GCheckBox_89=tk.Checkbutton(Sets)
        ft = tkFont.Font(family='Times',size=12)
        GCheckBox_89["font"] = ft
        GCheckBox_89["fg"] = "#333333"
        GCheckBox_89["justify"] = "center"
        GCheckBox_89["text"] = " Тёмная тема"
        GCheckBox_89.place(x=40,y=30,width=181,height=40)
        GCheckBox_89["offvalue"] = "0"
        GCheckBox_89["onvalue"] = "1"
        GCheckBox_89["command"] = self.GCheckBox_89_command

        GCheckBox_82=tk.Checkbutton(Sets)
        ft = tkFont.Font(family='Times',size=12)
        GCheckBox_82["font"] = ft
        GCheckBox_82["fg"] = "#333333"
        GCheckBox_82["justify"] = "center"
        GCheckBox_82["text"] = "Звуковое оповещение при обновлении данных"
        GCheckBox_82.place(x=220,y=30,width=360,height=40)
        GCheckBox_82["offvalue"] = "0"
        GCheckBox_82["onvalue"] = "1"
        GCheckBox_82["command"] = self.GCheckBox_82_command

    def GButton_142_command(self):
        print("command")


    def GButton_918_command(self):
        print("command")


    def GCheckBox_89_command(self):
        print("command")


    def GCheckBox_82_command(self):
        print("command")

    

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
