import relengine as Relengine
import msvcrt
import mysql.connector

def printSummary(e, b):
    
 mydb = mysql.connector.connect(
  host="localhost",
  user="NaveenMaurya",
  password="aJ9s_2@dSipSomePotatos",
  database="BodyData"
 )
 mycursor = mydb.cursor()

 tablename = "BeforeTransform" if b == False else "AfterTransform"
 mycursor.execute("CREATE TABLE " + tablename + " (BodyID INT, RestMass float, RelativisticMass float, position_x float(53), position_y float(53), position_z float(53), velocity_x float(53), velocity_y float(53), velocity_z float(53), force_x float(53), force_y float(53), force_z float(53), PRIMARY KEY(BodyID));")
 
 print("No. of bodies: ", len(e.Bodies))
 j = 0
 for i in e.Bodies:
  print(j, ".\nPosition: ", i.getPosition())
  print("Velocity: ", i.getVelocity())
  print("Force applied: ", i.getForce())
  print()

  sql = "INSERT INTO " + tablename + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
  val = (j, i.rest_mass, i.relativistic_mass(), i.getPosition()[0], i.getPosition()[1], i.getPosition()[2], i.getVelocity()[0], i.getVelocity()[1], i.getVelocity()[2], i.getForce()[0], i.getForce()[1], i.getForce()[2])
  
  mycursor.execute(sql, val)

  mydb.commit()

  j += 1

engine = Relengine.Engine()
zeroV = Relengine.vector_3d(0, 0, 0)
b = Relengine.body(Relengine.vector_3d(2.5e1, 4.8e3, 8.8e2), Relengine.vector_3d(1.8e2, 2.94e7, 1.83e8), 0.1, zeroV)
engine.addBody(b)
engine.addBody(Relengine.body(Relengine.vector_3d(0, 2, 0), Relengine.vector_3d(1.37e7, 1.3e8, 1.9e6), 5, zeroV))
engine.addBody(Relengine.body(Relengine.vector_3d(1.39e3, 1.04e3, -3.24e10), Relengine.vector_3d(1.37e7, 2.8e4, 9.2e2), 1, zeroV))
engine.addBody(Relengine.body(Relengine.vector_3d(1.03e2, 1.14e4, -3.35e2), Relengine.vector_3d(9.2e7, 1.5e8, 7.49e6), 500, Relengine.vector_3d(12.3, 43.6, -35.03)))

mydb = mysql.connector.connect(
 host="localhost",
 user="NaveenMaurya",
 password="aJ9s_2@dSipSomePotatos"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES;")

if(mycursor == False):
 mycursor.execute("CREATE DATABASE BodyData;")
  
print("Before simulation and transformation: \n")
printSummary(engine, False)
          
engine.run(10.0)
engine.relativeTranslation(b)

print("\n\nAfter simulation and transformation: \n")
printSummary(engine, True)

msvcrt.getch()
