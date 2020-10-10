import tkinter as tk
from tkinter import filedialog
import re

def gui():
    window = tk.Tk()
    window.title("FS Atomation")
    window.geometry("700x450")
    window.grid_columnconfigure((0,2), weight = 1)
    tk.Label(window, text = "Logo", font = 'Helvetica 18 bold').grid(row = 0, column = 1, padx = 10, pady = 10)

    fileList = []
    def browse_file():
        fname = filedialog.askopenfilename()
        # shortName = re.findall()
        # pathlabel.config(text = fname)
        fileList.append(fname)
        if len(fileList) == 1:
            tk.Label(window, text = fileList[0]).grid(row = 2, column = 1)
        else:
            tk.Label(window, text = fileList[1]).grid(row = 3, column = 1)

    tk.Label(window, text = "Input Files:", font = 'bold').grid(row = 1, column = 0)
    tk.Label(window, text = "Excel File:").grid(row = 2, column = 0, padx = 5, pady = 5)
    tk.Label(window, text = "Word File:").grid(row = 3, column = 0, padx = 5, pady = 5)
    excelFile = tk.Button(window, text = "Choose file...", command = lambda: browse_file())
    wordFile = tk.Button(window, text = "Choose file...", command = lambda: browse_file())

    excelFile.grid(row = 2, column = 2, padx = 5, pady = 5)
    wordFile.grid(row = 3, column = 2, padx = 5, pady = 5)

    window.mainloop()

if __name__ == '__main__':
    gui()
