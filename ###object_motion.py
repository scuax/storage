x0=float(input("Enter the initial position in m: "))
v0=float(input("Enter the initial velocity in m/s: "))
a=float(input("Enter the acceleration in m/s^2: "))
t=float(input("Enter the time in s: "))
x=x0+v0*t+0.5*a*t**2
v=v0+a*t
print("The final position is ",x,"m")
print("The final velocity is ",v,"m/s")