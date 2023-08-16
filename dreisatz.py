import tkinter as tk
from tkinter import messagebox

def dreisatz(a, b, c, method):
    if method == "Direkter Dreisatz":
        if a is None:
            return (b * c) / 100
        elif b is None:
            return (a * 100) / c
        elif c is None:
            return (a * 100) / b
    elif method == "Indirekter Dreisatz":
        if a is None:
            return 100 / (b / c)
        elif b is None:
            return (a * c) / 100
        elif c is None:
            return 100 / (a / b)
    else:
        raise ValueError("Ungültige Dreisatz-Methode.")

def convert_units(result, units):
    return f"{result} {units}"

def print_history(history):
    print("Berechnungshistorie:")
    for i, entry in enumerate(history, 1):
        print(f"{i}. {entry}")

def save_history_to_file(history):
    with open("berechnungshistorie.txt", "w") as file:
        for entry in history:
            file.write(entry + "\n")

def load_history_from_file():
    try:
        with open("berechnungshistorie.txt", "r") as file:
            history = [line.strip() for line in file]
    except FileNotFoundError:
        history = []
    return history

def calculate():
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    method = method_var.get()

    units = entry_units.get()
    rounding = int(entry_rounding.get())

    description = entry_description.get()

    result = dreisatz(a, b, c, method)
    if rounding is not None:
        result = round(result, rounding)

    if units is not None:
        result = convert_units(result, units)

    result_label.config(text=f"Ergebnis: {result}")

    history_entry = f"{description} | Ergebnis: {result}"
    history.append(history_entry)
    print_history(history)

    save_history_to_file(history)

    messagebox.showinfo("Berechnung abgeschlossen", "Die Dreisatz-Berechnung wurde erfolgreich durchgeführt.")

# GUI erstellen
root = tk.Tk()
root.title("Dreisatz-Berechner")

# Eingabefelder mit Beschriftungen
label_a = tk.Label(root, text="a:")
label_a.grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)
label_a_desc = tk.Label(root, text="Beschreibung für a (z.B. Anfangswert):")
label_a_desc.grid(row=1, column=0, columnspan=2)

label_b = tk.Label(root, text="b:")
label_b.grid(row=2, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=2, column=1)
label_b_desc = tk.Label(root, text="Beschreibung für b (z.B. Zuwachs/Abnahme pro Einheit):")
label_b_desc.grid(row=3, column=0, columnspan=2)

label_c = tk.Label(root, text="c:")
label_c.grid(row=4, column=0)
entry_c = tk.Entry(root)
entry_c.grid(row=4, column=1)
label_c_desc = tk.Label(root, text="Beschreibung für c (z.B. Einheiten, auf die sich b bezieht):")
label_c_desc.grid(row=5, column=0, columnspan=2)

label_units = tk.Label(root, text="Einheiten:")
label_units.grid(row=6, column=0)
entry_units = tk.Entry(root)
entry_units.grid(row=6, column=1)

label_rounding = tk.Label(root, text="Dezimalstellen:")
label_rounding.grid(row=7, column=0)
entry_rounding = tk.Entry(root)
entry_rounding.grid(row=7, column=1)

label_description = tk.Label(root, text="Beschreibung der Dreisatz-Berechnung:")
label_description.grid(row=8, column=0, columnspan=2)
entry_description = tk.Entry(root)
entry_description.grid(row=9, column=0, columnspan=2)

# Dropdown-Menü für die Dreisatz-Methode
method_var = tk.StringVar(root)
method_var.set("Direkter Dreisatz")
method_dropdown = tk.OptionMenu(root, method_var, "Direkter Dreisatz", "Indirekter Dreisatz")
method_dropdown.grid(row=10, column=0, columnspan=2)

# Ergebnis-Anzeige
result_label = tk.Label(root, text="Ergebnis: ")
result_label.grid(row=11, column=0, columnspan=2)

# Berechnungsknopf
calculate_button = tk.Button(root, text="Berechnen", command=calculate)
calculate_button.grid(row=12, column=0, columnspan=2)

# Historie laden
history = load_history_from_file()

root.mainloop()
