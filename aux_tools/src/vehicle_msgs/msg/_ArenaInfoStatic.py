# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from vehicle_msgs/ArenaInfoStatic.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg
import vehicle_msgs.msg

class ArenaInfoStatic(genpy.Message):
  _md5sum = "3fbfe50680ba43ac51b0d50c5fcfc8d8"
  _type = "vehicle_msgs/ArenaInfoStatic"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header

LaneNet     lane_net
ObstacleSet obstacle_set


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: vehicle_msgs/LaneNet
Header header

Lane[] lanes

================================================================================
MSG: vehicle_msgs/Lane
Header header

int32 id
int32 dir

int32[] child_id
int32[] father_id

int32 l_lane_id
bool l_change_avbl

int32 r_lane_id
bool r_change_avbl

string behavior

float32 length

geometry_msgs/Point start_point
geometry_msgs/Point final_point

geometry_msgs/Point[] points

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: vehicle_msgs/ObstacleSet
Header header

CircleObstacle[] obs_circle
PolygonObstacle[] obs_polygon

================================================================================
MSG: vehicle_msgs/CircleObstacle
Header header

int32 id
Circle circle

================================================================================
MSG: vehicle_msgs/Circle
geometry_msgs/Point center
float32 radius

================================================================================
MSG: vehicle_msgs/PolygonObstacle
Header header

int32 id
geometry_msgs/Polygon polygon

================================================================================
MSG: geometry_msgs/Polygon
#A specification of a polygon where the first and last points are assumed to be connected
Point32[] points

================================================================================
MSG: geometry_msgs/Point32
# This contains the position of a point in free space(with 32 bits of precision).
# It is recommeded to use Point wherever possible instead of Point32.  
# 
# This recommendation is to promote interoperability.  
#
# This message is designed to take up less space when sending
# lots of points at once, as in the case of a PointCloud.  

float32 x
float32 y
float32 z"""
  __slots__ = ['header','lane_net','obstacle_set']
  _slot_types = ['std_msgs/Header','vehicle_msgs/LaneNet','vehicle_msgs/ObstacleSet']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,lane_net,obstacle_set

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ArenaInfoStatic, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.lane_net is None:
        self.lane_net = vehicle_msgs.msg.LaneNet()
      if self.obstacle_set is None:
        self.obstacle_set = vehicle_msgs.msg.ObstacleSet()
    else:
      self.header = std_msgs.msg.Header()
      self.lane_net = vehicle_msgs.msg.LaneNet()
      self.obstacle_set = vehicle_msgs.msg.ObstacleSet()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.lane_net.header.seq, _x.lane_net.header.stamp.secs, _x.lane_net.header.stamp.nsecs))
      _x = self.lane_net.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.lane_net.lanes)
      buff.write(_struct_I.pack(length))
      for val1 in self.lane_net.lanes:
        _v1 = val1.header
        _x = _v1.seq
        buff.write(_get_struct_I().pack(_x))
        _v2 = _v1.stamp
        _x = _v2
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v1.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_2i().pack(_x.id, _x.dir))
        length = len(val1.child_id)
        buff.write(_struct_I.pack(length))
        pattern = '<%si'%length
        buff.write(struct.Struct(pattern).pack(*val1.child_id))
        length = len(val1.father_id)
        buff.write(_struct_I.pack(length))
        pattern = '<%si'%length
        buff.write(struct.Struct(pattern).pack(*val1.father_id))
        _x = val1
        buff.write(_get_struct_iBiB().pack(_x.l_lane_id, _x.l_change_avbl, _x.r_lane_id, _x.r_change_avbl))
        _x = val1.behavior
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.length
        buff.write(_get_struct_f().pack(_x))
        _v3 = val1.start_point
        _x = _v3
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v4 = val1.final_point
        _x = _v4
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        length = len(val1.points)
        buff.write(_struct_I.pack(length))
        for val2 in val1.points:
          _x = val2
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      _x = self
      buff.write(_get_struct_3I().pack(_x.obstacle_set.header.seq, _x.obstacle_set.header.stamp.secs, _x.obstacle_set.header.stamp.nsecs))
      _x = self.obstacle_set.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.obstacle_set.obs_circle)
      buff.write(_struct_I.pack(length))
      for val1 in self.obstacle_set.obs_circle:
        _v5 = val1.header
        _x = _v5.seq
        buff.write(_get_struct_I().pack(_x))
        _v6 = _v5.stamp
        _x = _v6
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v5.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.id
        buff.write(_get_struct_i().pack(_x))
        _v7 = val1.circle
        _v8 = _v7.center
        _x = _v8
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _x = _v7.radius
        buff.write(_get_struct_f().pack(_x))
      length = len(self.obstacle_set.obs_polygon)
      buff.write(_struct_I.pack(length))
      for val1 in self.obstacle_set.obs_polygon:
        _v9 = val1.header
        _x = _v9.seq
        buff.write(_get_struct_I().pack(_x))
        _v10 = _v9.stamp
        _x = _v10
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v9.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.id
        buff.write(_get_struct_i().pack(_x))
        _v11 = val1.polygon
        length = len(_v11.points)
        buff.write(_struct_I.pack(length))
        for val3 in _v11.points:
          _x = val3
          buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.lane_net is None:
        self.lane_net = vehicle_msgs.msg.LaneNet()
      if self.obstacle_set is None:
        self.obstacle_set = vehicle_msgs.msg.ObstacleSet()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.lane_net.header.seq, _x.lane_net.header.stamp.secs, _x.lane_net.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.lane_net.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.lane_net.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.lane_net.lanes = []
      for i in range(0, length):
        val1 = vehicle_msgs.msg.Lane()
        _v12 = val1.header
        start = end
        end += 4
        (_v12.seq,) = _get_struct_I().unpack(str[start:end])
        _v13 = _v12.stamp
        _x = _v13
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v12.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v12.frame_id = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.id, _x.dir,) = _get_struct_2i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%si'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.child_id = s.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%si'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.father_id = s.unpack(str[start:end])
        _x = val1
        start = end
        end += 10
        (_x.l_lane_id, _x.l_change_avbl, _x.r_lane_id, _x.r_change_avbl,) = _get_struct_iBiB().unpack(str[start:end])
        val1.l_change_avbl = bool(val1.l_change_avbl)
        val1.r_change_avbl = bool(val1.r_change_avbl)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.behavior = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.behavior = str[start:end]
        start = end
        end += 4
        (val1.length,) = _get_struct_f().unpack(str[start:end])
        _v14 = val1.start_point
        _x = _v14
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v15 = val1.final_point
        _x = _v15
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.points = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Point()
          _x = val2
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          val1.points.append(val2)
        self.lane_net.lanes.append(val1)
      _x = self
      start = end
      end += 12
      (_x.obstacle_set.header.seq, _x.obstacle_set.header.stamp.secs, _x.obstacle_set.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.obstacle_set.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.obstacle_set.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obstacle_set.obs_circle = []
      for i in range(0, length):
        val1 = vehicle_msgs.msg.CircleObstacle()
        _v16 = val1.header
        start = end
        end += 4
        (_v16.seq,) = _get_struct_I().unpack(str[start:end])
        _v17 = _v16.stamp
        _x = _v17
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v16.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v16.frame_id = str[start:end]
        start = end
        end += 4
        (val1.id,) = _get_struct_i().unpack(str[start:end])
        _v18 = val1.circle
        _v19 = _v18.center
        _x = _v19
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 4
        (_v18.radius,) = _get_struct_f().unpack(str[start:end])
        self.obstacle_set.obs_circle.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obstacle_set.obs_polygon = []
      for i in range(0, length):
        val1 = vehicle_msgs.msg.PolygonObstacle()
        _v20 = val1.header
        start = end
        end += 4
        (_v20.seq,) = _get_struct_I().unpack(str[start:end])
        _v21 = _v20.stamp
        _x = _v21
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v20.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v20.frame_id = str[start:end]
        start = end
        end += 4
        (val1.id,) = _get_struct_i().unpack(str[start:end])
        _v22 = val1.polygon
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v22.points = []
        for i in range(0, length):
          val3 = geometry_msgs.msg.Point32()
          _x = val3
          start = end
          end += 12
          (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
          _v22.points.append(val3)
        self.obstacle_set.obs_polygon.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.lane_net.header.seq, _x.lane_net.header.stamp.secs, _x.lane_net.header.stamp.nsecs))
      _x = self.lane_net.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.lane_net.lanes)
      buff.write(_struct_I.pack(length))
      for val1 in self.lane_net.lanes:
        _v23 = val1.header
        _x = _v23.seq
        buff.write(_get_struct_I().pack(_x))
        _v24 = _v23.stamp
        _x = _v24
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v23.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_2i().pack(_x.id, _x.dir))
        length = len(val1.child_id)
        buff.write(_struct_I.pack(length))
        pattern = '<%si'%length
        buff.write(val1.child_id.tostring())
        length = len(val1.father_id)
        buff.write(_struct_I.pack(length))
        pattern = '<%si'%length
        buff.write(val1.father_id.tostring())
        _x = val1
        buff.write(_get_struct_iBiB().pack(_x.l_lane_id, _x.l_change_avbl, _x.r_lane_id, _x.r_change_avbl))
        _x = val1.behavior
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.length
        buff.write(_get_struct_f().pack(_x))
        _v25 = val1.start_point
        _x = _v25
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v26 = val1.final_point
        _x = _v26
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        length = len(val1.points)
        buff.write(_struct_I.pack(length))
        for val2 in val1.points:
          _x = val2
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      _x = self
      buff.write(_get_struct_3I().pack(_x.obstacle_set.header.seq, _x.obstacle_set.header.stamp.secs, _x.obstacle_set.header.stamp.nsecs))
      _x = self.obstacle_set.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.obstacle_set.obs_circle)
      buff.write(_struct_I.pack(length))
      for val1 in self.obstacle_set.obs_circle:
        _v27 = val1.header
        _x = _v27.seq
        buff.write(_get_struct_I().pack(_x))
        _v28 = _v27.stamp
        _x = _v28
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v27.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.id
        buff.write(_get_struct_i().pack(_x))
        _v29 = val1.circle
        _v30 = _v29.center
        _x = _v30
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _x = _v29.radius
        buff.write(_get_struct_f().pack(_x))
      length = len(self.obstacle_set.obs_polygon)
      buff.write(_struct_I.pack(length))
      for val1 in self.obstacle_set.obs_polygon:
        _v31 = val1.header
        _x = _v31.seq
        buff.write(_get_struct_I().pack(_x))
        _v32 = _v31.stamp
        _x = _v32
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v31.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1.id
        buff.write(_get_struct_i().pack(_x))
        _v33 = val1.polygon
        length = len(_v33.points)
        buff.write(_struct_I.pack(length))
        for val3 in _v33.points:
          _x = val3
          buff.write(_get_struct_3f().pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.lane_net is None:
        self.lane_net = vehicle_msgs.msg.LaneNet()
      if self.obstacle_set is None:
        self.obstacle_set = vehicle_msgs.msg.ObstacleSet()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.lane_net.header.seq, _x.lane_net.header.stamp.secs, _x.lane_net.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.lane_net.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.lane_net.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.lane_net.lanes = []
      for i in range(0, length):
        val1 = vehicle_msgs.msg.Lane()
        _v34 = val1.header
        start = end
        end += 4
        (_v34.seq,) = _get_struct_I().unpack(str[start:end])
        _v35 = _v34.stamp
        _x = _v35
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v34.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v34.frame_id = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.id, _x.dir,) = _get_struct_2i().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%si'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.child_id = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%si'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.father_id = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
        _x = val1
        start = end
        end += 10
        (_x.l_lane_id, _x.l_change_avbl, _x.r_lane_id, _x.r_change_avbl,) = _get_struct_iBiB().unpack(str[start:end])
        val1.l_change_avbl = bool(val1.l_change_avbl)
        val1.r_change_avbl = bool(val1.r_change_avbl)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.behavior = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.behavior = str[start:end]
        start = end
        end += 4
        (val1.length,) = _get_struct_f().unpack(str[start:end])
        _v36 = val1.start_point
        _x = _v36
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v37 = val1.final_point
        _x = _v37
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.points = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Point()
          _x = val2
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          val1.points.append(val2)
        self.lane_net.lanes.append(val1)
      _x = self
      start = end
      end += 12
      (_x.obstacle_set.header.seq, _x.obstacle_set.header.stamp.secs, _x.obstacle_set.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.obstacle_set.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.obstacle_set.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obstacle_set.obs_circle = []
      for i in range(0, length):
        val1 = vehicle_msgs.msg.CircleObstacle()
        _v38 = val1.header
        start = end
        end += 4
        (_v38.seq,) = _get_struct_I().unpack(str[start:end])
        _v39 = _v38.stamp
        _x = _v39
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v38.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v38.frame_id = str[start:end]
        start = end
        end += 4
        (val1.id,) = _get_struct_i().unpack(str[start:end])
        _v40 = val1.circle
        _v41 = _v40.center
        _x = _v41
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        start = end
        end += 4
        (_v40.radius,) = _get_struct_f().unpack(str[start:end])
        self.obstacle_set.obs_circle.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obstacle_set.obs_polygon = []
      for i in range(0, length):
        val1 = vehicle_msgs.msg.PolygonObstacle()
        _v42 = val1.header
        start = end
        end += 4
        (_v42.seq,) = _get_struct_I().unpack(str[start:end])
        _v43 = _v42.stamp
        _x = _v43
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v42.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v42.frame_id = str[start:end]
        start = end
        end += 4
        (val1.id,) = _get_struct_i().unpack(str[start:end])
        _v44 = val1.polygon
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        _v44.points = []
        for i in range(0, length):
          val3 = geometry_msgs.msg.Point32()
          _x = val3
          start = end
          end += 12
          (_x.x, _x.y, _x.z,) = _get_struct_3f().unpack(str[start:end])
          _v44.points.append(val3)
        self.obstacle_set.obs_polygon.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_2i = None
def _get_struct_2i():
    global _struct_2i
    if _struct_2i is None:
        _struct_2i = struct.Struct("<2i")
    return _struct_2i
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f
_struct_i = None
def _get_struct_i():
    global _struct_i
    if _struct_i is None:
        _struct_i = struct.Struct("<i")
    return _struct_i
_struct_iBiB = None
def _get_struct_iBiB():
    global _struct_iBiB
    if _struct_iBiB is None:
        _struct_iBiB = struct.Struct("<iBiB")
    return _struct_iBiB
