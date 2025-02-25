import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
# Load environment variables
load_dotenv()

app = Flask(__name__)

# Database Config
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model Attendance
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    student_id = db.Column(db.String(100), unique=True, nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    major = db.Column(db.String(100), nullable=False)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/presensi", methods=["POST"])
def presensi():
    name = request.form['name']
    student_id = request.form['student_id']
    subject = request.form['subject']
    major = request.form['major']

    new_entry = Attendance(name=name, student_id=student_id, subject=subject, major=major)
    db.session.add(new_entry)
    db.session.commit()

    return redirect(url_for('after_submit'))


# Route untuk menampilkan hasil setelah submit
@app.route('/after-submit')
def after_submit():
    attendees = Attendance.query.with_entities(Attendance.id, Attendance.name).all()
    return render_template('after-submit.html', attendees=attendees)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
