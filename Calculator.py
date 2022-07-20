from imports import *


class Calculator:
    def __init__(self):
        self.width, self.height = settings.WINDOW_MIN_SIZE

        self.window = tk.Tk()
        self.window.geometry('+%i+%i' % ((self.window.winfo_screenwidth() - self.width) / 2, (self.window.winfo_screenheight() - self.height) / 2))
        self.window.minsize(self.width, self.height)
        self.window.title(settings.WINDOW_TITLE)
  
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
        
        # Entry
        self.screen_top = ttk.Entry(self.screen_top_frame)
                
        self.operations_buttons = []

    def setStyle(self):
        style = ttk.Style()
        style.configure('FrameA.TFrame', background='red')
        style.configure('FrameB.TFrame', background='green')
        style.configure('FrameC.TFrame', background='blue')
        style.configure('FrameD.TFrame', background='yellow')
        style.configure('FrameE.TFrame', background='purple')
        style.configure('FrameF.TFrame', background='orange')

    def placeComponents(self):
        self.screen_top_frame  .place(x=0    * self.width, y=0   * self.height, width=0.5  * self.width, height=0.2 * self.height)
        self.screen_right_frame.place(x=0.5  * self.width, y=0   * self.height, width=0.5  * self.width, height=0.8 * self.height)
        self.numbers_frame     .place(x=0    * self.width, y=0.4 * self.height, width=0.35 * self.width, height=0.8 * self.height)
        self.operations_A_frame.place(x=0    * self.width, y=0.2 * self.height, width=0.5  * self.width, height=0.2 * self.height)
        self.operations_B_frame.place(x=0.35 * self.width, y=0.4 * self.height, width=0.15 * self.width, height=0.6 * self.height)
        self.operations_C_frame.place(x=0.5  * self.width, y=0.8 * self.height, width=0.5  * self.width, height=0.2 * self.height)

        self.screen_top.place(x=settings.SCREEN_OFFSET, y=settings.SCREEN_OFFSET, width=0.5 * self.width - 2 * settings.SCREEN_OFFSET, height=0.2 * self.height - 2 * settings.SCREEN_OFFSET)

    def setBindings(self):
        self.window.bind('<Escape>', self.onExit)
        self.window.bind('<Configure>', self.onResize)

    def onResize(self, _):
        width       = self.window.winfo_width()
        height      = self.window.winfo_height()
        prev_width  = self.width
        prev_height = self.height
        self.width  = width  if width  > settings.WINDOW_MIN_SIZE[0] else prev_width
        self.height = height if height > settings.WINDOW_MIN_SIZE[1] else prev_height

        if self.width != prev_width or self.height != prev_height:
            self.window.geometry('%ix%i' % (self.width, self.height))
            self.placeComponents()

    def onExit(self, _):
        self.window.destroy()

    def mainloop(self):
        self.window.mainloop()


if __name__ == '__main__':
    try:
        calc = Calculator()
        calc.setStyle()
        calc.placeComponents()
        calc.setBindings()
        
        calc.mainloop()
    except Exception as e:
        print(f'Exception: {e}')
        input()