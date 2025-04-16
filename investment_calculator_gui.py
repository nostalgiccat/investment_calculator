import tkinter as tk

root = tk.Tk()
root.title("Investment Calculator")
root.geometry("300x300")

# A = P * (1 + r)^t
# Where:
#
# A = final amount
# P = initial principal (investment)
# r = annual return rate (in decimal)
# t = number of years

def calculate_investment():
    principal = int(initial_amount_entry.get())
    return_rate = int(return_rate_entry.get()) * .01
    years = int(investment_time_entry.get())

    final_amount = principal * ((1 + return_rate)** years)
    final_amount = round(final_amount, 2)
    final_amount_label.config(text=f"Your final amount will be: ${final_amount}")


initial_amount_label = tk.Label(root, text="Initial amount that you will be investing: ")
initial_amount_label.pack(pady=7)
initial_amount_entry = tk.Entry(root)
initial_amount_entry.pack(pady=5)

return_rate_label = tk.Label(root, text="What is the return rate?: ")
return_rate_label.pack(pady=7)
return_rate_entry = tk.Entry(root)
return_rate_entry.pack(pady=5)

investment_time_label = tk.Label(root, text="How long will it be invested?: ")
investment_time_label.pack(pady=7)
investment_time_entry = tk.Entry(root)
investment_time_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate_investment)
calculate_button.pack()

final_amount_label = tk.Label(root, text=f"Your final amount will be: ")
final_amount_label.pack()


root.mainloop()
