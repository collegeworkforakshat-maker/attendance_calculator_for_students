# attendance_calculator_for_students

A simple Python-based attendance calculator that helps students track their attendance percentage and determine whether they are safe (≥75%) or need to attend more classes.

---

##  Features

- Calculates attendance percentage
- Tells whether you are above or below 75%
- Suggests:
  - How many classes you can skip (if safe)
  - How many classes you must attend (if below 75%)
- Handles invalid input properly

---

##  How It Works

The program uses basic math:

- **Attendance %** = (Attended / Total) × 100

Based on the result:
- If ≥ 75% → You are **SAFE**
- If < 75% → You need to **attend more classes**

---

##  Technologies Used

- Python (basic concepts)
  - Functions
  - Loops
  - Conditional statements
  - Exception handling

---

##  How to Run

1. Make sure Python is installed
2. Save the file as `attendance_calculator.py`
3. Open terminal / command prompt
4. Run:

```bash
python attendance_calculator.py
