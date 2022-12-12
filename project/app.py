from flask import Flask, render_template, request, redirect, send_file, session
import pickle
from matplotlib.backend_bases import FigureCanvasBase
from flask_mysqldb import MySQL
import os
import matplotlib.pyplot as plt
from datetime import datetime

app = Flask(__name__)

#Database Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cancerapp'
mysql = MySQL(app)

app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start')
def start():
    if 'user_id' in session:
        return redirect('/options')
    else:
        return redirect('/login')

@app.route('/login')
def logIn():
    return render_template('login.html')

@app.route('/register')
def signUp():
    return render_template('register.html')

@app.route('/loginValidation', methods=['POST'])
def loginValitacion():
    email = request.form.get('email')
    password = request.form.get('password')
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'".format(email, password))
    users = cur.fetchall()
    
    if len(users)>0:
        session['user_id'] = users[0][0]
        return redirect('/options')
    else: 
        return redirect('/register') 

@app.route('/addUser', methods=['POST'])
def addUser():
    name = request.form.get('nname')
    license = request.form.get('nlicense')
    hospital = request.form.get('nhospital')
    email = request.form.get('nemail')
    password = request.form.get('npassword')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (name, license, hospital, email, password) VALUES ('{}','{}','{}','{}','{}')".format(name, license, hospital, email, password))
    mysql.connection.commit()

    cur.execute("SELECT * FROM users WHERE email LIKE '{}'".format(email))
    myuser = cur.fetchall()
    session['user_id'] = myuser[0][0]
    return redirect('/options')

model = pickle.load(open('lr_breastCancer.pkl', 'rb'))

@app.route("/predictor")
def hello():
    if 'user_id' in session:
        return render_template('predictor.html')
    else:
        return redirect('/login')


@app.route("/patients")
def view():
    if 'user_id' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM patient")
        patients = cur.fetchall()
        return render_template('patientsSaved.html', patients = patients)
    else:
        return redirect('/login')

@app.route("/options")
def choose():
    if 'user_id' in session:
        return render_template('options.html')
    else:
        return redirect('/login')

@app.route("/predict", methods=['POST'])
def predict():
    radius = float(request.form['radius'])
    texture = float(request.form['texture'])
    perimeter = float(request.form['perimeter'])
    area = float(request.form['area'])
    smoothness = float(request.form['smoothness'])
    compactness = float(request.form['compactness'])
    concavity = float(request.form['concavity'])
    concave_points = float(request.form['concave_points'])
    symmetry = float(request.form['symmetry'])
    fractal_dimension = float(request.form['fractal_dimension'])
    
    prediction = model.predict([[radius, texture, perimeter, area, smoothness, compactness, concavity,	concave_points,	symmetry, fractal_dimension]])
    diagnosis = prediction[0]
    if (diagnosis==0):
        tumor='Benign'
    else:
        tumor='Malignant'

    proba = model.predict_proba([[radius, texture, perimeter, area, smoothness, compactness, concavity,	concave_points,	symmetry, fractal_dimension]])
    percent = []
    percent.append(round(proba[0][0]*100, 2))
    percent.append(round(proba[0][1]*100,2))

    plt.style.use('seaborn-whitegrid')
    plt.rcParams["figure.figsize"] = [7, 4]
    plt.rcParams["figure.autolayout"] = True
    labels = ['Benign', 'Malignant']

    plt.figure()
    plt.title('Prediction Graph', fontsize=22, weight="medium")
    plt.ylabel('Percentage %', fontsize=16, fontname="Helvetica", weight="light")
    plt.xlabel('Diagnosis', fontsize=16, fontname="Helvetica", weight="light")

    p1 = plt.bar(labels, percent, color='#FF87B0')
    plt.tick_params(axis='x', labelsize=14)
    plt.tick_params(axis='y', labelsize=14)

    for rect1 in p1:
        height = rect1.get_height()
        plt.annotate( "{}%".format(height),(rect1.get_x() + rect1.get_width()/2, height+.05),ha="center",va="bottom",fontsize=15)
    plt.savefig('static/images/my_plot.png')


    #DataBase Insert's
    namePa = request.form.get('fullname')
    age = request.form.get('age')
    address = request.form.get('address')
    telephone = request.form.get('telephone')
    email = request.form.get('emailPacient')
    #Date 
    now = datetime.now()
    date = ('{}-{}-{}').format(now.year, now.month, now.day)

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO patient (name, age, address, telephone, email, diagnosis, diagnosisDate) VALUES ('{}', '{}','{}','{}','{}','{}','{}')".format(namePa, age, address, telephone, email, tumor, date))
    mysql.connection.commit()

    radius = request.form.get('radius')
    texture = request.form.get('texture')
    perimeter = request.form.get('perimeter')
    area = request.form.get('area')
    smoothness = request.form.get('smoothness')
    compactness = request.form.get('compactness')
    concavity = request.form.get('concavity')
    concave_points = request.form.get('concave_points')
    symmetry = request.form.get('symmetry') 
    fractal_dimension = request.form.get('fractal_dimension')

    cur.execute("INSERT INTO tumor (radius, texture, perimeter, area, smoothness, compactness, concavity, concave_points, symmetry, fractal_dimension) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(radius, texture, perimeter, area, smoothness, compactness, concavity,	concave_points,	symmetry, fractal_dimension))
    mysql.connection.commit()
    
    diagnosisDB = tumor
    cur.execute("INSERT INTO prediction (diagnosis) VALUES ('{}')".format(diagnosisDB))
    mysql.connection.commit()
    
    if (diagnosis==0):
        return render_template('diagnosisB.html', prediction_text=f'The tumor diagnosis is {tumor}', plot_url ="static/images/my_plot.png")
    else:
        return render_template('diagnosisM.html', prediction_text=f'The tumor diagnosis is {tumor}', plot_url ="static/images/my_plot.png")
   
if __name__ == "__main__":
    app.run(debug=True)

