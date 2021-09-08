from flask import Flask, render_template

app = Flask(__name__)

headings = ("Name", "GPA", "Age", "Department", "Province", "Gender")
data = (
    ("Abdullah", "2.8", "21", "econometrics", "adana", "male"),
    ("Kaan", "1.5", "21", "econometrics", "adana", "male"),
    ("Talha", "1.65", "21", "economics", "hatay", "male"),
    ("Rabia", "2.5", "22", "economics", "adana", "female")
)

@app.route("/")
def table():
    return render_template("table.html", headings = headings, data = data)