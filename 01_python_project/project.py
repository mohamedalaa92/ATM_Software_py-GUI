#########################################################
#########################################################
##########   Author: Mohamed Alaa Eldehimy    ###########
##########   SWC: Python_GUI                  ###########
##########   VER: 1.00                        ###########
#########################################################
#########################################################

import tkinter
import tkinter.messagebox as msgbox
main_window = tkinter.Tk()

#************************************* data base ********************************************#
#      	|user_name| |password|    |name|                   |balance|
id = {	215321701332 : [1783 , "Ahmed Abdelrazek Mohamed", 3500166 ],
		203659302214 : [1390 , "Salma Mohamed Foaad",      520001  ],
		126355700193 : [1214 , "Adel Khaled Abdelrahman",  111000  ],
		201455998011 : [2001 , "Saeed Amin Elsawy",        1200    ],
		201122369851 : [8935 , "Amir Salama Elgendy",      178933  ],
		201356788002 : [3420 , "Wael Mohamed khairy",      55000   ],
		203366789564 : [1179 , "Mina Sameh Bishoy",        18000   ],
		201236787812 : [1430 , "Omnia Ahmed Awad",         180350  ],
}
blocked = list()
global a
a=0
global b
b=0
#*********************************************************************************************#
def back():
	chang_p.withdraw()
	cash_w.withdraw()
	users_mode.withdraw()
	main_window.deiconify()
	username_entry.delete(0,'end')
	pass_entry.delete(0,'end')
	chpass_entry.delete(0,'end')
	chpass_entry2.delete(0,'end')


def user_mode():
	fawry_c.withdraw()
	chang_p.withdraw()
	balance_i.withdraw()
	cash_w.withdraw()
	main_window.withdraw()
	cash_entry.delete(0,'end')
	users_mode.deiconify()

def cash_withdraw():
	users_mode.withdraw()
	cash_w.deiconify()
	
def balance_cash():
	users_mode.withdraw()
	balance_i.deiconify()
	balance_b()

def chang_password():
	users_mode.withdraw()
	chang_p.deiconify()
	
def fawry():
	fawry_w.withdraw()
	users_mode.withdraw()
	facash_entry.delete(0,'end')
	facashnum_entry.delete(0,'end')
	fawry_c.deiconify()
	
def fawry_window():
	fawry_c.withdraw()
	fawry_w.deiconify()
	

	

################################################### fawry window ##############################################################################
fawry_w = tkinter.Tk()
fawry_w.withdraw()
fawry_w.title("Fawry window")
fawry_w.geometry("1000x600+150+50")
fawry_w.resizable(False,False)
fawry_w.configure(background = "gray")
topline1 = tkinter.Label(fawry_w, width = 1000, height = 10,bg = "#303030").place(x=0,y=0)
toptitle1 = tkinter.Label(fawry_w,text = "Alaa bank",font=("Arial",50), bg = "#303030").place(relx=0.35,rely=0.1)	


def fawry_withdraw_c():
	global fa
	global fawry_cash_a

	if (int(facashnum_entry.get()) < 999999999 ):
		msgbox.showwarning("warning","warning, the number should consist of 11 numbers ")
	else:
	
		if(id[ int(username_entry.get()) ][2] < int(facash_entry.get()) ):
			msgbox.showwarning("warning","warning, you dont have much balance inquiry ")
		else:
			if(int(facash_entry.get()) >= 10 ):
				conf = msgbox.askquestion("confirmation","Confirm the operation? ")
				if conf == "yes":
					id[int(username_entry.get())][2] -= int(facash_entry.get())
					fa = id[int(username_entry.get())][2]
					fawry_cash_a = tkinter.Label(fawry_w,text="your balance is %s $"%fa,font=("Arial",16) ,bg="gray").place(relx=0.39,rely=0.35)
				else:
					pass
			else:
				msgbox.showwarning("warning","you should enter more than 10 ")
	
def fawry_cancel():
	fawry_cash_a = tkinter.Label(fawry_w,text="                                                   ",font=("Arial",16) ,bg="gray").place(relx=0.39,rely=0.35)
	fawry()
facashnum_label = tkinter.Label(fawry_w,text="Enter The number :",font=("Arial",16) ,bg="gray").place(relx=0.1,rely=0.4)
facashnum_entry  = tkinter.Entry(fawry_w,width =25,font=("Arial",16))
facashnum_entry.place(relx=0.38,rely=0.4)
	
facash_label = tkinter.Label(fawry_w,text="The amount required :",font=("Arial",16) ,bg="gray").place(relx=0.1,rely=0.55)
fawry_cash_a = tkinter.Label(fawry_w,text="",font=("Arial",16) ,bg="gray").place(relx=0.39,rely=0.35)
facash_entry  = tkinter.Entry(fawry_w,width =25,font=("Arial",16))
facash_entry.place(relx=0.38,rely=0.55)

enter_cashBtn   = tkinter.Button(fawry_w,text = "Enter",font=("Arial",10),width = 10,command = fawry_withdraw_c).place(relx=0.6,rely=0.7)
cancel_cashBtn  = tkinter.Button(fawry_w,text = "cancel",font=("Arial",10),width = 10,command = fawry_cancel).place(relx=0.7,rely=0.7)

fawry_w.withdraw()


#################################################### fawry.. ##################################################################################
fawry_c = tkinter.Tk()
fawry_c.withdraw()
fawry_c.title("Fawry ")
fawry_c.geometry("1000x600+150+50")
fawry_c.resizable(False,False)
fawry_c.configure(background = "gray")
topline1 = tkinter.Label(fawry_c, width = 1000, height = 10,bg = "#303030").place(x=0,y=0)
toptitle1 = tkinter.Label(fawry_c,text = "Alaa bank",font=("Arial",50), bg = "#303030").place(relx=0.35,rely=0.1)	


voda_Btn   = tkinter.Button(fawry_c,text = "Vodafone",font=("Arial",25),width = 20,command = fawry_window)
voda_Btn.place(relx=0.1,rely=0.4)

etisalat_Btn= tkinter.Button(fawry_c,text = "Etisalat",font=("Arial",25),width = 20,command = fawry_window)
etisalat_Btn.place(relx=0.1,rely=0.55)

exit_f= tkinter.Button(fawry_c,text = "Exit",font=("Arial",25),width = 20,command = user_mode)
exit_f.place(relx=0.1,rely=0.7)	

we_Btn   = tkinter.Button(fawry_c,text = "We",font=("Arial",25),width = 20,command = fawry_window)
we_Btn.place(relx=0.52,rely=0.4)

orang_Btn= tkinter.Button(fawry_c,text = "Orange",font=("Arial",25),width = 20, command = fawry_window)
orang_Btn.place(relx=0.52,rely=0.55)

fawry_c.withdraw()

##################################################### change password ########################################################################
chang_p = tkinter.Tk()
chang_p.withdraw()
chang_p.title("change password")
chang_p.geometry("1000x600+150+50")
chang_p.resizable(False,False)
chang_p.configure(background = "gray")
topline1 = tkinter.Label(chang_p, width = 1000, height = 10,bg = "#303030").place(x=0,y=0)
toptitle1 = tkinter.Label(chang_p,text = "Alaa bank",font=("Arial",50), bg = "#303030").place(relx=0.35,rely=0.1)


def changpass():
	global r
	global change_s
	if  (int(chpass_entry.get())) == (int(chpass_entry2.get())):
		if(id[int(username_entry.get())][0] != int(chpass_entry.get()) ):
			yesnoq = msgbox.askquestion("confirmation","Confirm the operation? ")
			if yesnoq == "yes":
				id[int(username_entry.get())][0] = int(chpass_entry.get())
				msgbox.showinfo(" ","done,bassword changed")
				back()
			else:
				pass
	
		else:
			msgbox.showwarning("warning","its the same old password ")
	else:
		msgbox.showwarning("warning","you entered two different password ")



chpass_label = tkinter.Label(chang_p,text="The New password :",font=("Arial",16) ,bg="gray").place(relx=0.1,rely=0.4)
chpass_entry  = tkinter.Entry(chang_p,width =25,font=("Arial",16))
chpass_entry.place(relx=0.38,rely=0.4)

chpass_labe2 = tkinter.Label(chang_p,text="The New password again:",font=("Arial",16) ,bg="gray").place(relx=0.1,rely=0.5)
chpass_entry2  = tkinter.Entry(chang_p,width =25,font=("Arial",16))
chpass_entry2.place(relx=0.38,rely=0.5)

enter_chpassBtn   = tkinter.Button(chang_p,text = "Enter",font=("Arial",10),width = 10,command = changpass).place(relx=0.6,rely=0.7)
cancel_chpassBtn  = tkinter.Button(chang_p,text = "cancel",font=("Arial",10),width = 10,command = user_mode).place(relx=0.7,rely=0.7)
chang_p.withdraw()

##################################################### balance inquiry ########################################################################
balance_i = tkinter.Tk()
balance_i.withdraw()
balance_i.title("cash withdraw")
balance_i.geometry("1000x600+150+50")
balance_i.resizable(False,False)
balance_i.configure(background = "gray")
topline1 = tkinter.Label(balance_i, width = 1000, height = 10,bg = "#303030").place(x=0,y=0)
toptitle1 = tkinter.Label(balance_i,text = "Alaa bank",font=("Arial",50), bg = "#303030").place(relx=0.35,rely=0.1)

def balance_b():
	global b
	global blnc
	b = id[int(username_entry.get())][2]
	blnc = tkinter.Label(balance_i,text="your balance is %s $"%b,font=("Arial",16) ,bg="gray").place(relx=0.38,rely=0.4)


cancel_cashBtn  = tkinter.Button(balance_i,text = "cancel",font=("Arial",10),width = 10,command = user_mode).place(relx=0.7,rely=0.7)
			
balance_i.withdraw()

##################################################### cash withdraw ##########################################################################
cash_w = tkinter.Tk()
cash_w.withdraw()
cash_w.title("cash withdraw")
cash_w.geometry("1000x600+150+50")
cash_w.resizable(False,False)
cash_w.configure(background = "gray")
topline1 = tkinter.Label(cash_w, width = 1000, height = 10,bg = "#303030").place(x=0,y=0)
toptitle1 = tkinter.Label(cash_w,text = "Alaa bank",font=("Arial",50), bg = "#303030").place(relx=0.35,rely=0.1)



##################################################### cash buttom #############################################################################
def withdraw_c():
	global a
	global cash_a
	if(id[ int(username_entry.get()) ][2] < int(cash_entry.get()) ):
		msgbox.showwarning("warning","warning, you dont have much balance inquiry ")
	else:
		if(int(cash_entry.get()) < 5000 ):
			if((int(cash_entry.get())%100)== 0):
				conf = msgbox.askquestion("confirmation","Confirm the operation? ")
				if conf == "yes":
					id[int(username_entry.get())][2] -= int(cash_entry.get())
					a = id[int(username_entry.get())][2]
					#cash_a.place_forget(relx=0.39,rely=0.35)
					cash_a = tkinter.Label(cash_w,text="your balance is %s $"%a,font=("Arial",16) ,bg="gray").place(relx=0.39,rely=0.35)
				else:
					pass
			else:
				msgbox.showwarning("warning","blease your amount should be multible of 100 ")
		else:
			msgbox.showwarning("warning","the maximum amount that you can withdraw is 5000 ")
def screen_clear():
	cash_a = tkinter.Label(cash_w,text="                                                           ",font=("Arial",16) ,bg="gray").place(relx=0.39,rely=0.35)
	user_mode()

cash_label = tkinter.Label(cash_w,text="The amount required :",font=("Arial",16) ,bg="gray").place(relx=0.1,rely=0.4)
cash_a = tkinter.Label(cash_w,text="",font=("Arial",16) ,bg="gray").place(relx=0.39,rely=0.35)
cash_entry  = tkinter.Entry(cash_w,width =25,font=("Arial",16))
cash_entry.place(relx=0.38,rely=0.4)

enter_cashBtn   = tkinter.Button(cash_w,text = "Enter",font=("Arial",10),width = 10,command = withdraw_c).place(relx=0.6,rely=0.7)
cancel_cashBtn  = tkinter.Button(cash_w,text = "cancel",font=("Arial",10),width = 10,command = screen_clear).place(relx=0.7,rely=0.7)
cash_w.withdraw()

	
##################################################### basic frame #############################################################################
users_mode = tkinter.Tk()
users_mode.withdraw()
users_mode.title("user mode")
users_mode.geometry("1000x600+150+50")
users_mode.resizable(False,False)
users_mode.configure(background = "gray")
topline = tkinter.Label(users_mode, width = 1000, height = 10,bg = "#303030").place(x=0,y=0)
toptitle = tkinter.Label(users_mode,text = "Alaa bank",font=("Arial",50), bg = "#303030").place(relx=0.35,rely=0.1)


############################################################## user mode buttom #################################################################	
cash_Btn   = tkinter.Button(users_mode,text = "Cash Withdraw",font=("Arial",25),width = 20,command = cash_withdraw)
cash_Btn.place(relx=0.1,rely=0.4)

changepass_Btn= tkinter.Button(users_mode,text = "Password Change",font=("Arial",25),width = 20,command = chang_password)
changepass_Btn.place(relx=0.1,rely=0.55)

exit_Btn= tkinter.Button(users_mode,text = "Exit",font=("Arial",25),width = 20,command = back)
exit_Btn.place(relx=0.1,rely=0.7)	

Balance_Btn   = tkinter.Button(users_mode,text = "Balance Inquiry",font=("Arial",25),width = 20,command = balance_cash)
Balance_Btn.place(relx=0.52,rely=0.4)

fawry_Btn= tkinter.Button(users_mode,text = "Fawry Service",font=("Arial",25),width = 20, command = fawry)
fawry_Btn.place(relx=0.52,rely=0.55)

users_mode.withdraw()
#********************************************************************************************************************#
	


#************************************ check pass & id ****************************************#		
passowrd_counter = 3
def checkidpass():
	global passowrd_counter
	if(int(username_entry.get()) not in blocked):
		if(int(username_entry.get()) in id):
			print("pass user name")
			if int(pass_entry.get()) == id[int(username_entry.get())][0]:
				print("pass passowrd")
				passowrd_counter = 3
				t = "                                                                 "
				password_t = tkinter.Label(main_window,text = t, bg = "gray").place(relx=0.38,rely=0.58)
				user_mode()
			else:
				global enter_Btn
				passowrd_counter -=1
				t = "you have "+str(passowrd_counter)+" more tries.."
				if (passowrd_counter ==0 ):
					msgbox.showerror("Blocked","you are blocked")
					passowrd_counter=3
					t = "                                                                "
					blocked.append(int(username_entry.get() ))
					
				password_t = tkinter.Label(main_window,text = t, bg = "gray").place(relx=0.38,rely=0.58)
				#enter_Btn.place_forget(relx=0.6,rely=0.7)
				enter_Btn = tkinter.Button(main_window,text = "Enter",font=("Arial",10),width = 10,command = checkidpass)
				enter_Btn.place(relx=0.6,rely=0.7)
	
					
				
			
		else:
			msgbox.showwarning("warning","warning, the ID is not exist.")
	else:
		msgbox.showerror("Blocked","you are blocked, call technical support")
	
			

#*********************************************************************************************#

#************************************** main window *****************************************#
main_window.title("main")
main_window.geometry("1000x600+150+50")
main_window.resizable(False,False)
main_window.configure(background = "gray")

topline = tkinter.Label(main_window, width = 1000, height = 10,bg = "#303030").place(x=0,y=0)
toptitle = tkinter.Label(main_window,text = "Alaa bank",font=("Arial",50), bg = "#303030").place(relx=0.35,rely=0.1)
##iti photo##
photo_iti = tkinter.PhotoImage(file="iti.png")
photo_iti=photo_iti.subsample(2,2)
bicture = tkinter.Label(main_window, image=photo_iti, width = 200, height = 200,bg = "#303030")
bicture.photo = photo_iti
bicture.place(relx=-0.05,rely=-0.09)

botomline = tkinter.Label(main_window, width = 1000, height = 1).place(relx=0,rely=0.92)
##bank logo##
photo_atm = tkinter.PhotoImage(file="atmlogo.png")
photo_atm=photo_atm.subsample(4,4)
bicatm = tkinter.Label(main_window, image=photo_atm, width = 400, height = 10)
bicatm.photo = photo_atm
bicatm.place(relx=-0.1,rely=0.925)


##button & entry & label >>> in main frame##
enter_Btn   = tkinter.Button(main_window,text = "Enter",font=("Arial",10),width = 10,command = checkidpass).place(relx=0.6,rely=0.7)
cancel_Btn  = tkinter.Button(main_window,text = "cancel",font=("Arial",10),width = 10,command = exit).place(relx=0.7,rely=0.7)

user_name_label = tkinter.Label(main_window,text="Account Number (ID) :",font=("Arial",16) ,bg="gray").place(relx=0.1,rely=0.4)
pass_label      = tkinter.Label(main_window,text="Password :",           font=("Arial",16) ,bg="gray").place(relx=0.1,rely=0.48)
	
username_entry  = tkinter.Entry(main_window,width =25,font=("Arial",16))
username_entry.place(relx=0.38,rely=0.4)
pass_entry = tkinter.Entry(main_window,width =25,font=("Arial",16),show = '*')
pass_entry .place(relx=0.38,rely=0.48)


main_window.mainloop()
#*********************************************************************************************#
