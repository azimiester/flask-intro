# class for multiple reviews: aggregation, summary etc.
from config import notifs
from models.product import *
import datetime

class reviews:

    def get_date_arr(self, date_from, date_to):
        try:
            date_from = datetime.datetime.strptime(date_from, "%d-%m-%Y")
            date_to = datetime.datetime.strptime(date_to, "%d-%m-%Y")
            if date_to < date_from:
                return False
            return [date_from, date_to]
        except Exception as e:
            return False

    def product_preprocessing(self, pid, date_from, date_to):
        if not pid:
            raise Exception(notifs.errors['invalid_pid'])
        p = product(self.db, pid)
        date_arr = self.get_date_arr(date_from, date_to)

        if not date_arr:
            raise Exception(notifs.errors['invalid_arguments'])
        return p, date_arr

    def beautify_summary(self, summary):
        # fill up missing rating and find percentages.
        sum_map = {}
        count = 0
        for val in summary:
            sum_map[val[0]] = {'count' : val[1]}
            count+= val[1]
        for i in range (0,6):
            if (i in sum_map ):
                sum_map[i]['perc'] = (float(sum_map[i]['count'])/float(count))*100
            else:
                sum_map[i] = {'count': 0, 'perc': float(0.0)}
        return {'total_count': count, 'summary': sum_map}

    def __init__(self, db):
        self.db = db

    def get_product_summary(self, pid, date_from, date_to):
        p, date_arr = self.product_preprocessing(pid, date_from, date_to)
        query = """SELECT rating, count(*) FROM review WHERE pid = ? and ts >= ? and ts <= ? group by rating"""
        return self.beautify_summary(self.db.select(query, [p.id, date_arr[0], date_arr[1]]))

    def get_product_reviews(self, pid, date_from, date_to):
        p, date_arr = self.product_preprocessing(pid, date_from, date_to)

        # TODO: Extend to receive page num and return reviews using limit offset; not needed for now.
        query = """SELECT * FROM review WHERE pid = ? and ts >= ? and ts <= ?"""
        return self.db.select(query, [p.id, date_arr[0], date_arr[1]])
