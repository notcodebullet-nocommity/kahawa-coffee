from tkinter import *
from tkinter import ttk

# Creating tkinter root 
root = Tk() 
root.title('Combobox') 
root.geometry('500x250')

# label text for title 
ttk.Label(root, text="Choose How we get you your beans",  
          background='black', foreground="white",  
          font=("Arial", 15)).grid(row=0, column=1) 
  
# label 
ttk.Label(root, text="Delivery or Pick up :", 
          font=("Times New Roman", 10)).grid(column=0, row=5, padx=10, pady=25) 
  
# Combobox creation 
n = StringVar()
deliveryorpickup = ttk.Combobox(root, width=27, textvariable=n)
deliveryorpickup['values'] = (' Delivery', ' Pickup')
deliveryorpickup.grid(column=1, row=5)

def show_selected():
    selected_delivery = deliveryorpickup.get()
    result_label.config(text=f"You selected {selected_delivery}! Great Choice.")
    
    # Delivery option
    if selected_delivery == ' Delivery':
        import Deliveryimport
        root.destroy()
        Deliveryimport.worky()
    
    # Pickup option
    elif selected_delivery == ' Pickup':
        import Pickupimport
        root.destroy()
        Pickupimport.worky()

button = ttk.Button(root, text="Show Selected", command=show_selected)
button.grid(column=1, row=6, pady=10)

result_label = ttk.Label(root, text="", font=("Times New Roman", 10))
result_label.grid(column=1, row=7, pady=10)

root.mainloop()
