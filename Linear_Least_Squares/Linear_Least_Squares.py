from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

window = Tk()
window.title("Data Analysis Application")
window.geometry("700x300")
window.iconbitmap("C:/Users/TOSHIBA/Desktop/Python files/GUI/images/data.ico")

def graph(b,a):
    """User defined function to plot data."""
    g = lambda c: B*c + A
    yfit = g(b)
    plt.figure()
    plt.scatter(b,a)
    plt.plot(b,yfit,color='g')
    plt.title('Graph of the Best Fit Line')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(['data points'])
    plt.grid()
    plt.show()
    plt.savefig('graph1.png')


def par_cal(x, y):
    """"
    Function to calculate the slope and intercept
     of the best fit line Y = AX + B
    """
    global A
    global B
    global yfit

    tuples = list(zip(x,y))
    xy = []
    for x1,y1 in tuples:
        prod = x1*y1
        xy.append(prod)
    
    x_sq = [x2**2 for x2 in x]

    #sigma_y = sum(y)
    #sigma_x = sum(x)
    #sigma_xy = sum(xy)
    #sigma_x_sq = sum(x_sq)
    #N = len(tuples)
    results = {
        "x values" : x,
        "y values" : y,
        "xy values" : xy,
        "x^2 values" : x_sq,
        }
    df = pd.DataFrame(results)
    yfit = []
    #prompt = "is Y expected to lie on a straight line through the origin? "
    #response = messagebox.askyesno("Data Visualization Prompt",prompt)
        
    #if response == 1:       
    x = np.array(x)
    y = np.array(y)
    fitting_coe = np.polyfit(x,y,1)
    B,A = fitting_coe
    results["slope"] = B
    results["intercept"] = A
    df = pd.DataFrame(results)
    df.to_csv("results.csv", "|")
    rsl = "\nParameters of the best fit line \n Y = AX + B are: \n A = " + str(A) + "\t B = " + str(B)
    results_label = Label(window_2, text=rsl, font=("Brittanic", 15))
    results_label.pack()

    btn4 = Button(window_2, text="graph", padx=20, pady=3, font=("Brittanic", 15), command=lambda: graph(x,y))
    btn4.pack()
    btn5 = Button(window_2, text="exit", padx=20, pady=3, font=("Brittanic", 15), command=window_2.destroy)
    btn5.pack()

    #prompt = messagebox.askyesno("Graphing prompt", "would you like to visualize the data? ")
    #if prompt == 1:
    #    graph(x, y)
    #elif prompt == 0:
    #    window_2.destroy

    #elif response == 0:
    #    B = (N*sigma_xy - sigma_x*sigma_y)/(N*sigma_x_sq - sigma_x**2)
    #    A = (sigma_x_sq*sigma_y - sigma_x*sigma_xy)/(N*sigma_x_sq - sigma_x**2)
    #    results['slope'] = B
    #    results['intercept'] = A
     #   df = pd.DataFrame(results)
      #  df.to_csv("results.csv", "|")
     #   

     #   for xvalue in x:
     #       yvalue = B*xvalue + A
     #       yfit.append(yvalue)
     #   print(results)
     #   plt.figure()
     #   plt.scatter(x,y)
     #   plt.plot(x,yfit,color='g')
     #   plt.title('graph')
      #  plt.xlabel('x')
      #  plt.ylabel('y')
      #  plt.legend(['data'])
     #  plt.show()
     #   plt.savefig('graph1.png')

# Creating new windows
def open():
    """
    Function that opens a new window 
    depending on the kind of data analysis chosen.
    """
    global window_2
    window_2 = Toplevel()
    #window_2.iconbitmap("")
    window_2.geometry("800x300")
    if choice.get() == "Statiscal Analysis":
        window_2.title("Statiscal Analysis")
        label = Label(window_2, text="Currently under development.")
        label.pack()
        exit = Button(window_2, text="Close", command=window_2.destroy)
        exit.pack()
        
    elif choice.get() == "Linear Regression":
        window_2.title("Linear Regression")
        par_cal(data_tuple, y_tuple)
        
    elif choice.get() == "Error Analysis":
        window_2.title("Error Analysis")
        label = Label(window_2, text="Currently under development.").pack()
        exit = Button(window_2, text="Close", command=window_2.destroy).pack()





# Defining function to choose kind of data analysis
def kind_of_analysis():
    """
    User defined function to display options of data analysis and obtain choice from user.
    """
    global choice
    txt = "Click proceed to obtain the slope and intercept the best fit line"
    welcome_label = Label(window, text=txt, font=("Brittanic", 15))
    welcome_label.pack(anchor=N)

    choice = StringVar()
    #stat = Radiobutton(window, text="Statiscal Analysis", variable=choice, value="Statiscal Analysis", font=("Brittanic", 15))
    #stat.select()
    #stat.pack(anchor=W)
    linear_regression = Radiobutton(window, text="Linear Regression", variable=choice, value="Linear Regression", font=("Brittanic", 15))
    linear_regression.select()
    linear_regression.pack(anchor=W)
    #error= Radiobutton(window, text="Error Analysis", variable=choice, value="Error Analysis", font=("Brittanic", 15))
    #error.deselect()
    #error.pack(anchor=W)

    proceed_btn = Button(window, text="Proceed", padx=50, pady=5, command=open)
    proceed_btn.pack()

def enter_y():
    """Store the y values of the data."""
    global y_tuple
    global data_tuple
    if data_entry1.get() != 'q':
        try:
            y_values.append(float(data_entry1.get()))
        except ValueError:
            msg1 = messagebox.showerror("Error", "Value error: Enter only numbers")
        else:
            data_entry1.delete(0, END)
            #print(y_values)

    elif data_entry1.get() == 'q':
        y_tuple = tuple(y_values)
        data_tuple = tuple(data_values)
        #print(f"y_values : {y_tuple} \n data_values : {data_tuple}")
        #par_cal(data_tuple, y_tuple)
        label2.destroy()
        data_entry1.destroy()
        btn1.destroy()

        if len(y_tuple) == len(data_tuple):
            kind_of_analysis()
        else:
            messagebox.showerror("Error Message", "lists length error. ")
            get_data()
            #data_values = []
            #label1 = Label(window, text="Enter the data values(enter 'q' when done) : ", font=("Brittanic", 15))
            #label1.pack()
            #data_entry = Entry(window, borderwidth=5)
            #data_entry.pack()
            #btn = Button(window, text="Enter", padx=30, pady=3 , command=enter_data)
            #btn.pack()
    
def enter_data():
    """Store the x values of data."""
    global data_values
    global y_values
    if data_entry.get() != 'q':
        try:
            data_values.append(float(data_entry.get()))
        except ValueError:
            msg = messagebox.showerror("Error", "Value error: Enter only numbers")
        else:
            data_entry.delete(0, END)
            #print(data_values)

    elif data_entry.get() == 'q':
        global data_entry1
        global label2
        global btn1
        label1.destroy()
        data_entry.destroy()
        btn.destroy()
        label2 = Label(window, text="Enter the y measurment values (enter 'q' when done) : ", font=("Brittanic", 15))
        label2.pack()
        data_entry1 = Entry(window, borderwidth=5)
        data_entry1.pack()
        btn1 = Button(window, text="Enter", padx=30, pady=3, command=enter_y)
        btn1.pack()

# Getting data points
def get_data():
    global data_values
    global y_values
    global label1
    global data_entry
    global btn
    data_values = []
    y_values = []
    label1 = Label(window, text="Welcome. Enter the x measurment values (enter 'q' when done) : ", font=("Brittanic", 15))
    label1.pack()
    data_entry = Entry(window, borderwidth=5)
    data_entry.pack()
    btn = Button(window, text="Enter", padx=30, pady=3 , command=enter_data)
    btn.pack()

get_data()

mainloop()