from flask import Flask, render_template
# import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # # Get the testimonials
    # sqliteConnection = sqlite3.connect('db/sitedata.db', timeout=20)
    # cursor = sqliteConnection.cursor()
    # cursor.execute("SELECT * from testimonials")
    # testimonials = cursor.fetchall()
    # cursor.close()
    # # Get the properties
    # sqliteConnection = sqlite3.connect('db/sitedata.db', timeout=20)
    # cursor = sqliteConnection.cursor()
    # cursor.execute("select * from propertyinfo p order by random() limit 6")
    # propinfo = cursor.fetchall()
    # cursor.close()
    
    # return render_template('index.html',testimonials=testimonials,propinfo=propinfo)
    return render_template('index.html')

@app.route('/vm')
def vm():
    return render_template('vm.html')

# @app.route('/search')
# def search():
#     return render_template('search.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)