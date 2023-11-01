import subprocess as sp
import pymysql
import pymysql.cursors

def Report():
    """
    Function to evaluate and analyse the given Database
    """
    print("1. Retrieve complete data about employees who are chefs :SELECTION")
    print("2. project restaurant location in employee relation :PROJECTION")
    print("3. Find the average salary of all the professions :AGGREGATE")
    
    print("4. Exit")
    val = int(input("Choose the query you want to execute> "))

    if val == 4:
        return

    elif val == 1:

        try:

            print("")
            print("Retrieving complete data about employees who are chefs")
            print("")
            #query="SELECT COUNT(M.WonBy) \"COUNT\", T.TeamID FROM MATCHES AS M, TEAMS AS T WHERE WonBy IS NOT NULL AND T.TeamID = M.WonBy GROUP BY T.TeamID"
            query="SELECT * FROM employee WHERE profession='Chef';"
            print("")
            cur.execute(query)
            result=cur.fetchall()
            print(result)

        except Exception as e:
            con.rollback()
            print("Failed to select from database")
            print("************",e)

    elif val == 2:

        try:

            print("")
            print("project restaurant location from employee relation.")
            print("")
            #query="SELECT PID, Fname, Lname from PLAYERS WHERE PID = (SELECT PID FROM BATSMAN WHERE Runs = (SELECT MAX(Runs) FROM BATSMAN))"
            query="SELECT DISTINCT restaurant_location FROM employee";

            print("")
            cur.execute(query)
            result=cur.fetchall()
            print(result)

        except Exception as e:
            con.rollback()
            print("Failed to project from database")
            print("************",e)

    elif val == 3:

        try:

            print("")
            print("Finding the average salary of all the professions")
            print("")
            #query="SELECT PID, Fname, Lname from PLAYERS WHERE PID = (SELECT PID FROM BOWLER WHERE Wickets = (SELECT MAX(Wickets) FROM BOWLER))"
            query="SELECT AVG(Salary) FROM Profession;"
            print("")
            cur.execute(query)
            result=cur.fetchall()
            print(result)

        except Exception as e:
            con.rollback()
            print("Failed to get the average salary of all the professions in database")
            print("************",e)

    

     

def Deletion():
    try:
        print("")
        print("________________________________________Deleting data of a resigned Employee ________________________________________")
        print("")

        print("Employee TABLE")
        print("")
        query="SELECT * FROM Employee"
        print("")
        cur.execute(query)
        result=cur.fetchall()
        print(result)

        print("educational_qualification TABLE")
        print("")
        query="SELECT * FROM educational_qualification"
        print("")
        cur.execute(query)
        result=cur.fetchall()
        print(result)


        print("")
        vid1 = int(input("Please Enter Employee_Id to be deleted: "))
        print("")

        query = "DELETE FROM Employee WHERE (Employee_Id = '%d')" %(vid1)
        cur.execute(query)
        con.commit()

        query = "DELETE FROM educational_qualification WHERE (Employee_Id = '%d')" %(vid1)
        cur.execute(query)
        con.commit()

        print("")
        print("________________________________________Successfully Deleted ________________________________________")
        print("")

        print("Employee TABLE")
        print("")
        query="SELECT * FROM Employee"
        print("")
        cur.execute(query)
        result=cur.fetchall()
        print(result)

        print("educational_qualification TABLE")
        print("")
        query="SELECT * FROM educational_qualification"
        print("")
        cur.execute(query)
        result=cur.fetchall()
        print(result)
        

    except Exception as e:
        con.rollback()
        print("Failed to update in database")
        print("************",e)
    

def Updation():
      """
      Function to update queries mentioned in SRS Document
      """
      print("1. updating the costs and ratings of each food item")
      print("2. Updating the Salary of the Profession Table")
      print("3. Exit")
      val = int(input("Choose the query you want to execute> "))

      if val == 3:
        return

      elif val == 1:
        try:
            print("-------------------UPDATING STARTS------------------------")
            print("")
            print("food_items TABLE")
            print("")
            query="SELECT * FROM food_items"
            print("")
            cur.execute(query)
            result=cur.fetchall()
            print(result)

            print("")
            pid = int(input("Please enter the item number of food_item whose data needs to be updated: "))
            query = "SELECT * FROM food_items WHERE (item_number = '%d')" %(pid)
            cur.execute(query)
            result = cur.fetchall() 

            print("")
            inp1 = float(input("Please enter updated Price: "))
            inp2 = int(input("Please enter updated rating: "))
            
            
            query = "UPDATE food_items SET Rating = '%d' WHERE item_number = '%d'" %(inp2 , pid)
            cur.execute(query)
            con.commit()

            query = "UPDATE food_items SET Price = '%f' WHERE item_number = '%d'" %(inp1 , pid)
            cur.execute(query)
            con.commit() 
            
            print("==============================================UPDATED==============================================")

            print("food_items TABLE")
            print("")
            query="SELECT * FROM food_items"
            print("")
            cur.execute(query)
            result=cur.fetchall()
            print(result)

        except Exception as e:
            con.rollback()
            print("Failed to update in database")
            print("************",e)

    # +++++++++++++++++++++++++++++++++++++++++++++
      elif val == 2:
        try:
            print("-------------------UPDATING STARTS------------------------")
            print("")
            print("Profession TABLE")
            print("")
            query="SELECT * FROM Profession"
            print("")
            cur.execute(query)
            result=cur.fetchall()
            print(result)

            print("")
            pid = str(input("Please enter the profession of Profession Table whose data needs to be updated: "))
            query = "SELECT * FROM Profession WHERE (profession = '%s')" %(pid)
            cur.execute(query)
            result = cur.fetchall() 

            print("")
            inp1 = int(input("Please enter updated Salary: "))
            
            
            query = "UPDATE Profession SET Salary = '%d' WHERE profession = '%s'" %(inp1 , pid)
            cur.execute(query)
            con.commit()
            
            print("==============================================UPDATED==============================================")

            print("Profession TABLE")
            print("")
            query="SELECT * FROM Profession"
            print("")
            cur.execute(query)
            result=cur.fetchall()
            print(result)

        except Exception as e:
            con.rollback()
            print("Failed to update in database")
            print("************",e)
    # +++++++++++++++++++++++++++++++++++++++++++++
    
      else:
            print("")
            print("INVALID")

def Insertion():
    
    print("1. Insertion of a New employee and his educational qualification")
    print("2. Inserting a new profession")
    print("3. Insertion of a New customer")
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
            team["profession"]=(input("profession: "))
            team["Salary"]=int(input("Salary: "))
            team["Employee_Working_Hours"]=int(input("Employee_Working_Hours: "))
            team["PF_Percentage"]=int(input("PF_Percentage: "))

            query= "INSERT INTO Profession VALUES('%s', '%d','%d','%d')"%(team["profession"], team["Salary"],team["Employee_Working_Hours"],team["PF_Percentage"])
            #query= "INSERT INTO Profession VALUES('%s', '%d','%d')"%(team["profession"], team["Salary"],team["PF_Percentage"])
            cur.execute(query)
            con.commit()

            

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
    #port = 3306;

    try:
        con = pymysql.connect(host='localhost',
                port=30306,
                user=username,
                password=password,
                db='restaurant_chain',
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
                print("======================Functions of Database======================")
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
