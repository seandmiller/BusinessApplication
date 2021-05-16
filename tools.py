from tkinter import *
from PIL import ImageTk,Image
import requests 
import yfinance as yf 

def stk_img(ticker):
	stck=yf.Ticker(ticker)
	img_src=stck.info['logo_url']
	response = requests.get(img_src)
	file=open('stockimg.png','wb')
	file.write(response.content)
	file.close()
def comma(arg):
   i=0
   r=0
   end_r=""
   result=str(arg).strip()
   result=list(result)

   for x in result:

	   if r==-3 :
	    	
	    	result.insert(i, ",")
	    	  	    
	   elif r < -3:
	    	r=0			
	   i-=1
	   r-=1
	   
   for y in result:
	   end_r+= y
   end_r += "$"
   return end_r    	
def discounted_cashf(exp_cf, perc, yr):
	    translation=""
	    perc=perc/100
	    result= int(exp_cf/(1+ perc)**yr)
	    return result
def investment(whole, percentage, time, contribution=0):
	contribution=int(contribution)
	whole=int(whole)
	time=int(time)
	percentage=float(percentage)
	percentage=percentage/100
	for x in range(time):
		whole=whole*(1+percentage)
		whole+=contribution
	return comma(int(whole))	    
class stck_db:
	def add(dta):
		data=open('log.txt','a')
		data.write(f"{dta.upper()} ")
		data.close()
	def r():
	    data=open('log.txt','r')
	    print(data.readlines())
	    data.close()
	def clear_all():
	    data=open('log.txt','w+')
	    data.write('')
	    data.close()    
	data=open('log.txt','r')
	data_=''
	for x in data:
	    data_+=x
	data.close()
	current_data=data_.split()
def figures(answer):
	    counter=0
	    for x in answer:
	        if x==',':
	           counter+=1 
	    if counter==1:
	       figure=f"{answer} Thousand"
	    elif counter==2:
	       figure=f"{answer} Million"
	    elif counter==3:
	       figure=f"{answer} Billion"
	    elif counter==4:
	       figure=f"{answer} Trillion"
	    return figure                      

