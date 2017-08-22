from connection import *
# from models.review import * 

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
						ts DATETIME DEFAULT CURRENT_TIMESTAMP,
						FOREIGN KEY(pid) REFERENCES product(id) 
					)
				"""
db.insert(create_review, ())

#add products in table.
products = [(815, 'Foobar-Soundsystem'), (1337, 'Soundblaster Pro')]
add_product = """INSERT INTO product VALUES (?, ?) """

for product in products:
	db.insert(add_product, product)


# def get_random_rating():
#     products = [1337, 815]
#     review = randint(0, 5)
#     product_id = products[randint(0, 1)]
#     return review, product_id

# for i in range(1000):
#     pid , review, uid, comment = get_random_rating(), None, None
#     r = review(db, None, pid, review, uid, comment)
#     r.set_review()





