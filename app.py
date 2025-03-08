from flask import Flask, render_template, request, jsonify,redirect,url_for,flash,session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'


# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Afran@2003',  # Update with your database password
    'database': 'fitness_data'
}

def get_db_connection():
    """Create a connection to the MySQL database."""
    return mysql.connector.connect(**db_config)

@app.route("/")
def first():
    return render_template('first.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/member_login")
def member_login():
    return render_template('member_login.html')

@app.route("/user_login")
def user_login():
    return render_template('user_login.html')

@app.route("/payment")
def payment():
    return render_template('payment.html')

@app.route("/search")
def search():
     return render_template('search.html')
 
@app.route("/equip_dis")
def equip_dis():
    user = get_equipment() 
    return render_template('equip_dis.html',user=user)

@app.route("/payment_his")
def payment_his():
    user = get_memberpayment() 
    return render_template('payment_his.html',user=user)

@app.route("/user_payhis")
def userpayment_his():
    user = get_userpayment() 
    return render_template('user_payhis.html',user=user)

@app.route("/blood_ser")
def blood_ser():
    return render_template('blood_ser.html')

@app.route("/equip")
def get_eqip():
    return render_template('equip.html')

@app.route("/member_profile")
def member_profile():
    user = get_memberprofile()  # Retrieve doctor data from the database
    return render_template('member_profile.html',user=user)

@app.route("/member_reg")
def member_reg():
    return render_template('member_reg.html')

@app.route("/trainer_profile")
def trainer_profile():
    user = get_trainerdetails() 
    return render_template('trainer_profile.html',user=user)

@app.route("/trainer_reg")
def trainer_reg():
    return render_template('trainer_reg.html')

@app.route("/user_reg")
def user_reg():
    return render_template('user_reg.html')

@app.route("/workouts")
def workouts():
    user = get_workouts()
    return render_template('workouts.html',user=user)




#userlogin

@app.route('/user_login', methods=['POST'])
def userlogin():
    # Retrieve username and password from the form
    usernames = request.form.get('username')
    password = request.form.get('password')

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Query the 'user' table to check for matching username and password
    query = "SELECT * FROM user WHERE user_id = %s AND password = %s"
    cursor.execute(query, (usernames, password))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    # Check if user is found in the database
    if user:
        session['u_id']=user['user_id']
        return redirect(url_for('user_dash'))
        
    else:
        flash('Invalid username or password','error')
        return redirect(url_for('user_login'))


@app.route('/user_dash')
def user_dash():
    return render_template("user_dash.html")
    
    
#memberlogin
    
@app.route('/member_login', methods=['POST'])
def memberlogin():
    # Retrieve username and password from the form
    username = request.form.get('username')
    password = request.form.get('password')
    session['member_id']=username

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Query the 'user' table to check for matching username and password
    query = "SELECT * FROM member WHERE member_id = %s AND password = %s"
    cursor.execute(query, (username, password))
    member = cursor.fetchone()

    cursor.close()
    conn.close()

    # Check if user is found in the database
    if member:
        return redirect(url_for('member_dash'))
        
    else:
        flash('Invalid username or password','error')
        return redirect(url_for('member_login'))

        flash('Invalid username or password','error')

@app.route('/member_dash')
def member_dash():
    return render_template("member_dash.html")

#memberprofile

def get_memberprofile():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute('SELECT member_id, name, age, gender, dob, address, contact, email, package, joining_date, ending_date FROM member WHERE member_id = %s', (session.get('member_id'),))
    user = cursor.fetchone()
    conn.close()
    return user

#memberpayment

def get_memberpayment():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM payment WHERE member_id = %s', (session.get('member_id'),))
    user = cursor.fetchall()
    conn.close()
    return user

#trainerdetails

def get_trainerdetails():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute('SELECT i.instructor_id,i.name,i.email,i.contact,i.address '
                  ' FROM instructor i JOIN member w ON i.instructor_id = w.instructor_id WHERE w.member_id = %s', (session.get('member_id'),))
    user = cursor.fetchone()
    conn.close()
    return user

#workoutdetails

def get_workouts():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute('SELECT name,description,count '
                   'FROM workout')
    user = cursor.fetchall()
    conn.close()
    return user

#member search

@app.route('/api/member/<int:member_id>', methods=['GET'])
def get_member_profile(member_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute('SELECT * FROM member WHERE member_id = %s', (member_id,))
    member = cursor.fetchone()

    cursor.close()
    conn.close()

    if member:
        return jsonify({
            "success": True,
            "member": member
        })
    else:
        return jsonify({
            "success": False,
            "message": "Member not found"
        }), 404
        
#Blood Search

@app.route('/api/members', methods=['GET'])
def get_members_by_blood_group():
    blood_group = request.args.get('blood_group')  # Get blood group from query string

    if not blood_group:
        return jsonify({
            "success": False,
            "message": "Blood group parameter is required"
        }), 400

    # Clean up blood group input (e.g., removing spaces or handling case-sensitivity)
    blood_group = blood_group.strip().upper()

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Query to fetch all members with the given blood group
    query = 'SELECT * FROM member WHERE blood_group LIKE %s'
    cursor.execute(query, (f'{blood_group}%',))


 # Using LIKE to match substrings (case-insensitive)
    members = cursor.fetchall()

    cursor.close()
    conn.close()

    if members:
        return jsonify({
            "success": True,
            "members": members
        })
    else:
        return jsonify({
            "success": False,
            "message": "No members found with the specified blood group"
        }), 404
        
#payment history
        
def get_userpayment():
    conn=get_db_connection()
    cursor=conn.cursor()
    query = 'SELECT * FROM payment WHERE user_id = %s'
    cursor.execute(query, (session['u_id'],))
    user = cursor.fetchall()
    conn.close()
    return user

#equipment display

def get_equipment():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM status')
    user = cursor.fetchall()
    conn.close()
    return user

#user payment history
        
def get_userpayment():
    conn=get_db_connection()
    cursor=conn.cursor()
    query = 'SELECT * FROM payment WHERE user_id = %s'
    cursor.execute(query, (session['u_id'],))
    user = cursor.fetchall()
    conn.close()
    return user

#payment insertion

@app.route("/payment", methods=['GET', 'POST'])
def book_details():
    if request.method == 'POST':
        reg = request.form['reg']
        bdate = request.form['bdate']
        edate = request.form['edate']
        amount = request.form['amount']

        # Database connection
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            # Insert query
            cursor.execute( 'INSERT INTO payment (member_id, payment_date, ending_date, amount, user_id) VALUES (%s, %s, %s, %s, %s)',
                            (reg, bdate, edate, amount, session['u_id'])
                         )
            conn.commit()  # Save changes
            
            cursor.execute( 'update member set ending_date=%s where member_id=%s',
                            (edate,reg)
                         )
            conn.commit()  # Save changes
            
            return jsonify({'success': True})
        
        
        except Exception as e:
            print("Error:", e)  # Print the error message for debugging
            return jsonify({'success': False, 'message': 'Error: ' + str(e)}), 500
        finally:
            cursor.close()
            conn.close()  # Close the connection

    return render_template('payment.html')

@app.route('/payment_success')
def payment_success():
    return render_template('payment_success.html')

#Trainer Registration

@app.route("/trainer_reg", methods=['GET', 'POST'])
def trainer_regi():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pnumber = request.form['pnumber']
        address = request.form['address']

        # Database connection
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            # Insert query
            cursor.execute(
                'INSERT INTO instructor (name, email, contact, address, user_id) VALUES (%s, %s, %s, %s, %s)',
                (name,email,pnumber,address,session['u_id'])
            )
            conn.commit()  # Save changes
            cursor = conn.cursor()

# Query to get the maximum member_id
            cursor.execute('SELECT MAX(instructor_id) FROM instructor')
            registration_number = cursor.fetchone()

        # Ensure the registration_number is extracted correctly
            if registration_number and registration_number[0] is not None:
              registration_number = registration_number[0]  # Get the actual value
            else:
              registration_number = None  # If no records, set as None

# Commit changes (if needed)
            conn.commit()

# Check if registration_number has a value before using it
            if registration_number is not None:
               print("Your registration number is:", registration_number)
            else:
                print("Error: No members found in the database.")

# Close the cursor and connection
            cursor.close()
            conn.close()
            return render_template('reg_success.html', registration_number=registration_number)
        except Exception as e:
            print("Error:", e)  # Print the error message for debugging
            return jsonify({'success': False, 'message': 'Error: ' + str(e)}), 500
        finally:
            cursor.close()
            conn.close()  # Close the connection

    return render_template('trainer_reg.html')

@app.route('/reg_success')
def reg_success():
    return render_template('reg_success.html')

#user registration

@app.route("/user_reg", methods=['GET', 'POST'])
def user_regi():
    if request.method == 'POST':
        name = request.form['name']
        pnumber = request.form['pnumber']
        address = request.form['address']
        password = request.form['password']

        # Database connection
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            # Insert query
            cursor.execute(
                'INSERT INTO user (user_name, contact, address, password) VALUES (%s, %s, %s, %s)',
                (name,pnumber,address,password)
            )
            conn.commit()  # Save changes
            cursor = conn.cursor()

# Query to get the maximum member_id
            cursor.execute('SELECT MAX(user_id) FROM user')
            registration_number = cursor.fetchone()

        # Ensure the registration_number is extracted correctly
            if registration_number and registration_number[0] is not None:
              registration_number = registration_number[0]  # Get the actual value
            else:
              registration_number = None  # If no records, set as None

# Commit changes (if needed)
            conn.commit()

# Check if registration_number has a value before using it
            if registration_number is not None:
               print("Your registration number is:", registration_number)
            else:
                print("Error: No members found in the database.")

# Close the cursor and connection
            cursor.close()
            conn.close()
            return render_template('reg_success.html', registration_number=registration_number)
        except Exception as e:
            print("Error:", e)  # Print the error message for debugging
            return jsonify({'success': False, 'message': 'Error: ' + str(e)}), 500
        finally:
            cursor.close()
            conn.close()  # Close the connection

    return render_template('user_reg.html')

@app.route('/reg_success')
def reg_successs():
    return render_template('reg_success.html')

#member registration


@app.route("/member_reg", methods=['GET', 'POST'])
def member_regi():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        blood = request.form['blood']
        pack = request.form['pack']
        jdate = request.form['jdate']
        sex = request.form['sex']
        age = request.form['age']
        dob = request.form['dob']
        address = request.form['address']
        pnumber = request.form['pnumber']
        email = request.form['email']
        pack = request.form['pack']
        in_id = request.form['in_id']

        # Database connection
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            # Insert query
            cursor.execute(
                'INSERT INTO member (name, blood_group, email, joining_date, gender, age, contact, address, dob, ending_date, user_id,package,password,instructor_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (name,blood,email,jdate,sex,age,pnumber,address,dob,jdate,session['u_id'],pack,password,in_id)
            )
            conn.commit()  # Save changes
            cursor = conn.cursor()

# Query to get the maximum member_id
            cursor.execute('SELECT MAX(member_id) FROM member')
            registration_number = cursor.fetchone()

        # Ensure the registration_number is extracted correctly
            if registration_number and registration_number[0] is not None:
              registration_number = registration_number[0]  # Get the actual value
            else:
              registration_number = None  # If no records, set as None

# Commit changes (if needed)
            conn.commit()

# Check if registration_number has a value before using it
            if registration_number is not None:
               print("Your registration number is:", registration_number)
            else:
                print("Error: No members found in the database.")

# Close the cursor and connection
            cursor.close()
            conn.close()
            return render_template('reg_success.html', registration_number=registration_number)
        except Exception as e:
            print("Error:", e)  # Print the error message for debugging
            return jsonify({'success': False, 'message': 'Error: ' + str(e)}), 500
        finally:
            conn.close()  # Close the connection

    return render_template('member_reg.html')

@app.route('/reg_success')
def reg_successss():
    return render_template('reg_success.html')

#equipment status

@app.route("/equip", methods=['GET', 'POST'])
def stat():
    if request.method == 'POST':
        name = request.form['name']
        status = request.form['status']

        # Database connection
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute( 'update status set status=%s where name=%s',
                            (status,name)
                         )
        conn.commit()  # Save changes
        return render_template('equip.html')


if __name__ == '__main__':
    app.run(debug=True)