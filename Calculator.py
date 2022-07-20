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

    def placeComponents(self):
        self.screen_top_frame.place(relx=0, rely=0, relwidth=0.5, relheight=0.2)
        self.screen_right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
        self.numbers_frame.place(relx=0, rely=0.2, relwidth=0.25, relheight=0.8)
        self.operations_A_frame.place(relx=0.25, rely=0.2, relwidth=0.25, relheight=0.4)
        self.operations_B_frame.place(relx=0.25, rely=0.6, relwidth=0.25, relheight=0.4)

    def setStyle(self):
        style = ttk.Style()
        style.configure('FrameA.TFrame', background='red')
        style.configure('FrameB.TFrame', background='green')
        style.configure('FrameC.TFrame', background='blue')
        style.configure('FrameD.TFrame', background='yellow')
        style.configure('FrameE.TFrame', background='purple')

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