import subprocess as sp
import pymysql
import pymysql.cursors


def Insertion():
    
    print("1. Insertion of a New employee and his educational qualification")
    print("3. Insertion of a New customer")
    #print("3. Insertion of a New food item and its ingredients")#
    #print("4. Insertion of  a New table")
    #print("4. Insertion of a New restaurant")#
    print("2. Inserting a new profession")
    #print("6. Inserting a new order")#
    #print("7. Inserting a new fooditem in the menu of a restaurant")
    print("4. Exit")
    
    val = int(input("Enter your choice: "))

    if val == 4:
        return
    
    elif val == 1:
        try:
            print("")
            print("Enter the employee's Details: ")
            player={}
            player["employee_id"]=int(input("employee_id: "))
            #name= input("Name (Fname Lname): ").split(' ')
            #player["Fname"] = name[0]
            #player["Lname"] = name[1]
            
            player["profession"] = (input("profession: "))
            player["restaurant_location"] = (input("restaurant_location: "))
            player["Employee_name"] = (input("Employee_name: "))
            player["Restaurant_name"] = (input("Restaurant_name: "))
            player["PF_amount"] = float(input("PF_amount: "))
            player["Month_of_joining"] = int(input("Month_of_joining: "))
            player["Year_of_joining"] = int(input("Year_of_joining: "))
            player["Date_of_joining"] = int(input("Date_of_joining: "))
            
            
            query= "INSERT INTO employee VALUES('%d', '%s', '%s', '%s', '%s', '%f', '%d', '%d','%d')" %(player["employee_id"],player["profession"],player["restaurant_location"], 
            player["Employee_name"],player["Restaurant_name"],player["PF_amount"],player["Month_of_joining"],player["Year_of_joining"],player["Date_of_joining"])
            cur.execute(query)
            # print(query)

            

            print("")
            print("==============================================INSERTED==============================================")
            print("")

            print("EMPLOYEE TABLE")
            print("")
            query="SELECT * FROM employee"
            cur.execute(query)
            result=cur.fetchall()
            print(result)
            print("")
            
      
      
        except Exception as e:
            con.rollback()
            print("Failed to Insert Into the Database")
            print(">>>>>>>>>>>>>",e)
        
        return

    elif val == 2:
        try:

            team={}
            print("")
            print("Enter New Profession's Details: ")
            team["Profession"]=(input("Profession: "))
            team["Salary"]=int(input("Salary: "))
            team["Employee_Working_Hours"]=int(input("Employee_Working_Hours: "))
            team["PF_Percentage"]=int(input("PF_Percentage: "))

            query= "INSERT INTO Profession VALUES('%s', '%d','%d','%d')"%(team["Profession"], team["Salary"],team["Employee_Working_Hours"],team["PF_Percentage"])
            cur.execute(query)
            con.commit()
            # print(query)

            

            print("")
            print("==============================================INSERTED==============================================")
            print("")

            print("PROFESSION TABLE")
            print("")
            query="SELECT * FROM Profession"
            cur.execute(query)
            result=cur.fetchall()
            print(result)
            print("")

            


        except Exception as e:
            con.rollback()
            print("Failed to Insert Into the Database")
            print(">>>>>>>>>>>>>",e)

        return

    elif val == 3:
        try:
            team={}
            print("")
            print("Enter New customer's Details: ")
            team["Phone_number"]=int(input("Phone_number: "))
            team["user_name"]=(input("user_name: "))
            team["Email"]=(input("Email: "))
            team["Amount_Recieved"]=True
            team["Name"]=(input("Name: "))
            team["Order_number"]=pymysql.NULL

            query= "INSERT INTO Customer VALUES('%d', '%s','%s', 'True','%s','NULL')"%(team["Phone_number"], team["user_name"],team["Email"],team["Name"])
            cur.execute(query)
            con.commit()
            # print(query)

            

            print("")
            print("==============================================INSERTED==============================================")
            print("")

            print("CUSTOMER TABLE")
            print("")
            query="SELECT * FROM Customer"
            cur.execute(query)
            result=cur.fetchall()
            print(result)
            print("")

            


        except Exception as e:
            con.rollback()
            print("Failed to Insert Into the Database")
            print(">>>>>>>>>>>>>",e)
        return

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch==1): 
        Insertion()
    elif(ch==2):
        Updation()
    elif(ch==3):
        Deletion()
    elif(ch==4):
        Report()
    else:
        print("Error: Invalid Option")

# Global
while(1):
    tmp = sp.call('clear',shell=True)
    username = input("username: ")
    password = input("password: ")

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='RESTAURANT_CHAIN',
                cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear',shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")
        tmp = input("Enter any key to CONTINUE>")

        with con:
            cur = con.cursor()
            while(1):
                tmp = sp.call('clear',shell=True)
                print("")
                print("======================Functions of RESTAURANT_CHAIN Database======================")
                print("")
                print("1. Insertion")
                print("2. Updation")
                print("3. Delete")
                print("4. Report")
                print("5. Logout")
                print("")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear',shell=True)
                if ch==5:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")


    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
        
        """Insert:
     -Insertion of a New customer(with order number,amount received as NULL).
        - Insertion of a New employee and his educational qualification.
       - Inserting a new order(it updates order num,amount received in customer relation)
       -Insertion of a New food item 
       -Inserting a new profession
       -Insertion of a New restaurant
       
    Delete:
             - delete data about a newly resigned employee
    Update:
              -modifying/incrementing salaries of the employees with time
              - updating the costs and ratings of each food item
              -updating Pf percentage of profession.

    Selection:
        Retrieve complete data about employees in the cooking dept(cooks)

    projection:
        project restaurant location in employee relation.
    
    Aggregate:
        Find the average salary of an employee in the restaurant.

    Search:
        
    analysis:
        Number of  employees who had passed 12th standard in all the restaurants.
    """
