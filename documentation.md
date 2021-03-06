# 0. What is Relengine?
Relengine is a point-body engine for special relativity physics,
available under the github respository: https://github.com/NaveenMaurya749/special-relativity-engine

# 1. What is relativity?
Relativity refers to the concept that space and time, are relative measurements, stemming from a frame of reference.
Earlier, space was considered to be relative while time was considered absolute.
Colloiuqually, meaning that if you observe an object moving about with a certain velocity, it observe itself to be still, but you moving away with the same speed, opposite in direction.
Hence, space is a measurement that is conveyed relative to a frame of reference.
So light, being an entity traversing through space, it should slow down or speed up based on frame of reference. Right?

Albert Einstein, a famous German-native physicist proposed the extended version of relativity, called Special Relativity, and then a while later General Relativity, that remains undebunked till this day despite being one of the most experimented topic in physics.
He proposed that along with space, time is also relative.
In his 1905 theory of Special Relativity, he stated three postulates all bodies must follow:
1. Laws of physics take the same form in all inertial frames of reference.
2. The speed of light shall remain invariant in all frames of reference.

# 2. How does Relengine implement it?
Relengine develops the notion of a vector in space, and then associates a body with a position vector and a velocity vector.
Through Relengine, one may transcend from one frame of reference to another, while the related spacetime, position and velocity vectors for all bodies under consideration are morphed by applicable physical laws.

Relengine also allows simulation of the space-time continuum for a set amount of time, with forces involved.

Relengine provides a way to study, interpret or implement into your projects, a relativistic engine.

# 3. Classes

## 3.1 vector_3d
This is the class for a three-dimensional vector, a mathematical entity that expresses multiple numbers across perpendicular dimensions, in this case three, altogether.
Vectors indicate a magnitude and a direction.
Commonly, position, velocity, acceleration, torque etc. are expressed using vectors.

### 3.1.0 Initializer
The initializer "**\_init\_(self, x, y, z)**" initiates the vector with coordinates x, y and z.

### 3.1.1 Members
The class has three coordinate attributes: x, y, z.
These are doubles that function as Cartesian Coordinates.

### 3.1.2 Methods
#### 3.1.2.0 \_add\_, \_sub\_, \_mul\_, \_pow\_ (Operator Overloading)
Operators '+', '-', '\*', '\*\*', have been overloaded for the purposes of convenience during computations.
'+' and '-' so as to perform individually on each of the Cartesian coordinates.
'*' has been used to implement dot product of two vectors
'**' has been used to implement multiplication of the vector by a scalar. (Scaling)
#### 3.1.2.0 getCoordinates(self)
Returns a three-wide array of its coordinates.
#### 3.1.2.2 setCoordinates(self, x, y, z)
Set all three coordinates at once.
#### 3.1.2.3 magnitude(self)
Returns the magnitude, or radial distance from the origin for the said vector.

## 3.2 body
The "body" is a point-sized body, with or without mass that occupies a particular position and velocity.
It is subject to relativity as the frame of reference is shifted.

### 3.2.0 Initializers
This class has two initializers, namely:

#### 3.2.0.1 \_init\_(self)
This initializes the body with no mass, no velocity and at the origin.

#### 3.2.0.2 \_jnit\_(self, p, v, m)
It initializes the body with mass m, at position p and velocity v.

### 3.2.1 Members
#### 3.2.1.1 rest_mass
The mass of the body, in kg when it is at rest and not influenced by relativistic phenomena.

#### 3.2.1.2 position
A vector_3d that stores the position of the body relative to the current frame of reference, in Cartesian coordinates.

#### 3.2.1.3 velocity
Another vector_3d that stores the velocity of the body in Cartesian coordinates.

#### 3.2.1.4 force
A final vector_3d that dictates the rate of change of velocity after consideration of mass m, the relativistic kind.

### 3.2.2 Methods

#### 3.2.2.1 getPosition(self)
Returns a list of position coordinates x, y and z.
#### 3.2.2.2 getVelocity(self)
Returns a list of velocity coordinates x, y and z.

#### 3.2.2.3 relativistic_mass(self)
As the speed of a body increases and becomes comparable to the speed of light, its energy increases and in its own frame of reference, it is reflected in the form of mass given by the infamous mass-energy equivalence relationship

E = m_0 c?? + 1/2 m_0 v?? = mc??

where m_0 is the rest mass of the body, v its speed and m is the relativistic mass.

#### 3.2.2.4 dilation_factor(self)
Given by ???(1-v??/c??), this constant dictates how slower time behaves for an object of speed v.

## 3.3 Engine
The Engine is the core component of the library.
It runs 

### 3.3.0 Initializer
The Initializer "\_init\_(self)" initializes the engine with a blank array for the Bodies it shall factor and simulate.
It initializes member "time" with 0.0, ready to engineer.

### 3.3.1 Members

#### 3.3.1.1 time
Current simulated time. It increases as more simulation occurs.

#### 3.3.1.2 Bodies[]
This is a list of instances of class body that are taken into consideration in the engine.

### 3.3.2 Methods
#### 3.3.2.1 run(self, t)
This method runs a simulation of the bodies and stops after time interval t.

#### 3.3.2.2 addBody(self, Body)
This method adds the said Body into the array of bodies, under consideration.

#### 3.3.2.2 relativeTranslation(self, Body)
This is where the engine drops one inertial frame of reference to another. The newer positions and velocities of objects (bodies) *relative* to the new inertial frame of reference, i.e., Body.
The concept of relativity initially proposed by Gallileo, is now called Gallilean Relativity.
It was as simple as subtracting each component of the Body from every body in consideration.
For a plot of spacetime, it will appear like a skewing linear transformation.
However, it was later discovered this notion was incorrect and the true nature of relativity allows not only space but time to be relative, and that no body may exceed the speed of light, as Albert Einstein proposed. The transform thus responsible to percieve a point in spacetime from a different speed is called Lorentz transform.

Mathematically, for the speed v, for a point in spacetime, it is given by
[r, t] -> [??(r-vt), ??(t-xv/c??)]
where r is the component of space in the direction of said speed.
And ?? = 1/???(1-v??/c??) is the dilation factor.

# 4. Usage and main.py
One might use main.py to write scripts, or this library so as to:
1. Observe, Study and Interpret Special Relativity
2. Use it in your projects that need a physics engine. This one happens to consider special relativity as well.
3. Expand the library and the engine.

An example of usage has been included in main.py
