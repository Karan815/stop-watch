import tkinter as tk
from tkinter import ttk, messagebox

# Hardcoded exchange rates relative to USD
EXCHANGE_RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "INR": 83.5,
    "GBP": 0.79,
    "JPY": 157.3,
    "AUD": 1.5,
    "CAD": 1.36,
    "CNY": 7.1
}

CURRENCIES = list(EXCHANGE_RATES.keys())

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_combobox.get()
        to_currency = to_combobox.get()

        if from_currency == "" or to_currency == "":
            messagebox.showerror("Error", "Please select both currencies.")
            return

        usd_amount = amount / EXCHANGE_RATES[from_currency]
        converted = usd_amount * EXCHANGE_RATES[to_currency]

        result_label.config(text=f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create GUI
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Currency Converter", font=("Arial", 18), bg="#f0f0f0").pack(pady=10)

amount_entry = tk.Entry(root, font=("Arial", 14))
amount_entry.pack(pady=10)

from_combobox = ttk.Combobox(root, values=CURRENCIES, font=("Arial", 12), state="readonly")
from_combobox.set("USD")
from_combobox.pack(pady=5)

to_combobox = ttk.Combobox(root, values=CURRENCIES, font=("Arial", 12), state="readonly")
to_combobox.set("EUR")
to_combobox.pack(pady=5)

convert_button = tk.Button(root, text="Convert", font=("Arial", 12), command=convert_currency)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0", fg="green")
result_label.pack(pady=10)

root.mainloop()
