import operator
from openravepy import *
import numpy

def _in(obj_, list_, env=None):
    return obj_ in list_

def _objectFrom(_id, env):
    obj = env.GetKinBody(_id)
    if obj == None:
        obj = env.GetSensor(_id)
    return obj

def _isRobot(entity, env=None):
    if isinstance(entity, unicode):
        entity = _objectFrom(entity, env)
    if type(entity) == openravepy_int.Robot:
        return True
    return False

def _isSensor(entity, env=None):
    if isinstance(entity, unicode):
        entity = _objectFrom(entity, env)
    if type(entity) == openravepy_int.Sensor:
        return True
    return False

def _isKinbody(entity, env=None):
    if isinstance(entity, unicode):
        entity = _objectFrom(entity, env)
    if type(entity) == openravepy_int.KinBody:
        return True
    return False

def _robot(entity, env=None):
    if isinstance(entity, unicode):
        entity = _objectFrom(entity, env)
    if type(entity) == openravepy_int.Robot:
        return entity

def _sensor(entity, env=None):
    if isinstance(entity, unicode):
        entity = _objectFrom(entity, env)
    if type(entity) == openravepy_int.Sensor:
        return entity

def _kinbody(entity, env=None):
    if isinstance(entity, unicode):
        entity = _objectFrom(entity, env)
    if type(entity) == openravepy_int.KinBody:
        return entity

def _type(entity, env=None):
    if isinstance(entity, unicode):
        entity = _objectFrom(entity, env)
    return type(entity)

def _position(entity, b=0, e=3, env=None):
    if isinstance(entity, unicode):
        entity = _objectFrom(entity, env)
    return list((poseFromMatrix(entity.GetTransform())[4:])[b:e])

def _positionX(entity, env=None):
    return _position(entity, env)[0]

def _positionY(entity, env=None):
    return _position(entity, env)[1]

def _positionZ(entity, env=None):
    return _position(entity, env)[2]

def _orientation(entity, b=0, e=4, env=None):
    if isinstance(entity, unicode):
        entity = _objectFrom(entity, env)
    return list((poseFromMatrix(entity.GetTransform())[:4])[b:e])

def _pose(entity, b=0, e=7, env=None):
    if isinstance(entity, unicode):
        entity = _objectFrom(entity, env)
    return list(poseFromMatrix(entity.GetTransform())[b:e])

def _isVisible(entity, env=None):
    if isinstance(entity, unicode):
        entity = _objectFrom(entity, env)
    return entity.IsVisible()

def _isEnabled(entity, env=None):
    if isinstance(entity, unicode):
        entity = _objectFrom(entity, env)
    return entity.IsEnabled()

def _identifer(entity, env=None):
    if isinstance(entity, unicode):
        return entity
    else:
        return entity.GetName()

def _object(entity, env=None):
    return entity

def _distance(p1, p2, env=None):

    if not isinstance(p1, list):
        p1 = _position(p1, env=env)
    if not isinstance(p2, list):
        p2 = _position(p2, env=env)

    dist = 0

    for i in range(len(p1)):
        dist += (float(p1[i])-float(p2[i]))**2

    return dist**0.5

def _isSensing(sensor, entity, env=None):
    if isinstance(sensor, unicode):
        sensor = _objectFrom(sensor, env)
    if isinstance(entity, unicode):
        entity = _objectFrom(entity, env)

    if not _isSensor(sensor) or _isSensor(entity):
        return False

    envID = entity.GetEnvironmentId()
    res = sensor.SendCommand('collidingbodies')
    return envID in numpy.fromstring(res, dtype=int, sep=' ')

def _getEnvironmentID(entity, env=None):
    if isinstance(entity, unicode):
        entity = _objectFrom(entity, env)
    return entity.GetEnvironmentId()

def _sensingAmount(sensor, entity, env=None):
    if isinstance(entity, unicode):
        entity = _objectFrom(entity, env)
    if isinstance(sensor, unicode):
        sensor = _objectFrom(sensor, env)

    if not _isSensor(sensor):
        return False
    envID = entity.GetEnvironmentId()
    res = sensor.SendCommand('collidingbodies')
    res = numpy.fromstring(res, dtype=int, sep=' ')
    res = res.tolist()

    return  float(res.count(envID)) / float(len(res))

def _sensingEnvironmentIDs(sensor, env=None):
    if isinstance(sensor, unicode):
        sensor = _objectFrom(sensor, env)

    if not _isSensor(sensor):
        return None
    res = sensor.SendCommand('collidingbodies')
    res = list(set(res.tolist()))
    return res

def _volumeAABB(entity, env=None):
    if isinstance(entity, unicode):
        entity = _objectFrom(entity, env)

    if not _isKinbody(entity):
        return 0
    ab = entity.ComputeAABB()

    return ab.extents()[0] * ab.extents()[1] * ab.extents()[2]

def _above(o1, o2, env=None):
    if isinstance(o1, unicode):
        o1 = _objectFrom(o1, env=env)
    if isinstance(o2, unicode):
        o2 = _objectFrom(o2, env=env)

    if o1 == o2:
        return False

    ab  = o1.ComputeAABB()
    pos = o2.GetTransform()[:3,3]

    if ab.pos()[0] - ab.extents()[0] <= pos[0] <= ab.pos()[0] + ab.extents()[0]:
        if ab.pos()[1] - ab.extents()[1] <= pos[1] <= ab.pos()[1] + ab.extents()[1]:
            if pos[2] >= ab.pos()[2] + ab.extents()[2]:
                return True

    return False

def _below(o1, o2, env=None):
    return not _above(o1, o2, env)
    #if o1 == o2:
    #    return False

    #ab  = o1.ComputeAABB()
    #pos = o2.GetTransform()[:3,3]

    #if ab.pos()[0] - ab.extents()[0] <= pos[0] <= ab.pos()[0] + ab.extents()[0]:
    #    if ab.pos()[1] - ab.extents()[1] <= pos[1] <= ab.pos()[1] + ab.extents()[1]:
    #        if pos[2] < ab.pos()[2]:
    #            return True

    #return False

def _within(o1, o2, env=None):
    if o1 == o2:
        return False

    if isinstance(o1, unicode):
        o1 = _objectFrom(o1, env)
    if isinstance(o2, unicode):
        o2 = _objectFrom(o2, env)

    ab  = o1.ComputeAABB()
    pos = o2.GetTransform()[:3,3]

    if ab.pos()[0] - ab.extents()[0] < pos[0] < ab.pos()[0] + ab.extents()[0]:
        if ab.pos()[1] - ab.extents()[1] < pos[1] < ab.pos()[1] + ab.extents()[1]:
            if ab.pos()[2] - ab.extents()[2] < pos[2] < ab.pos()[2] + ab.extents()[2]:
                return True

    return False

def _checkCollision(obj, env=None):
    if isinstance(obj, unicode):
        obj = _objectFrom(obj, env)

    return env.CheckCollision(obj)

def _moveObjectToPosition(entity, position, env=None):
    if isinstance(entity, unicode):
        entity = _objectFrom(entity, env)

    cur_pos = entity.GetTransform()
    for i, pos in enumerate(position):
        cur_pos[i][3] = pos

    entity.SetTransform(cur_pos)
    return position



#def _collision(obj1, obj2=None):
#    if obj1 == obj2:
#        return False
#    if isinstance(obj1, str):
