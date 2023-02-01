import tkinter as tk
from Cdna import Cdna
from tkinter import ttk, Text

class App(tk.Tk):

  def __init__(self):
    super().__init__()

    # configure the root window
    self.title('PycDNA')
    self.geometry('500x500')

    self.label = ttk.Label(self, text='CDS Converter')
    self.label.pack()

    self.text = Text(self, height=25, width=70)
    self.text.pack()

    # button
    self.btn = tk.Button(self, text="Convert", command=lambda: self.convert())
    self.btn.pack()


  def convert(self):
    cdna = Cdna(self.text.get(1.0, "end-1c"))
    result = cdna.parse_to_cdna()
    self.text.delete(1.0, 'end')
    self.text.insert('end', result)
