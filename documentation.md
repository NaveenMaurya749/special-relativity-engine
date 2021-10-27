# What is Relengine?
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
These 
### 3.1.2 Methods
#### 3.1.1 getCoordinates(self)
#### 3.1.2 setCoordinates(self, x, y, z)
#### 3.1.2 magnitude(self)

## 3.2 vector_4d
### 3.2.0 Initializer
### 3.2.1 Members
### 3.2.2 Methods

## 3.3 body
### 3.3.0 Initializers
### 3.3.1 Members
#### 3.3.1.1 rest_mass
#### 3.3.1.2 position
#### 3.3.1.3 velocity
### 3.3.2 Methods
#### 3.3.2.1 relativistic_mass(self)
As the speed of a body increases and becomes comparable to the speed of light, its energy increases and in its own frame of reference, it is reflected in the form of mass given by the infamous mass-energy equivalence relationship
E = m_0 c² + 1/2 m_0 v² = mc²

where m_0 is the rest mass of the body, v its speed and m is the relativistic mass.

## 3.4 Force
### 3.3.0 Initializers

## 3.5 Engine
The Engine is the core component of the library.
It runs 

### 3.5.0 Initializers
### 3.5.1 Members
#### 3.5.1.1 inertialFrameOfReference
This is a pointer to a certain body that is considered the inertial frame of reference. When a transformation of the frame occurs, the positions and velocities of all bodies in the engine are altered.

#### 3.5.1.2 time
Current simulated time. It increases as more simulation occurs.

#### 3.5.1.3 Bodies[]
This is a list of instances of class body that are taken into consideration in the engine.

### 3.5.2 Methods
#### 3.5.2.1 run(self, t)
This method runs a simulation of the bodies and stops after time interval t.

#### 3.5.2.2 addBody(self, Body)
This method adds the said Body into the array of bodies, under consideration.

#### 3.5.2.2 relativeTranslation(self, Body)
This is where the engine drops one inertial frame of reference to another. The newer positions and velocities of objects (bodies) *relative* to the new inertial frame of reference, i.e., Body.
The concept of relativity initially proposed by Gallileo, is now called Gallilean Relativity.
It was as simple as subtracting each component of the Body from every body in consideration.
For a plot of spacetime, it will appear like a skewing linear transformation.
However, it was later discovered this notion was incorrect and the true nature of relativity allows not only space but time to be relative, and that no body may exceed the speed of light, as Albert Einstein proposed. The transform thus responsible to percieve a point in spacetime from a different speed is called Lorentz transform.

Mathematically, under gaussian coordinates, for the speed v, it is given by
[r, t] -> (1/A) 
where, A = √(1-v²/c²) is the dilation constant.

# 4. Usage and main.py
One might use main.py to write scripts, or this library so as to:
1. Observe, Study and Interpret Special Relativity
2. Use it in your projects that need a physics engine. This one happens to consider special relativity as well.
