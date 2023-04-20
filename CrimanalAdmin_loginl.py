import mysql.connector as s
from getpass import getpass


def login():
    db=input("Enter the User Name ")
    ps=getpass("Enter the Password to login ")

    if db=="" or ps=="":
        print("Error All fields are required ")
    else:
        try:
            log=s.connect(host='localhost',user='root',password='Kaletha@123',database='management')
            cursor=log.cursor()
            
            sql="select userid,password from login where userid=%s and password=%s"
            cursor.execute(sql,(db,ps))
            tupl_rs=cursor.fetchall()
            if db==tupl_rs[0][0] and ps==tupl_rs[0][1]:
                print('*****WELCOME*****')
                import mycm_m
                mycm_m.perform_operations()
            else:
                print("Enter the Valid Password")
                return login()
        except Exception as e:
            print('Error',f'Due to {str(e)}')
            return login()
    
login()    



