TABLE_products = """
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    category TEXT,
    size TEXT,
    price TEXT,
    product_id TEXT,
    photo TEXT
    )
"""


INSERT_TABLE_products = """
    INSERT INTO products (name_product, category, size, price, product_id, photo)
    VALUES (?, ?, ?, ?, ?, ?)
"""