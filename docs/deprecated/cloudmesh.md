
C.  Cloudmesh REST

Cloudmesh Rest is a reference implementation for the NBDRA. It allows
for automatic definition of a REST service based on the objects
specified by the NBDRA. In collaboration with other cloudmesh
components, it allows easy interaction with hybrid clouds and the
creation of user-managed Big Data services.

1.  Prerequisites

The prerequisites for cloudmesh Rest are Python 2.7.13 or 3.6.1. It can
easily be installed on a variety of systems (At this time, only ubuntu
greater 16.04 and OSX Sierra have been tested.). However, it would
naturally be possible to also port it to Windows. At the time of
publication, the installation instructions in this document are not
complete. The reader is referred to the cloudmesh manuals, which are
under development. The goal will be to make the installation (after the
system is set up for developing Python) as simple as the following:

pip install cloudmesh.rest

2.  REST Service

With the cloudmesh REST framework, it is easy to create REST services
while defining the resources via example JSON objects. This is achieved
while leveraging the Python eve [2] and a modified version of Python
evengine [3].

A valid JSON resource specification looks like this:

```
{

 'profile': {
  'description': 'The Profile of a user',
  'email': 'laszewski\@gmail.com',
  'firstname': 'Gregor',
  'lastname': 'von Laszewski',
  'username': 'gregor'
 }
}
```

In this example, an object called profile is defined, which contains a
number of attributes and values. The type of the values is automatically
determined. All JSON specifications are contained in a directory and can
easily be converted into a valid schema for the eve REST service by
executing the following commands:

```
cms schema cat . all.json

cms schema convert all.json
```

This will create the configuration \\verb\|all.settings.py\| that can be
used to start an eve service.

Once the schema has been defined, cloudmesh specifies defaults for
managing a sample database that is coupled with the REST service.
MongoDB was used, which could be placed on a shared mongo service.
