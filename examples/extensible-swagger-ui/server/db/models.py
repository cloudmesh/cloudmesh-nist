from mongoengine import Document
from mongoengine.fields import StringField, ListField, DictField


class Vm(Document):
    cloud_id = StringField(primary_key=True)
    cloud = StringField()
    name = StringField()
    image = StringField()
    region = StringField()
    size = StringField()
    state = StringField()
    private_ips = ListField(StringField())
    public_ips = ListField(StringField())
    metadata = StringField()


class Image(Document):
    cloud_id = StringField()
    name = StringField()
    tag = StringField()
    description = StringField()
    cloud = StringField()
    os = StringField()
    osVersion = StringField()
    status = StringField()
    visibility = StringField()
    extra = StringField()


class Flavor(Document):
    cloud_id = StringField()
    name = StringField()
    label = StringField()
    metadata = StringField()
    uuid = StringField()
    ram = StringField()
    disk = StringField()
    price = StringField()
    cloud = StringField()
    cloud_id = StringField()
