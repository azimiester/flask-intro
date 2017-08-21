import sqlite3

#make connection
conn = sqlite3.connect('python_flask.db')
c = conn.cursor()

#create products table
create_product = """
					CREATE TABLE IF NOT EXISTS  product(id INTEGER PRIMARY KEY, name TEXT NOT NULL)
				 """
c.execute(create_product)


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
c.execute(create_review)

#add products in table.
products = [(815, 'Foobar-Soundsystem'), (1337, 'Soundblaster Pro')]
add_product = """INSERT INTO product VALUES (?, ?) """
c.executemany(add_product, products)





