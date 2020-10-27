# Examples

This example is maintained at

* <https://github.com/cloudmesh-community/nist/tree/main/examples/flask-connexion-swagger>



## Rest Service Generation from Open API yaml without swagger codegen

This exampel is one of the most simplest examples we provide to
retrieve information from a dynamic information source as part of a
program that autogenerates the REST service directly form the OpenAPI
rest service specification while not using swagger codegen.

The example showcases a REST service that retrieves the cpu
information and
ex[pose this informrmantion throug a get call to the REST service.

We have create a simple example and if you are on a macOS, yo can start it with

```bash
make demo
```

This will start up an separate terminal in whiich the server is run
and a curl call retrieves the information. In case you like to start
it agian, please kill the terminal.

Alternatively, you can open up two terminals seperatly and in one you
firts execute

```bash
make server
```

and in the other you say

```bash
curl http://localhost:8080/cloudmesh/cpu
```

The result will look similar to

```json
curl http://localhost:8080/cloudmesh/cpu
{
  "model": "Intel(R) Core(TM) i7-6920HQ CPU @ 2.90GHz"
}
```

## Rest Service Generation with swagger codegen

see ... just point to right location, we have this but the link needs
to be included here

## Comparison of the methods

Using our two methods can be used but there are advantages and
disadvantages for each of them

### Using swagger codegen

The advantage fo this method is that 

* a structured program is created,
* the program is uniform for different resources, and
* it is easy to identify what needs to be changed.

In addition we provided a build infrastructure that does not require
tho check in the entire code generated, but instead the makefile
gernerate the code and also replaces only the portions that we
define.

The special part about cloudmesh codgen usage is that identified
OpenAPI specification can easily integrated into a single
specification. This allows the specification to be modularized and
users that only need a subset being able to select that subset.

This also include the logic of placing different controllers into the
code increasing modularity and decreasing code length.

The disadvantage of this approach is the following.

The building process is a bit more complex, but with our build process
makefiles this is hidden from the developer. So as a result this may
not be viewed as a disadvantage at all.

The generated code structure is more complex as it follows the
hierarchical creation of code representing the models defined in the
yaml specification.

### Not using swagger codegen

The advantage of this method is that the code structure is very simple
and models are derived internally from the code structure. Anyone that
can define in OpenAPI a specification can generate a template in
minutes, however, that is also the case for the generation with codegen.

The disadvantage is that the method is so simple that it does not
expose the model directly as visible code structure to the user.

## Conclusion

Both methods provide suitable solutions for defining REST services
from OpenAPI in python. For more sophisticated program that need a
finer level of model abstraction the swagger codegen is preferred, for
those that want to quickly develop and test rest service specification
the second method can be used also.
