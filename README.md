# 🚆 Indian Railways — Online Ticket Booking System

A desktop-based railway ticket booking application built with **Python** and **Tkinter**.  
It simulates a full end-to-end booking flow — from selecting passengers to generating a PNR and viewing your e-ticket.

---

## 📸 Features

| Feature | Description |
|---|---|
| 👥 Passenger Details | Enter name, age, and gender for up to 4 passengers |
| 🗺️ Journey Selection | Choose boarding station, destination, train, and travel class |
| 💺 Seat Picker | Interactive 8×8 clickable seat grid (64 seats) |
| 💰 Fare Calculator | Live fare preview based on class × number of passengers |
| 💳 Payment | Supports UPI, Credit/Debit Card, Net Banking, and Cash at Counter |
| 🎫 E-Ticket | Auto-generated ticket with a unique 10-digit PNR number |
| 🔍 PNR Status | Look up any previously booked ticket by PNR number |

---

## 🖥️ Tech Stack

- **Language:** Python 3
- **GUI Library:** Tkinter (built-in)
- **No external dependencies required**

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed.

```bash
python --version
```

### Run the App

```bash
python indian_railways.py
```

---

## 📋 Booking Flow

```
Select No. of Passengers
        ↓
Enter Passenger Details (Name, Age, Gender)
        ↓
Select Journey Details (Station, Train, Class)
        ↓
Pick Seats (Interactive Grid)
        ↓
Make Payment (UPI / Card / Net Banking / Cash)
        ↓
View E-Ticket with PNR Number
```

---

## 🚉 Available Stations (30)

Ahmedabad, Bengaluru, Bhopal, Bhubaneswar, Chennai Central, Coimbatore, Ernakulam, Guntur, Guwahati, Howrah, Jaipur, Jammu, Kanpur, Lucknow, Madurai, Mumbai Central, Mysore, Nagpur, New Delhi, Patna, Pune, Raipur, Ranchi, Secunderabad, Surat, Tirupati, Vadodara, Varanasi, Visakhapatnam, Vijayawada

---

## 🚂 Available Trains (8)

| Train No. | Train Name |
|---|---|
| 12345 | Rajdhani Express |
| 12678 | Shatabdi Express |
| 11023 | Chennai Mail |
| 12723 | Telangana Express |
| 12002 | Bhopal Shatabdi |
| 22691 | Rajdhani Express |
| 12301 | Howrah Rajdhani |
| 12951 | Mumbai Rajdhani |

---

## 💰 Fare Chart

| Class | Fare per Passenger |
|---|---|
| Sleeper (SL) | ₹ 500 |
| Third AC (3A) | ₹ 1,000 |
| Second AC (2A) | ₹ 1,500 |
| First AC (1A) | ₹ 2,500 |

---

## 📁 Project Structure

```
indian-railways-booking/
│
└── indian_railways.py      # Main application file
```

---

## ⚠️ Limitations

- PNR data is stored **in-memory only** — bookings are lost when the app is closed
- Seat availability is **not persistent** across sessions
- Payment is **simulated** — no real transaction occurs

---

## 🔮 Possible Future Improvements

- [ ] Save bookings to a local database (SQLite)
- [ ] Add date of journey selection
- [ ] Persist seat availability across sessions
- [ ] Add cancellation and refund flow
- [ ] Export ticket as PDF

---

## 👨‍💻 Author

Built as a Python GUI project using Tkinter.  
For help or queries related to Indian Railways, call **139**.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
