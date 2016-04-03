'''
Contains clases and objects for
UI/ view of abacus
'''
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
import Models.BudgetModel as bm
from tkinter import ttk



LARGE_FONT = ("Verdana", 12)



class Abacusapp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Abacus Client")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, BudgetFrame, PageTwo):
            
            frame = F(container,self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        

class StartPage(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1  = ttk.Button(self,text="Look at Budget",
                             command=lambda: controller.show_frame(BudgetFrame))
        button1.pack()
        button2  = ttk.Button(self,text="Page Two",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        
##        button2  = ttk.Button(self,text="Page Three",
##                             command=lambda: controller.show_frame(PageThree))



class BudgetFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self,text="Back Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        button2 = ttk.Button(self,text="Page Two",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Create Budget",
                             command=lambda: bm.Budget())
        button3.pack()





class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1  = ttk.Button(self,text="Back Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2  = ttk.Button(self,text="Page One",
                             command=lambda: controller.show_frame(PageOne))

        button2.pack()

##class PageThree(tk.Frame):
##
##    def __init__(self, parent, controller):
##        tk.Frame.__init__(self, parent)
##        label = tk.Label(self, text="Page Three", font=LARGE_FONT)
##        label.pack(pady=10, padx=10)
##
##        button1  = ttk.Button(self,text="Back Home",
##                             command=lambda: controller.show_frame(StartPage))
##        button1.pack()
##
##        f = Figure(figsize=(5,5), dpi=100)
##        a = f.add_subplot(111)
##        a.plot([1,2,3,4],[12,30,12,13])
##
##        canvas = FigureCanvasTkAgg(f, self)
##        canvas.show()
##        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
##
##        toolbar = NavigationToolbar2TkAgg(canvas, self)
##        toolbar.update()
##        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        
        
app = Abacusapp()
app.mainloop()
