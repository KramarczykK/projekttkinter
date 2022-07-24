from operator import index
from tkinter import CENTER, StringVar
import xdrlib
import sys
import os

from kiwisolver import Expression
from numpy import delete
from imports import *
from math import sqrt, sin, cos, log10

def resourcePath(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)

class Calculator:
    def __init__(self):
        self.width, self.height = settings.WINDOW_MIN_SIZE

        self.window = tk.Tk()
        self.window.geometry('+%i+%i' % ((self.window.winfo_screenwidth() - self.width) / 2, (self.window.winfo_screenheight() - self.height) / 2))
        self.window.iconbitmap(resourcePath('calc.ico'))
        self.window.minsize(self.width, self.height)
        self.window.title(settings.WINDOW_TITLE)
        self.action_list = []
        self.percentage_list = []
        self.sign = ''
        
        
  
        # Frames
        self.screen_top_frame   = ttk.Frame(self.window, style='FrameA.TFrame')
        self.screen_right_frame = ttk.Frame(self.window, style='FrameA.TFrame')
        self.numbers_frame      = ttk.Frame(self.window, style='FrameA.TFrame')
        self.operations_A_frame = ttk.Frame(self.window, style='FrameD.TFrame')
        self.operations_B_frame = ttk.Frame(self.window, style='FrameE.TFrame')
        self.operations_C_frame = ttk.Frame(self.window, style='FrameF.TFrame')

        
        
        self.number = tk.StringVar(value = '0')
        self.txtplot = tk.StringVar(value = '0')
        self.var =  tk.StringVar()

        # Top screen
        self.screen_top = ttk.Label(self.screen_top_frame, textvariable = self.number , anchor='e', style='TopScreen.TLabel')

        # Right - bot screen
        self.screen_rightbot = ttk.Label(self.operations_C_frame, textvariable = self.txtplot, anchor = 'e', style = 'FrameF.TFrame') 

       
    
        # Buttons
        self.number_buttons = [
            tk.Button(self.numbers_frame, text='7'  , command=lambda: self.button_click(7)),
            tk.Button(self.numbers_frame, text='8'  , command=lambda: self.button_click(8)),
            tk.Button(self.numbers_frame, text='9'  , command=lambda: self.button_click(9)),
            tk.Button(self.numbers_frame, text='4'  , command=lambda: self.button_click(4)),
            tk.Button(self.numbers_frame, text='5'  , command=lambda: self.button_click(5)),
            tk.Button(self.numbers_frame, text='6'  , command=lambda: self.button_click(6)),
            tk.Button(self.numbers_frame, text='1'  , command=lambda: self.button_click(1)),
            tk.Button(self.numbers_frame, text='2'  , command=lambda: self.button_click(2)),
            tk.Button(self.numbers_frame, text='3'  , command=lambda: self.button_click(3)),
            tk.Button(self.numbers_frame, text='+/-', command=lambda: self.button_changingsign()),
            tk.Button(self.numbers_frame, text='0'  , command=lambda: self.button_click(0)),
            tk.Button(self.numbers_frame, text='.'  , command=lambda: self.button_comma('.')),
        ]
        
        self.operations_buttons = [
            tk.Button(self.operations_B_frame, text='X'  , command=lambda: self.button_multiply()),
            tk.Button(self.operations_B_frame, text='-'  , command=lambda: self.button_minus()),
            tk.Button(self.operations_B_frame, text='+'  , command=lambda: self.button_add()),
            tk.Button(self.operations_B_frame, text='='  , command=lambda: self.button_equal()),
        ]

        self.functions_buttons = [
            tk.Button(self.operations_A_frame, text='%'  , command= lambda: self.button_percentage()),
            tk.Button(self.operations_A_frame, text='CE'  , command=lambda: self.button_partclear()),
            tk.Button(self.operations_A_frame, text='C'  , command=lambda: self.button_clear()),
            tk.Button(self.operations_A_frame, text='\u232b', command=lambda: self.button_backspace()),
            tk.Button(self.operations_A_frame, text='1/x'  , command=lambda: self.button_homographic()),    
            tk.Button(self.operations_A_frame, text='x\u00B2'  , command=lambda: self.button_square()),
            tk.Button(self.operations_A_frame, text='\u221Ax'  , command=lambda: self.button_sqrt()),
            tk.Button(self.operations_A_frame, text='\u00F7'  , command=lambda: self.button_division()),
        ]
    
    

        

        # Right screen
        self.figure       = Figure()
        self.ax           = self.figure.add_subplot(111)
        self.canvas       = FigureCanvasTkAgg(self.figure, self.screen_right_frame)        
        self.screen_right = self.canvas.get_tk_widget()

        # Placeholder for entry
        placeholder = "Write your equation"
        self.placeholder = placeholder
        self.state = 'normal'

        # Entry
        self.right_entry = tk.Entry(self.operations_C_frame, textvariable = self.var)
        self.button_func = tk.Button(self.operations_C_frame, text = "Enter equation", command = lambda: self.drawChart())
        self.screen_right.pack()
        self.put_placeholder()
        

        # Styling  
    def setStyle(self):
        self.window.configure(bg=settings.COLOR_GRAY)

        style = ttk.Style()
        style.configure('FrameA.TFrame', background=settings.COLOR_GRAY)
        style.configure('FrameB.TFrame', background='green')
        style.configure('FrameC.TFrame', background='blue')
        style.configure('FrameD.TFrame', background='yellow')
        style.configure('FrameE.TFrame', background='purple')
        style.configure('FrameF.TFrame', background= settings.COLOR_GRAY,  FONT = settings.RIGHT_BOT_SCREEN_FONT)

        style.configure('TopScreen.TLabel', background=settings.COLOR_CREME, font=settings.TOP_SCREEN_FONT)

        for button in self.number_buttons:
            button.configure(bg=settings.COLOR_GRAY, fg=settings.COLOR_WHITE, font=settings.BUTTON_FONT, borderwidth=0, activebackground=settings.COLOR_DARKGRAY, activeforeground=settings.COLOR_WHITE)
        
        for button_operation in self.operations_buttons:
            button_operation.configure(bg=settings.COLOR_GRAY, fg=settings.COLOR_WHITE, font=settings.BUTTON_FONT, borderwidth=0, activebackground=settings.COLOR_DARKGRAY, activeforeground=settings.COLOR_WHITE)
    
        for button_function in self.functions_buttons:
            button_function.configure(bg=settings.COLOR_GRAY, fg=settings.COLOR_WHITE, font=settings.BUTTON_FONT, borderwidth=0, activebackground=settings.COLOR_DARKGRAY, activeforeground=settings.COLOR_WHITE)
    
        self.button_func.configure(bg=settings.COLOR_GRAY, fg=settings.COLOR_WHITE, font=settings.BUTTON_FONT, borderwidth=0, activebackground=settings.COLOR_DARKGRAY, activeforeground=settings.COLOR_WHITE)
        self.right_entry.configure(bg = settings.COLOR_LIGHTGRAY, font = settings.RIGHT_BOT_SCREEN_FONT, fg=settings.COLOR_WHITE)

    
    # Arragement
    def placeComponents(self):
        # Frames
        self.screen_top_frame  .place(x=0   * self.width, y=0   * self.height, width=0.4 * self.width, height=0.2 * self.height)
        self.screen_right_frame.place(x=0.4 * self.width, y=0   * self.height, width=0.6 * self.width, height=0.8 * self.height)
        self.numbers_frame     .place(x=0   * self.width, y=0.4 * self.height, width=0.3 * self.width, height=0.6 * self.height)
        self.operations_A_frame.place(x=0   * self.width, y=0.2 * self.height, width=0.4 * self.width, height=0.2 * self.height)
        self.operations_B_frame.place(x=0.3 * self.width, y=0.4 * self.height, width=0.1 * self.width, height=0.6 * self.height)
        self.operations_C_frame.place(x=0.4 * self.width, y=0.8 * self.height, width=0.6 * self.width, height=0.2 * self.height)

        # Buttons
        numbers_frame_width  = 0.3 * self.width
        numbers_frame_height = 0.6 * self.height
        j = 0
        for i, button in enumerate(self.number_buttons):
            button.place(x=(i % 3) / 3 * numbers_frame_width, y=j * numbers_frame_height, width=numbers_frame_width / 3, height=numbers_frame_height / 4)
            if i % 3 == 2:
                j += 0.25

        # Operation buttons
        operation_frame_width  = 0.1 * self.width
        operation_frame_height = 0.6  * self.height
        j = 0
        for i, button_operation in enumerate(self.operations_buttons):
            button_operation.place(x= 0, y=j * operation_frame_height, width = operation_frame_width, height = operation_frame_height / 4)
            if i % 1 == 0:
                j += 0.25


        # Function buttons
        function_frame_width  = 0.4 * self.width
        function_frame_height = 0.2  * self.height
        j = 0
        for i, button_function in enumerate(self.functions_buttons):
            button_function.place(x=(i % 4) / 4 * function_frame_width, y=j * function_frame_height, width = function_frame_width / 4, height = function_frame_height / 2)
            if i % 4 == 3:
                j += 0.5    

        b_frame_width = 0.6 * self.width
        b_frame_height = 0.2 * self.height
        self.button_func.place(x = 0, y =  b_frame_height / 2, width = b_frame_width, height  = b_frame_height / 2 )  
        self.right_entry.place(x = b_frame_width / 5 , y = 0, width = 3 * b_frame_width / 5, height = b_frame_height / 2 ) 

        # Screens
        self.screen_top  .place(x=settings.SCREEN_OFFSET, y=settings.SCREEN_OFFSET, width=0.4 * self.width - 2 * settings.SCREEN_OFFSET, height=0.2 * self.height - 2 * settings.SCREEN_OFFSET)
        self.screen_right.place(x=settings.SCREEN_OFFSET, y=settings.SCREEN_OFFSET, width=0.6 * self.width - 2 * settings.SCREEN_OFFSET, height=0.8 * self.height - 2 * settings.SCREEN_OFFSET)

        self.window.update()

    # Bindings
    def setBindings(self):
        self.window.bind('<Escape>', self.onExit)
        self.window.bind('<Configure>', self.onResize)

        self.right_entry.bind("<FocusIn>", self.foc_in)
        self.right_entry.bind("<FocusOut>", self.foc_out)
        

        # Color button change
        self.number_buttons[0]. bind('<Enter>', lambda _: self.number_buttons[0]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.number_buttons[0]. bind('<Leave>', lambda _: self.number_buttons[0]. configure(bg=settings.COLOR_GRAY))
        self.number_buttons[1]. bind('<Enter>', lambda _: self.number_buttons[1]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.number_buttons[1]. bind('<Leave>', lambda _: self.number_buttons[1]. configure(bg=settings.COLOR_GRAY))
        self.number_buttons[2]. bind('<Enter>', lambda _: self.number_buttons[2]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.number_buttons[2]. bind('<Leave>', lambda _: self.number_buttons[2]. configure(bg=settings.COLOR_GRAY))
        self.number_buttons[3]. bind('<Enter>', lambda _: self.number_buttons[3]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.number_buttons[3]. bind('<Leave>', lambda _: self.number_buttons[3]. configure(bg=settings.COLOR_GRAY))
        self.number_buttons[4]. bind('<Enter>', lambda _: self.number_buttons[4]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.number_buttons[4]. bind('<Leave>', lambda _: self.number_buttons[4]. configure(bg=settings.COLOR_GRAY))
        self.number_buttons[5]. bind('<Enter>', lambda _: self.number_buttons[5]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.number_buttons[5]. bind('<Leave>', lambda _: self.number_buttons[5]. configure(bg=settings.COLOR_GRAY))
        self.number_buttons[6]. bind('<Enter>', lambda _: self.number_buttons[6]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.number_buttons[6]. bind('<Leave>', lambda _: self.number_buttons[6]. configure(bg=settings.COLOR_GRAY))
        self.number_buttons[7]. bind('<Enter>', lambda _: self.number_buttons[7]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.number_buttons[7]. bind('<Leave>', lambda _: self.number_buttons[7]. configure(bg=settings.COLOR_GRAY))
        self.number_buttons[8]. bind('<Enter>', lambda _: self.number_buttons[8]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.number_buttons[8]. bind('<Leave>', lambda _: self.number_buttons[8]. configure(bg=settings.COLOR_GRAY))
        self.number_buttons[9]. bind('<Enter>', lambda _: self.number_buttons[9]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.number_buttons[9]. bind('<Leave>', lambda _: self.number_buttons[9]. configure(bg=settings.COLOR_GRAY))
        self.number_buttons[10].bind('<Enter>', lambda _: self.number_buttons[10].configure(bg=settings.COLOR_LIGHTGRAY))
        self.number_buttons[10].bind('<Leave>', lambda _: self.number_buttons[10].configure(bg=settings.COLOR_GRAY))
        self.number_buttons[11].bind('<Enter>', lambda _: self.number_buttons[11].configure(bg=settings.COLOR_LIGHTGRAY))
        self.number_buttons[11].bind('<Leave>', lambda _: self.number_buttons[11].configure(bg=settings.COLOR_GRAY))

        
        self.operations_buttons[0]. bind('<Enter>', lambda _: self.operations_buttons[0]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.operations_buttons[0]. bind('<Leave>', lambda _: self.operations_buttons[0]. configure(bg=settings.COLOR_GRAY))
        self.operations_buttons[1]. bind('<Enter>', lambda _: self.operations_buttons[1]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.operations_buttons[1]. bind('<Leave>', lambda _: self.operations_buttons[1]. configure(bg=settings.COLOR_GRAY))
        self.operations_buttons[2]. bind('<Enter>', lambda _: self.operations_buttons[2]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.operations_buttons[2]. bind('<Leave>', lambda _: self.operations_buttons[2]. configure(bg=settings.COLOR_GRAY))
        self.operations_buttons[3]. bind('<Enter>', lambda _: self.operations_buttons[3]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.operations_buttons[3]. bind('<Leave>', lambda _: self.operations_buttons[3]. configure(bg=settings.COLOR_GRAY))

        
        self.functions_buttons[0]. bind('<Enter>', lambda _: self.functions_buttons[0]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.functions_buttons[0]. bind('<Leave>', lambda _: self.functions_buttons[0]. configure(bg=settings.COLOR_GRAY))
        self.functions_buttons[1]. bind('<Enter>', lambda _: self.functions_buttons[1]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.functions_buttons[1]. bind('<Leave>', lambda _: self.functions_buttons[1]. configure(bg=settings.COLOR_GRAY))
        self.functions_buttons[2]. bind('<Enter>', lambda _: self.functions_buttons[2]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.functions_buttons[2]. bind('<Leave>', lambda _: self.functions_buttons[2]. configure(bg=settings.COLOR_GRAY))
        self.functions_buttons[3]. bind('<Enter>', lambda _: self.functions_buttons[3]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.functions_buttons[3]. bind('<Leave>', lambda _: self.functions_buttons[3]. configure(bg=settings.COLOR_GRAY))
        self.functions_buttons[4]. bind('<Enter>', lambda _: self.functions_buttons[4]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.functions_buttons[4]. bind('<Leave>', lambda _: self.functions_buttons[4]. configure(bg=settings.COLOR_GRAY))
        self.functions_buttons[5]. bind('<Enter>', lambda _: self.functions_buttons[5]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.functions_buttons[5]. bind('<Leave>', lambda _: self.functions_buttons[5]. configure(bg=settings.COLOR_GRAY))
        self.functions_buttons[6]. bind('<Enter>', lambda _: self.functions_buttons[6]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.functions_buttons[6]. bind('<Leave>', lambda _: self.functions_buttons[6]. configure(bg=settings.COLOR_GRAY))
        self.functions_buttons[7]. bind('<Enter>', lambda _: self.functions_buttons[7]. configure(bg=settings.COLOR_LIGHTGRAY))
        self.functions_buttons[7]. bind('<Leave>', lambda _: self.functions_buttons[7]. configure(bg=settings.COLOR_GRAY))
        
    # Screen settings
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
        '''Chart creating'''
        self.ax.clear()

        self.X = np.linspace(-5, 5, 100)
        self.equation = self.var.get()
        self.Y = []

        self.equation = self.equation.replace('^', '**')

        try:
            for x in self.X:
                self.Y.append(eval(self.equation))
        except Exception as e:
            print(e)
            return 
        self.ax.plot(self.X,self.Y)
        
        self.canvas.draw()

       
    # Functions for buttons

    def button_click(self, nmb):
        '''Button with number'''
        self.number.set(self.number.get().lstrip('0') + str(nmb))
        perc = float(self.number.get())
        self.percentage_list.append(perc)
       
 
    def button_clear(self):       
        '''Clear button'''
        button = self.number.set(0)
        self.sign = "clear"
        if self.sign == "clear":
            self.screen_top.configure(font = settings.TOP_SCREEN_FONT)


    def button_add(self):
        '''Add button'''
        first_number = self.number.get()
        self.f_num = float(first_number)
        self.number.set(0)
        self.sign = "addition"
        self.action_list.append(self.f_num)

    def button_minus(self):
        '''Minus button'''
        first_number = self.number.get()
        self.f_num = float(first_number)
        self.number.set(0)
        self.sign = "minus"
        self.action_list.append(self.f_num)

    def button_multiply(self):
        '''Multiply button'''
        first_number = self.number.get()
        self.f_num = float(first_number)
        self.number.set(0)
        self.sign = "multiply"
        self.action_list.append(self.f_num)

    def button_division(self):
        '''Division button'''
        first_number = self.number.get()
        self.f_num = float(first_number)
        self.number.set(0)
        self.sign = "division"
        self.action_list.append(self.f_num)

    def button_equal(self):
        '''Equal sign button'''
        second_number = self.number.get()
        self.number.set(0)
        if self.sign == "addition":
            answer = self.number.set(self.f_num + float(second_number))
        elif self.sign == "minus":
            answer = self.number.set(self.f_num - float(second_number))
        elif self.sign == "multiply":
            answer = self.number.set(self.f_num * float(second_number))
        elif self.sign == "division":
            if int(second_number) != 0:
                answer = self.number.set(self.f_num / float(second_number))
            else:                              
                self.screen_top.configure(font = settings.DIVIDING_BY_0_FONT)
                self.number.set(" Nie można dzielić przez 0")
        self.action_list.append(self.number.get())
        
    def button_changingsign(self):
        '''Change sign button'''
        nmb = self.number.get()
        if int(nmb) > 0:
            self.number.set(-abs( int(self.number.get())))
        else:
            self.number.set(abs( int(self.number.get())))
       

    def button_square(self): 
        '''Square button'''
        self.number.set(int(self.number.get()) * int(self.number.get()))

    def button_sqrt(self):
        '''Sqrt button'''
        self.number.set(math.sqrt(int(self.number.get())))

    def button_homographic(self):
        '''1/x button'''
        self.number.set(1 / int(self.number.get()))

    def button_partclear(self):
        '''Part-clear button'''
        del self.action_list[-1]
        self.number.set(self.action_list[-1])
        print(self.action_list)

    def button_percentage(self):
        '''Percent sign button'''
        self.number.set(int(self.number.get()) / 100)

    def button_comma(self, cmm):
        '''Comma button'''
        com_nmb = self.number.get()
        self.number.set(com_nmb + str(cmm))
       
    def button_backspace(self):
        '''Backspace button'''
        del self.percentage_list[-1]
        self.number.set(self.percentage_list[-1])

    def put_placeholder(self):
        '''Placeholder function'''
        self.state = 'empty'
        self.right_entry.insert(0, self.placeholder)

    def foc_in(self, *args):
        if self.state == 'empty':
            self.state = 'normal'
            self.right_entry.delete('0', 'end')
            
    def foc_out(self, *args):
        if not self.right_entry.get():
            self.put_placeholder()
     

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