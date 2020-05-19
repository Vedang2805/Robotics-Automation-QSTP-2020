import math
inp=input("Enter required conversion")
if inp="Cartesian to Polar" :
   x=float(input("Enter x co-ordinat:")
   y=float(input("Enter y co-ordinate:")
   r=((x**2) + (y**2))**(1/2)
   a=math.atan((y/x))
   print("The polar co-ordinates are:",r,a)
elif inp="Polar to Cartesian" :
   r=float(input("Enter length from origin:"))
   a=float(input("Enter angle made with x-axis:))
   x=r*(math.cos(a))
   y=r*(math.sin(a))
   print("The Cartesian co-ordinates are:",x,y)    
           
   
