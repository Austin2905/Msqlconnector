print("........................................................................")
print("\n")
print("---------------WELCOMING - YOU FOR UPDATING AADHAR CARD ----------")
import mysql.connector as sql
 #importing mysql to the program
mycon=sql.connect(host="localhost",user="root",passwd="root",database="aadhar")
if mycon.is_connected():
 print("\n")
 print( "*********** Successfully connected with mysql *************")
 print("\n")
else:
 print("Error while connecting , try again")

 #main program
def menu():
 print("_ _ _ _ _ _ Update Your Aadhar Card using this program_ _ _ _ _ _ _")
 print("\n")
 c='y'
 while (c=="y"):
    c=input("Do you want to continue or not (y/n):")
    print("\n")
 if c=='y':
     print("1.Update your photo using biometric update")
     print("\n")
     print("2.Update your name with address")
     print("\n")
     print("3.Update your name with phone numeber")
     print("\n")
     print("4.update only name ")
     print("\n")
     print("5.Applying newly")
     print("\n")
     print("6.exit")
     print("\n")
 choice=int(input("Enter your choice(1-6)"))
 print("\n")
 if choice==1:
     photo()
 elif choice==2:
       name_adrs()
 elif choice==3:
       name_phn()
 elif choice==4:

       name()
 elif choice==5:
       new()
 else:
      print("Exited ")
      print("\n")
      print("Visit again...&...Have a nice day ")
      print("_________________________________________________")
      break
    
 print("Visit again...&...Have a nice day ")
 print("\n")
 print("thank you ")
 print( "_________________________________________________________" )
def photo():
 count=int(input("how many updates are you doing(max:4):"))
 for i in range(count):
     print(" For the member" ,(i+1)," , enter the details :")
     print("\n")
 p_s_no=(i+1)
 p_aadhar=int(input("Enter your Aadhar number's last 6 dights :"))
 print("\n")
 p_name=input( "Enter your Full Name : ")
 print("\n")
 p_photo=input("Enter in which month did you born:")
 print("\n")
 p_pn=input("Enter your Parents Name:")
 print("\n")
 import mysql.connector as sql


conn=sql.connect(host="localhost",user="root",passwd="root",database="aadhar")
mycursor=conn.cursor()
st='''insert into photo(S_no,Aadhar_no,Name_of_candidate,photo,parents_name)

values(%s,%s,'%s','%s','%s')'''%((p_s_no),(p_aadhar),(p_name),(p_photo),(p_pn))
 mycursor.execute(st)
conn.commit()
 print("registered successfully")
 print("\n")
 print("Congrats you have Updated your Aadhar Card ")
 print("\n")
 print(" Thanks for joining with us . Thank you , visit us again ")
 print("\n")
 print("Within 30 working days you will get a new updated Aadhar card .....")
def name_adrs():
 count=int(input("how many updates are you doing(max:4):"))
 print("\n")
 for i in range(count):
 #input

 print(" For the member" ,(i+1)," , enter the details :")
 print("\n")
 p_s_no=(i+1)
 p_aadhar=int(input("Enter your Aadhar number's last 6 dights :"))
 print("\n")
 p_name=input( "Enter your Full Name : ")
 print("\n")
 p_address=input("Enter your address:")
 print("\n")
 p_pn=input("Enter your Parents Name:")
 print("\n")
 p_paadhar=int(input("Enter your father/mother 's aadhar number :"))
 print("\n")
 import mysql.connector as sql


conn=sql.connect(host="localhost",user="root",passwd="root",database="aadhar")
 mycursor=conn.cursor()

 #insert queries
 st='''insert into
name_adrs(S_no,Aadhar_no,Name_of_candidate,address,parents_name,parents_add)

values(%s,%s,'%s','%s','%s',%s)'''%((p_s_no),(p_aadhar),(p_name),(p_address),(p_pn),
(p_paadhar))
 mycursor.execute(st)
 conn.commit()
 print("registered successfully")
 print("\n")
 print("Congrats you have Updated your Aadhar Card ")
 print("\n")
 print(" Thanks for joining with us . Thank you , visit us again ")
 print("\n")
 print("Within 30 working days you will get a new updated Aadhar card .....")

 def name_phn():
 count=int(input("how many updates are you doing(max:4):"))
 print("\n")
 for i in range(count):
 #inputs

 print(" For the member" ,(i+1)," , enter the details :")
 print("\n")
 p_s_no=(i+1)
 p_aadhar=int(input("Enter your Aadhar number's last 6 dights :"))
 print("\n")
 p_name=input( "Enter your Full Name : ")
 print("\n")
 p_pn=int(input("Enter your phone number :"))
 print("\n")
 import mysql.connector as sql


conn=sql.connect(host="localhost",user="root",passwd="root",database="aadhar")
 mycursor=conn.cursor()

 #insert queries
 st='''insert into name_phn(S_no,Aadhar_no,Name_of_candidate,phone_no)
 values(%s,%s,'%s',%s)'''%((p_s_no),(p_aadhar),(p_name),(p_pn))
 mycursor.execute(st)
 conn.commit()
 print("registered successfully")
 print("\n")
 print("Congrats you have Updated your Aadhar Card ")
 print("\n")
 print(" Thanks for joining with us . Thank you")
 print("\n")
 print("Within 30 working days you will get a new updated Aadhar card .....")
def name():
 count=int(input("how many updates are you doing(max:4):"))
 print("\n")
 for i in range(count):
 #inputs

     print(" For the member" ,(i+1)," , enter the details :")
 print("\n")
 p_s_no=(i+1)
 p_aadhar=int(input("Enter your Aadhar number's last 6 dights :"))
 print("\n")
 p_name=input( "Enter your Full Name : ")
 print("\n")
 import mysql.connector as sql


conn=sql.connect(host="localhost",user="root",passwd="root",database="aadhar")
 mycursor=conn.cursor()

 #insert queries
 st='''insert into name(S_no,Aadhar_no,Name_of_candidate)
 values(%s,%s,'%s')'''%((p_s_no),(p_aadhar),(p_name))
 mycursor.execute(st)
 conn.commit()
 print("registered successfully")
 print("\n")
 print("Congrats you have Updated your Aadhar Card ")
 print("\n")
 print(" Thanks for joining with us . Thank you")
 print("\n")
 print("Within 30 working days you will get a new updated Aadhar card .....")
def new():
 count=int(input("how many updates are you doing(max:4):"))
 print("\n")
 for i in range(count):
 #inputs
 print(" For the member" ,(i+1)," , enter the details :")
 print("\n")
 p_s_no=(i+1)
 p_name=input( "Enter your Full Name : ")
 print("\n")
 p_gender=input( "Enter your gender : ")
 print("\n")
 p_dob=input("Enter your date of birth (YYYY-MM-DD:")
 print("\n")
 p_fn=input("Enter your fathers Name:")
 print("\n")
 p_fn_a=int(input("Enter your fathers Aadhar number:"))

 print("\n")
 p_mn=input("Enter your mothers Name:")
 print("\n")
 p_mn_ad=int(input("Enter your mothers Aadhar number:"))
 print("\n")
 p_add=input("Enter your Address:")
 print("\n")
 p_pn=int(input("Enter your phone number:"))
 print("\n")
 import mysql.connector as sql


conn=sql.connect(host="localhost",user="root",passwd="root",database="aadhar")
 mycursor=conn.cursor()

 #insert queries
 st='''insert into
new(S_no,name_of_candidate,gender,dob,fathers_name,fathers_aadhar , mothers_name ,
mothers_aadhar ,address ,phone_no)

values(%s,'%s','%s','%s','%s',%s,'%s',%s,'%s',%s)'''%((p_s_no),(p_name),(p_gender),(
p_dob),(p_fn),(p_fn_a),(p_mn),(p_mn_ad),(p_add),(p_pn))

 mycursor.execute(st)
 conn.commit()

 print("registered successfully")
 print("\n")
 print("Congrats you have Updated your Aadhar Card ")
 print("\n")
 print(" Thanks for joining with us . Thank you")
 print("\n")
 print("Within 30 working days you will get a new updated Aadhar card .....")
menu() #again runing the program
