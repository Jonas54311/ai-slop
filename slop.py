import tkinter as tk
from tkinter import ttk, messagebox

#Jag vet inte vad majoriteten av det här är


# Skapa huvudfönster
root = tk.Tk()
root.title("Min planeringsapp")
root.geometry("500x550")
root.configure(bg="#f0f0f0")

# Kategorier
kategorier = ["Skola", "Hemma", "Fritid", "Övrigt"]

# Rubrik
rubrik = tk.Label(
    root,
    text="Min planering",
    font=("Arial", 22, "bold"),
    bg="#f0f0f0"
)
rubrik.pack(pady=15)

# Inmatning av syssla
tk.Label(root, text="Vad ska du göra?", bg="#f0f0f0").pack()

syssla_input = tk.Entry(root, width=35, font=("Arial", 11))
syssla_input.pack(pady=5)

# Välj kategori
tk.Label(root, text="Välj kategori:", bg="#f0f0f0").pack()

kategori_val = ttk.Combobox(
    root,
    values=kategorier,
    state="readonly"
)
kategori_val.current(0)
kategori_val.pack(pady=5)

# Lista med sysslor
lista = tk.Listbox(root, width=55, height=15, font=("Arial", 10))
lista.pack(pady=15)

# Lagra sysslor
sysslor = []

def uppdatera_lista():
    lista.delete(0, tk.END)

    for kategori in kategorier:
        lista.insert(tk.END, f"--- {kategori} ---")

        for syssla in sysslor:
            if syssla["kategori"] == kategori:
                status = "✓" if syssla["klar"] else "○"
                lista.insert(
                    tk.END,
                    f"  {status} {syssla['namn']}"
                )

def lagg_till():
    namn = syssla_input.get().strip()
    kategori = kategori_val.get()

    if namn == "":
        messagebox.showwarning(
            "Fel",
            "Skriv in en syssla först!"
        )
        return

    sysslor.append({
        "namn": namn,
        "kategori": kategori,
        "klar": False
    })

    syssla_input.delete(0, tk.END)
    uppdatera_lista()

def markera_klar():
    val = lista.curselection()

    if not val:
        return

    index = val[0]
    text = lista.get(index)

    if text.startswith("  ○ "):
        namn = text[4:]
        for syssla in sysslor:
            if syssla["namn"] == namn:
                syssla["klar"] = True
                break

    uppdatera_lista()

def ta_bort():
    val = lista.curselection()

    if not val:
        return

    text = lista.get(val[0])

    if text.startswith(("  ○ ", "  ✓ ")):
        namn = text[4:]

        for syssla in sysslor:
            if syssla["namn"] == namn:
                sysslor.remove(syssla)
                break

    uppdatera_lista()

# Knappar
tk.Button(
    root,
    text="Lägg till syssla",
    command=lagg_till,
    bg="#4CAF50",
    fg="white"
).pack(pady=4)

tk.Button(
    root,
    text="Markera som klar",
    command=markera_klar,
    bg="#2196F3",
    fg="white"
).pack(pady=4)

tk.Button(
    root,
    text="Ta bort syssla",
    command=ta_bort,
    bg="#f44336",
    fg="white"
).pack(pady=4)

# Visa kategorier och starta programmet
uppdatera_lista()
root.mainloop()