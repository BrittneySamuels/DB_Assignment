"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, login_manager
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from forms import LoginForm
import uuid
#from sqlalchemy import create_engine
import MySQLdb
import time

#engine = create_engine("mysql://root:password@localhost/pmh_db", convert_unicode=True)

###
# Routing for your application.
###

#engine = create_engine("mysql://:root@localhost/pmh_db", convert_unicode=True)
db = MySQLdb.connect("localhost","root","password123","PMH_DB")
cur = db.cursor()
Login_id = ""

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


################################################## Doctors and nurses Insert medical data ###############################

@app.route('/doctor_view')
def doctor_view():
    return render_template('doc_view.html');

@app.route('/doctor_add')
def doctor_add():
    return render_template('doctor_add.html');

@app.route('/add_med_data', methods =["GET", "POST"])
def doctor_add_test():
    """Render a secure page on our website that only logged in users can access."""
    #if current_user.is_authenticated:
        
    if request.method == 'POST':
        cur = db.cursor()
        docid= "D00000"
        pat_id = request.form['pat_id1']
        test = request.form['test1']
        result = request.form['result1']
        
        sqlquery2 = "INSERT INTO Patient_Test VALUES (\""+docid+"\",\""+pat_id+"\",\""+test+"\", \""+result+"\" );"
        cur.execute(sqlquery2)
        db.commit()
        return redirect(url_for('doctor_view'))

@app.route('/add_med_data2', methods =["GET", "POST"])         
def doctor_add_proc():
    """Render a secure page on our website that only logged in users can access."""
    #if current_user.is_authenticated:
     #   docid= current_user.get_id()
    if request.method == 'POST':
        cur = db.cursor()
        docid= "D00000"
        pat_id = request.form['pat_id3']
        proc_id = request.form['proc1']
        
        sqlquery2 = "INSERT INTO Patient_Procedure VALUES (\""+docid+"\",\""+pat_id+"\",\""+proc_id+"\" );"
        cur.execute(sqlquery2)
        db.commit()
        return redirect(url_for('doctor_view'))

@app.route('/add_med_data3', methods =["GET", "POST"])
def doctor_add_diag():
    """Render a secure page on our website that only logged in users can access."""
    #if current_user.is_authenticated:
    #    docid= current_user.get_id()
    if request.method == 'POST':
        cur = db.cursor()
        docid= "D00000"
        pat_id = request.form['pat_id2']
        diag_id = request.form['diag1']
        diag_date = time.strftime("%Y%m%d")

        sqlquery2 = "INSERT INTO Patient_Diagnosis VALUES (\""+docid+"\",\""+pat_id+"\",\""+diag_id+"\",\""+diag_date+"\" );"
        cur.execute(sqlquery2)
        db.commit()
        return redirect(url_for('doctor_view'))

@app.route('/add_med_data4', methods =["GET", "POST"])
def doctor_add_med():
    """Render a secure page on our website that only logged in users can access."""
   # if current_user.is_authenticated:
    #    docid= current_user.get_id()
    if request.method == 'POST':
        cur = db.cursor()
        docid= "D00000"
        pat_id = request.form['pat_id4']
        med_id = request.form['med1']
        
        sqlquery2 = "INSERT INTO Patient_Medicine VALUES (\""+docid+"\",\""+pat_id+"\",\""+med_id+"\" );"
        cur.execute(sqlquery2)
        db.commit()
        return redirect(url_for('doctor_view'))


@app.route('/daily_updates')
def nurse_view():
    """Render a secure page on our website that only logged in users can access."""
    return render_template('nurse_view.html')

@app.route('/update_form3', methods =["GET", "POST"])
def nurse_form2():
    print "hey"
    """Render a secure page on our website that only logged in users can access."""
    #if current_user.is_authenticated:
    #    nurid= current_user.get_id()
    if request.method == 'POST':
        print "heyYYYYYYY"
        cur = db.cursor()
        nurid= "N00000"
        pat_id = request.form.get('patid')
        bodytemp = request.form.get('temp')
        resp = request.form.get('resp')
        pulse = request.form.get('pulse')
        bloodp = request.form.get('bloodp')
        med_id = request.form.get('med')
        med_dosage = request.form.get('meddosage')
        now = time.strftime("%Y%m%d")
        print cur ,nurid, bodytemp, resp, pulse, bloodp, med_id, med_dosage, now
        sqlquery2 = "INSERT INTO Daily_Updates VALUES (\""+nurid+"\",\""+pat_id+"\",\""+now+"\"," +bodytemp+ ","+resp+","+pulse+",\""+bloodp+"\",\""+med_id+"\",\""+med_dosage+"\" );"
        print sqlquery2
        cur.execute(sqlquery2)
        db.commit()
        return redirect(url_for('nurse_view'))
    
@app.route('/nurse_add')
def nurse_add():
    return render_template('daily_updates_form.html');


############################################### End Doctors and nurses Insart medical data ###############################

################################################## REGISTRATION DETAILS ################################################

@app.route('/registration_details',methods=["GET", "POST"])
def registration_details():
    db = MySQLdb.connect("localhost","root","password123","PMH_DB")
    """Remember to specify login required for only Secretaries."""
    if request.method == 'POST':
        cur = db.cursor()
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        street = request.form['street']
        town = request.form['town']
        parish = request.form['parish']
        phone_num = request.form['phone_num']

        
        patient_id = "P0000" + str(uuid.uuid4().fields[-1])[:4]
        
       
        flash('Patient Registerd')

        sqlquery2 = "INSERT INTO Patient VALUES (\""+patient_id+"\",\""+first_name+"\",\""+last_name+"\",\""+dob+"\");"
        cur.execute(sqlquery2)
        db.commit()

        sqlquery3 = "INSERT INTO Patient_Address VALUES (\""+patient_id+"\",\""+street+"\",\""+town+"\",\""+parish+"\");"
        cur.execute(sqlquery3)
        db.commit()

        sqlquery4 = "INSERT INTO Patient_Contact VALUES (\""+patient_id+"\","+phone_num+ ");"
        cur.execute(sqlquery4)
        db.commit()

        return redirect(url_for('home'))
    """Render the website's registration_details page."""
    return render_template('registration_details.html')

################################################## GET INFO #########################################################

@app.route("/get_info", methods=["GET", "POST"])
#@login_required
def get_info():
    return render_template('get_info.html')

@app.route("/diagnosis", methods=["GET", "POST"])
def diagnosis():
    cur = db.cursor()
    if request.method == 'POST':
        diagnosis = request.form['diagnosis']
        date_start = request.form['date_start']
        date_end = request.form['date_end']
        sqlquery = "SELECT first_name, last_name from Patient JOIN Patient_Diagnosis JOIN Diagnosis ON Patient.pat_id = Patient_Diagnosis.pat_id AND Patient_Diagnosis.diag_id = Diagnosis.diag_id where diag_date between \""+date_start+"\" AND \""+date_end+"\" AND diag_name= \""+diagnosis+"\";"
        print sqlquery
        cur.execute(sqlquery)
        result =  cur.fetchall()
        

    """Render the website's diagnosis."""
    return render_template('get_info.html', result1 = result)

@app.route("/allergies", methods=["GET", "POST"])
def allergies():
    cur = db.cursor()
    if request.method == 'POST':
        pat_id = request.form['pat_id']
        sqlquery = "SELECT med_name from Patient JOIN Allergies JOIN Medicine ON Patient.pat_id = Allergies.pat_id AND Allergies.med_id = Medicine.med_id where Patient.pat_id= \""+pat_id + "\";"
        print sqlquery
        cur.execute(sqlquery)
        result =  cur.fetchall()

    """Render the website's diagnosis."""
    return render_template('get_info.html', result2=result)


@app.route("/medication", methods=["GET", "POST"])
def medication():
    cur = db.cursor()
    if request.method == 'POST':
        sqlquery = "SELECT med_name from Allergies JOIN Medicine ON Allergies.med_id = Medicine.med_id Group BY Allergies.med_id HAVING COUNT(pat_id) = (SELECT MAX(x) AS Y FROM (SELECT COUNT(pat_id) AS x FROM Allergies GROUP BY med_id) AS Z);"
        cur.execute(sqlquery)
        result =  cur.fetchall()


    """Render the website's diagnosis."""
    return render_template('get_info.html', result3=result)   


@app.route("/results", methods=["GET", "POST"])
def results():
    cur = db.cursor()
    if request.method == 'POST':
        pat_id = request.form['pat_id']
        sqlquery = "SELECT test_result FROM Patient_Test WHERE test_result LIKE '%Scan%' AND pat_id= \""+pat_id + "\";"
        cur.execute(sqlquery)
        result =  cur.fetchall()

    # SELECT med_name FROM 
    # Patient JOIN Allergies JOIN Medicine ON
    # Patient.pat_id = Allergies.pat_id AND Allergies.med_id = Medicine.med_id
    # GROUP BY Allergies.med_id HAVING COUNT(pat_id) as count1= 
    # (SELECT MAX(pat_id_count) as max_id FROM 
    # (SELECT med_id, count(pat_id) as pat_id_count FROM Allergies GROUP BY (med_id)));

    """Render the website's diagnosis."""
    return render_template('get_info.html', result4=result)

@app.route("/nurse_getInfo", methods=["GET", "POST"])
def nurse_getInfo():
    cur = db.cursor()
    if request.method == 'POST':
        pat_id = request.form['pat_id']
        spec_date = request.form['spec_date']
        sqlquery = "SELECT Nurse.first_name, Nurse.last_name from Nurse JOIN Daily_Updates ON Daily_Updates.nur_id = Nurse.nur_id where pat_id = \""+pat_id + "\" AND update_date = \""+spec_date + "\";"
        cur.execute(sqlquery)
        result =  cur.fetchall()

    """Render the website's diagnosis."""
    return render_template('get_info.html', result5=result)

@app.route("/intern", methods=["GET", "POST"])
def intern():
    if request.method == 'POST':
        cur = db.cursor()
        sqlquery = "SELECT Intern.first_name, Intern.last_name from Intern JOIN Patient_Procedure ON Patient_Procedure.doc_id = Intern.doc_id Group By Patient_Procedure.doc_id Having COUNT(pat_id) = (SELECT MAX(x) AS Y FROM (SELECT Intern.doc_id, COUNT(pat_id) AS x FROM Patient_Procedure JOIN Intern ON Patient_Procedure.doc_id = Intern.doc_id GROUP BY Intern.doc_id ) AS Z);"
        cur.execute(sqlquery)
        result =  cur.fetchall()

    """Render the website's diagnosis."""
    return render_template('get_info.html', result6=result)


################################################## END OF GET INFO ######################################################

###################################################### LOGIN ############################################################  

@app.route("/login", methods=["GET", "POST"])
def login():
    cur = db.cursor()
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        # change this to actually validate the entire form submission
        # and not just one field
        if form.username.data:
            # Get the username and password values from the form.
            id_ = form.username.data
            password = form.password.data
            # using your model, query database for a user based on the username
            # and password submitted
            # store the result of that query to a `user` variable so it can be
            if request.form['option'] == 'Doctor':
                sqlquery = "SELECT doc_id FROM Doctor where doc_id = \""+id_ +"\";"
                cur.execute(sqlquery)
                return redirect(url_for('doctor_view'))
            elif request.form['option'] == 'Nurse':
                sqlquery = "SELECT nur_id FROM Nurse where nur_id = \""+ id_ +"\";" 
                cur.execute(sqlquery)              
                return redirect(url_for('nurse_view'))
            elif request.form['option'] == 'Secretary':
                sqlquery = "SELECT sec_id FROM Secretary where sec_id = \""+ id_ +"\";" 
                cur.execute(sqlquery)
                return redirect(url_for('registration_details'))
            else:
                return redirect(url_for('home'))
            # passed to the login_user() method.

            # get user id, load into session
            login_user(sqlquery)

            # remember to flash a message to the user
            flash('Logged in successfully.', 'success')

    return render_template("login.html", form=form)



################################################## Procedures ###########################################################

@app.route("/procedures", methods=["GET", "POST"])
def procedures():
        return render_template('procedures.html')
   

@app.route("/num_of_diag_Procedure", methods=["GET", "POST"])
def num_of_diag_Procedure():
    if request.method == 'POST':
        cur.execute("Call Num_of_diag_Procedure();")
        result =  cur.fetchall()
    """Render the website's intern."""
    return render_template('procedures.html', result2=result)

@app.route("/hereditary_diseases_Procedure", methods=["GET", "POST"])
def hereditary_diseases_Procedure():
    if request.method == 'POST':
        diag_id = request.form['diag_id']
        cur.execute("Call Hereditary_diseases_Procedure (\""+diag_id+"\");")
        result =  cur.fetchall()

    """Render the website's intern."""
    return render_template('procedures.html', result3=result)


@app.route("/popular_Medication_Procedure", methods=["GET", "POST"])
def popular_Medication_Procedure():
    if request.method == 'POST':
        cur.execute("Call Popular_Medication();")
        result =  cur.fetchall()

    """Render the website's intern."""
    return render_template('procedures.html', result4=result)


@app.route("/area_diagnosis_Procedure", methods=["GET", "POST"])
def area_diagnosis_Procedure():
    if request.method == 'POST':
        city = request.form['city']
        cur.execute("Call Area_Diagnosis_Procedure (\""+city+"\");")
        result =  cur.fetchall()

    """Render the website's intern."""
    return render_template('procedures.html', result5=result) 


@app.route("/getDocPatients", methods=["GET", "POST"])
def getDocPatients():
    if request.method == 'POST':
        doc_id = request.form['doc_id']
        cur.execute("Call GetDocPatients (\""+doc_id+"\");")
        result =  cur.fetchall()

    """Render the website's intern."""
    return render_template('procedures.html', result1=result) 





################################################## END of Procedures ####################################################

@app.route("/logout")
def logout():
        # Logout the user and end the session
        logout_user()
        flash('You have been logged out.', 'danger')
        return redirect(url_for('home'))


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
