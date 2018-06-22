Lessons Learned
---------------

Originally, a full REpresentational State Transfer (REST) specification
was used for defining the objects related to the NBDRA [11]. However,
at this stage of the document, it would introduce too complex of a
notation framework. This would result in (1) a considerable increase in
length of this document; (2) a more complex framework reducing potential
public participation in the project; and (3) a more complex framework
for developing a reference implementation. Thus, in this version of the
document, a design concept by example will be introduced, which is used
to automatically create a schema as well as a reference implementation.



Focusing first on examples allows acceleration of the design process and
simplification of discussions about the objects and interfaces. Hence,
complex specifications should not encumber the development. The
processes and specifications used in this document will also permit
automatic creation of an implementation of the objects that can be
integrated into a reference architecture, such as the cloudmesh client
and REST project [9] [11].

An example object will demonstrate this approach. The following object
defines a JSON object representing a user.


```
{
    'profile': {
        'description': 'The Profile of a user',
        'uuid': 'jshdjkdh\...',
        'context:': 'resource',
        'email': 'laszewski\@gmail.com',
        'firstname': 'Gregor',
        'lastname': 'von Laszewski',
        'username': 'gregor',
        'publickey': 'ssh \....'
    }
}
```

Object 3.1: Example Object Specification


Such an object can be translated to a schema specification while
introspecting the types of the original example.

All examples are managed in Github and links to them are automatically
generated to be included into this document. The resulting schema object
follows the Cerberus [1] specification and looks for the specific
object, introduced earlier, as follows:

```
profile = {
        'schema': {
        'username': {'type': 'string'},
        'context:': {'type': 'string'},
        'description': {'type': 'string'},
        'firstname': {'type': 'string'},
        'lastname': {'type': 'string'},
        'publickey': {'type': 'string'},
        'email': {'type': 'string'},
        'uuid': {'type': 'string'}
    }
}
```

Defined objects can also be embedded into other objects by using the
*objectid* tag. This is later demonstrated between the profile and the
user objects (see Objects 4.1 and 4.2).

When using the objects, it is assumed that one can implement the typical
CRUD actions using HTTP methods mapped as follows:

  GETprofile  Retrieves a list of profile
  -------- ----------- --------------------------------
  GETprofile12Retrieves a specific profile
  POST  profile  Creates a new profile
  PUTprofile12Updates profile \#12
  PATCH profile12Partially updates profile \#12
  DELETEprofile12Deletes profile \#12

In the reference implementation in this document, these methods are
provided automatically.
