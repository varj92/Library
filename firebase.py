import pyrebase

config = {
  "apiKey": "AIzaSyCBJFEu7DpRnhwaQPunDAfAAqf7ae81cdY",
  "authDomain": "users-2c2b6.firebaseapp.com",
  "databaseURL": "https://users-2c2b6.firebaseio.com",
  "storageBucket": "users-2c2b6.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
# data = {"first": 'Haruo',"last": 'Nakano',"born":'1930'}
# db.child("users").push(data)

# all_users = db.child("users").get()
# print(all_users.val(first))
# print('\n')
# all_users = db.child("users").get()
# for user in all_users.each():
#     print(user.val()) # {name": "Mortimer 'Morty' Smith"}

