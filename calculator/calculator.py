import tkinter as tk
from tkinter import messagebox

class DiscountApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Discount Calculator Pro")
        self.root.geometry("400x600")
        self.root.configure(bg="#2c3e50")

        self.setup_ui()

    def setup_ui(self):
        # Header
        tk.Label(self.root, text="DISCOUNT CALCULATOR", font=("Arial", 16, "bold"), 
                 fg="#ecf0f1", bg="#2c3e50").pack(pady=(30, 20))
        
        # Input Container
        container = tk.Frame(self.root, bg="#2c3e50")
        container.pack(padx=40, fill="x")

        # Original Price Input
        tk.Label(container, text="Original Price:", fg="#bdc3c7", bg="#2c3e50").pack(anchor="w")
        self.entry_price = tk.Entry(container, font=("Arial", 12), justify="center")
        self.entry_price.pack(fill="x", ipady=8, pady=(0, 15))

        # Discount Percentage Input
        tk.Label(container, text="Discount (%):", fg="#bdc3c7", bg="#2c3e50").pack(anchor="w")
        self.entry_discount = tk.Entry(container, font=("Arial", 12), justify="center")
        self.entry_discount.pack(fill="x", ipady=8, pady=(0, 15))

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#2c3e50")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Calculate", command=self.calculate, bg="#27ae60", 
                  fg="white", width=12, font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5)
        
        tk.Button(btn_frame, text="Reset", command=self.reset_fields, bg="#e67e22", 
                  fg="white", width=12, font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5)

        # Result Display
        self.label_final = tk.Label(self.root, text="Final Price: $ 0.00", font=("Arial", 14, "bold"), 
                                    fg="#f1c40f", bg="#2c3e50")
        self.label_final.pack(pady=20)

        # History Section
        history_header = tk.Frame(self.root, bg="#2c3e50")
        history_header.pack(fill="x", padx=40)
        
        tk.Label(history_header, text="History Log:", fg="#bdc3c7", bg="#2c3e50").pack(side="left")
        tk.Button(history_header, text="Clear", command=self.clear_history, font=("Arial", 8),
                  bg="#c0392b", fg="white", bd=0).pack(side="right")

        self.history_list = tk.Listbox(self.root, height=8, bg="#34495e", fg="white", 
                                       font=("Courier", 10), bd=0)
        self.history_list.pack(padx=40, pady=10, fill="both")

    def calculate(self):
        try:
            p_text = self.entry_price.get().replace(",", "")
            d_text = self.entry_discount.get()

            if not p_text or not d_text:
                messagebox.showwarning("Input Required", "Please fill in all fields!")
                return

            price = float(p_text)
            discount = float(d_text)
            
            if not (0 <= discount <= 100):
                messagebox.showerror("Range Error", "Discount must be 0-100%!")
                return

            final = price - (price * discount / 100)
            res_str = f"$ {final:,.2f}"
            
            self.label_final.config(text=f"Final Price: {res_str}")
            self.history_list.insert(0, f"P:{price:,.0f} | D:{discount}% | Total:{res_str}")

        except ValueError:
            messagebox.showerror("Type Error", "Please enter numbers only!")

    def reset_fields(self):
        self.entry_price.delete(0, tk.END)
        self.entry_discount.delete(0, tk.END)
        self.label_final.config(text="Final Price: $ 0.00")

    def clear_history(self):
        if messagebox.askyesno("Confirm", "Delete history?"):
            self.history_list.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = DiscountApp(root)
    root.mainloop()