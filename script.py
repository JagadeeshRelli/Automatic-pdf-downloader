#for user interaction
import tkinter as tk
from tkinter import *
#for searching the topic in google
from googlesearch import search as sch
#for parsing the urls
from urllib.parse import urlparse 
import urllib.request as ureq
import os

import ssl
#to display the message box after completion of downloading
from tkinter import messagebox
#to pass the unverified certification errors
ssl._create_default_https_context = ssl._create_unverified_context

#creation of main window
mainn=tk.Tk()
mainn.title('AUTOMATIC PDF DOWNLOADER')
mainn.geometry('400x400')
#utility function to search and downlaod pdf files
def searchndownload():
    #to take the input from text box
    inp=txt.get('1.0','end-1c')
    qry=inp+"pdf free download"
    #searching and storing urls in a list
    ll=list(sch(qry,num_results=20))
    print(ll)
    j=1
    k=0
    for i in ll:
        path=urlparse(i).path
        ext=os.path.splitext(path)[1]     
        #checking whether the url is related to pdf or not
        if(ext==".pdf"):
            try:
                #downloading pdf files
                k+=1
                respo=ureq.urlopen(i)
                file=open(str(j)+inp+".pdf",'wb')
                file.write(respo.read())
                file.close()
                j+=1
            except:
                pass
    #displaying the process completion message
    messagebox.showinfo("completed","found "+str(k)+" files, downloading completed")

#creating a text box to take input from the user
txt=tk.Text(mainn,height=3)
txt.insert(INSERT,"insert topic names here")
#button to inintiate the process
btn=tk.Button(mainn,text="search and download pdf",command=searchndownload)
#packing the widgets and main window
txt.pack()
btn.pack()

mainn.mainloop()


