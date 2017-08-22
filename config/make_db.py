from connection import *

db = db_con()
#create products table
create_product = """
					CREATE TABLE IF NOT EXISTS  product(id INTEGER PRIMARY KEY, name TEXT NOT NULL)
				 """
db.insert(create_product, ())


#create reviews table
create_review = """
					CREATE TABLE IF NOT EXISTS review 
					( 
						id INTEGER PRIMARY KEY,
						pid INTEGER NOT NULL,
						uid INTEGER,
						rating INTEGER NOT NULL,
						comment TEXT,
						FOREIGN KEY(pid) REFERENCES product(id) 
					)
				"""
db.insert(create_review, ())

#add products in table.
products = [(815, 'Foobar-Soundsystem'), (1337, 'Soundblaster Pro')]
add_product = """INSERT INTO product VALUES (?, ?) """

for product in products:
	db.insert(add_product, product)





