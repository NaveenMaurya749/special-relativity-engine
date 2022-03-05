import relengine as Relengine
import msvcrt

def printSummary(e):
 print("No. of bodies: ", len(e.Bodies))
 j = 0
 for i in e.Bodies:
  print(j, ".\nPosition: ", i.getPosition())
  print("Velocity: ", i.getVelocity())
  if(i.force != 0):
   print("Force applied: ", i.getForce())
  print()
  j += 1

engine = Relengine.Engine()
zeroV = Relengine.vector_3d(0, 0, 0)
b = Relengine.body(Relengine.vector_3d(2.5e1, 4.8e3, 8.8e2), Relengine.vector_3d(1.8e2, 2.94e7, 1.83e8), 0.1, zeroV)
engine.addBody(b)
engine.addBody(Relengine.body(Relengine.vector_3d(0, 2, 0), Relengine.vector_3d(1.37e7, 1.3e8, 1.9e6), 5, zeroV))
engine.addBody(Relengine.body(Relengine.vector_3d(1.39e3, 1.04e3, -3.24e10), Relengine.vector_3d(1.37e7, 2.8e4, 9.2e2), 1, zeroV))
engine.addBody(Relengine.body(Relengine.vector_3d(1.03e2, 1.14e4, -3.35e2), Relengine.vector_3d(9.2e7, 1.5e8, 7.49e6), 500, Relengine.vector_3d(12.3, 43.6, -35.03)))

print("Before simulation and transformation: \n")
printSummary(engine)

engine.run(10.0)
engine.relativeTranslation(b)

print("\n\nAfter simulation and transformation: \n")
printSummary(engine)

msvcrt.getch()
