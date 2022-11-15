from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from addtext import Modify

mod = Modify()

CURRIMG = ""
string = "watermark.io"
def getfile():
    global CURRIMG
    #Tk().withdraw() # prevents an empty tkinter window from appearing
    file_path = filedialog.askopenfile().name
    CURRIMG = file_path
    return None
    
def chkchange():
    global string , textbox
    input = textbox.get()
    if input != "":
        string = input
    else:
        string = "watermark.io"
    return None

def run():
    chkchange()
    mod.process(string, CURRIMG)
    return None

root = Tk()
root.title('WaterMark')
root.geometry("650x800")

style=PhotoImage(file='style.png')
upload=PhotoImage(file='upload.png')

frm = ttk.Frame(root)
frm.grid()
ttk.Label(frm,image=style).grid(row=0, column=0)
ttk.Label(frm, text="*************** WaterMark App **************\nAdd watermark filter to an image and save it." , padding="20").grid(column=0, row=1)

ttk.Label(frm, text="Upload ↓").grid(column=0, row=2)
ttk.Button(frm, text="Upload",padding="5", image=upload, command=getfile).grid(column=0, row=3)

ttk.Button(frm, text="Finish →", padding="5" , command=run).grid(column=0, row=4)
ttk.Label(frm, text="Change mark-text ↓").grid(column=0, row=5)
ttk.Label(frm, text=f"Current mark-text: {string}").grid(column=0, row=6)

textbox = ttk.Entry(frm , width=30)
textbox.grid(column=0, row=7)   

root.mainloop()

