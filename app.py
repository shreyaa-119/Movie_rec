from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

# ---------------- MySQL Connection ----------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Shreyya1!'   # put your MySQL password here
app.config['MYSQL_DB'] = 'moviedb'

mysql = MySQL(app)

# ---------------- Routes ----------------
@app.route('/')
def home():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM movies LIMIT 20;")  # ✅ correct table name
    movies = cur.fetchall()
    cur.close()
    return render_template('index.html', movies=movies)

@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.form['genre']
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """
        SELECT m.title, m.genres, AVG(r.rating) AS avg_rating
        FROM movies m
        JOIN ratings r ON m.movie_id = r.movie_id
        WHERE m.genres LIKE %s
        GROUP BY m.movie_id
        ORDER BY avg_rating DESC
        LIMIT 10;
    """
    cur.execute(query, ('%' + genre + '%',))
    results = cur.fetchall()
    cur.close()
    return render_template('recommendations.html', movies=results, genre=genre)

if __name__ == '__main__':
    app.run(debug=True)
