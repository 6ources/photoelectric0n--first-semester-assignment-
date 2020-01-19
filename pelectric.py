"""program for photo electric effect by
	 MD OMAR FARUK  --41---
	---K18AZ---
	PHY-109(lab at home)
"""
#main module
"""
cases this program will solve---
	--it'll calculate the KE(Kinetic Energy)
	--it'll calculate stopping potential of the particle
	--it'll calculate work function
	--it'll calculate threshold wavelength

but for fast calculation we'll preDEFine some values by default...if you want to give custom value make sure you give the value...

or just type 'n' so that the default value can take the part
"""

#defining value

#planks constant as h		
h=6.63*10**-34

#speed of light as c
c=3*10**8

#change on an electron as e
e=1.6*10**-19

#wave length of light in meter as lambda1
lambda1=5.89*10**-7

#wave length of photo electron in meter as lambda2
lambda2=7.32*10**-7

#stopping potential v
v=1.98

#assuming work function of sodium as w
w=2.2

#program to calculate KE of the particle as ke

ke=(h*c)*(1/lambda1-1/lambda2)


#program for stopping potential as sp

sp=ke/e

#program for work function as wf
enew=e*v
lambda2=1/((1/lambda1)-(enew/(h*c)))

wf=((h*c)/lambda2)

#program for threshold as th

th=((h*c)/(w*e))



#user interface or custom input
print("Here we'll calculate the numerical for photoelectric effect")
print("[+] press 1 to calculate KE-kinetic energy")
print("[+] press 2 to calculate Stopping potential")
print("[+] press 3 to calculate Work Function")
print("[+] press 4 to calculate Threshold wavelength")
print("[+] press 5 to plot a graph")
print("[+] print 6 to export data to exel file")
choice=int(input("\n-your call is :==> "))


#for KE calculation
if (choice==1):
  choice1=input("[+] Do you want to give custom input? : y/n :==> ")
  if (choice1 == "y" ):
      print("nyou can change the lambda values (/light & photo electron)/ in here others are just constant")
      lambda1a=float(input("tell the wave length of light in meter :=> "))
      lambda2a=float(input("tell the wave length of photo electron in meter :=> "))
      ke1=(h*c)*(1/lambda1a-1/lambda2a)
      print("solution is : ",ke1)
  elif(choice1 == "n"):
    print("nFor KE calculation we used formula => \n\t\tke=(h*c)*(1/lambda1-1/lambda2)")
    print("where -n\t\t      h = 6.63*10**-34,\n   \t\t      c = 3*10**8,\n\t\tlambda1 = 5.89*10**-7,\n\t\tlambda2 = 7.32*10**-7")
    print("nso the solution is :=>> ",ke,"\n")
  else:
    print("sorry wrong input!")
    

#custom stopping potential value program
elif(choice==2):
  choice1 = input("[+] Do you want to give custom input? : y/n :==> ")
  if (choice1 == "y"):
    print("[+] here you can change the value oflambda values only and rest are constant")
    lambda1a = float(input("tell the wave length of light in meter :"))
    lambda2a = float(input("tell the wave length of photo electron in meter :"))
    ke1 = (h*c)*(1/lambda1a-1/lambda2a)
    sp1 = ke1/e
    print("\nso the solution is : ",sp1)  
  elif(choice1 == "n"):
    print("For stopping potential calculation we used formula => sp=ke/e")
    print(" where we got the formula of ke from the previous option and we know e=1.6*10**-19")
    print("\nso the solution is : ",sp)
  else:
    print("sorry wrong input!")

#custom work function value program
elif(choice == 3):
  choice1 = input("[+] Do you want to give custom input? : y/n :=>")
  if (choice1 == "y"):
      print("here you can change the value of stopping potetial,lambda value and rest are constant")
      v1=float(input("tell me the custom stopping potential value :"))
      lambda1a = float(input("tell the wave length of light in meter :"))
      lambda2a = float(input("tell the wave length of photo electron in meter :"))
      #custom values formula
      enew1 = e*v1
      lambda2a = 1/((1/lambda1a)-(enew1/(h*c)))
      wf1 = ((h*c)/lambda2a)
      print("ok so the work function will be :=> ",wf1)
      
  elif(choice1 == "n"):
    print("For working function calculation we used formula => wf=((h*c)/lambda2)")
    print("where h=6.63*10**-34,c=3*10**8,lambda2=7.32*10**-7")
    print("\nso the solution is :",wf)
  else:
    print("sorry wrong input!")


#threshold calculation
elif(choice == 4):
  choice1 = input("[+] Do you want to give custom input? : y/n :=>")
  if (choice1 == "y"):
    print("here you only change the work function")
    w1 = float(input("tell the work function you want to give :"))
    
    th1 = ((h*c)/(w1*e))
    
    print("\nso the solution for thresh hold value is :=>",th1)
  elif(choice1 == "n"):
    print("For Threshold calculation we used formula => th=((h*c)/(w*e))")
    print("where h=6.63*10**-34,c=3*10**8,w=2.2,e=1.6*10**-19")
    print("\nso the solution is :=>",th)
  else:
    print("sorry wrong input!")

elif(choice == 5):
  # importing matplotlib module
  from matplotlib import pyplot as plt

  #axis naming
  plt.ylabel("Energy (eV)")
  plt.xlabel("Frequency (10^15Hz)")
      # x-axis values 
  x = [0.55, 3.00] 

      # Y-axis values 
  y = [0, 10.5]
      
      # Function to plot 
  plt.plot(x,y) 

      # function to show the plot 
  plt.show() 


elif(choice == 6):
  import xlwt 
  from xlwt import Workbook 

  print("your data has been exported check it in the same folder")
  # Workbook is created 
  wb = Workbook() 

  # add_sheet is used to create sheet. 
  data1 = wb.add_sheet('photo electric') 
  #col-01
  data1.write(0, 0, 'Planks Constant') 
  data1.write(1, 0, 'h') 
  data1.write(2, 0, h)
  #col-02
  data1.write(0, 1, 'speed of light') 
  data1.write(1, 1, 'c') 
  data1.write(2, 1, c)
  #col-03
  data1.write(0, 2, 'electron changes') 
  data1.write(1, 2, 'e') 
  data1.write(2, 2, e) 
  #col-04
  data1.write(0, 3, 'length of light')
  data1.write(1, 3, 'lambda1')
  data1.write(2, 3, lambda1)
  #col-05
  data1.write(0, 4, 'length of wave')
  data1.write(1, 4, 'lambda2')
  data1.write(2, 4, lambda2)
  #col-06
  data1.write(0, 5, 'stopping potential')
  data1.write(1, 5, 'v')
  data1.write(2, 5, v)
  #col-07
  data1.write(0, 6, 'assigned work function')
  data1.write(1, 6, 'w')
  data1.write(2, 6, w)
  #col-08
  data1.write(0, 7, 'kinetic energy')
  data1.write(1, 7, 'ke=(h*c)*(1/lambda1-1/lambda2)')
  data1.write(2, 7, ke)
  #col-09
  data1.write(0, 8, 'stopping potential')
  data1.write(1, 8, 'sp=ke/e')
  data1.write(2, 8, sp)
  #col-10
  data1.write(0, 9, 'work function')
  data1.write(1, 9, 'wf=((h*c)/(1/((1/lambda1)-((e*v)/(h*c))))')
  data1.write(2, 9, wf)
  #col-11
  data1.write(0, 10, 'threshold')
  data1.write(1, 10, '((h*c)/(w*e))')
  data1.write(2, 10, th)

  wb.save('PelectricData.xls')

else:
  print("sorry wrong input!")
#done :)
