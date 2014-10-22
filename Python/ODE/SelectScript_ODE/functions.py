from ode import Body, GeomObject, GeomBox, GeomPlane, GeomCapsule, GeomCCylinder, GeomCylinder, \
                GeomRay, GeomSphere, GeomTransform, GeomTriMesh, collide

def Sode_position(geom, b=0, e=3):
    if isinstance(geom, GeomPlane):
        return list(geom.getParams()[0])[b:e]
    elif isinstance(geom, (GeomObject, Body)):
        return list(geom.getPosition())[b:e]

def Sode_posX(geom): return Sode_position(geom, 0, 1)[0]
def Sode_posY(geom): return Sode_position(geom, 1, 2)[0]
def Sode_posZ(geom): return Sode_position(geom, 2, 3)[0]

def Sode_rotation(geom):
    if isinstance(geom, (GeomObject, Body)):
        return list(geom.getRotation())
    
def Sode_quaternion(geom):
    if isinstance(geom, (GeomObject, Body)):
        return list(geom.getQuaternion())
    
def Sode_quantum(val):
    if isinstance(val, list):
        q = 0
        for v in val:
            q += v**2.0
        return q**0.5
    return val
    
def Sode_identifer(geom, space):
    if isinstance(geom, GeomObject):
        for i,elem in enumerate(space):
            if geom == elem:
                return i
    return -1

def Sode_aabb(geom):
    if isinstance(geom, GeomObject):
        return list(geom.getAABB())
    
def Sode_obj(entity): return entity

def Sode_isEnabled(geom):
    if isinstance(geom, (GeomObject, Body)):
        return list(geom.isEnabled())
    
def Sode_isSpace(geom):
    if isinstance(geom, GeomObject):
        return list(geom.isSpace())

def Sode_gravityMode(obj):
    if isinstance(obj, GeomObject):
        return list(obj.getBody().getGravityMode())
    elif isinstance(obj, Body):
        return list(obj.getGravityMode())

def Sode_torque(obj,b=0, e=3):
    if isinstance(obj, GeomObject):
        return list(obj.getBody().getTorque())[b:e]
    elif isinstance(obj, Body):
        return list(obj.getTorque())[b:e]

def Sode_force(obj, b=0, e=3):
    if isinstance(obj, GeomObject):
        return list(obj.getBody().getForce())[b:e]
    elif isinstance(obj, Body):
        return list(obj.getForce())[b:e]
    
def Sode_LinearVel(obj, b=0, e=3):
    if isinstance(obj, GeomObject):
        return list(obj.getBody().getLinearVel())[b:e]
    elif isinstance(obj, Body):
        return list(obj.getLinearVel())[b:e]
    
def Sode_velocity(obj):
    return Sode_quantum(Sode_LinearVel(obj))

def Sode_type(geom):         return type(geom).__name__

def Sode_isGeom(obj):        return isinstance(obj, GeomObject)
def Sode_isBox(obj):         return isinstance(obj, GeomBox)
def Sode_isCapsule(obj):     return isinstance(obj, GeomCapsule)
def Sode_isCCylinder(obj):   return isinstance(obj, GeomCCylinder)
def Sode_isCylinder(obj):    return isinstance(obj, GeomCylinder)
def Sode_isHeightfield(obj): return isinstance(obj, GeomHeightfield)
def Sode_isPlane(obj):       return isinstance(obj, GeomPlane)
def Sode_isRay(obj):         return isinstance(obj, GeomRay)
def Sode_isSphere(obj):      return isinstance(obj, GeomSphere)
def Sode_isTransform(obj):   return isinstance(obj, GeomTransform)
def Sode_isTriMesh(obj):     return isinstance(obj, GeomTriMesh)

def Sode_collision(geom1, geom2):
    if geom1 != geom2:
        if isinstance(geom1, GeomObject) and isinstance(geom2, GeomObject):
            if collide(geom1, geom2) != []:
                return True
    return False
    
def Sode_unique(list_):
    return list(set(list_))

def Sode_distance(pos1, pos2):
    if isinstance(pos1, (GeomObject, Body)):
        pos1 = Sode_position(pos1)
    if isinstance(pos2, (GeomObject, Body)):
        pos2 = Sode_position(pos2)
        
    return ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2 + (pos1[2] - pos2[2])**2)**0.5

def Sode_hasBody(obj):
    if isinstance(obj, Body):
        return True
    elif isinstance(obj, GeomObject):
        if obj.getBody() != None:
            return True
    
    return False

def Sode_mass(obj):
    
    if Sode_hasBody(obj):
        if isinstance(obj, Body):
            m = obj.getMass()  
        else:
            m = obj.getBody().getMass()
            
        s = m.__str__()
        p1 = s.find("Mass=")
        if p1 != -1:
            
            p2 = s[p1+5:].find('\n')
            
            return float(s[p1+5:p2+5])
        
    return None

def Sode_volume(obj):
    if Sode_isBox(obj):
        (a,b,c) = obj.getLengths()
        return a*b*c 
    elif Sode_isSphere(obj):
        r = obj.getRadius()
        return (4./3.) * 3.14159265359 * r**3
    elif Sode_isCapsule(obj) or Sode_isCCylinder(obj):
        (r, l) = obj.getParams()
        return 3.14159265359 * r**2 *( (4./3.)*r + l)
    elif Sode_isCylinder(obj):
        (r, l) = obj.getParams()
        return 3.14159265359 * r**2 * l
    