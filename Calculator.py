from imports import *


class Calculator:
    def __init__(self):
        self.width, self.height = settings.WINDOW_MIN_SIZE

        self.window = tk.Tk()
        self.window.geometry('+%i+%i' % ((self.window.winfo_screenwidth() - self.width) / 2, (self.window.winfo_screenheight() - self.height) / 2))
        self.window.minsize(self.width, self.height)
        self.window.title(settings.WINDOW_TITLE)
  
        # Frames
        self.screen_top_frame          = ttk.Frame(self.window, style='FrameA.TFrame')
        self.screen_right_frame        = ttk.Frame(self.window, style='FrameA.TFrame')
        self.buttons_frame             = ttk.Frame(self.window, style='FrameA.TFrame')
        self.graphing_operations_frame = ttk.Frame(self.window, style='FrameA.TFrame')

        # Buttons
        self.buttons = [
            tk.Button(self.buttons_frame, text='%'      , command=lambda: self.pressOneNumberOperationButton('%')),
            tk.Button(self.buttons_frame, text='CE'     , command=lambda: self.pressClearButton('CE')),
            tk.Button(self.buttons_frame, text='C'      , command=lambda: self.pressClearButton('C')),
            tk.Button(self.buttons_frame, text='\u232b' , command=lambda: self.pressClearButton('Backspace')),
            tk.Button(self.buttons_frame, text='1/x'    , command=lambda: self.pressOneNumberOperationButton('1/x')),
            tk.Button(self.buttons_frame, text='x\u00B2', command=lambda: self.pressOneNumberOperationButton('x^2')),
            tk.Button(self.buttons_frame, text='\u221Ax', command=lambda: self.pressOneNumberOperationButton('sqrt')),
            tk.Button(self.buttons_frame, text='\u00F7' , command=lambda: self.pressTwoNumbersOperationButton('/')),
            tk.Button(self.buttons_frame, text='7'      , command=lambda: self.pressNumberButton('7')),
            tk.Button(self.buttons_frame, text='8'      , command=lambda: self.pressNumberButton('8')),
            tk.Button(self.buttons_frame, text='9'      , command=lambda: self.pressNumberButton('9')),
            tk.Button(self.buttons_frame, text='x'      , command=lambda: self.pressTwoNumbersOperationButton('*')),
            tk.Button(self.buttons_frame, text='4'      , command=lambda: self.pressNumberButton('4')),
            tk.Button(self.buttons_frame, text='5'      , command=lambda: self.pressNumberButton('5')),
            tk.Button(self.buttons_frame, text='6'      , command=lambda: self.pressNumberButton('6')),
            tk.Button(self.buttons_frame, text='-'      , command=lambda: self.pressTwoNumbersOperationButton('-')),
            tk.Button(self.buttons_frame, text='1'      , command=lambda: self.pressNumberButton('1')),
            tk.Button(self.buttons_frame, text='2'      , command=lambda: self.pressNumberButton('2')),
            tk.Button(self.buttons_frame, text='3'      , command=lambda: self.pressNumberButton('3')),
            tk.Button(self.buttons_frame, text='+'      , command=lambda: self.pressTwoNumbersOperationButton('+')),
            tk.Button(self.buttons_frame, text='+/-'    , command=lambda: self.pressNegateNumberButton()),
            tk.Button(self.buttons_frame, text='0'      , command=lambda: self.pressNumberButton('0')),
            tk.Button(self.buttons_frame, text='.'      , command=lambda: self.pressDotButton()),
            tk.Button(self.buttons_frame, text='='      , command=lambda: self.pressEqualsButton()),
        ]

        # Top screen
        self.top_screen_value = tk.StringVar(value='0')
        self.screen_top       = ttk.Label(self.screen_top_frame, textvariable=self.top_screen_value, anchor='e', style='TopScreen.TLabel')

        # Right screen
        self.figure       = Figure()
        self.ax           = self.figure.add_subplot(111)
        self.canvas       = FigureCanvasTkAgg(self.figure, self.screen_right_frame)        
        self.screen_right = self.canvas.get_tk_widget()

        # Others
        self.resetVars()
        
    def resetVars(self):
        self.current_number    = None
        self.first_number      = None
        self.second_number     = None
        self.current_operation = None
        self.save_number       = True
        self.is_new_number     = True

    def setStyle(self):
        self.window.configure(bg=settings.COLOR_GRAY)

        style = ttk.Style()
        style.configure('FrameA.TFrame', background=settings.COLOR_GRAY)
        
        style.configure('TopScreen.TLabel', background=settings.COLOR_CREME, font=settings.TOP_SCREEN_FONT)

        for button in self.buttons:
            button.configure(bg=settings.COLOR_GRAY, fg=settings.COLOR_WHITE, font=settings.BUTTON_FONT, borderwidth=0, activebackground=settings.COLOR_DARKGRAY, activeforeground=settings.COLOR_WHITE)
        
    def placeComponents(self):
        # Frames
        self.screen_top_frame         .place(x=0   * self.width, y=0   * self.height, width=0.4 * self.width, height=0.2 * self.height)
        self.screen_right_frame       .place(x=0.4 * self.width, y=0   * self.height, width=0.6 * self.width, height=0.8 * self.height)
        self.buttons_frame            .place(x=0   * self.width, y=0.2 * self.height, width=0.4 * self.width, height=0.8 * self.height)
        self.graphing_operations_frame.place(x=0.4 * self.width, y=0.8 * self.height, width=0.6 * self.width, height=0.2 * self.height)

        # Buttons
        buttons_frame_width  = 0.4 * self.width
        buttons_frame_height = 0.8 * self.height
        j = 0
        for i, button in enumerate(self.buttons):
            button.place(x=(i % 4) / 4 * buttons_frame_width, y=j * buttons_frame_height, width=buttons_frame_width / 4, height=buttons_frame_height / 6)
            if i % 4 == 3:
                j += 1 / 6

        # Screens
        self.screen_top  .place(x=2 * settings.SCREEN_OFFSET[0], y=settings.SCREEN_OFFSET[1], width=0.4 * self.width - 3 * settings.SCREEN_OFFSET[0], height=0.2 * self.height - 2 * settings.SCREEN_OFFSET[1])
        self.screen_right.place(x=settings.SCREEN_OFFSET[0], y=settings.SCREEN_OFFSET[1], width=0.6 * self.width - 3 * settings.SCREEN_OFFSET[0], height=0.8 * self.height - 2 * settings.SCREEN_OFFSET[1])

        self.window.update()

    def setBindings(self):
        self.window.bind('<Escape>', self.onExit)
        self.window.bind('<Configure>', self.onResize)
        self.window.bind('q', lambda _: self.drawChart())

        self.buttons[0]. bind('<Enter>', lambda _: self.buttons[0]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[0]. bind('<Leave>', lambda _: self.buttons[0]. configure(bg=settings.COLOR_GRAY))
        self.buttons[1]. bind('<Enter>', lambda _: self.buttons[1]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[1]. bind('<Leave>', lambda _: self.buttons[1]. configure(bg=settings.COLOR_GRAY))
        self.buttons[2]. bind('<Enter>', lambda _: self.buttons[2]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[2]. bind('<Leave>', lambda _: self.buttons[2]. configure(bg=settings.COLOR_GRAY))
        self.buttons[3]. bind('<Enter>', lambda _: self.buttons[3]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[3]. bind('<Leave>', lambda _: self.buttons[3]. configure(bg=settings.COLOR_GRAY))
        self.buttons[4]. bind('<Enter>', lambda _: self.buttons[4]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[4]. bind('<Leave>', lambda _: self.buttons[4]. configure(bg=settings.COLOR_GRAY))
        self.buttons[5]. bind('<Enter>', lambda _: self.buttons[5]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[5]. bind('<Leave>', lambda _: self.buttons[5]. configure(bg=settings.COLOR_GRAY))
        self.buttons[6]. bind('<Enter>', lambda _: self.buttons[6]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[6]. bind('<Leave>', lambda _: self.buttons[6]. configure(bg=settings.COLOR_GRAY))
        self.buttons[7]. bind('<Enter>', lambda _: self.buttons[7]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[7]. bind('<Leave>', lambda _: self.buttons[7]. configure(bg=settings.COLOR_GRAY))
        self.buttons[8]. bind('<Enter>', lambda _: self.buttons[8]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[8]. bind('<Leave>', lambda _: self.buttons[8]. configure(bg=settings.COLOR_GRAY))
        self.buttons[9]. bind('<Enter>', lambda _: self.buttons[9]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[9]. bind('<Leave>', lambda _: self.buttons[9]. configure(bg=settings.COLOR_GRAY))
        self.buttons[10].bind('<Enter>', lambda _: self.buttons[10].configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[10].bind('<Leave>', lambda _: self.buttons[10].configure(bg=settings.COLOR_GRAY))
        self.buttons[11].bind('<Enter>', lambda _: self.buttons[11].configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[11].bind('<Leave>', lambda _: self.buttons[11].configure(bg=settings.COLOR_GRAY))
        self.buttons[12].bind('<Enter>', lambda _: self.buttons[12].configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[12].bind('<Leave>', lambda _: self.buttons[12].configure(bg=settings.COLOR_GRAY))
        self.buttons[13].bind('<Enter>', lambda _: self.buttons[13].configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[13].bind('<Leave>', lambda _: self.buttons[13].configure(bg=settings.COLOR_GRAY))
        self.buttons[14].bind('<Enter>', lambda _: self.buttons[14].configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[14].bind('<Leave>', lambda _: self.buttons[14].configure(bg=settings.COLOR_GRAY))
        self.buttons[15].bind('<Enter>', lambda _: self.buttons[15].configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[15].bind('<Leave>', lambda _: self.buttons[15].configure(bg=settings.COLOR_GRAY))
        self.buttons[16].bind('<Enter>', lambda _: self.buttons[16].configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[16].bind('<Leave>', lambda _: self.buttons[16].configure(bg=settings.COLOR_GRAY))
        self.buttons[17].bind('<Enter>', lambda _: self.buttons[17].configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[17].bind('<Leave>', lambda _: self.buttons[17].configure(bg=settings.COLOR_GRAY))
        self.buttons[18].bind('<Enter>', lambda _: self.buttons[18].configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[18].bind('<Leave>', lambda _: self.buttons[18].configure(bg=settings.COLOR_GRAY))
        self.buttons[19].bind('<Enter>', lambda _: self.buttons[19].configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[19].bind('<Leave>', lambda _: self.buttons[19].configure(bg=settings.COLOR_GRAY))
        self.buttons[20].bind('<Enter>', lambda _: self.buttons[20].configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[20].bind('<Leave>', lambda _: self.buttons[20].configure(bg=settings.COLOR_GRAY))
        self.buttons[21].bind('<Enter>', lambda _: self.buttons[21].configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[21].bind('<Leave>', lambda _: self.buttons[21].configure(bg=settings.COLOR_GRAY))
        self.buttons[22].bind('<Enter>', lambda _: self.buttons[22].configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[22].bind('<Leave>', lambda _: self.buttons[22].configure(bg=settings.COLOR_GRAY))
        self.buttons[23].bind('<Enter>', lambda _: self.buttons[23].configure(bg=settings.COLOR_LIGHTGRAY))
        self.buttons[23].bind('<Leave>', lambda _: self.buttons[23].configure(bg=settings.COLOR_GRAY))

    def onResize(self, _):
        width       = self.window.winfo_width()
        height      = self.window.winfo_height()
        prev_width  = self.width
        prev_height = self.height
        self.width  = width  if width  >= settings.WINDOW_MIN_SIZE[0] else prev_width
        self.height = height if height >= settings.WINDOW_MIN_SIZE[1] else prev_height

        if self.width != prev_width or self.height != prev_height:
            self.window.geometry('%ix%i' % (self.width, self.height))
            self.placeComponents()

    def onExit(self, _):
        self.window.destroy()

    def drawChart(self):
        self.ax.clear()

        X = np.linspace(-5, 5, 100)
        Y = [X, X**2, X**3, X**4]
        self.ax.plot(X, random.choice(Y))
        self.ax.set_title('Test', weight='bold')
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')

        self.canvas.draw()

    def mainloop(self):
        self.window.mainloop()

    def pressNumberButton(self, nmb):
        self.save_number = True

        if self.is_new_number:
            self.top_screen_value.set(nmb)
            self.current_number = float(self.top_screen_value.get())
            self.is_new_number = False
        else:
            self.top_screen_value.set(self.top_screen_value.get() + str(nmb))
            self.current_number = float(self.top_screen_value.get())

    def pressDotButton(self):
        self.is_new_number = False
        self.top_screen_value.set(self.top_screen_value.get() + '.')
        self.current_number = float(self.top_screen_value.get())

    def pressTwoNumbersOperationButton(self, op):
        if self.save_number:
            self.save_number = False
            
            if self.first_number == None:
                self.first_number = float(self.top_screen_value.get())
            else:
                self.second_number = float(self.top_screen_value.get())

                if self.current_operation == '+':
                    self.first_number = self.first_number + self.second_number
                elif self.current_operation == '-':
                    self.first_number = self.first_number - self.second_number
                elif self.current_operation == '*':
                    self.first_number = self.first_number * self.second_number
                elif self.current_operation == '/':
                    if self.second_number == 0:
                        self.top_screen_value.set('\u221E')
                        self.resetVars()
                        return
                    self.first_number = self.first_number / self.second_number
                
                self.second_number = None
                self.top_screen_value.set(str(int(self.first_number)) if self.first_number % 1 == 0 else self.first_number)

        self.is_new_number     = True
        self.current_operation = op
        print('eee')

    def pressOneNumberOperationButton(self, op):
        if self.current_operation == '1/x':
            if self.current_number == 0:
                self.top_screen_value.set('\u221E')
                self.resetVars()
                return
            self.current_number = 1 / self.current_number
        elif self.current_operation == 'x^2':
            self.current_number **= 2
        elif self.current_operation == 'sqrt':
            try:
                self.current_number = math.sqrt(self.current_number)
            except Exception:
                self.top_screen_value.set('Invalid input')
                self.resetVars()
                return
        elif self.current_operation == '%':
            self.current_operation /= 100

        self.top_screen_value.set(str(self.current_number))
                
    def pressEqualsButton(self):
        if self.first_number != None and self.second_number != None:
            if self.current_operation == '+':
                self.first_number = self.first_number + self.second_number
            elif self.current_operation == '-':
                self.first_number = self.first_number - self.second_number
            elif self.current_operation == '*':
                self.first_number = self.first_number * self.second_number
            elif self.current_operation == '/':
                if self.second_number == 0:
                    self.top_screen_value.set('\u221E')
                    self.resetVars()
                    return
                self.first_number = self.first_number / self.second_number

            self.is_new_number = True
       
    def pressClearButton(self, mode):
        if mode == 'C':
            self.resetVars()

            self.top_screen_value.set('0')
        elif mode == 'CE':
            print('CE')
        elif mode == 'Backspace':
            self.current_number = float(self.top_screen_value.get()[-1])
            self.top_screen_value.set(str(self.current_number))

    def pressNegateNumberButton(self):
        self.current_number = -float(self.top_screen_value.get())
        if self.current_number == -0.0:
            self.current_number = 0
        self.top_screen_value.set(str(int(self.current_number)) if self.current_number % 1 == 0 else self.current_number)


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