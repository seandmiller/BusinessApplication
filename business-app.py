from tkinter import *
import yfinance as yf
from PIL import Image,ImageTk
import requests
from tools import stk_img,comma, discounted_cashf,investment,stck_db,figures


window=Tk()
window.configure(bg="#E6E6FA")

text_c="green"
lab_c="#E6E6FA"


def btn_pres(arg):

	data=int(arg)	
# INVESMENT CALCULATOR
	if data==2:

	  for x in window.winfo_children():
	  
	  	x.destroy()
	  labl=Label(text="Investment Calculator",padx=15,borderwidth=3,fg="green")
	
	  labl.grid(row=0,column=0)
	  def ans(answer):
		  if int(yr.get())==1:
		  	yer="year"
		  else:
		    yer="years"	
	
		  label.config(text=f"After {yr.get()} {yer} your invesment of\n {comma(principal.get())}\n turned into {answer}")

		
	  text_c="green"
	  lab_c="#E6E6FA"

	  label=Label(window,text="Answer will appear here",fg="green",padx=30,pady=20,bg=lab_c)
	  label.grid(row=10,column=1,columnspan=3)
	  
	  
	  en_padx=5
	  en_pady=30
	  window.title("Invesment")
	  
	  lab_prin=Label(window,text="  Enter the starting principal  ",padx=en_padx,pady=en_pady,fg=text_c,bg=lab_c)
	  principal=Entry(window, borderwidth=3,fg=text_c)
	  lab_perc=Label(window,text="  Enter the percentange  ",padx=en_padx,pady=en_pady,fg=text_c,bg=lab_c)
	  perc=Entry(window,borderwidth=3,fg=text_c)
	  lab_yr=Label(window,text="  Enter the time  ",padx=en_padx,pady=en_pady,fg=text_c,bg=lab_c)
	  yr=Entry(window,borderwidth=3,fg=text_c)
	  lab_contr=Label(window,text="  Enter the contribution  ",padx=en_padx,pady=en_pady,fg=text_c,bg=lab_c)
	  contr=Entry(window,borderwidth=3,fg=text_c)
	  contr.insert(0,0)
# space
	  spac=Label(window,text="    ",pady=10,bg=lab_c)
	  lab_prin.grid(row=2,column=0)
	  principal.grid(row=3,column=0)
	  lab_perc.grid(row=2,column=1)
	  perc.grid(row=3,column=1)
	  lab_yr.grid(row=4,column=0)
	  yr.grid(row=5,column=0)
	  lab_contr.grid(row=4,column=1)
	  contr.grid(row=5,column=1)
	  btn=Button(window,text="Click for Result",padx=25,pady=15,fg=text_c,command=lambda: ans(investment(principal.get(), perc.get() ,yr.get(), contr.get() )))
	  spac.grid(row=8,column=0)
	  btn.grid(row=10,column=0)
	  
	  btn_tick=Button(text='Stock Ticker',borderwidth=3,fg="green",padx=15,bg=lab_c,command=lambda: btn_pres(3))
	  btn_tick.grid(row=0,column=2)
	  btn_dcf=Button(window,text="Discounted Cash Flow",borderwidth=3,fg='green',padx=15,bg=lab_c,command=lambda: btn_pres(1))
	  btn_dcf.grid(row=0,column=1)
	  window.mainloop()
# discounted cashflow 	
	elif data==1:
		for x in window.winfo_children():
			x.destroy()
		
		def ans(answer):
		  if int(time.get())==1 or int(time.get())==0:
		  	yer="year"
		  else:
		    yer="years"	
		  label.config(text=f"{comma(expected_cf.get())} {time.get()} {yer} out is worth\n {answer} today,\n w/ {perce.get()}% interest on capital")
		

		lab_c="#E6E6FA"
		labl=Label(text="Discounted Cashflow",padx=30,borderwidth=3,fg="green")
		labl.grid(row=0,column=0,columnspan=3)
		
		lab_exp=Label(window,text="Enter the expected Cashflow",fg="green",padx=30,bg=lab_c,pady=10)

		expected_cf=Entry(window,borderwidth=3,fg="green")
		lab_time=Label(window,text="Enter The amount of time",fg="green",padx=30,bg=lab_c,pady=10)

		time=Entry(window,borderwidth=3,fg="green")
		lab_perce=Label(window,text="Enter the interest rate",fg="green",padx=30,bg=lab_c,pady=10)

		perce=Entry(window,borderwidth=3,fg="green")
		lab_exp.grid(row=2,column=0)
		lab_time.grid(row=4,column=0)
		lab_perce.grid(row=6,column=0)
    # grid for entry

		expected_cf.grid(row=3,column=0)
		time.grid(row=5,column=0)
		perce.grid(row=7,column=0)

		btn_ticker=Button(borderwidth=3,fg="green",text='Stock Ticker',bg=lab_c,command=lambda: btn_pres(3))
		btn_ticker.grid(row=0,column=3)
		#btn spacer
		btn_s=Label(window,text=' ',pady=1,bg=lab_c)
		btn_s.grid(row=1,column=3)


		btn_inv=Button(window,text="Investment\nCalculator",bg=lab_c,fg='green',borderwidth=3,command=lambda: btn_pres(2))
		btn_inv.grid(row=2,column=3)
		label=Label(text="Answer will appear here",padx=25,pady=25,fg="green",bg=lab_c)
		result_btn=Button(window,text="Click for Results", padx=40,pady=15,fg="green",command=lambda: ans(comma(discounted_cashf(int(expected_cf.get()),float(perce.get()),int(time.get()) ))))
		spac=Label(text="   ",pady=20,bg=lab_c)
		spac.grid(row=10)
		label.grid(row=11,column=0,columnspan=2)
		result_btn.grid(row=12,column=0)
# stock tickers 	
	elif data==3:
	    def stck(ticker):
	      stk_img(ticker)
	      img=ImageTk.PhotoImage(Image.open('stockimg.png'))
	      
	      imags=Label(root,bg=lab_c)
	      try:
	      	stock=yf.Ticker(ticker)
	      	price=stock.info['regularMarketPrice']

	      	shares_outstanding=stock.info['sharesOutstanding']
	      	dividend=stock.info['dividendYield']
	      	market_cap=stock.info['marketCap']
	      	comp_name=stock.info['longName']


	      	stck_db.add(ticker)
	      	data=open('log.txt','r')
	      	data_=''
	      	for x in data:
	      		data_+=x
	      	data.close()
	      	current_dta=data_.split()
	      	stock1=yf.Ticker(current_dta[-1])
	      	stock2=yf.Ticker(current_dta[-2])
	      	stock3=yf.Ticker(current_dta[-3])
	      	stock4=yf.Ticker(current_dta[-4])

	      	first_stock.config(text=stock1.info['longName'],command=lambda: stck(current_dta[-1]))
	      	sec_stock.config(text=current_dta[-2])
	      	third_stock.config(text=current_dta[-3])
	      	fourth_stock.config(text=current_dta[-4])

	      	if current_dta[-2]!='NONE':
	      		sec_stock.config(command=lambda: stck(current_dta[-2]),text=stock2.info['longName'])
	      	if current_dta[-3]!='NONE':
	      		third_stock.config(command=lambda: stck(current_dta[-3]),text=stock3.info['longName'])
	      	if current_dta[-4]!='NONE':
	      		fourth_stock.config(command=lambda: stck(current_dta[-4]),text=stock4.info['longName'])
	      		


	      	lbel.config(text=f'current price of this stock is {price}$')
	      	
	      	market_CP.config(text=f"The Market Cap\n for this company is\n{figures(comma(market_cap))}")
	   
	      	company_name.config(text=f"{comp_name}")

	      	company_name.grid(row=3,column=3)
	      	company_div.config(text=f"Dividend: {dividend}")

	      	market_CP.grid(row=5,column=3)
	      	company_div.grid(row=7,column=3)


	      	imags.config(image=img) 
	      	lbel.grid(row=13,column=0,columnspan=3)
	      	imags.grid(row=5,column=0,columnspan=3)
	      	lbel_E.config(text='  stock found ✔ ',fg='white',bg='green',padx=20)
	      	lbel_E.grid(row=1,column=3)

	      	root.grid(row=12,column=0,columnspan=4)

	      except KeyError:
	      	lbel_E.config(text=f'{ticker} not found ✘',bg='red')
	      	lbel.config(text=f'',bg=lab_c)
	      	
	      	market_CP.config(text="",bg=lab_c)
	   
	      	company_name.config(text="",bg=lab_c)

	      	company_name.grid(row=3,column=3)
	      	company_div.config(text=f"",bg=lab_c)

	      	market_CP.grid(row=5,column=3)
	      	company_div.grid(row=7,column=3)
	      	lbel_E.grid(row=1,column=0)
	      	lbel.grid(row=13,column=0,columnspan=3)
	      	root.grid(row=12,column=0,columnspan=4)
	      window.mainloop()

	  # outside the function     


	    bg_stck='#9ADFB7'
	    text_c="green"
	    lab_c="#E6E6FA"
	    for x in window.winfo_children():
	        x.destroy()
	    root=Frame(window,bg=lab_c)
	    btnpadx=20
	    

	    
	    
	    updated_data=""
	    data=open('log.txt','r')

	    for x in data:
	    	updated_data += x
	    data.close()
	    updated_data=updated_data.split()


	    lbel=Label(root,text=f'',fg='green',bg=lab_c,padx=30)
	    first_stock=Button(window,text=f"{updated_data[-1]}",fg='green',bg=lab_c,borderwidth=0)
	    sec_stock=Button(window,text=f"{updated_data[-2]}",fg='green',bg=lab_c,borderwidth=0)
	    third_stock=Button(window,text=f"{updated_data[-3]}",fg='green',bg=lab_c,borderwidth=0)
	    fourth_stock=Button(window,text=f"{updated_data[-4]}",fg='green',bg=lab_c,borderwidth=0)

	    market_CP=Label(root,fg='green',bg= lab_c)
	    company_name=Label(root,bg='lightblue',fg='green')
	    company_div=Label(root,fg='green')
	    


	    btn_inv=Button(window,borderwidth=3,text='Investment Calculator',fg='green',bg=lab_c,command=lambda: btn_pres(2))
	    btn_dcf=Button(window,borderwidth=3,text='Discounted Cashflow',bg=lab_c,fg="green",command=lambda: btn_pres(1))
	    stocks_lab=Label(window,text="Enter The stock you would like to see",fg="green",bg=lab_c)
	    stocks_choice=Entry(window,borderwidth=5,fg='green')
	    stocks_btn=Button(window,padx=btnpadx,text='Click to see result',borderwidth=5,fg='lightgray',bg='green',command=lambda: stck(stocks_choice.get().upper()))
	    spacer=Label(window,text="  ",pady=10,bg=lab_c)
	    spacer1=Label(window,text="  ",pady=3,bg=lab_c)

	    stock_history=Label(window,text='Stock History',fg='green',bg=lab_c)
	    stock_history.grid(row=0,column=0,columnspan=2)

	    first_stock.grid(row=1,column=0)
	    sec_stock.grid(row=1,column=1)
	    third_stock.grid(row=2,column=0)
	    fourth_stock.grid(row=2,column=1)


	    btn_inv.grid(row=0,column=2)
	    btn_dcf.grid(row=1,column=2)
	    stocks_lab.grid(row=4,column=0,columnspan=2)
	    stocks_choice.grid(row=5,column=0,columnspan=2)
	    spacer.grid(row=6,column=0)
	    spacer1.grid(row=3,column=1)
	    stocks_btn.grid(row=9,column=0,columnspan=2)
	    lbel_E=Label(root,text=f'stock not found ✘',bg='red',padx=20)
	    







labl=Label(text="What would you like to do today Mr Miller?",padx=5,borderwidth=3,pady=20,fg="green",bg=lab_c)
labl.grid(row=0,column=0,columnspan=4)

btn4=Button(window,text="Discounted Cashflow",pady=10,command=lambda: btn_pres(1),fg="green",borderwidth=2,bg=lab_c)
btn6=Button(window,text="Investment Calculator",pady=10,command=lambda: btn_pres(2),fg="green",borderwidth=2,bg=lab_c)
btn7=Button(window,text="Stock Tickers",padx=40,pady=10,command=lambda: btn_pres(3),fg="green",borderwidth=2,bg=lab_c)

space1=Label(window,text=" ",pady=6,bg=lab_c)
space2=Label(window,text=" ",pady=6,bg=lab_c)

img_1=Image.open('ticker.png')
img_1=img_1.resize((40,35),Image.ANTIALIAS)
img1=ImageTk.PhotoImage(img_1)

labl_img1=Label(window,image=img1)

#invesment image
img_2=Image.open('investment.png')
img_2=img_2.resize((40,35),Image.ANTIALIAS)
img2=ImageTk.PhotoImage(img_2)

labl_img2=Label(window,image=img2)

img_3=Image.open('DCF.png')
img_3=img_3.resize((40,35),Image.ANTIALIAS)
img3=ImageTk.PhotoImage(img_3)

labl_img3=Label(window,image=img3)

labl_img3.grid(row=6,column=1)
labl_img2.grid(row=4,column=1)
labl_img1.grid(row=2,column=1)
btn6.grid(row=4,column=0)
space1.grid(row=5,column=0)
btn4.grid(row=6,column=0)
space2.grid(row=3,column=0)
btn7.grid(row=2,column=0)

window.mainloop()