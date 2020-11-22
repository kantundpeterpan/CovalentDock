#!/usr/bin/python

import Tkinter
import tkFileDialog
from Tkinter import *
from tkFileDialog import askopenfilename

root = Tk()

root.title("CDGUI")

root.grid()

#event of main button
def OnButtonClick():
   
    #get the inputs and move them to the new folder
    import os
    homedir = os.getcwd()    
    os.system("mkdir "+root.entry.get())
    newmol2name = homedir+"/"+root.entry.get()+"/"+root.entry.get()+"_ligand.mol2"
    #print(newmol2name)
    newpdbname = homedir+"/"+root.entry.get()+"/"+root.entry.get()+"_receptor.pdb"
    newcenter = homedir+"/"+root.entry.get()+"/"+"center"
    os.rename(mol2name,newmol2name)
    os.rename(pdbname,newpdbname)
    os.rename(center,newcenter)
    
    filename = os.environ.get('PYTHONSTARTUP')
    if filename and os.path.isfile(filename):
        execfile(filename)
    #print(filename)
    
   
    os.chdir(homedir+"/"+root.entry.get())
    os.system("mkdir prep")
    os.chdir(homedir+"/"+root.entry.get()+"/prep")
    os.system("cp "+homedir+"/script/* .")
    os.chdir(homedir+"/"+root.entry.get())
    os.system(homedir+"/preprocessing "+root.entry.get())
    os.chdir(homedir+"/"+root.entry.get()+"/bond")
    print("Now runing covalentGrid,please wait...")
    os.system("for name in $(ls *.gpf); do "+homedir+"/covalentGrid < ${name} >${name}.glg; done")
    print("Now runing covalentDock,please wait...")
    os.system("for name in $(ls *.dpf); do "+homedir+"/covalentDock -p ${name}; done")
    print("Job finished!")
   
#def entry
est = StringVar()
root.entry = Entry(root,textvariable=est)
root.entry.grid(column=0,row=0,sticky='EW')
root.entry.bind("<Return>", OnButtonClick)
est.set("defaulttaskname")

   

    
#def main button
button = Button(root,text=u"Run!",
                                command=OnButtonClick)
button.grid(column=1,row=0)

#def lable1
root.label1Variable = StringVar()
label1 = Label(root,textvariable=root.label1Variable,
                              anchor="w",fg="black",bg="white")
label1.grid(column=0,row=1,sticky='EW')

#event of button 1
def OnButton1Click():
        from tkFileDialog import askopenfilename

        global pdbname
        pdbname = askopenfilename()
        root.label1Variable.set(pdbname)

#def button 1
button1 = Button(root,text=u"choose your receptor here!",
                                 command=OnButton1Click)
button1.grid(column=1,row=1)

#def label2
root.label2Variable = StringVar()
label2 = Label(root,textvariable=root.label2Variable,
                              anchor="w",fg="black",bg="white")
label2.grid(column=0,row=2,sticky='EW')

#event button 2
def OnButton2Click():
        from tkFileDialog import askopenfilename

        global mol2name
        mol2name = askopenfilename()
        root.label2Variable.set(mol2name)

#def button2
button2 = Button(root,text=u"choose your ligand here!",
                                 command=OnButton2Click)
button2.grid(column=1,row=2)

#def label 3
root.label3Variable = StringVar()
label3 = Label(root,textvariable=root.label3Variable,
                              anchor="w",fg="black",bg="white")
label3.grid(column=0,row=3,sticky='EW')

#event button 3
def OnButton3Click():
        from tkFileDialog import askopenfilename

        global center
        center = askopenfilename()
        root.label3Variable.set(center)

#def button 3
button3 = Button(root,text=u"choose your center file here!",
                                 command=OnButton3Click)
button3.grid(column=1,row=3)

root.grid_columnconfigure(0,weight=1)
root.resizable(True,False)


root.mainloop()
