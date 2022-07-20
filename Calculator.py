from imports import *


class Calculator:
    def __init__(self):
        self.width, self.height = settings.WINDOW_SIZE

        self.window = tk.Tk()
        self.window.geometry('+%i+%i' % ((self.window.winfo_screenwidth() - self.width) / 2, (self.window.winfo_screenheight() - self.height) / 2))
        self.window.minsize(self.width, self.height)
        self.window.title(settings.WINDOW_TITLE)

        # Bindings
        self.window.bind('<Escape>', self.onExit)

        # Frames
        self.screen_top_frame   = ttk.Frame(self.window, style='FrameA.TFrame')
        self.screen_right_frame = ttk.Frame(self.window, style='FrameB.TFrame')
        self.numbers_frame      = ttk.Frame(self.window, style='FrameC.TFrame')
        self.operations_A_frame = ttk.Frame(self.window, style='FrameD.TFrame')
        self.operations_B_frame = ttk.Frame(self.window, style='FrameE.TFrame')
        self.operations_C_frame = ttk.Frame(self.window, style='FrameF.TFrame')

        # Buttons
        self.number_buttons = [
            tk.Button(self.numbers_frame, text='7', command=lambda: print('7')),
            tk.Button(self.numbers_frame, text='8', command=lambda: print('8')),
            tk.Button(self.numbers_frame, text='9', command=lambda: print('9')),
            tk.Button(self.numbers_frame, text='4', command=lambda: print('4')),
            tk.Button(self.numbers_frame, text='5', command=lambda: print('5')),
            tk.Button(self.numbers_frame, text='6', command=lambda: print('6')),
            tk.Button(self.numbers_frame, text='1', command=lambda: print('1')),
            tk.Button(self.numbers_frame, text='2', command=lambda: print('2')),
            tk.Button(self.numbers_frame, text='3', command=lambda: print('3')),
        ]
        
        # for number in self.number_buttons:
        #     if tk.Button in range(1,3):

                
                



        self.operations_buttons = []

    def placeComponents(self):
        self.screen_top_frame.place(relx=0, rely=0, relwidth=0.5, relheight=0.2)
        self.screen_right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.8)
        self.numbers_frame.place(relx=0, rely=0.4, relwidth=0.35, relheight=0.8)
        self.operations_A_frame.place(relx=0, rely=0.2, relwidth=0.5, relheight=0.2)
        self.operations_B_frame.place(relx=0.35, rely=0.4, relwidth=0.15, relheight=0.6)
        self.operations_C_frame.place(relx=0.5, rely=0.8, relwidth=0.5, relheight=0.2)

    def setStyle(self):
        style = ttk.Style()
        style.configure('FrameA.TFrame', background='red')
        style.configure('FrameB.TFrame', background='green')
        style.configure('FrameC.TFrame', background='blue')
        style.configure('FrameD.TFrame', background='yellow')
        style.configure('FrameE.TFrame', background='purple')
        style.configure('FrameF.TFrame', background='orange')

    def onExit(self, event):
        self.window.destroy()

    def mainloop(self):
        self.window.mainloop()


if __name__ == '__main__':
    try:
        calc = Calculator()
        calc.setStyle()
        calc.placeComponents()
        
        calc.mainloop()
    except Exception as e:
        print(f'Exception: {e}')
        input()