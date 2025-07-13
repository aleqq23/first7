# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, redirect, request, url_for
from datetime import datetime
import pytz
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, world!"

@app.route('/melluzhi', methods=["GET", "POST"])
def mel():
    # Подключение к базе
    mydb = mysql.connector.connect(
        host="sql7.freesqldatabase.com",  # замени на свой host
        user="sql7788941",                # замени на свой user
        passwd=os.environ.get('DB_PASS'), # пароль из переменной окружения
        database="sql7788941",            # замени на имя своей базы
        port=3306
    )
    mycursor = mydb.cursor()

    if request.method == "GET":
        mycursor.execute("SELECT Autors, Komentars, Datums FROM Complaints")
        koments0 = mycursor.fetchall()

        mycursor.execute("SELECT Name, Surname, Exam_name, Exam_date FROM Registrations1")
        exams1 = mycursor.fetchall()

        mycursor.execute("SELECT Name, Surname, Crime_date, Crime_cause, Criminal_status, Law_abuse, Punishments, Prison_time, Attendance FROM Punishments1")
        crimes1 = mycursor.fetchall()

        mydb.close()
        return render_template("melluzhi_render.html", koments0=koments0, exams1=exams1, crimes1=crimes1)

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

        name3 = request.form.get("first_name3", "").strip()
        surname3 = request.form.get("last_name3", "").strip() 
        datetimein = request.form.get("date21", "").strip() 
        datetimeout = request.form.get("date22", "").strip() 
        citstatus = request.form.get("exc5", "").strip() 
        pers_code3 = request.form.get("pers_code", "").strip() 
        sudimost = request.form.get("exc6", "").strip() 
        dopkom3 = request.form.get("dopkom", "").strip() 
        
        if autors0 and komentars_mel:
            riga_time = datetime.now(pytz.timezone('Europe/Riga'))
            sql0 = "INSERT INTO Complaints (Autors, Komentars, Datums) VALUES (%s, %s, %s)"
            mycursor.execute(sql0, (autors0, komentars_mel, riga_time))

        if name1 and surname1 and examname1 and examdate1:
            riga_time = datetime.now(pytz.timezone('Europe/Riga'))
            sql1 = "INSERT INTO Registrations1 (Name, Surname, Exam_name, Exam_date, Registracijas_datums) VALUES (%s, %s, %s, %s, %s)"
            mycursor.execute(sql1, (name1, surname1, examname1, examdate1, riga_time))

        if name2 and surname2:
            sql2 = "INSERT INTO Punishments1 (Name, Surname, Crime_date, Crime_cause, Criminal_status, Law_abuse, Punishments, Prison_time, Attendance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            mycursor.execute(sql2, (name2, surname2, crimedate, crimecause2, crimstatus, lawabuse, punishment2, prisontime2, attend2))
        if name3 and surname3:
            sql3 = "INSERT INTO `Arrivals1`(`Имя`, `Фамилия`, `Дата и время въезда`, `Дата и время выезда`, `Гражданский статус`, `Персональный код`, `Судимость`, `Комментарии`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            mycursor.execute(sql3, (name3, surname3, datetimein, datetimeout, citstatus, pers_code3, sudimost, dopkom3))

        mydb.commit()
        mydb.close()
        return redirect(url_for('mel'))

if __name__ == "__main__":
    app.run(debug=True)

