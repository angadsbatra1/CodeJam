from flask import Flask, render_template, request, redirect
import sqlite3
import click
import pandas as pd
query1 = []
data = pd.read_csv('C:\\Users\\CodeJam\\Downloads\\CodeJam_FilteredCourses.csv')
data['duration'] = data['duration'].replace(' total hours','')

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search',methods = ['POST', 'GET'])
def search():
    if request.method == 'POST':
        print(request.form)
        query1 = data[data.rating > float(request.form["lower_rating"]) ]
        query1 = query1[query1.rating < float(request.form["upper_rating"]) ]
        query1 = query1[query1.duration > float(request.form["lower_duration"]) ]
        query1 = query1[query1.duration < float(request.form["upper_duration"]) ]
        query1 = query1[query1.num_published_lectures > float(request.form["lower_lectures"]) ]
        query1 = query1[query1.num_published_lectures < float(request.form["upper_lectures"]) ]
        lst = list(query1["title"])
        string = ""
        for i in range(len(lst)):
            string += (str(i) + ". " + lst[i] + " <br> ")
        return string
    else:
        return render_template("search.html")


@app.route('/copy')
def copy():
    return render_template("base copy.html")

if __name__ == "__main__":
    app.run(debug=True)





