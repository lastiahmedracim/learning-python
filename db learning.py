import sqlite3

db = sqlite3.connect("app.db")

cr = db.cursor()

cr.execute("Create Table if not exists Users(user_id integer, name text)")
cr.execute("Create Table if not exists Skills(name text,progress integer, user_id integer)")

#cr.execute("Insert Into Users(user_id, name) Values (1,'Ahmed')")
#cr.execute("Insert Into Users(user_id, name) Values (2,'Sayed')")
#cr.execute("Insert Into Users(user_id, name) Values (3,'Osama')")

my_list = ["Ahmed", "Sayed", "Osama", "kamel", "Ibrahim", "Sameh", "Enas"]

for key, user in enumerate(my_list):
    cr.execute(f"Insert Into Users(user_id, name) Values({key + 1},'{user}')")

db.commit()

db.close() 

# new shit