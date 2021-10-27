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

## 3.4 Force

## 3.5 Engine
### 3.5.0 Initializers
### 3.5.1 Members
#### 3.5.1.1 inertialFrameOfReference
#### 3.5.1.2 time
#### 3.5.1.3 Bodies[]
### 3.5.2 Methods
#### 3.5.2.1 run(self, t)
#### 3.5.2.2 addBody(self, Body)
#### 3.5.2.2 relativeTranslation(self, Body)

# 4. Usage and main.py

