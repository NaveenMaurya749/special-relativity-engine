# 0. What is Relengine?
Relengine is a point-body engine for special relativity physics.
Available at the github respository: https://github.com/NaveenMaurya749/special-relativity-engine
# 1. What is relativity?
# 2. How does Relengine implement it?
# 3. Classes

## 3.1 vector_3d
This is the class for a three-dimensional vector.
### 3.1.0 Initializer
### 3.1.1 Members
The class has three coordinate attributes: x, y, z.
These are doubles that function as Cartesian Coordinates.

### 3.1.2 Methods
#### 3.1.0 \_add\_, \_sub\_, \_mul\_, \_pow\_Operator Overloading
Operators '+', '-', '\*', '\*\*', have been overloaded for the purposes of convenience during computations.
'+' and '-' so as to perform individually on each of the Cartesian coordinates.
'*' has been used to implement dot product of two vectors
'**' has been used to implement multiplication of the vector by a scalar. (Scaling)
#### 3.1.1 getCoordinates(self)
Returns a three-wide array of its coordinates.
#### 3.1.2 setCoordinates(self, x, y, z)
Set all three coordinates at once.
#### 3.1.2 magnitude(self)
Returns the magnitude, or radial distance from the origin for the said vector.

## 3.2 body
### 3.2.0 Initializers

### 3.2.1 Members
#### 3.2.1.1 rest_mass
The mass of the body, in kg when it is at rest and not influenced by relativistic phenomena.

#### 3.2.1.2 position
A vector_3d that stores the position of the body relative to the current frame of reference, in Cartesian coordinates.

#### 3.2.1.3 velocity
Another vector_3d that stores the velocity of the body in Cartesian coordinates.


### 3.2.2 Methods

#### 3.2.2.0 setForce(f)
Sets the force being applied to the body to f

#### 3.2.2.1 relativistic_mass(self)
As the speed of a body increases and becomes comparable to the speed of light, its energy increases and in its own frame of reference, it is reflected in the form of mass given by the infamous mass-energy equivalence relationship

E = m_0 c² + 1/2 m_0 v² = mc²

where m_0 is the rest mass of the body, v its speed and m is the relativistic mass.

#### 3.2.2.2 dilation_constant(self)
Given by √(1-v²/c²), this constant dictates how slower time behaves for an object of speed v.

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
[r, t] -> [γ(r-vt), γ(t-xv/c²)]
where r is the component of space in the direction of said speed.
And γ = 1/√(1-v²/c²) is the dilation factor.

# 4. Usage and main.py
One might use main.py to write scripts, or this library so as to:
1. Observe, Study and Interpret Special Relativity
2. Use it in your projects that need a physics engine. This one happens to consider special relativity as well.
