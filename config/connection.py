import sqlite3
import config

class db_con:
	def __init__(self):
		self.conn = sqlite3.connect(config.db, timeout=1)
		self.cur = self.conn.cursor()

	def execute(self, query, params):
		try:
			self.cur.execute(query, params)
			self.conn.commit()
			return True
		except Exception as err: 
			print(str(err))
			return False
	
	def insert(self, query, params):
		if self.execute(query, params):
			return self.cur.lastrowid
		else:
			return False

	def update_delete(self, query, params):
		return self.execute(query, params)

	def select(self, query, params):
		if (self.execute(query, params)):
			return self.cur.fetchall()
		else:
			return False

	def close_conn(self):
		self.conn.close()