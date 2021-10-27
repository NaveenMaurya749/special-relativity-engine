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

  def _mul_(self,other):  #Dot Product
   return self.x*other.x + self.y*other.y + self.z*other.z

  def _pow_(self, alpha): #Product with scalar
   r = vector_3d(0,0,0)
   r.x *= alpha
   r.y *= alpha
   r.z *= alpha
   
  def getCoordinates(self):
   return [self.x, self.y, self.z]
  def setCoordinates(self, x, y, z):
   self.x = x
   self.y = y
   self.z = z
  def magnitude(self):
   return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)


class body:
  def _init_(self):
   self.rest_mass = 0.0
   self.position = vector_3d(0,0,0)
   self.velocity = vector_3d(0,0,0)
   self.force = vector_3d(0,0,0)

  def _init_(self, p, v, m, f):
   self.rest_mass = m
   self.position = p
   self.velocity = v
   self.force = f

  def relativistic_mass(self):
   return self.rest_mass*(1+self.velocity*self.velocity/(2*c*c))
  def dilation_factor(self):
   return 1/(math.sqrt(1-self.velocity*self.velocity/(c*c)))

class Engine:
  def _init_(self):
   self.Bodies = []
   self.time = 0.0

  def run(self, t):
   j = 0
   tps = 1000 #iterations for each second
   while(j < t*tps):
    dt = float(j)/tps
    for i in Bodies:
     i.velocity += i.force**(1/i.relativistic_mass())
     i.position += i.velocity * dt
    time += dt
    j += 1


  def addBody(b):
   Bodies.append(b)

  def relativeTranslation(b):
   for i in Bodies:
    i.position -= b.position
    
    #Lorentz Transform following
    speed = b.velocity.magnitude()
    gamma = b.dilation_factor()
    r = b.velocity/speed
    X = (i.position * r) #The to-be contracted length component
    i.position = i.position - (X**(1-gamma))

    #Now, for their speeds:
    V_x = i.velocity * r
    V_yz = i.velocity - V
    V_x_prime = (V_x - b.velocity)/(1 - V_x.magnitude()*speed/(c*c))
    i.velocity = V_yz + V_x_prime
