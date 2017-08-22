# flask-intro
A python Flask based API.

# How to run:
1. Clone Repository.
2. Install packages from requirements.txt (I suggest using virtualenv)
3. in the project root run python app.py
4. access it with http://127.0.0.1:5000/

# Api Methods Implemented:

| Method | 	End Point                                 |	Auth | Data Required | Purpose | 
| -------|--------------------------------------------|------| ------------- | -------- |
| GET	   | /review/<review_id>                             |	NO	 | In URL	                    | Get a single Review |
| POST   | /review/	                                  | NO	 | pid, uid, rating, comment	| Add a new Review |
| GET	   | /review/reviews/<p_id>/<date_from>/< date_to> | YES  | In URL	                    | All reviews for a product |
| GET	   | /review/summary/<p_id>/<date_from>/<date_to>  | YES  | In URL                       | Summary for a product |
| DELETE | /review/<id>                             | YES  | In URL	                    | Delete review |


For Authenticated end pointest, the username is username and password is password.
