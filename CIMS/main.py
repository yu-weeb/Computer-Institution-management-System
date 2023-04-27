import sqlite3

# Connect to the database
conn = sqlite3.connect('students.db')
c = conn.cursor()

# Create the 'students' table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS students (
             roll_no INTEGER PRIMARY KEY,
             name TEXT,
             course TEXT,
             arrears INTEGER,
             fees INTEGER,
             grades TEXT,
             year INTEGER
             )''')
conn.commit()
stud_defualt_creds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
admin = 0
# Login
for i in stud_defualt_creds:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "1234":
        print("Admin Login successful!")
        admin += 1
        break
    elif username in stud_defualt_creds and password in stud_defualt_creds:
        print("Login successful! Welcome,", username)
        roll = username
    else:
        print("Invalid username or password.")
        exit()

# Main menu
while True and admin != 1:
    print("\nSelect an option:")
    print("1. Fetch your grades")
    print("2. Check Arrears")
    print("3. Check Fees")
    print("4. Check Course taken")
    print("5. Check your year of graduation")
    print("0. Exit")

    option = input("Enter your choice (1-5) or 0 to exit: ")

    # Option 1: Fetch based on roll number
    if option == "1":
        c.execute("SELECT grades FROM students WHERE roll_no=?", (roll,))
        row = c.fetchone()
        if row:
            print("Grade:", row)
        else:
            print("No profile found for roll number", roll)

    # Option 2: Check Arrear
    elif option == "2":
        c.execute("SELECT arrears FROM students WHERE roll_no=?", (roll,))
        row = c.fetchone()
        if row:
            print("Arrears:", row)
        else:
            print("No profile found for roll number", roll)

    # Option 3: Check fees
    elif option == "3":
        c.execute("SELECT fees FROM students WHERE roll_no=?", (roll,))
        row = c.fetchone()
        if row:
            print("Fees to be paid:", row)
        else:
            print("No profile found for roll number", roll)

    # Option 4: Check course taken
    elif option == "4":
        c.execute("SELECT course FROM students WHERE roll_no=?", (roll,))
        row = c.fetchone()
        if row:
            print("Your course is:", row)
        else:
            print("No profile found for roll number", roll)

    # Option 4: Check year of graduation
    elif option == "5":
        c.execute("SELECT year FROM students WHERE roll_no=?", (roll,))
        row = c.fetchone()
        if row:
            print("Your year of graduation is:", row)
        else:
            print("No profile found for roll number", roll)
            # Option 0: Exit
    elif option == "0":
        print("Exiting...")
        break

    # Invalid option
    else:
        print("Invalid option. Exiting....")
        break


if admin == 1:
    print("Welcome to Admin Menu!\n")
    print("\nSelect an option:")
    print("1. Fetch a Profile")
    print("2. Update Profile")
    print("3. Add Profile")
    print("0. Exit")

    admin_option = input("Enter your choice (1-3) or 0 to exit: ")

    # AdminOption 1: Fetch a profile
    if admin_option == "1":
        roll_no = int(
            input("Enter the roll number foe profile display: "))
        c.execute("SELECT * FROM students WHERE roll_no=?", (roll_no,))
        row = c.fetchone()
        if row:
            print("\nRoll Number:", row[0])
            print("Name:", row[1])
            print("Course Taken:", row[2])
            print("Arrears:", row[3])
            print("Fees Paid:", row[4])
            print("Grade:", row[5])
            print("Year of Graduation:", row[6])
        else:
            print("No profile found for roll number", roll_no)

    # AdminOption 2: Update a profile
    if admin_option == "2":
        roll_no = int(
            input("Enter the roll number for profile updating: "))
        c.execute("SELECT * FROM students WHERE roll_no=?", (roll_no,))
        row = c.fetchone()
        if row:
            print("\nRoll Number:", row[0])
            print("Name:", row[1])
            print("Course Taken:", row[2])
            print("Arrears:", row[3])
            print("Fees Paid:", row[4])
            print("Grade:", row[5])
            print("Year of Graduation:", row[6])
            field = input(
                "Enter the field you want to update (name/rollno/course/arrears/grade/year): ")
            value = input("Enter the new value: ")
            c.execute(
                f"UPDATE students SET {field}=? WHERE roll_no=?", (value, roll_no))
            conn.commit()
            print("Profile updated successfully.")
        else:
            print("No profile found for roll number", roll_no)

    # AdminOption 3: Add a profile
    if admin_option == "3":
        roll_no = int(input("Enter the roll number: "))
        name = input("Enter the name: ")
        course = input("Enter the course: ")
        arrears = int(input("Enter the arrears: "))
        fees = 0
        grade = input("Enter the grade: ")
        year = int(input("Enter the year of graduation: "))
        c.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (roll_no, name, course, arrears, fees, grade, year))
        conn.commit()
        print("Profile added successfully.")

else:
    print("Admin status not present, exiting...")
