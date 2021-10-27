c = 299792458 #speed of light in m/s

class point_3d:
public:
 _init(double, double, double)
 getCoordinates()
 setCoordinates(double x, double y, double z
 getX()
 getY()
 getZ()

private:
 double x
 double y
 double z

class point_4d:
public:
 _init(double, double, double, double)
 getCoordinates()
 setCoordinates(double x, double y, double z, double t)
 getX()
 getY()
 getZ()
 getT()

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
 float relative_mass
 point_3d position
