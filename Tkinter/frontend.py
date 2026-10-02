import tkinter as tk

# Create the main application window
root = tk.Tk()  
root.title("Simple Tkinker App")
root.geometry("200x100") # set window size

#Function to print "Hello ,World !" in the console
def say_hello():
    print("Hello,World!")

 #create a button that trigger the say_hello functiom
hello_button = tk.Button(root, text="Click me",command=say_hello)
hello_button.pack(pady=20)

#start the event loop
root.mainloop()