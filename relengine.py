c = 299792458.0 #speed of light in m/s
import math

class vector_3d:
  def __init__(self, x, y, z):
   self.x = x
   self.y = y
   self.z = z
  
  def __add__(self,other):
   r = vector_3d(0,0,0)
   r.x = self.x + other.x
   r.y = self.y + other.y
   r.z = self.z + other.z
   return r

  def __sub__(self,other):
   r = vector_3d(0,0,0)
   r.x = self.x - other.x
   r.y = self.y - other.y
   r.z = self.z - other.z
   return r

  def __pow__(self, other):  #Dot Product
   return self.x*other.x + self.y*other.y + self.z*other.z

  def __mul__(self, alpha): #Product with scalar
   r = vector_3d(0.0,0.0,0.0)
   if isinstance(alpha, float):
    r.x = self.x * alpha
    r.y = self.y * alpha
    r.z = self.z * alpha
    return r
   
  def getCoordinates(self):
   return [self.x, self.y, self.z]
  def setCoordinates(self, x, y, z):
   self.x = x
   self.y = y
   self.z = z
  def magnitude(self):
   return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
  def direction(self):
   return self * (1/self.magnitude())


class body:
  def __init__(self):
   self.rest_mass = 1.0
   self.position = vector_3d(0,0,0)
   self.velocity = vector_3d(0,0,0)
   self.force = vector_3d(0,0,0)

  def __init__(self, p, v, m, f):
   self.rest_mass = m
   self.position = p
   self.velocity = v
   self.force = f

  def getPosition(self):
   return ([self.position.x, self.position.y, self.position.z])
  def getVelocity(self):
   return ([self.velocity.x, self.velocity.y, self.velocity.z])
  def getForce(self):
   return ([self.force.x, self.force.y, self.force.z])

  def relativistic_mass(self):
   return self.rest_mass*(1+self.velocity.magnitude()*self.velocity.magnitude()/(2*c*c))
  def dilation_factor(self):
   return 1/(math.sqrt(1-self.velocity.magnitude()*self.velocity.magnitude()/(c*c)))

class Engine:
  Bodies = []
  
  def __init__(self):
   self.Bodies = []
   self.time = 0.0

  def run(self, t):
   j = 0
   time = 0
   tps = 1000 #iterations for each second
   while(j < t*tps):
    dt = float(j)/tps
    for i in self.Bodies:
     if(i.force != vector_3d(0, 0, 0)):
      i.velocity += (i.force*(1/i.relativistic_mass()))*dt
     i.position += i.velocity * dt
    time += dt
    j += 1


  def addBody(self, b):
   self.Bodies.append(b)

  def relativeTranslation(self, b):
   for i in self.Bodies:
    i.position -= b.position
    
    #Lorentz Transform following
    speed = b.velocity.magnitude()
    gamma = b.dilation_factor()
    r = b.velocity*(1/speed)
    X = (i.position ** r) #The to-be contracted length component
    i.position = i.position * (1.0-(X*(1-gamma)))

    #Now, for their speeds:
    V_x = r.direction() * (i.velocity ** r)
    V_yz = i.velocity - V_x
    V_x_prime = (V_x - b.velocity)*(1/(1 - V_x.magnitude()*speed/(c*c)))
    i.velocity = V_yz + V_x_prime
