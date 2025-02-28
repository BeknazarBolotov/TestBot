import sqlite3
from db import queries

db = sqlite3.connect('db/db.sqlite')
cursor = db.cursor()

async def create_tables():
    if db:
        print('База данных подключена')
        cursor.execute(queries.TABLE_products)



async def sql_insert_products(name_product, category, size, price, product_id, photo):
    cursor.execute(queries.INSERT_TABLE_products, (name_product, category, size, price, product_id, photo))
    db.commit()


#==================================================



def get_db_connection():
    conn = sqlite3.connect('db/db.sqlite')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    select * from products p 
    """).fetchall()
    conn.close()
    return products