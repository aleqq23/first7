# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify, render_template, redirect, request, url_for
import json

from datetime import datetime
import pytz
import mysql.connector

app = Flask(__name__)
comments = []
koments = []
momentr=[]

@app.route('/melluzhi', methods=["GET", "POST"])
def mel():

    mydb = mysql.connector.connect(
        host="asafrey074.mysql.pythonanywhere-services.com",
        user="asafrey074",
        passwd="lakroda23",
        database="asafrey074$melluzhi",
    )

    mycursors = mydb.cursor()

    if request.method == "GET":
        mycursors.execute("SELECT Autors, Komentars, Datums FROM Complaints")
        koments0 = mycursors.fetchall()

        mycursors.execute("SELECT Name, Surname, Exam_name, Exam_date FROM Registrations1")
        exams1 = mycursors.fetchall()

        mycursors.execute("SELECT Name, Surname, Crime_date, Crime_cause, Criminal_status, Law_abuse, Punishments, Prison_time, Attendance FROM Punishments1")
        crimes1 = mycursors.fetchall()
        mydb.close()
        return render_template("melluzhi.html", koments0=koments0, exams1=exams1, crimes1=crimes1)


    if request.method == "POST":
        autors0 = request.form.get("autors0", "").strip()
        komentars_mel = request.form.get("komentars_mel", "").strip()

        name1 = request.form.get("first_name1", "").strip()
        surname1 = request.form.get("last_name1", "").strip()
        examname1 = request.form.get("exc", "").strip()
        examdate1 = request.form.get("birthday1", "").strip()


        name2 = request.form.get("first_name2", "").strip()
        surname2 = request.form.get("last_name2", "").strip()
        crimedate = request.form.get("date2", "").strip()
        crimecause2 = request.form.get("crimecause2", "").strip()
        crimstatus = request.form.get("exc2", "").strip()
        lawabuse = request.form.get("laws2", "").strip()
        punishment2 = request.form.get("punishment2", "").strip()
        prisontime2 = request.form.get("prisontime", "").strip()
        attend2 = request.form.get("exc21", "").strip()

        if autors0 and komentars_mel:
           riga_time = datetime.now(pytz.timezone('Europe/Riga'))
           sql0 = "INSERT INTO Complaints (Autors, Komentars, Datums) VALUES (%s, %s, %s)"
           mycursors.execute(sql0, (autors0, komentars_mel, riga_time))

        if name1 and surname1 and examname1 and examdate1:
           sql1 = "INSERT INTO Registrations1 (Name, Surname, Exam_name, Exam_date) VALUES (%s, %s, %s, %s)"
           mycursors.execute(sql1, (name1, surname1, examname1, examdate1))

        if name2 and surname2:
           sql2 = "INSERT INTO Punishments1 (Name, Surname, Crime_date, Crime_cause, Criminal_status, Law_abuse, Punishments, Prison_time, Attendance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
           mycursors.execute(sql2, (name2, surname2, crimedate, crimecause2, crimstatus, lawabuse, punishment2, prisontime2, attend2))

        mydb.commit()
        mydb.close()
        return redirect(url_for('mel'))

    if __name__ == "__main__":
        app.run(debug=True)