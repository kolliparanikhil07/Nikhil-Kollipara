import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string
passenger_data = []
journey_data   = {}
seat_data      = []
pnr_db         = {}

STATIONS = [
    "Ahmedabad", "Bengaluru", "Bhopal", "Bhubaneswar", "Chennai Central",
    "Coimbatore", "Ernakulam", "Guntur", "Guwahati", "Howrah",
    "Jaipur", "Jammu", "Kanpur", "Lucknow", "Madurai",
    "Mumbai Central", "Mysore", "Nagpur", "New Delhi", "Patna",
    "Pune", "Raipur", "Ranchi", "Secunderabad", "Surat",
    "Tirupati", "Vadodara", "Varanasi", "Visakhapatnam", "Vijayawada"
]

TRAINS = [
    "12345 - Rajdhani Express",
    "12678 - Shatabdi Express",
    "11023 - Chennai Mail",
    "12723 - Telangana Express",
    "12002 - Bhopal Shatabdi",
    "22691 - Rajdhani Express",
    "12301 - Howrah Rajdhani",
    "12951 - Mumbai Rajdhani",
]

CLASS_FARE = {
    "Sleeper (SL)"  : 500,
    "Third AC (3A)" : 1000,
    "Second AC (2A)": 1500,
    "First AC (1A)" : 2500,
}

VALID_SEATS = set(range(1, 65))
def generate_pnr():
    return ''.join(random.choices(string.digits, k=10))

def clear_globals():
    global passenger_data, journey_data, seat_data
    passenger_data = []
    journey_data   = {}
    seat_data      = []
def click1():
    count = var1.get()
    if count == 0:
        messagebox.showwarning("Warning", "Please select number of passengers.")
        return
    if count > 4:
        messagebox.showwarning("Warning",
            "You can book tickets for up to 4 passengers at a time.\n"
            "Please book again for additional passengers.")
        return
    clear_globals()
    open_passenger_window(count)
def open_passenger_window(count):
    win2 = tk.Toplevel()
    win2.title("Passenger Details")

    entries = []

    for i in range(count):
        row = i * 3
        tk.Label(win2, text=f"Passenger {i+1} Name:", font=("Arial", 13)).grid(
            row=row, column=0, padx=30, pady=4, sticky="w")
        e_name = tk.Entry(win2, width=25)
        e_name.grid(row=row, column=1, padx=20, pady=4)

        tk.Label(win2, text=f"Passenger {i+1} Age:", font=("Arial", 13)).grid(
            row=row+1, column=0, padx=30, sticky="w")
        e_age = tk.Entry(win2, width=25)
        e_age.grid(row=row+1, column=1, padx=20)

        tk.Label(win2, text=f"Passenger {i+1} Gender:", font=("Arial", 13)).grid(
            row=row+2, column=0, padx=30, sticky="w")
        g_var = tk.StringVar()
        ttk.Combobox(win2, values=["Male", "Female", "Other"],
                     textvariable=g_var, width=22).grid(row=row+2, column=1, padx=20)

        entries.append((e_name, e_age, g_var))

    def submit_passengers():
        global passenger_data
        passenger_data = []
        for idx, (en, ea, gv) in enumerate(entries):
            name   = en.get().strip()
            age_s  = ea.get().strip()
            gender = gv.get()

            if not name:
                messagebox.showwarning("Warning", f"Enter name for passenger {idx+1}.")
                return
            if not age_s.isdigit() or not (1 <= int(age_s) <= 120):
                messagebox.showwarning("Warning", f"Enter valid age for passenger {idx+1}.")
                return
            if not gender:
                messagebox.showwarning("Warning", f"Select gender for passenger {idx+1}.")
                return

            passenger_data.append({"name": name, "age": int(age_s), "gender": gender})

        win2.destroy()
        open_journey_window()

    tk.Button(win2, text="Next ➜", font=("Arial", 13), bg="#1565C0", fg="white",
              command=submit_passengers).grid(
        row=count*3, column=1, pady=15, padx=20, sticky="e")
def open_journey_window():
    win3 = tk.Toplevel()
    win3.title("Journey Details")

    var_board = tk.StringVar()
    var_dest  = tk.StringVar()
    var_train = tk.StringVar()
    var_class = tk.StringVar()

    tk.Label(win3, text="Boarding Station:", font=("Arial", 13)).grid(
        row=0, column=0, padx=30, pady=8, sticky="w")
    ttk.Combobox(win3, values=STATIONS, textvariable=var_board, width=28).grid(
        row=0, column=1, padx=20)

    tk.Label(win3, text="Destination Station:", font=("Arial", 13)).grid(
        row=1, column=0, padx=30, pady=8, sticky="w")
    ttk.Combobox(win3, values=STATIONS, textvariable=var_dest, width=28).grid(
        row=1, column=1, padx=20)

    tk.Label(win3, text="Select Train:", font=("Arial", 13)).grid(
        row=2, column=0, padx=30, pady=8, sticky="w")
    ttk.Combobox(win3, values=TRAINS, textvariable=var_train, width=28).grid(
        row=2, column=1, padx=20)

    tk.Label(win3, text="Select Class:", font=("Arial", 13)).grid(
        row=3, column=0, padx=30, pady=8, sticky="w")
    ttk.Combobox(win3, values=list(CLASS_FARE.keys()), textvariable=var_class, width=28).grid(
        row=3, column=1, padx=20)
    fare_label = tk.Label(win3, text="Fare per passenger: ₹ --", font=("Arial", 12), fg="#1565C0")
    fare_label.grid(row=4, column=0, columnspan=2, pady=6)

    def update_fare(*_):
        cls = var_class.get()
        if cls in CLASS_FARE:
            base = CLASS_FARE[cls]
            total = base * len(passenger_data)
            fare_label.config(
                text=f"Fare: ₹{base} × {len(passenger_data)} passenger(s) = ₹{total}")

    var_class.trace_add("write", update_fare)

    def submit_journey():
        global journey_data
        board = var_board.get()
        dest  = var_dest.get()
        train = var_train.get()
        cls   = var_class.get()

        if not board:
            messagebox.showwarning("Warning", "Select boarding station."); return
        if not dest:
            messagebox.showwarning("Warning", "Select destination station."); return
        if board == dest:
            messagebox.showwarning("Warning", "Boarding and destination cannot be the same."); return
        if not train:
            messagebox.showwarning("Warning", "Select a train."); return
        if not cls:
            messagebox.showwarning("Warning", "Select a class."); return

        journey_data = {
            "boarding"    : board,
            "destination" : dest,
            "train"       : train,
            "travel_class": cls,
            "fare_per_pax": CLASS_FARE[cls],
            "total_fare"  : CLASS_FARE[cls] * len(passenger_data),
        }
        win3.destroy()
        open_seat_window()

    tk.Button(win3, text="Next ➜", font=("Arial", 13), bg="#1565C0", fg="white",
              command=submit_journey).grid(row=5, column=1, pady=15, padx=20, sticky="e")
def open_seat_window():
    win4 = tk.Toplevel()
    win4.title("Seat Selection")

    tk.Label(win4, text="Seat Layout (1–64)", font=("Arial", 14, "bold")).pack(pady=8)
    tk.Label(win4, text="Click a seat to select / deselect it.",
             font=("Arial", 11), fg="gray").pack()

    count = len(passenger_data)
    selected = set()
    btn_map   = {}

    frame = tk.Frame(win4)
    frame.pack(padx=20, pady=10)

    def toggle_seat(seat_no):
        if seat_no in selected:
            selected.remove(seat_no)
            btn_map[seat_no].config(bg="#ECEFF1", fg="black")
        else:
            if len(selected) >= count:
                messagebox.showwarning("Warning",
                    f"You can only select {count} seat(s) for {count} passenger(s).")
                return
            selected.add(seat_no)
            btn_map[seat_no].config(bg="#1565C0", fg="white")
    for seat in range(1, 65):
        r, c = divmod(seat - 1, 8)
        b = tk.Button(frame, text=str(seat), width=4, height=2,
                      bg="#ECEFF1", font=("Arial", 10),
                      command=lambda s=seat: toggle_seat(s))
        b.grid(row=r, column=c, padx=3, pady=3)
        btn_map[seat] = b

    status_lbl = tk.Label(win4, text="", font=("Arial", 11), fg="#1565C0")
    status_lbl.pack()

    def submit_seats():
        global seat_data
        if len(selected) != count:
            messagebox.showwarning("Warning",
                f"Please select exactly {count} seat(s). You selected {len(selected)}.")
            return
        seat_data = sorted(selected)
        win4.destroy()
        open_payment_window()

    tk.Button(win4, text="Confirm Seats ➜", font=("Arial", 13),
              bg="#1565C0", fg="white", command=submit_seats).pack(pady=12)
def open_payment_window():
    win5 = tk.Toplevel()
    win5.title("Payment")

    total = journey_data["total_fare"]
    var_pay = tk.StringVar()

    tk.Label(win5, text="Payment", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(win5, text=f"Total Amount Due:  ₹ {total}",
             font=("Arial", 14), fg="#C62828").pack(pady=6)

    tk.Label(win5, text="Select Payment Method:", font=("Arial", 13)).pack(pady=4)
    for method in ["UPI", "Credit / Debit Card", "Net Banking", "Cash at Counter"]:
        tk.Radiobutton(win5, text=method, variable=var_pay, value=method,
                       font=("Arial", 12)).pack(anchor="w", padx=40)
    detail_frame = tk.Frame(win5)
    detail_frame.pack(pady=8)
    detail_label = tk.Label(detail_frame, text="", font=("Arial", 12))
    detail_label.grid(row=0, column=0, padx=10)
    detail_entry = tk.Entry(detail_frame, width=30)

    def on_method_change(*_):
        method = var_pay.get()
        if method == "UPI":
            detail_label.config(text="Enter UPI ID:")
            detail_entry.grid(row=0, column=1)
        elif method == "Credit / Debit Card":
            detail_label.config(text="Enter Card Number (last 4 digits):")
            detail_entry.grid(row=0, column=1)
        elif method in ("Net Banking", "Cash at Counter"):
            detail_label.config(text="")
            detail_entry.grid_remove()

    var_pay.trace_add("write", on_method_change)

    def submit_payment():
        method = var_pay.get()
        if not method:
            messagebox.showwarning("Warning", "Please select a payment method.")
            return

        if method == "UPI":
            uid = detail_entry.get().strip()
            if not uid or "@" not in uid:
                messagebox.showwarning("Warning", "Enter a valid UPI ID (e.g. name@upi).")
                return
        elif method == "Credit / Debit Card":
            card = detail_entry.get().strip()
            if not card.isdigit() or len(card) != 4:
                messagebox.showwarning("Warning", "Enter the last 4 digits of your card.")
                return

        messagebox.showinfo("Payment Successful",
                            f"✅ Payment of ₹{total} received via {method}.\nGenerating your ticket...")
        win5.destroy()
        generate_ticket()

    tk.Button(win5, text=f"Pay ₹ {total}", font=("Arial", 14, "bold"),
              bg="#2E7D32", fg="white", command=submit_payment).pack(pady=16)
def generate_ticket():
    pnr = generate_pnr()

    booking = {
        "pnr"        : pnr,
        "passengers" : passenger_data[:],
        "journey"    : journey_data.copy(),
        "seats"      : seat_data[:],
    }
    pnr_db[pnr] = booking

    show_ticket(booking)

def show_ticket(booking):
    win6 = tk.Toplevel()
    win6.title("Your Ticket")
    win6.configure(bg="#E3F2FD")
    tk.Label(win6, text="🚆  INDIAN RAILWAYS", font=("Arial", 18, "bold"),
             bg="#1565C0", fg="white").pack(fill="x", pady=0)
    tk.Label(win6, text="E-Ticket / Booking Confirmation",
             font=("Arial", 11), bg="#1565C0", fg="#BBDEFB").pack(fill="x")

    body = tk.Frame(win6, bg="#E3F2FD")
    body.pack(padx=30, pady=15, fill="both")

    def row(label, value, r):
        tk.Label(body, text=label, font=("Arial", 11, "bold"),
                 bg="#E3F2FD", anchor="w").grid(row=r, column=0, sticky="w", pady=3)
        tk.Label(body, text=value, font=("Arial", 11),
                 bg="#E3F2FD", anchor="w").grid(row=r, column=1, sticky="w", padx=20)

    j = booking["journey"]
    row("PNR Number",      booking["pnr"],          0)
    row("Train",           j["train"],              1)
    row("From",            j["boarding"],           2)
    row("To",              j["destination"],        3)
    row("Class",           j["travel_class"],       4)
    row("Total Fare",      f"₹ {j['total_fare']}",  5)
    row("Seats",           ", ".join(map(str, booking["seats"])), 6)
    ttk.Separator(win6, orient="horizontal").pack(fill="x", padx=20, pady=4)

    tk.Label(win6, text="Passenger Details", font=("Arial", 12, "bold"),
             bg="#E3F2FD").pack(pady=4)

    cols = ("No.", "Name", "Age", "Gender", "Seat")
    tree = ttk.Treeview(win6, columns=cols, show="headings", height=len(booking["passengers"]))
    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=100, anchor="center")

    for i, p in enumerate(booking["passengers"]):
        seat = booking["seats"][i] if i < len(booking["seats"]) else "-"
        tree.insert("", "end", values=(i+1, p["name"], p["age"], p["gender"], seat))

    tree.pack(padx=20, pady=6)

    tk.Label(win6, text=f"Save your PNR: {booking['pnr']}",
             font=("Arial", 12, "bold"), fg="#C62828", bg="#E3F2FD").pack(pady=6)

    tk.Button(win6, text="Close", font=("Arial", 12),
              bg="#1565C0", fg="white",
              command=win6.destroy).pack(pady=10)
def check_pnr():
    pnr = e1.get().strip()
    if not pnr:
        messagebox.showwarning("Warning", "Enter a PNR number.")
        return
    if pnr not in pnr_db:
        messagebox.showerror("Not Found",
            f"PNR '{pnr}' not found.\n"
            "Please check the number or book a ticket first.")
        return
    show_ticket(pnr_db[pnr])
root = tk.Tk()
root.title("INDIAN RAILWAYS")
root.configure(bg="#E3F2FD")
root.resizable(False, False)
tk.Label(root, text="🚆  INDIAN RAILWAYS",
         font=("Arial", 22, "bold"), bg="#1565C0", fg="white").pack(fill="x")
tk.Label(root, text="Online Ticket Booking System",
         font=("Arial", 11), bg="#1565C0", fg="#BBDEFB").pack(fill="x")

main_frame = tk.Frame(root, bg="#E3F2FD")
main_frame.pack(padx=40, pady=20)
tk.Label(main_frame, text="1.  Book a Ticket",
         font=("Arial", 14, "bold"), bg="#E3F2FD").grid(
    row=0, column=0, columnspan=2, sticky="w", pady=(10, 4))

tk.Label(main_frame, text="Number of Passengers:",
         font=("Arial", 12), bg="#E3F2FD").grid(row=1, column=0, sticky="w")

var1 = tk.IntVar()
ttk.Combobox(main_frame, values=[1, 2, 3, 4], textvariable=var1, width=10).grid(
    row=1, column=1, padx=10, pady=4, sticky="w")

tk.Button(main_frame, text="Book Ticket  ➜", font=("Arial", 12),
          bg="#1565C0", fg="white", command=click1).grid(
    row=2, column=1, pady=8, sticky="w")

ttk.Separator(main_frame, orient="horizontal").grid(
    row=3, column=0, columnspan=2, sticky="ew", pady=12)
tk.Label(main_frame, text="2.  Check PNR Status",
         font=("Arial", 14, "bold"), bg="#E3F2FD").grid(
    row=4, column=0, columnspan=2, sticky="w", pady=(0, 4))

tk.Label(main_frame, text="Enter PNR Number:",
         font=("Arial", 12), bg="#E3F2FD").grid(row=5, column=0, sticky="w")

e1 = tk.Entry(main_frame, width=20, font=("Arial", 12))
e1.grid(row=5, column=1, padx=10, pady=4, sticky="w")

tk.Button(main_frame, text="Check Status  ➜", font=("Arial", 12),
          bg="#2E7D32", fg="white", command=check_pnr).grid(
    row=6, column=1, pady=8, sticky="w")
tk.Label(root, text="© Indian Railways — For help call 139",
         font=("Arial", 9), bg="#1565C0", fg="#BBDEFB").pack(fill="x", side="bottom")

root.mainloop()