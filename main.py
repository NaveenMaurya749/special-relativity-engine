import "relengine.py" as Relengine

def printSummary(e):
 print("No. of bodies: ", e.Bodies.length)
 for i in e.Bodies:
  print(i, ".\nPosition: ", i.getPosition())
  print("Velocity: ", i.getVelocity())
  if(i.force != 0):
   print("Force applied: ", i.force())
  print()

engine = Relengine.Engine()
engine.addBody(Relengine.vector_3d(0, 2, 0), Relengine.vector_3d(1.37e7, 1.3e8, 1.9e6), 5)
engine.addBody(Relengine.vector_3d(1.39e3, 1.04e3, -3.24e10), Relengine.vector_3d(1.37e7, 2.8e4, 9.2e2), 5)
engine.addBody(Relengine.vector_3d(1.03e2, 1.14e4, -3.35e2), Relengine.vector_3d(9.2e7, 1.5e8, 7.49e6), 5)

engine.printSummary()
