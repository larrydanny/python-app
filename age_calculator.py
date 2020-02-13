from tkinter import *
from datetime import date

window = Tk()

window.title("Python GUI Tkinter")
window.geometry("450x100")


def age(dob_date):
    today_year = date.today().year
    today_month = date.today().month
    today_day = date.today().day

    dob_year = date.fromisoformat(dob_date).year
    dob_month = date.fromisoformat(dob_date).month
    dob_day = date.fromisoformat(dob_date).day

    month_list_31 = [1, 3, 5, 7, 8, 10, 12]

    if today_day < dob_day:
        today_month -= 1
        if today_month in month_list_31:
            today_day += 31
        else:
            today_day += 30

    if today_month < dob_month:
        today_year -= 1
        today_month += 12

    days = today_day - dob_day
    months = today_month - dob_month
    years = today_year - dob_year

    return_data = f"Your age is {years} years {months} months {days} days"

    return return_data


def calculate():
    get_age = age(dob.get())

    label = Label(window,
                  text=get_age,
                  font=("Helvetica", 20))
    label.grid(row=2, column=0, columnspan=2)
    dob.delete(0, END)
    # myLabel.after(5000, myLabel.destroy)


dob_label = Label(window, text="DoB (YYYY-MM-DD)")
dob_label.grid(row=0, column=0, stick=W+E+N+S)

dob = Entry(window)
dob.grid(row=0, column=1, stick=W+E+N+S)

calculate_btn = Button(window,
                       text="Calculate",
                       highlightbackground="#333333",
                       command=calculate)
calculate_btn.grid(row=1, column=1, stick=W+E+N+S)

window.mainloop()
