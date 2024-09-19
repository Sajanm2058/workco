from tkinter  import ttk
import random
import time
import datetime
from tkinter import messagebox
import numpy as npy

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management system")
        self.root.geometry("1540*800+0+0")


root = Tk()
ob = Hospital(root)
root.mainloop()
