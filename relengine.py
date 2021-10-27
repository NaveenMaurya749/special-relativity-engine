c = 299792458 #speed of light in m/s
import math

class vector_3d:
  def _init_(self, x, y, z):
   self.x = x
   self.y = y
   self.z = z

  def getCoordinates(self):
   return [self.x, self.y, self.z]
  def setCoordinates(self, x, y, z):
   self.x = x
   self.y = y
   self.z = z
  def magnitude(self):
   return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

class vector_4d:
  def _init_(self, x, y, z):
   self.x = x
   self.y = y
   self.z = z

  def getCoordinates(self):
   return [self.x, self.y, self.z, self.t]
  def setCoordinates(self, x, y, z, t):
   self.x = x
   self.y = y
   self.z = z
   self.t = t

class body:
  def _init_(self):
   pass
  def _init_(self, p, v, m):
   self.rest_mass = m
   self.position = p
   self.velocity = v

  get_rest_mass()
  set_rest_mass(float)
  get_position()
  set_position(point_3d)

  rest_mass = 0.0f
  relativistic_mass
  dilation_constant
  position = new vector_3d(0.0, 0.0, 0.0)
  velocity = new vector_4d(0.0, 0.0, 0.0)

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
