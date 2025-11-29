import datetime as dt

def say_hello(name):
    Current_hour=dt.datetime.now().hour
     
    if Current_hour<12:
       greeting="Good morning"
    elif 12<=Current_hour<17:
       greeting="Good afternoon" 
    else:
       greeting="Good evening"    
    print(f"{greeting},{name}")
            
   