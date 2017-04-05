"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db 
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from forms import LoginForm
from sqlalchemy import create_engine

###
# Routing for your application.
###

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
#@login_required
def doctor_view():
    return render_template('doc_view.html');


@app.route('/add_med_data', methods =["GET", "POST"])
#@login_required
def doctor_add():
    """Render a secure page on our website that only logged in users can access."""
    if request.method == 'POST':
       #  db.create_all()
       #  #userid = str(uuid.uuid4().fields[-1])[:8]
       #  #fil = file.filename
       #  if pic:
       #      file_folder = app.config['UPLOAD_FOLDER']
       #      filename = secure_filename(pic.filename)
       #      pic.save(os.path.join(file_folder, filename))
       #  profiles = UserProfile(userid, request.form['username'],tim , request.form['fname'],request.form['lname'], filename, request.form['age'], request.form['gender'], request.form['bio'])
       # # profiles.set_id(userid)
       #  db.session.add(profiles)
       #  db.session.commit()
        flash('New person was added ')
        return redirect(url_for('doctor_view'))
    return render_template('doctor_add.html')

@app.route('/daily_updates')
#@login_required
def nurse_view():
    """Render a secure page on our website that only logged in users can access."""
    return render_template('nurse_view.html')

@app.route('/daily_updates_form')
#@login_required
def nurse_form():
    """Render a secure page on our website that only logged in users can access."""
    return render_template('daily_updates_form.html')

############################################### End Doctors and nurses Insart medical data ###############################

################################################## REGISTRATION DETAILS ################################################

@app.route('/registration-details')
#@login_required
def registration_details():
    """Remember to specify login required for only Secretaries."""
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        street = request.form['street']
        town = request.form['town']
        parish = request.form['parish']
        phone_num = request.form['phone_num']


        sqlquery = "SELECT pat_id from Patient \
                    where pat_id= MAX(pat_id)"
        result = engine.execute(sqlquery, [1]).all()


        patient_id = result+1
       
        flash('Patient Registerd')

        patient = Patient(id=patient_id, dob=dob, first_name=first_name, last_name=last_name)
        address = Patient_Address(address_line_1=town, address_line_2=parish, address_line_3=street)
        num = Patient_Contact(pat_number=phone_num)
        db.session.add(num)
        db.session.add(patient)
        db.session.add(address)
        db.session.commit()
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
    if request.method == 'POST':
        diagnosis = request.form['diagnosis']
        date_start = request.form['date_start']
        date_end = request.form['date_end']
        sqlquery = "SELECT first_name, last_name from Patient JOIN Patient_Diagnosis JOIN Diagnosis \
                    ON Patient.pat_id = Patient_Diagnosis.pat_id AND Patient_Diagnosis.diag_id = Diagnosis.diag_id\
                    where diag_date between"+date_start+" AND "+date_end+" AND diag_name= "+diagnosis
        result = engine.execute(sqlquery, [1]).all()

    """Render the website's diagnosis."""
    return render_template('get_info.html', result1=result)

@app.route("/allergies", methods=["GET", "POST"])
def allergies():
    if request.method == 'POST':
        pat_id = request.form['pat_id']
        sqlquery = "SELECT med_name from Patient JOIN Allergies JOIN Medication \
                    ON Patient.pat_id = Allergies.pat_id AND Allergies.med_id = Medication.med_id\
                    where pat_id= "+pat_id 
        result = engine.execute(sqlquery, [1]).all()

    """Render the website's diagnosis."""
    return render_template('get_info.html', result2=result)

@app.route("/medication", methods=["GET", "POST"])
def medication():
    if request.method == 'POST':
        ssqlquery = "SELECT MAX(IDs) from Patient JOIN Allergies JOIN Medication \
                    ON Patient.pat_id = Allergies.pat_id AND Allergies.med_id = Medication.med_id\
                    where Group BY Allergies.med_id AS IDs"
        result = engine.execute(sqlquery, [1]).all()


    """Render the website's diagnosis."""
    return render_template('get_info.html', result3=result)   

@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == 'POST':
        pat_id = request.form['pat_id']
        sqlquery = "SELECT test_result from Patient JOIN Patient_Test JOIN Test \
                    ON Patient.pat_id = Patient_Test.pat_id AND Patient_Test.test_id = Test.test_id\
                    where "+"Scan"+" IN test_result AND pat_id= "+pat_id
        result = engine.execute(sqlquery, [1]).all()

    """Render the website's diagnosis."""
    return render_template('get_info.html', result4=result)

@app.route("/nurse_getInfo", methods=["GET", "POST"])
def nurse_getInfo():
    if request.method == 'POST':
        pat_id = request.form['pat_id']
        spec_date = request.form['spec_date']
        sqlquery = "SELECT first_name, last_name from Nurse JOIN Daily_Updates JOIN Patient \
                    ON Patient.pat_id = Daily_Updatest.pat_id AND Daily_Updates.nur_id = Nurse.nur_id\
                    where pat_id = "+pat_id+" AND update_date = "+spec_date
        result = engine.execute(sqlquery, [1]).all()

    """Render the website's diagnosis."""
    return render_template('get_info.html', result5=result)


@app.route("/intern", methods=["GET", "POST"])
def intern():
    if request.method == 'POST':
        sqlquery = "SELECT first_name, last_name from Intern JOIN Patient_Procedure JOIN Patient \
                    ON Patient.pat_id = Patient_Procedure.pat_id AND Patient_Procedure.doc_id = Intern.doc_id\
                    where pat_id = "+pat_id+" AND update_date = "+spec_date+ "Group BY Patient.pat_id AS IDs \
                    HAVING Max(IDs)"
        result = engine.execute(sqlquery, [1]).all()

    """Render the website's diagnosis."""
    return render_template('get_info.html', result6=result)

################################################## END OF GET INFO ######################################################

###################################################### LOGIN ############################################################  

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        # change this to actually validate the entire form submission
        # and not just one field
        if form.username.data:
            # Get the username and password values from the form.
            id = form.username.data
            password = form.password.data
            # using your model, query database for a user based on the username
            # and password submitted
            # store the result of that query to a `user` variable so it can be
            if form.option == 'Doctor':
                user = Doctor.query.filter_by(doc_id=id, password=password).first()
                return redirect(url_for('doctor_view'))
            elif form.option == 'Nurse':
                user = Nurse.query.filter_by(nur_id=id, password=password).first()
                return redirect(url_for('nurse_view'))
            elif form.option == 'Secretary':
                user = Secretary.query.filter_by(sec_id=id, password=password).first()
                return redirect(url_for('registration-details'))
            else:
                return redirect(url_for('home'))
            # passed to the login_user() method.

            # get user id, load into session
            login_user(user)

            # remember to flash a message to the user
            flash('Logged in successfully.', 'success')

    return render_template("login.html", form=form)

################################################## Procedures ###########################################################

@app.route("/procedures", methods=["GET", "POST"])
#@login_required
def procedures():
    return render_template('procedures.html')

@app.route("/medical_Data_Procedure", methods=["GET", "POST"])
def medical_Data_Procedure():
    if request.method == 'POST':
        #pat_id = request.form['pat_id']
        result =  db.execute('Medical_Data_Procedure', fields=['pat_id'])

    """Render the website's intern."""
    return render_template('Procedures.html', result1=result) 


@app.route("/num_of_diag_Procedure", methods=["GET", "POST"])
def num_of_diag_Procedure():
    if request.method == 'POST':
        result =  db.execute('Num_of_diag_Procedure')

    """Render the website's intern."""
    return render_template('Procedures.html', result2=result) 

@app.route("/hereditary_diseases_Procedure", methods=["GET", "POST"])
def hereditary_diseases_Procedure():
    if request.method == 'POST':
        #pat_id = request.form['pat_id']
        result =  db.execute('Hereditary_diseases_Procedure', fields=['age'])

    """Render the website's intern."""
    return render_template('Procedures.html', result3=result) 

@app.route("/popular_Medication_Procedure", methods=["GET", "POST"])
def popular_Medication_Procedure():
    if request.method == 'POST':
        result =  db.execute('Popular_Medication_Procedure')

    """Render the website's intern."""
    return render_template('Procedures.html', result4=result) 


@app.route("/area_diagnosis_Procedure", methods=["GET", "POST"])
def area_diagnosis_Procedure():
    if request.method == 'POST':
        #city = request.form['city']
        result =  db.execute('Area_diagnosis_Procedure', fields=['city'])

    """Render the website's intern."""
    return render_template('Procedures.html', result5=result) 


################################################## END of Procedures ####################################################

@app.route("/logout")
#@login_required
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
