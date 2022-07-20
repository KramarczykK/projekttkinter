from imports import *


class Calculator:
    def __init__(self):
        self.width, self.height = settings.WINDOW_SIZE

        self.window = tk.Tk()
        self.window.geometry('+%i+%i' % ((self.window.winfo_screenwidth() - self.width) / 2, (self.window.winfo_screenheight() - self.height) / 2))
        self.window.minsize(self.width, self.height)
        self.window.title(settings.WINDOW_TITLE)

        self.number_buttons     = []
        self.operations_buttons = []
    
        # Frames
        self.screen_top_frame   = ttk.Frame(self.window, style='FrameA.TFrame')
        self.screen_right_frame = ttk.Frame(self.window, style='FrameB.TFrame')
        self.numbers_frame      = ttk.Frame(self.window, style='FrameC.TFrame')
        self.operations_A_frame = ttk.Frame(self.window, style='FrameD.TFrame')
        self.operations_B_frame = ttk.Frame(self.window, style='FrameE.TFrame')
        self.operations_C_frame = ttk.Frame(self.window, style='FrameF.TFrame')

        self.window.bind('<Escape>', self.onExit)

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