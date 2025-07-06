# Tkinter
# GUI - Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Apa ini!")

# Variabel dan Fungsi
NAMA_BELAKANG = tk.StringVar()
NAMA_DEPAN = tk.StringVar()

def tombol_click():
	'''fungsi ini akan dipanggil oleh tombol'''
	pesan = f"Hai {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, welcome toh mai app"
	showinfo(title="Sapa",message=pesan)

#frame input
input_frame = ttk.Frame(window)
# penempatan, grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen-komponen
# 1. label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan:")
nama_depan_label.pack(padx=10,fill="x",expand=True)

# 2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)

# 3. label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama Belakang:")
nama_belakang_label.pack(padx=10,fill="x",expand=True)

# 4. entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)

# 5. tombol
tombol_sapa = ttk.Button(input_frame,text="Sapa!",command=tombol_click)
tombol_sapa.pack(fill="x",expand=True,pady=10,padx=10)

# Main loop window
window.mainloop()




















