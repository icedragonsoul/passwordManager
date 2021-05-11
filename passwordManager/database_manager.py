import psycopg2
import json
import mysql.connector



def store_passwords(password, user_email, username, url, app_name):
    #try:
        connection = connect()
        cursor = connection.cursor(buffered=True)
        postgres_insert_query = """ INSERT INTO `password`.`accounts` (password, user_email, username, url, app_name) VALUES (%s, %s, %s, %s, %s)"""
        record_to_insert = (password, user_email, username, url, app_name)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        connection.close()
    #except (Exception, psycopg2.Error) as error:
        #print("oh no")
        #print(error)

def connect():
    #try:
        connection = mysql.connector.connect(host="localhost", user="root", password="root")
        print(connection)
        mycursor = connection.cursor()
        # app_name = 'a'
        # mycursor.execute("SELECT * FROM `password`.`accounts` WHERE app_name = '""" + app_name + "'", app_name)
        # myresult = mycursor.fetchall()
        # print("test")  
        # print (myresult[0][1])
        return connection
    #     connection = psycopg2.connect(user='root', password='root', host='127.0.0.1', database='password', port='3306')
    #     return connection
    # except (Exception, psycopg2.Error) as error:
    #     print(error)

def find_password(app_name):
    # try:
        connection = connect()
        cursor = connection.cursor(buffered=True)
        postgres_select_query = """ SELECT password FROM `password`.`accounts` WHERE app_name = '""" + app_name + "'"
        cursor.execute(postgres_select_query, app_name)
        connection.commit()
        result = cursor.fetchall()
        try:
            print('Password is: ' )
            print(result[0][0])
        except:
            print ("password not found")
            
        cursor.close()
    
    # except (Exception, psycopg2.Error) as error:
    #     print(error)
def find_users(user_email):
    data = ('Password: ', 'Email: ', 'Username: ', 'url: ', 'App/Site name: ') 
    try:
        connection = connect()
        cursor = connection.cursor(buffered=True)
        postgres_select_query = """ SELECT * FROM `password`.`accounts` WHERE user_email = '""" + user_email + "'"
        cursor.execute(postgres_select_query, user_email)
        connection.commit()
        result = cursor.fetchall()
        print('')
        print('RESULT')
        print('')
        for row in result:
            for i in range(0, len(row)-1):
                print(str(data[i]) + str(row[i]))
        print('')
        print('-'*30)
        cursor.close()
        
        
    except (Exception, psycopg2.Error) as error:
        print(error)
