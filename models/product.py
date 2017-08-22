from config import notifs

class product:
    def __init__(self, db, product_id, name=None):
        self.db = db
        if name is None:
            if not isinstance(product_id, (long, int)):
                raise Exception(notifs.errors['invalid_pid'])
            product = self.get_product(product_id)
            if product is not False:
                self.id, self.name = product[0], product[1]
            else: 
                raise Exception(notifs.errors['invalid_pid'])
        
        # if name is not none, that means a new product
        # Todo: implement db insertion new product name.

    def get_product(self, product_id):
        query = """ SELECT * FROM `product` WHERE id = ?"""
        product = self.db.select(query, [product_id])
        if (not product):
            return False
        else:
            return product.pop()
