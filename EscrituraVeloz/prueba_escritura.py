import tkinter as tk
import time
import threading
import random

class TypeSpeedGUI:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Prueba de escritura veloz")
        self.root.geometry("800x600")

        self.texts = open("textos.txt", "r").read().split("\n")
        self.frame = tk.Frame(self.root)

        self.imagen = tk.PhotoImage(file="Imagenproyecto.png")
        self.imagen_label = tk.Label(image=self.imagen)
        self.imagen_label.grid(column=1, row=0)
        self.imagen_label.pack()


        self.sample_label = tk.Label(self.frame, text=random.choice(self.texts), font=("Arial", 12))
        self.sample_label.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

        self.input_entry = tk.Entry(self.frame, width=40, font=("Arial", 24))
        self.input_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyPress>", self.start)

        self.speed_label = tk.Label(self.frame, text="Velocidad: \n0.00 CPS\n0.00 CPM", font=("Arial", 18))
        self.speed_label.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(self.frame, text="Reiniciar", command=self.reset)
        self.reset_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False

        self.root.mainloop()

    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()

        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")
        if self.input_entry.get() == self.sample_label.cget('text')[:-1]:
            self.running = False
            self.input_entry.config(fg="green")


    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 1.0
            cps = len(self.input_entry.get())/self.counter
            cpm = cps * 60
            self.speed_label.config(text=f"Velocidad: \n{cps:.2f} CPS\n{cpm:.2f} CPM")

    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Velocidad: \n0.00 CPS\n0.00 CPM", font=("Arial", 18))
        self.sample_label.config(text= random.choice(self.texts))
        self.input_entry.delete(0, tk.END)


TypeSpeedGUI()

