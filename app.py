from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model): 
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    description = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.now)
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
        




@app.route("/", methods = ['GET','POST'])
   
#represents home page
     
def hello_world():
    if (request.method == "POST"):
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title = title, description = desc)
        db.session.add(todo)
        db.session.commit()
    
    alltodo = Todo.query.all()
    print(alltodo)
    return render_template("index.html", alltodo = alltodo)
    # return "<p>Hello, World!</p>"




@app.route("/update/<int:sno>", methods = ['GET','POST'])
#endpoints
def update(sno):
    if (request.method == 'POST'):
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno = sno).first()
        todo.title = title
        todo.description = desc
        db.session.commit()
        return redirect("/")
        
    
    todo = Todo.query.filter_by(sno = sno).first()
    return render_template('update.html', todo = todo)
    # return "<p> Hello this is Products page</p>"


@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno = sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")
    
if(__name__ == "__main__"):
    app.run(debug=True,port=8000)
    app.config['DEBUG'] = True