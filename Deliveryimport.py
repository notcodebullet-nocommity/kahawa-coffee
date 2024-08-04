from tkinter import *
from tkinter import ttk
def worky():
    # Creating tkinter root 
    root = Tk() 
    root.title('Combobox') 
    root.geometry('500x250') 
  
    # label text for title 
    Label(root, text = "Choose Your Roast Type",
          background = 'black', foreground ="white",
          font = ("Arial", 15)).grid(row = 0, column = 1) 
  
    # label 
    Label(root, text = "Select the Roast :",
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
  
    # Combobox creation 
    n = StringVar()
    n2 = StringVar()

    roastchosen = ttk.Combobox(root, width = 27, textvariable = n)
    crushchosen = ttk.Combobox(root, width = 27, textvariable = n2)
  
    # Adding combobox drop down list 
    roastchosen['values'] = (' Arabica',  
                          ' Robusta', 
                          ' Liberica', 
                          ' Excelsa') 
    crushchosen['values'] = (' Extra Dark',  
                          ' Dark', 
                          ' Medium', 
                          ' Light') 
  
    roastchosen.grid(column = 1, row = 5)
    crushchosen.grid(column = 1, row = 6)


    def show_selected():
        selected_roast = roastchosen.get()
        selected_crush = crushchosen.get()
        result_label.config(text=f"You selected a {selected_crush}{selected_roast}! Great Choice.")

    # Button to trigger the display function
    button = Button(root, text="Show Selected ", command=show_selected)
    button.grid(column=2, row=6, pady=10)

    # Label to display the result
    result_label = Label(root, text="", font=("Times New Roman", 10))
    result_label.grid(column=1, row=7, pady=10)

    root.mainloop()

    
    
    