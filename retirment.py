import sqlite3
import csv

# connecting to sqlite and cursor
conn = sqlite3.connect("retirement.db")
cursor = conn.cursor()

# dropping the tables for testing
cursor.execute("DROP TABLE IF EXISTS Employee")
cursor.execute("DROP TABLE IF EXISTS Pay")
cursor.execute("DROP TABLE IF EXISTS SocialSecurityMin")

# creating the tables
cursor.execute("""
    CREATE TABLE Employee (
        EmployeeID INTEGER PRIMARY KEY,
        Name TEXT
    )
""")

cursor.execute("""
    CREATE TABLE Pay (
        EmployeeID INTEGER,
        Year INTEGER,
        Earnings REAL,
        FOREIGN KEY(EmployeeID) REFERENCES Employee(EmployeeID)
    )
""")

cursor.execute("""
    CREATE TABLE SocialSecurityMin (
        Year INTEGER PRIMARY KEY,
        Minimum REAL
    )
""")

# importing employee 
with open("Employee.txt", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skipping the heder
    for row in reader:
        cursor.execute("INSERT INTO Employee (EmployeeID, Name) VALUES (?, ?)", (int(row[0]), row[1]))

# importing pay
with open("Pay.txt", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skipping the header
    for row in reader:
        cursor.execute("INSERT INTO Pay (EmployeeID, Year, Earnings) VALUES (?, ?, ?)",
        (int(row[0]), int(row[1]), float(row[2])))

# importing social security
with open("SocialSecurityMinimum.txt", "r") as file:
    reader = csv.reader(file)
    next(reader)  #skipping the header
    for row in reader:
        cursor.execute("INSERT INTO SocialSecurityMin (Year, Minimum) VALUES (?, ?)", 
        (int(row[0]), float(row[1])))


conn.commit()

# query using join
query = """
    SELECT E.EmployeeID, E.Name, P.Year, P.Earnings, S.Minimum,
           CASE 
               WHEN P.Earnings >= S.Minimum THEN 'Yes'
               ELSE 'No'
           END as IncludeYear
    FROM Employee E
    JOIN Pay P ON E.EmployeeID = P.EmployeeID
    JOIN SocialSecurityMin S ON P.Year = S.Year
    ORDER BY E.Name, P.Year
"""

# the header
print(f"{'Employee Name':<16}{'Year':<8}{'Earnings':<13}{'Minimum':<12}{'Include'}")

# outputting the rows with formatting
for row in cursor.execute(query):
    name = row[1]
    year = row[2]
    earnings = f"{row[3]:,.2f}"
    minimum = f"{row[4]:,.2f}"
    include = row[5]
    print(f"{name:<16}{year:<8}{earnings:<13}{minimum:<12}{include}")

# closing the connection
conn.close()

#very fun assignment it sucks its the last one though
