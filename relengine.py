c = 299792458 #speed of light in m/s

class vector_3d:
 public:
  def _init_(self, double X, double Y, double Z):
   self.x = x
   self.y = y
   self.z = z
  getCoordinates():
   return [self.x, self.y, self.z]
  setCoordinates(double x, double y, double z)
  double getX()
  double getY()
  double getZ()
  setX(double)
  setY(double)
  setZ(double)
  double magnitude()

  double x
  double y
  double z

class vector_4d:
 public:
  _init(double, double, double, double)
  getCoordinates()
  setCoordinates(double x, double y, double z, double t)
  getX()
  getY()
  getZ()
  getT()
  setX(double)
  setY(double)
  setZ(double)
  setT(double)

 private:
  double x
  double y
  double z

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
