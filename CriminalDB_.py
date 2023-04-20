
from datetime import date
from datetime import datetime, timedelta
import mysql.connector as s
from prettytable import PrettyTable
def perform_operations():
    def add_data():
        Case_id=int(input("ENTER CASE ID "))
        Criminal_id=int(input("Enter Criminal No "))
        Criminal_name=input("Enter Criminal Name ")
        Nick_name=input("Enter Criminal NickName ")
        
        arrest_date= input("Enter the arrest date (yyyy-mm-dd): ")
        dateOfcrime = input("Enter the date of crime (yyyy-mm-dd): ")

        while True:
            # arrest_date, dateOfcrime = times(arrest_date, dateOfcrime)
            if datetime.strptime(dateOfcrime, '%Y-%m-%d') <= datetime.strptime(arrest_date, '%Y-%m-%d'):
                break
            else:
                print("Crime date cannot be greater than arrest date. Please try again.")
                arrest_date = input("Enter the arrest date (yyyy-mm-dd): ")
                dateOfcrime = input("Enter the date of crime (yyyy-mm-dd): ")
                

        address=input("Enter Address Of Criminal ")
        
        def age():
            criminal_age = int(input("Enter the age of the criminal: "))
            if criminal_age >= 1 and criminal_age <= 150:
                return criminal_age
            else:
                print("Invalid age ")
                return age()
            
            
        occupation=input("Enter the Occupation of Crimanal ")
        BirthMark=input("Enter the BirthMark of Crimanal ")
        crimeType=input("Enter Crime Type ")
        fatherName=input("Enter Father Name ")
        
        def gender():
            criminal_gender=input("Enter the gender  (M/F): ")
            if criminal_gender == "M":
                print("You have selected Male.")
            elif criminal_gender == "F":
                print("You have selected Female.")
            else:
                print("Invalid input. Please select M or F.")
                return gender()
            return str(criminal_gender)
            
        
        def wanted():
            criminal_imp=input("Criminal is wanted [Y/N] ")
            if criminal_imp=='Y':
                print("Wanted Criminal ")
            elif criminal_imp=='N':
                print('Not Wanted ')
            else:
                return wanted()
            return str(criminal_imp)
            
                
        if Case_id=="":
            print("ERROR ", 'All fields are required ')
        else:
            try:
                conn=s.connect(host="localhost",user="root",password="Kaletha@123",database="management")
                cursor=conn.cursor()
                q="insert into criminal(Case_id,Criminal_id,Criminal_name,Nick_name,arrest_date,dateofcrime,address,age,occupation,BirthMark,crimeType,fatherName,gender,wanted) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(q,([Case_id,Criminal_id,Criminal_name,Nick_name,arrest_date,dateOfcrime,address,age(),occupation,BirthMark,crimeType,fatherName,gender(),wanted()]))
                conn.commit()
            except Exception as e:
                print('error',f'Due to {str(e)}')
                
            fetch_data()

    # add_data()
    
    def fetch_data():
        conn=s.connect(host="localhost",user="root",password="Kaletha@123",database="management")
        cursor=conn.cursor()
        cursor.execute('select * FROm criminal')
        data=cursor.fetchall()
        
        table = PrettyTable()
        table.field_names = ['Case ID', 'Criminal ID', 'Criminal Name', 'Nick Name', 'Arrest Date', 'Date of Crime', 'Address', 'Age', 'Occupation', 'Birth Mark', 'Crime Type', 'Father Name', 'Gender', 'Wanted']
        
        for row in data:
            table.add_row(row)
        
        print(table)
        
        
    def update_data():
        conn = s.connect(host="localhost", user="root", password="Kaletha@123", database="management")
        cursor = conn.cursor()

        case_id = input("Enter the Case ID of the criminal record you want to update: ")
        cursor.execute("SELECT * FROM criminal WHERE Case_id = %s", (case_id,))
        data = cursor.fetchone()
        if case_id=="":
            print('Error','All Field are Required ')
        else:
            try:
                if data:
                    print("1. Criminal ID")
                    print("2. Criminal Name")
                    print("3. Nick Name")
                    print("4. Arrest Date")
                    print("5. Date of Crime")
                    print("6. Address")
                    print("7. Age")
                    print("8. Occupation")
                    print("9. Birth Mark")
                    print("10. Crime Type")
                    print("11. Father Name")
                    print("12. Gender")
                    print("13. Wanted")

                    field_num = int(input("Enter the field number you want to update: "))

                    if field_num == 1:
                        criminal_id = int(input("Enter the new Criminal ID: "))
                        cursor.execute("UPDATE criminal SET Criminal_id = %s WHERE Case_id = %s", (criminal_id, case_id))

                    elif field_num == 2:
                        criminal_name = input("Enter the new Criminal Name: ")
                        cursor.execute("UPDATE criminal SET Criminal_name = %s WHERE Case_id = %s", (criminal_name, case_id))

                    elif field_num == 3:
                        nick_name = input("Enter the new Nick Name: ")
                        cursor.execute("UPDATE criminal SET Nick_name = %s WHERE Case_id = %s", (nick_name, case_id))

                    elif field_num == 4:
                        arrest_date = input("Enter the new Arrest Date (yyyy-mm-dd): ")
                        cursor.execute("UPDATE criminal SET arrest_date = %s WHERE Case_id = %s", (arrest_date, case_id))

                    elif field_num == 5:
                        date_of_crime = input("Enter the new Date of Crime (yyyy-mm-dd): ")
                        cursor.execute("UPDATE criminal SET dateOfcrime = %s WHERE Case_id = %s", (date_of_crime, case_id))

                    elif field_num == 6:
                        address = input("Enter the new Address: ")
                        cursor.execute("UPDATE criminal SET address = %s WHERE Case_id = %s", (address, case_id))

                    elif field_num == 7:
                        age = int(input("Enter the new Age: "))
                        cursor.execute("UPDATE criminal SET age = %s WHERE Case_id = %s", (age, case_id))

                    elif field_num == 8:
                        occupation = input("Enter the new Occupation: ")
                        cursor.execute("UPDATE criminal SET occupation = %s WHERE Case_id = %s", (occupation, case_id))

                    elif field_num == 9:
                        birth_mark = input("Enter the new Birth Mark: ")
                        cursor.execute("UPDATE criminal SET BirthMark =%s WHERE Case_id=%s", (birth_mark , case_id))

                    elif field_num == 11:
                        father_name = input("Enter the new Father Name: ")
                        cursor.execute("UPDATE criminal SET fatherName = %s WHERE Case_id = %s", (father_name, case_id))

                    elif field_num == 12:
                        gender = input("Enter the new Gender (M/F): ") 
                        cursor.execute("UPDATE criminal SET Gender =%s WHERE Case_id = %s",(gender, case_id))  
                        
                    elif field_num ==13:
                        wanted=input("Enter the Wanted status :")
                        cursor.execute("UPDATE criminal SET wanted =%s WHERE Case_id=%s",(wanted, case_id))
                        
                    else:
                        if not update:
                            return
                    conn.commit()
                    fetch_data()
                    conn.close()
                    print('successful', 'Criminal record has been updated ')
            except Exception as e:
                print('error',f'Due to {str(e)}') 
        fetch_data()   
                
    def delete_data():
        conn = s.connect(host="localhost", user="root", password="Kaletha@123", database="management")
        cursor = conn.cursor()

        case_id = input("Enter the Case ID of the criminal record you want to delete: ")
        cursor.execute("SELECT * FROM criminal WHERE Case_id = %s", (case_id,))
        data = cursor.fetchone()

        if case_id=="":
            print('Error','All Field are Required ')
        elif data == None:
            print('Error', f"No criminal record found with Case ID {case_id}")
        else:
            confirm = input(f"Are you sure you want to delete the criminal record with Case ID {case_id}? (Y/N)")
            if confirm == "Y":
                cursor.execute("DELETE FROM criminal WHERE Case_id = %s", (case_id,))
                conn.commit()
                print(f"The criminal record with Case ID {case_id} has been deleted.")
            else:
                print("Deletion cancelled.")
                
        fetch_data()
                
    def exit():
        exit()
        
    def structure():
        while True:
            print("\nSelect an operation:")
            print("1. Add data")
            print("2. Fetch data")
            print("3. Update data")
            print("4. Delete data")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                add_data()
            elif choice == "2":
                fetch_data()
            elif choice == "3":
                update_data()
            elif choice == "4":
                delete_data()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Try again.")
                return structure()


    structure()           




            
   