from db_func import Database
# Path: py-script\db_func.py

db = Database("words.csv")
db.merge_awk_db("awk-export.txt")

print(db.content)