c = 299792458 #speed of light in m/s
import math

class vector_3d:
  def _init_(self, x, y, z):
   self.x = x
   self.y = y
   self.z = z

  def getCoordinates():
   return [self.x, self.y, self.z]
  def setCoordinates(x, y, z):
   self.x = x
   self.y = y
   self.z = z

  def getX():
   return self.x
  def getY():
   return self.y
  def getZ():
   return self.z

  def setX(x)
   self.x = x
  def setY(y)
   self.y = y
  def setZ(z)
   self.z = z
  def magnitude():
   return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

class vector_4d:
  def _init_(self, x, y, z):
   self.x = x
   self.y = y
   self.z = z

  def getCoordinates():
   return [self.x, self.y, self.z, self.t]
  def setCoordinates(x, y, z, t):
   self.x = x
   self.y = y
   self.z = z
   self.t = t

  def getX():
   return self.x
  def getY():
   return self.y
  def getZ():
   return self.z
  def getT():
   return self.t

  def setX(x)
   self.x = x
  def setY(y)
   self.y = y
  def setZ(z)
   self.z = z
  def setT(t)
   self.t = t

class body:
 public:
  _init()
  get_rest_mass()
  set_rest_mass(float)
  get_position()
  set_position(point_3d)

 private:
  float rest_mass = 0.0f
  float relativistic_mass
  vector_3d position
  vector_3d velocity

class Engine:
 public:
  _init()
  run(float t)
  getFOR()
  setFOR(body)
  addBody(body)
  relativeTranslation(body)

  body Bodies[]
private:
  body inertialFrameOfReference
  double time
