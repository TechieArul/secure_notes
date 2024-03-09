from tkinter import *
from tkinter import messagebox as msg


#-------------------------------admin-----------------------------------------




passwordfile=open("userlogin.pass","r")
password=passwordfile.read()
passwordfile.close()

paswindow=Tk()
logo=PhotoImage(file="safe.png")
try:
    paswindow.iconphoto(False,logo)
except:pass
paswindow.title("Secure Notes")
paswindow["bg"]="gray60"
paswindow.geometry("780x296")

paswindow.resizable(False,False)

#passwindowmain
paswindowmain=Frame(paswindow,highlightbackground="blue",highlightthickness=3,bg="gray60")
paswindowmain.pack()

#header wel to secure notes
paswindowhead=Frame(paswindowmain,bg="gray60")
paswindowhead.pack()

#body buttons
paswindowbody=Frame(paswindowmain,bg="gray60")
paswindowbody.pack()

#about session
paswindowend=Frame(paswindowmain,bg="gray60")
paswindowend.pack()

#functions and login

#function for open notes
def openbutton():
    #destroy buttons
    opennote.destroy()
    resetpas.destroy()

    #check password function
    def checkpassword():
        enteredpassword=getpasswordentry.get()
        if password==enteredpassword:
            paswindow.destroy()
                        
            window=Tk()
            logo=PhotoImage(file="safe.png")
            window.resizable(False,False)
            try:
                window.iconphoto(False,logo)
            except:pass
            #main frame (both bottons and box)
            mainframe=Frame(window,highlightbackground="gray60",highlightthickness=5)
            mainframe.pack()
            window.title("Secure Notes")

            #head frame (buttons)
            head=Frame(mainframe)
            head.pack()

            #body frame (Description box)
            body=Frame(mainframe)
            body.pack()

            #Functions and algorithm------------------------------------------------------------------

            #function for clear changes button
            def clear_ascii():
                demo=Tk()
                try:
                    demo.iconphoto(False,logo)
                except:pass
            
                demo.title("Clear Changes")
                demo.resizable(False,False)

                def clearchangessubmit():
                    note.delete("1.0",END)
                    note.insert("1.0",tempfile)
                    demo.destroy()

                subtext=Label(demo,text="Are you sure to 'clear changes'" )
                subtext.pack()
                sub=Button(demo,text="Submit",command=clearchangessubmit)
                sub.pack(padx=100,pady=10)

                demo.mainloop()

            #function for unedit button
            def uneditbutton():
                unedit.config(state="disabled")
                edit.config(state="normal")
                note.config(state="disabled")

            #functon for edit button
            def editbutton():
                unedit.config(state="normal")
                edit.config(state="disabled")
                note.config(state="normal")

            #function for save button
            def savebutton():
                if noteformat=="ascii":
                    msg.showwarning("Format Error","You are in Ascii format")
                elif noteformat=="word":
                    #convert word to ascii
                    def savingfile():
                        #function for binary conversion
                        def binaryof(decimal):
                            a=bin(decimal)
                            return int(a[2:])
                        
                        notepad=note.get("1.0",END)#get words from discription
                        convertwordtoascii=[str(ord(i)) for i in notepad]#convert word to ascii (output in string)
                        convert2encode=[int(i)+1024 for i in convertwordtoascii]#add each number +24

                        #binary conversion
                        encode2binary=str([int(binaryof(i))+9234710427 for i in convert2encode])

                        removefirstbracket=encode2binary[1:]#remove first bracket
                        finalascii=removefirstbracket[:-1]#final binary in ("0101,01010,0101")

                        #Dumping into file
                        filename=open("encode.crypt","w")#open file
                        filename.write(finalascii)#write file
                        msg.showinfo("Successfull","Saved Successfull")
                        savewindow.destroy()

                    savewindow=Tk()
                    savewindow.title("Save The File")
                    savewindow.resizable(False,False)
                    try:
                        savewindow.iconphoto(False,logo)
                    except:pass
                    textsave=Label(savewindow,text="Are you sure to save this notes")
                    textsave.pack()
                    confrimsave=Button(savewindow,text="Save this notes",command=savingfile)
                    confrimsave.pack(padx=100,pady=10)
                    savewindow.mainloop()

            #function for convert to ascii button

            def converttoasciibutton():
                global noteformat
                if noteformat=="word":
                    #converting to ascii
                    noteformat="ascii"
                    note.config(state="normal")
                    connotepad=note.get("1.0",END)#get words from discription
                    conconvertwordtoascii=[str(ord(i)) for i in connotepad]#convert word to ascii (output in string)
                    conconvert2encode=str([int(i) for i in conconvertwordtoascii])#add each number +24
                    conremovefirstbracket=conconvert2encode[1:]#remove first bracket
                    confinalascii=conremovefirstbracket[:-1]#final ascii in ("65,65,65,65,54")
                    note.delete("1.0",END)
                    note.insert("1.0",confinalascii)
                    #config button
                    showascii.config(text="Show In Words")
                elif noteformat=="ascii":
                    noteformat="word"
                    #converting to word
                    note.config(state="normal")
                    wordb1=note.get("1.0",END)
                    try:
                        wordsp=wordb1.split(",")#split and convert string to list
                        #add=[chr(int(i)-24) for i in wordsp]#decode using -24
                        wordword=""
                        for i in wordsp:#convert list word to string
                            wordword=wordword+chr(int(i))#final word
                        note.delete("1.0",END)
                        note.insert("1.0",wordword)
                        
                        #config button
                        showascii.config(text="Show In Ascii")

                    except:pass


            #head frame buttons--------------------------------------------------------------------------

            #clearchanges
            clearchange=Button(head,text="Clear Changes",bg="gray59",font=("russo one",20),width=15,command=clear_ascii)
            clearchange.grid(column=0,row=0,pady=8)

            #unedit
            unedit=Button(head,text="Unedit",bg="gray59",font=("russo one",20),width=14,command=uneditbutton)
            unedit.grid(column=1,row=0)

            #edit
            edit=Button(head,text="Edit",bg="gray59",font=("russo one",20),width=14,command=editbutton)
            edit.grid(column=2,row=0)

            #save
            save=Button(head,text="Save",bg="gray59",font=("russo one",20),padx=60,width=5,command=savebutton)#width=10
            save.grid(column=3,row=0)

            #showascii
            showascii=Button(head,text="Show In Ascii",bg="gray59",font=("russo one",20),width=12,command=converttoasciibutton)
            showascii.grid(column=4,row=0)

            #body box---------------------------------------------------------------------

            #scrollbar
            yscrollbar=Scrollbar(body,orient=VERTICAL,width=25)
            xscrollbar=Scrollbar(body,orient=HORIZONTAL,width=25)

            #discription box
            note=Text(body,width=65,height=13,font=(None,25),bg="gray80",yscrollcommand=yscrollbar.set,xscrollcommand=xscrollbar.set,wrap="none",)

            yscrollbar.config(command=note.yview)
            xscrollbar.config(command=note.xview)

            yscrollbar.pack(side=RIGHT,fill=Y)
            xscrollbar.pack(side=BOTTOM,fill=X)

            note.pack()

            #botton functions

            
            a1=open("encode.crypt","r")#open ascii file
            b1=a1.read()#read ascii file

            try:

                def bin2dec(bin):
                        decimal,i=0,0
                        while bin!=0:
                            dec=bin%10
                            decimal=decimal+dec*pow(2,i)
                            bin=bin//10
                            i=i+1
                        return decimal

                #binary to decimal conversion
                binarynote=b1.split(",")#split and convert binary to list
                decimal=[]
                for i in binarynote:#convert list word to string
                    decimal.append(bin2dec((int(i)-9234710427)))#final word

                word=""
                for i in decimal:#convert list word to string
                    word=word+chr(int(i)-1024)#final word
                tempfile=word

                note.insert("1.0",word)
                uneditbutton()
            except:pass

            global noteformat
            noteformat="word"



            window.mainloop()
#-----------------------------------------------------------------------------------------------
        else:
            msg.showerror("Incorrect","Incorrect Password")

    #get password file
    

    #getpassword
    getpasswordtext=Label(paswindowbody,text="Enter the password : ",font=("russo one",28),bg="gray60",pady=25)
    getpasswordtext.grid(row=0,column=0,)

    getpasswordentry=Entry(paswindowbody,width=20,font=("russo one",20))
    getpasswordentry.grid(row=0,column=1)

    passwordsubmit=Button(paswindowbody,text="Submit",font=("russo one",20),command=checkpassword)
    passwordsubmit.grid(row=2,column=1)
    pass

#----------------------------------------------------------------------

#head
headprint=Label(paswindowhead,text="Welcome to Secure Notes",font=("lemon",30),width=30,bg="white",)
headprint.pack()

#--------------------------------------------------------------------------

#buttons

#function for reset button
def resetbutton():
    #destroy button
    opennote.destroy()
    resetpas.destroy()

    #get old password
    oldpasswordtext=Label(paswindowbody,text="Enter old password : ",font=("russo one",28),bg="gray60",pady=25)
    oldpasswordtext.grid(row=0,column=0,)

    getoldpasswordentry=Entry(paswindowbody,width=20,font=("russo one",20))
    getoldpasswordentry.grid(row=0,column=1)

    #checkoldpassword
    def checkoldpassword():
        if getoldpasswordentry.get()==password:
            #destroy button
            oldpasswordtext.destroy()
            getoldpasswordentry.destroy()
            oldpasswordsubmit.destroy()

            newpasswordtext=Label(paswindowbody,text="Enter new password : ",font=("russo one",28),bg="gray60",pady=25)
            newpasswordtext.grid(row=0,column=0,)

            newpasswordentry=Entry(paswindowbody,width=20,font=("russo one",20))
            newpasswordentry.grid(row=0,column=1)
            
            #function for change password button
            def changepassword():
                passwordfile=open("userlogin.pass","w")
                passwordfile.write(newpasswordentry.get())
                msg.showinfo("Successful",f"Your new pasword is '{newpasswordentry.get()}'\n\nPassword changed successfully")
                paswindow.destroy()
                exit()

                


            newpasswordsubmit=Button(paswindowbody,text="Change",font=("russo one",20),command=changepassword)
            newpasswordsubmit.grid(row=2,column=1)
            

            
        else:
            msg.showerror("Incorrect","Incorrect old password")

    oldpasswordsubmit=Button(paswindowbody,text="Submit",font=("russo one",20),command=checkoldpassword)
    oldpasswordsubmit.grid(row=2,column=1)
    
    pass

opennote=Button(paswindowbody,text="Open Notes",font=("russo one",30),width=14,height=1,command=openbutton)
opennote.grid(row=1,column=0,pady=35)

resetpas=Button(paswindowbody,text="Change password",font=("russo one",30),width=15,height=1,command=resetbutton)
resetpas.grid(row=1,column=1,pady=10,padx=1)

#---------------------------------------------------------------------------

#about session

space=Label(paswindowend,bg="gray60")#space
space.pack(pady=10)

about=Label(paswindowend,text="Developed By Arul Selvam [Intelligent Softwares]",font=("times new roman",20),fg="blue",width=57,bg="white",)
about.pack()



paswindow.mainloop()





#-------------------------------admin-----------------------------------------