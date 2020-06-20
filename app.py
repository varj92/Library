from flask import Flask, render_template,request,redirect,url_for
from firebase import db
#import uuid

app = Flask(__name__)

@app.route('/')
def Index():
    #book_id = random.random()
    all_books = db.child("books").get()
    if all_books.val() == None:
        return render_template('index.html')
    else:
        return render_template('index.html', books_lst= all_books)
    
@app.route('/add_book', methods = ['POST'])
def add_book():
    #book_id = uuid.uuid1().hex
    #id_b = str(book_id.hex)
    name = request.form['name']
    author = request.form['author']
    data = {
            #"id":book_id,
            "name": name,
            "author": author
            }
    db.child("books").push(data)
    #flash('Book Added!')
    return redirect("/")

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        name = request.form['name']
        author = request.form['author']
        data = {
            "name": name,
            "author": author
            }
        #update the book
        db.child("books").child(id).update(data)
        return redirect("/")
    
    book = db.child("books").order_by_key().equal_to(id).get()
    return render_template('edit.html', data = book)

@app.route("/delete/<id>", methods=["POST"])
def delete(id):
    db.child("books").child(id).remove()
    return redirect("/")

###################################################################################################
if __name__ == '__main__':
    app.run(debug=True)