from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
# import database tables
from database_setup import Base, User, Category, Topic

app = Flask(__name__)

# create a connection to database
engine = create_engine('mysql+mysqldb://root:admin@127.0.0.1:3306/marriedtochinese1', echo=True)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
##################### end

@app.route('/')
@app.route('/categories/')
def showCategories():
  return render_template('showCategories.html')

@app.route('/categories/new', methods=['GET','POST'])
def newShowCategories():
  if request.method == 'POST':
    name = request.form['name']
    description = request.form['description']
    # test = session.query(Category).filter_by(name = 'coco').one()
    # print test + 'this is printing of test'
    # print test.name + 'this is printing of one variable'
    print Category
    newCategory = Category(name = name, description = description)
    session.add(newCategory)
    session.commit()
  else:
    return render_template('newShowCategories.html')

@app.route('/categories/<int:category_id>/list/')
def Category(category_id):
  return render_template('category.html')

@app.route('/categories/<int:category_id>/list/<int:story_id>/')
def Story(category_id, story_id):
  return render_template('story.html')

if __name__ == '__main__':
  app.debug = True
  app.run(host = '0.0.0.0', port = 11000)
