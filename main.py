from datetime import date
import mysql.connector
today=date.today()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12457"
  )
mycursor = mydb.cursor()
mycursor.execute("use mydatabase;")

datevar=today.strftime('%d%m%Y')
subject='EC18301'

finalstr="create table attendance2%s%s (name varchar(20),time TIME);"%(datevar,subject)
#val2=(datevar,subject)
mycursor.execute(finalstr)
sql = "INSERT INTO attendance (name, time) VALUES (%s, %s)"
namevar='parvesh7'
val = (namevar, "13:30:05")
mycursor.execute(sql, val)


mydb.commit()

