# class responsible for a single review.
from flask_intro import notifs
from models.product import *

class review:

    def __init__(self, db, id=None, product_id=None, rating = None, user_id = None, comment = None ):
        self.db = db

        if id is None:
	        if not isinstance(rating, (long, int)) and (rating > 5 or rating < 0) : 
	        	raise Exception(notifs.errors.invalid_rating)
	        
	        self.product = product(db, product_id)
	        self.rating = rating
	        self.user_id = user_id
	        self.comment = comment
        elif id is not None:
        	review = self.get_from_id(id)
        	if review is False:
        		raise Exception(notifs.errors.invalid_arguments)
    		self.product, self.user_id, self.rating, self.comment = product(db, review[0]), review[1], review[2], review[3]
    	else:
    		raise Exception(notifs.errors.invalid_arguments)

	def get_from_id(self, id):
		query = """SELECT * FROM review where id = ? """
		review = self.db.select(query, [id])
        if (review is False or len(review) is 0):
            return False
        else:
            return review.pop()

    def set(self):
    	query = """INSERT INTO review(pid, uid, rating, comment) VALUES (?,?,?,?)"""
    	params = [self.product.id, self.user_id, self.rating, self.comment]
    	review_id = self.db.insert(query, params)
    	if (review_id is False):
    		raise Exception(notifs.errors.invalid_review)
    	self.id = review_id

# TODO: Implement update/delete if needed.