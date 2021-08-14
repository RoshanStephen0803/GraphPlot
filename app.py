#!/usr/bin/env python
# coding: utf-8

# In[12]:


import tkinter as tk
from tkinter import filedialog, Text, ttk
from tkinter import *
import pandas as pd
#%matplotlib inline
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

root = tk.Tk()
root.title("Application")
root.geometry("1000x900")
root.resizable(False, False)

p=[]

def new():
        
    for w3 in frame3.winfo_children():
        w3.destroy()
        
    for w4 in file_frame.winfo_children():
        w4.destroy()
        
    for w5 in Attribute.winfo_children():
        w5.destroy()
    
    for w in range(x):
        p.pop()
    

def addFile():
    global filename
    global label
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                         filetypes=(("CSV","*.csv"),("all files","*.*")))
    label=Label.config(SFP, text=filename, font=("Times",15))
    
def ShowData():
    global df
    file_path = filename
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] != ".csv":
            a=tk.messagebox.showerror("Information", "The file you have chosen is invalid")
            if a=='ok':
                addFile()  
        else:
            df = pd.read_csv(excel_filename)
        #df = pd.read_csv(excel_filename)
    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) 

    df_rows = df.to_numpy().tolist() 
    for row in df_rows:
        tv1.insert("", "end", values=row) 
    return None

def clear_data():
    tv1.delete(*tv1.get_children())
    return None
    
def showColumn():
    d = pd.read_csv(filename)
    sn=1
    clear_col()
    tv2["column"]= list(d.columns)
    tv2["show"] = "headings"
    tv2.heading('#1', text='Sr.No')
    tv2.heading('#2', text='Attribute')
    for colu in tv2["column"]:
        tv2.insert("", "end", values=(sn,colu))
        sn=sn+1
    tv2.bind('<Double 1>', getrow)
    

def clear_col():
    tv2.delete(*tv2.get_children())
    return None

def getrow(event):
    global c1
    global x
    c1=StringVar()
    
    rowid=tv2.identify_row(event.y)
    item=tv2.item(tv2.focus())
    c1=(item['values'][1])
    cbf=tk.Label(Attribute,text="Selected Column is {} -->".format(c1), font=('Times',20), fg="#228B22")
    cbf.pack()
    
    p.append(str(c1))
    x=len(p)

    
    
def histlabel():
    hl=tk.Label(file_frame,text="Please select one column for generating Histogram Plot",font=('Times',20), fg="#DC143C")
    hl.pack()
    hb = tk.Button(Attribute, text="Plot Graph",  command=histgrp, fg='black', bg='ghost white', font='bold')
    hb.pack(ipadx=50,side=RIGHT)

def histgrp():
    if df[p[0]].isnull().any():
        tk.messagebox.showinfo('Return','There is values missing in {} attrbute, please provide proper data'.format(c1))
    else:
        fig = Figure(figsize = (9.5, 4.5), dpi = 100)
        hg = fig.add_subplot(111)
        hg.hist(df[c1], bins = 50)
        hg.set_xlabel(c1)
        hg.set_ylabel("Y Label")
        hg.set_title("Hist Plot of {} ".format(c1))
        hg.grid(True)
        canvas = FigureCanvasTkAgg(fig,master = frame3)  
        canvas.draw()
  
        canvas.get_tk_widget().pack()
    
        toolbar = NavigationToolbar2Tk(canvas,frame3)
        toolbar.update()
  
        canvas.get_tk_widget().pack()
    
def boxlabel():
    bl=tk.Label(file_frame,text="Please select one column for generating Box Plot",font=('Times',20), fg="#DC143C")
    bl.pack()
    bb = tk.Button(Attribute, text="Plot Graph",  command=boxgrp, fg='black', bg='ghost white', font='bold')
    bb.pack(ipadx=50,side=RIGHT)
    
def boxgrp():
    if df[p[0]].isnull().any():
        tk.messagebox.showinfo('Return','There is values missing in {} attrbute, please provide proper data'.format(c1))
    else:
        fig = Figure(figsize = (9.5, 4.5), dpi = 100)
        boxg = fig.add_subplot(111)
        boxg.boxplot(df[c1])
        boxg.set_xlabel(c1)
        boxg.set_ylabel("Y Label")
        boxg.set_title("Box Plot of {} ".format(c1))
        boxg.grid(True)
        canvas = FigureCanvasTkAgg(fig,master = frame3)  
        canvas.draw()
  
        canvas.get_tk_widget().pack()
    
        toolbar = NavigationToolbar2Tk(canvas,frame3)
        toolbar.update()
  
        canvas.get_tk_widget().pack()
    
def scatterlabel():
    pl=tk.Label(file_frame,text="Please select two column for generating Scatter Plot",font=('Times',20), fg="#DC143C")
    pl.pack()
    pb = tk.Button(Attribute, text="Plot Graph",  command=scattergrp, fg='black', bg='ghost white', font='bold')
    pb.pack(ipadx=50,side=RIGHT)
    
def scattergrp():
    if df[p[0]].isnull().any():
        tk.messagebox.showinfo('Return','There is values missing in {} attrbute, please provide proper data'.format(p[0]))
    elif df[p[1]].isnull().any():
        tk.messagebox.showinfo('Return','there is values missing in {} attrbute, please provide proper data'.format(p[1]))
    else:
        fig = Figure(figsize = (9.5, 4.5), dpi = 100)
        pg = fig.add_subplot(111)
        pg.scatter(df[p[0]], df[p[1]])
        pg.set_xlabel(p[0])
        pg.set_ylabel(p[1])
        pg.set_title("Relation between {} and {}".format(p[0],p[1]))
        pg.grid(True)
        canvas = FigureCanvasTkAgg(fig,master = frame3)  
        canvas.draw()
  
        canvas.get_tk_widget().pack()
    
        toolbar = NavigationToolbar2Tk(canvas,frame3)
        toolbar.update()
  
        canvas.get_tk_widget().pack()
    
def plotlabel():
    pll=tk.Label(file_frame,text="Please select two column for Ploting graph",font=('Times',20), fg="#DC143C")
    pll.pack()
    pb = tk.Button(Attribute, text="Plot Graph",  command=plotgrp, fg='black', bg='ghost white', font='bold')
    pb.pack(ipadx=50,side=RIGHT)
    
def plotgrp():
    if df[p[0]].isnull().any():
        tk.messagebox.showinfo('Return','There is values missing in {} attrbute, please provide proper data'.format(p[0]))
    elif df[p[1]].isnull().any():
        tk.messagebox.showinfo('Return','there is values missing in {} attrbute, please provide proper data'.format(p[1]))
    else:
        fig = Figure(figsize = (9.5, 4.5), dpi = 100)
        plg = fig.add_subplot(111)
        plg.plot(df[p[0]], df[p[1]])   
        plg.set_xlabel(p[0])
        plg.set_ylabel(p[1])
        plg.set_title("Relation between {} and {}".format(p[0],p[1]))
        plg.grid(True)
        canvas = FigureCanvasTkAgg(fig,master = frame3)  
        canvas.draw()
  
        canvas.get_tk_widget().pack()
    
        toolbar = NavigationToolbar2Tk(canvas,frame3)
        toolbar.update()
  
        canvas.get_tk_widget().pack()
    
def barlabel():
    pll=tk.Label(file_frame,text="Please select two column for Bar graph",font=('Times',20), fg="#DC143C")
    pll.pack()
    pb = tk.Button(Attribute, text="Plot Graph",  command=bargrp, fg='black', bg='ghost white', font='bold')
    pb.pack(ipadx=50,side=RIGHT)
    
def bargrp():
    if df[p[0]].isnull().any():
        tk.messagebox.showinfo('Return','There is values missing in {} attrbute, please provide proper data'.format(p[0]))
    elif df[p[1]].isnull().any():
        tk.messagebox.showinfo('Return','there is values missing in {} attrbute, please provide proper data'.format(p[1]))
    else: 
        fig = Figure(figsize = (9.5, 4.5), dpi = 100)
        bag = fig.add_subplot(111)
        bag.bar(df[p[0]], df[p[1]])   
        bag.set_xlabel(p[0])
        bag.set_ylabel(p[1])
        bag.set_title("Relation between {} and {}".format(p[0],p[1]))
        canvas = FigureCanvasTkAgg(fig,master = frame3)  
        canvas.draw()
  
        canvas.get_tk_widget().pack()
    
        toolbar = NavigationToolbar2Tk(canvas,frame3)
        toolbar.update()
  
        canvas.get_tk_widget().pack()   
    
      

##Generating Menu

menubar = Menu(root)
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label="New", command = new)
file.add_command(label="Open", command=addFile) 
file.add_separator()
file.add_command(label="Exit", command=root.destroy)

view = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=view)
view.add_command(label="Data", command=ShowData)
view.add_command(label="Columns",command=showColumn) 


pg = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Plot Graph", menu=pg)
pg.add_command(label="Histogram", command=histlabel)
pg.add_command(label="Box Plot", command=boxlabel) 
pg.add_command(label="Scatter Plot", command=scatterlabel) 
pg.add_command(label="Graph Plot", command=plotlabel) 
pg.add_command(label="Bar Plot", command=barlabel) 
    

##Frames

SFP = tk.Label(root, text="----")
SFP.place(height=25, width=1000 )

frame1 = tk.LabelFrame(root, text="Data")
frame1.place(height=200, width=700,y=25)

frame2 = tk.LabelFrame(root, text="Columns")
frame2.place(height=200, width=300,x=700,y=25)

frame3 = tk.LabelFrame(root, text="Graph")
frame3.place(height=500, width=1000, y=250)

file_frame = tk.LabelFrame(root, text="Attributes required")
file_frame.place(height=50, width=1000, y=750, relx=0)

Attribute = tk.LabelFrame(root, text="Attribute")
Attribute.place(height=100, width=1000, y=800, relx=0)

## Treeview Widget
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1) 

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) 
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) 
treescrollx.pack(side="bottom", fill="x") 
treescrolly.pack(side="right", fill="y") 

tv2 = ttk.Treeview(frame2)
tv2.place(relheight=1, relwidth=1) 

treescrolly = tk.Scrollbar(frame2, orient="vertical", command=tv2.yview) 
treescrollx = tk.Scrollbar(frame2, orient="horizontal", command=tv2.xview) 
tv2.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) 
treescrollx.pack(side="bottom", fill="x") 
treescrolly.pack(side="right", fill="y") 



root.config(menu=menubar)
root.mainloop()


# In[ ]:




