###temperature convertion
tipo=str(input("choose your the one you want to convert, c or f\n"))
if(tipo=="c"):
    celsius=float(input("how hot is it?\n"))
    farenheid=celsius*(9/5)+32
    print("the temperature in fahrenheit is ",farenheid)
if(tipo=="f"):
    farenheid=float(input("how hot is it?\n"))
    celsius=farenheid/(9/5)-32
    print("the temperature in fahrenheit is ",celsius)