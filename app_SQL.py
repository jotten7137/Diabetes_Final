#dependencies
import os
from flask_sqlalchemy import SQLAlchemy
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

app = Flask(__name__)

#SQL url
password = "#######" #specify your db password here
app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('DATABASE_URL',f'mysql://root:{password}@localhost:3306/')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db
db = SQLAlchemy(app)

class Nutrition(db.Model):
    __tablename__ = 'comments'

    #to be used lower
    string = db.String(64)
    integer= db.Integer

    col1 = db.Column(db.Integer, primary_key=True)
    col2 = db.Column(string)
    col3 = db.Column(integer)
    col4 = db.Column()
    col5 = db.Column()
    col6 = db.Column()
    col7 = db.Column()
    
    def __repr__(self):
        return '<####### %r>' % (self.name)

#### ROUTES #####
#Home Route
@app.route('/')
def home():
    return render_template('index.html')

#Form Route - (if applicable)
@app.route("/send",methods=['GET','POST'])
def send():
    if request.method=="POST":
        col1 = request.form['1']
        col2 = request.form['2']
        col3 = request.form['3']
        col4 = request.form['4']
        col5 = request.form['5']
        col6 = request.form['6']
        col7 = request.form['7']
        # ... keep adding based on columns in db

        nutrition_db = Nutrition(col1=col1, col2=col2, col3=col3, col4=col4, col5=col5, col6=col6, col7=col7)
        db.session.add(nutrition_db)
        db.session.commit()
        return redirect('/', code=302)
    return render_template('form.html')

#API Route
@app.route('/api/nutrition')
def nutrition():
    results = db.session.query(
        Nutrition.col1,
        Nutrition.col2,
        Nutrition.col3,
        Nutrition.col4,
        Nutrition.col5,
        Nutrition.col6,
        Nutrition.col7).all()
        # ... keep adding based on columns in db
    
    #future state -> for loop this
    col1 = [result[0] for result in results]
    col2 = [result[1] for result in results]
    col3 = [result[2] for result in results]
    col4 = [result[3] for result in results]
    col5 = [result[4] for result in results]
    col6 = [result[5] for result in results]
    col7 = [result[6] for result in results]
    # ... keep adding based on columns in db

    nutrition_data = [{
        "col1": col1,
        "col2": col2,
        "col3": col3,
        "col4": col4,
        "col5": col5,
        "col6": col6,
        "col7": col7
        # ... keep adding based on columns in db
    }]
    return jsonify(nutrition_data)
        
#lazy loading
if __name__ == '__main__':
    app.run(debug=True)
