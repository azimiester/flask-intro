# class responsible for a single review.
from config import notifs
from models.product import *

class review:

    def __init__(self, db, id_=None, product_id=None, rating = None, user_id = None, comment = None ):
        self.db = db

        # constructor overloading the pythonic way could have been done. 
        if id_ is None:
            if not isinstance(rating, (long, int)) or not (rating <= 5 and rating >= 0) : 
                raise Exception(notifs.errors['invalid_rating'])
            
            self.product = product(db, product_id)
            self.rating = rating
            self.user_id = user_id
            self.comment = comment
        elif id_ is not None:
            r = self.get_review(id_)
            if r is not False:
                self.product = product(db, r[1])
                self.user_id = r[2]
                self.rating = r[3] 
                self.comment = r[4]
                self.id = id_
            else:
                raise Exception(notifs.errors['invalid_arguments'])

    # pretty cool op overloading!
    def __eq__(self, other):
        return self.id == other

    def get_object(self):
        return {
            'id': self.id,
            'pid': self.product.id,
            'rating': self.rating,
            'uid': self.user_id,
            'comment': self.comment
        }

    def get_review(self, id_):
        query = """SELECT * FROM review where id = ? """

        rv = self.db.select(query, [id_])
        if (not rv):
            return False
        else:
            return rv.pop()

    def delete_review(self, id_):
        query = """DELETE FROM review where id = ? """
        return self.db.update_delete(query, [id_])

    def set_review(self):
        query = """INSERT INTO review(pid, uid, rating, comment) VALUES (?,?,?,?)"""
        params = [self.product.id, self.user_id, self.rating, self.comment]
        review_id = self.db.insert(query, params)
        if (review_id is False):
            raise Exception(notifs.errors['invalid_review'])
        self.id = review_id

# TODO: Implement update/delete if needed; not needed..