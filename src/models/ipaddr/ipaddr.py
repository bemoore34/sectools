import uuid
import ipaddress
from src.common.database import Database
from src.common.utils import Utils

__author__ = 'bmoore'


class IPAddr(object):
    def __init__(self, value, ipv4, internal, location=None, owner=None, attributes=None, _id=None):
        self.value = value
        self.ipv4 = ipv4  # Boolean
        self.location = location
        self.owner = owner
        self.attributes = attributes
        self.internal = internal
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<IPAddr {}>".format(self.value)


