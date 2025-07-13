import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import csv
import matplotlib.pyplot as plt

# -------------------- BMI Logic --------------------
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = round(weight / (height ** 2), 2)
        result_label.config(text=f"BMI: {bmi}")

        # Category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        category_label.config(text=f"Category: {category}")

        # Save to file
        name = name_entry.get()
        with open("bmi_data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().date(), name, weight, height, bmi, category])

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

# -------------------- Plotting BMI Trend --------------------
def show_graph():
    dates = []
    bmis = []
    try:
        with open("bmi_data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == name_entry.get():  # Filter by name
                    dates.append(row[0])
                    bmis.append(float(row[4]))

        if not dates:
            raise ValueError("No data for this user.")

        plt.figure(figsize=(8, 4))
        plt.plot(dates, bmis, marker='o', linestyle='-', color='cyan')
        plt.title("BMI Trend Over Time", color='white')
        plt.xlabel("Date", color='white')
        plt.ylabel("BMI", color='white')
        plt.xticks(rotation=45, color='white')
        plt.yticks(color='white')
        plt.gca().set_facecolor('#2e2e2e')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror("Data Error", str(e))

# -------------------- GUI Setup --------------------
root = tk.Tk()
root.title("BMI Calculator (Dark Mode)")
root.configure(bg="#2e2e2e")

label_font = ("Segoe UI", 10)
entry_bg = "#444444"
entry_fg = "#ffffff"

def add_dark_label(row, col, text):
    label = tk.Label(root, text=text, font=label_font, bg="#2e2e2e", fg="white")
    label.grid(row=row, column=col, padx=5, pady=5, sticky="w")
    return label

def add_dark_entry(row, col):
    entry = tk.Entry(root, bg=entry_bg, fg=entry_fg, insertbackground="white")
    entry.grid(row=row, column=col, padx=5, pady=5)
    return entry

add_dark_label(0, 0, "Name:")
name_entry = add_dark_entry(0, 1)

add_dark_label(1, 0, "Weight (kg):")
weight_entry = add_dark_entry(1, 1)

add_dark_label(2, 0, "Height (m):")
height_entry = add_dark_entry(2, 1)

tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="#007acc", fg="white").grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="BMI:", font=("Segoe UI", 11), bg="#2e2e2e", fg="lightgreen")
result_label.grid(row=4, column=0, columnspan=2)

category_label = tk.Label(root, text="Category:", font=("Segoe UI", 11), bg="#2e2e2e", fg="lightblue")
category_label.grid(row=5, column=0, columnspan=2)

tk.Button(root, text="Show BMI Trend", command=show_graph, bg="#444444", fg="white").grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
