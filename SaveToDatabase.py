
from datetime import datetime

import mysql.connector
from mysql.connector import Error
import dbConfig

def Save(args,storedProcedure):
    try:

        connection = mysql.connector.connect(host=dbConfig.host,
                                             database=dbConfig.database,
                                             user=dbConfig.user,
                                             password=dbConfig.password)
        if connection.is_connected():
            # db_Info = connection.get_server_info()
            # print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.callproc(storedProcedure, args)
            connection.commit()
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def GetData(storedProcedure):
    output=[]
    try:

        connection = mysql.connector.connect(host=dbConfig.host,
                                             database=dbConfig.database,
                                             user=dbConfig.user,
                                             password=dbConfig.password)
        if connection.is_connected():
            # db_Info = connection.get_server_info()
            # print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.callproc(storedProcedure)

            # print out the result
            for result in cursor.stored_results():
                output=result.fetchall()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return output