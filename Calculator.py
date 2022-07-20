from imports import *


class Calculator:
    def __init__(self):
        self.width, self.height = settings.WINDOW_SIZE

        self.window = tk.Tk()
        self.window.geometry('+%i+%i' % ((self.window.winfo_screenwidth() - self.width) / 2, (self.window.winfo_screenheight() - self.height) / 2))
        self.window.minsize(self.width, self.height)
    
    def mainloop(self):
        self.window.mainloop()

if __name__ == '__main__':
    try:
        calc = Calculator()
        calc.mainloop()
    except Exception as e:
        print(f'Exception: {e}')
        input()