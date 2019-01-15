# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	

import Tkinter as tk


LARGE_FONT= ("Verdana", 12)


class MainApplication(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, ValidatePage, FinalPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        data=12

        button = tk.Button(self, text="Visit Validation Page", command=lambda: controller.show_frame(ValidatePage, data))
        button.pack()

        button2 = tk.Button(self, text="Visit Final Page", command=lambda: controller.show_frame(FinalPage))
        button2.pack()


class ValidatePage(tk.Frame):

    print data

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Validation Page!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Start", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Final Page", command=lambda: controller.show_frame(FinalPage))
        button2.pack()


class FinalPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Final Page!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Start",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Validation Page",
                            command=lambda: controller.show_frame(ValidatePage))
        button2.pack()
        


app = MainApplication()
app.mainloop()