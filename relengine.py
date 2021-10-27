c = 299792458 #speed of light in m/s
import math

class vector_3d:
  def _init_(self, x, y, z):
   self.x = x
   self.y = y
   self.z = z
  
  def _add_(self,other):
   r = vector_3d(0,0,0)
   r.x = self.x + other.x
   r.y = self.y + other.y
   r.z = self.z + other.z
   return r

  def _sub_(self,other):
   r = vector_3d(0,0,0)
   r.x = self.x - other.x
   r.y = self.y - other.y
   r.z = self.z - other.z
   return r

  def getCoordinates(self):
   return [self.x, self.y, self.z]
  def setCoordinates(self, x, y, z):
   self.x = x
   self.y = y
   self.z = z
  def magnitude(self):
   return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

"""
class vector_4d:
  def _init_(self, x, y, z):
   self.x = x
   self.y = y
   self.z = z

  def getCoordinates(self):
   return [self.x, self.y, self.z, self.t]
  def setCoordinates(self, x, y, z, t):
"""

class body:
  def _init_(self):
   rest_mass = 0.0

  def _init_(self, p, v, m):
   self.rest_mass = m
   self.position = p
   self.velocity = v

  def relativistic_mass(self):
   return self.rest_mass*(1+self.velocity*self.velocity/(2*c*c))
  def dilation_factor(self):
   return 1/(math.sqrt(1-self.velocity*self.velocity/(c*c)))

class Engine:
  def _init_():
   Bodies = []

  def run(self, t):
   for i in Bodies:
    i.position += i.velocity * t
   time += t
  def addBody(b):
   Bodies.append(b)
  def relativeTranslation(b):
   for i in Bodies:
    i.position -= b.position
    i.position /= b.dilation_factor
    #To Be Finished
