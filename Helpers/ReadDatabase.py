import pymysql
import pytest
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utilities.connectDatabase import Mysql


'''
def get_data(query):
    conn_cls = Mysql()
    conn = conn_cls.get_conection()
    expect_data =[]
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        all_data = cursor.fetchall()
        for data in all_data:
            expect_data.append(data)
    finally:
        
        cursor.close()
        conn.close()
        
      
    return expect_data

'''
def get_data(query, params= None):
    # Replace with your actual database connection details
    conn_cls = Mysql()
    conn = conn_cls.get_conection()
    expect_data =[]
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        all_data = cursor.fetchall()
        for data in all_data:
            expect_data.append(data)
    finally:
        cursor.close()
        conn.close()
    return expect_data