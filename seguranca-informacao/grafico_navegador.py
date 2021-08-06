import webbrowser
from tkinter import *

def google():
    webbrowser.open('www.google.com')

if __name__ == '__main__':
    root = Tk()
    root.title('Abrir Browser')
    root.geometry('300x200')
    
    mygoogle = Button(root, text='Abrir o Google', command = google).pack(pady=20)
    
    root.mainloop()