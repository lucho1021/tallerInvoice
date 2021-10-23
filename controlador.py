from pymysql import connect
from confidb import get_conexion

def add_cliente(name, status, mobile):
    cnn = get_conexion()
    with cnn.cursor() as cursor:
        cursor.execute("INSERT INTO INVOICE (name, status, mobile) VALUES (%s,%s,%s)",(name, status, mobile))
    cnn.commit()
    cnn.close()

def update_cliente(name, status, mobile, id):
    cnn = get_conexion()
    with cnn.cursor() as cursor:
        cursor.execute("UPDATE INVOICE SET name = %s, status = %s, mobile = %s WHERE id = %s", (name, status, mobile, id)) 
    cnn.commit()   
    cnn.close()

def delete_cliente(id):
    cnn = get_conexion():
    with cnn.cursor() as cursor:
        cursor.execute("DELETE FROM INVOICE WHERE id = %s", (id))
    cnn.commit()
    cnn.close()

def get_clientes():
    cnn = get_conexion()
    INVOICES = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, status, mobile FROM customer")
        INVOICES = cursor.fetchall()
    cnn.close()
    return INVOICES

def get_cliente_id(id):
    cnn = get_conexion()
    INVOICE = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, status, mobile FROM customer WHERE id = %s", (id))
        INVOICE =cursor.fetchone()
    cnn.close
    return INVOICE