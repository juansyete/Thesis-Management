from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///thesis.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Thesis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    student = db.Column(db.String(100), nullable=True)
    advisor = db.Column(db.String(100), nullable=True)

with app.app_context():
    db.create_all()

@app.route('/add_thesis', methods=['GET', 'POST'])
def add_thesis():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        student = request.form.get('student')
        advisor = request.form.get('advisor')

        new_thesis = Thesis(title=title, author=author, year=year, student=student, advisor=advisor)
        db.session.add(new_thesis)
        db.session.commit()

        return redirect(url_for('show_theses'))

    return render_template('add_thesis.html')

@app.route('/theses')
def show_theses():
    theses = Thesis.query.all()
    return render_template('theses.html', theses=theses)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        if 'action' in request.form and request.form['action'] == 'add_thesis':
            # Redirect to the add_thesis page
            return redirect(url_for('add_thesis'))
        
        search_query = request.form['query']  # The user's search input

        # Query the database
        search_results = Thesis.query.filter(
            (Thesis.title.like(f'%{search_query}%')) |
            (Thesis.author.like(f'%{search_query}%')) |
            (Thesis.year.like(f'%{search_query}%'))
        ).all()

        return render_template('search_results.html', theses=search_results, query=search_query)

    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)
