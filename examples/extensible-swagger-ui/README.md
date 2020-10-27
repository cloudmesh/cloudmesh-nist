# Extensible Swagger with UI

The client/server structure of this example is based on the materials found in Real Python's 
[Building and Documenting Python REST APIs With Flask and Connexion](https://github.com/realpython/materials/tree/main/flask-connexion-rest/version_4) materials.

## Run

**Requirements**

This demo uses MongoDB for a mock database. A mongo service should be available for the connection. 

```python
connect("cloudmesh-mock", alias="default")
```

If you do not have MongoDB installed, it can be added with:

```bash
sudo apt install -y mongodb
```

If your setup does not allow this, replace `cloudmesh-mock` with a MongoDB connection string that
is more appropriate for your environment. 

To run the Swagger server

```bash
make install
make serve
# python server/serve.py
```

## Key Concepts

### Extensible swagger specs.

A key goal of this project is to simplify the building and management of the final swagger spec file.
The current structure has each service defined in a standalone swagger file. These files repeat important API header information such as:

*vm.yaml*

```yaml
swagger: '2.0'
info:
  version: 3.0.1
  title: hadoop
  description: A Virtual Machine...
definitions:
    VM: ...
paths:
    /vm: 
...
```

This setup also misapplies object descriptions to the top level `info` element instead of the `description` property for the definition itself.

The topology proposed here is made possible by the [spec-synthase](https://github.com/MicroarrayTecnologia/spec-synthase) project, which makes the `definitions`
and `paths` portions of the Swagger spec extensible. That means we can break those definitions into multiple files and programatically add them to a base API:

*cm4.yaml*

```yaml
swagger: '2.0'
info:
  version: 3.0.1
  title: Cloudmesh API
  description: The Cloudmesh API provides a REST...
```

*vm.yaml*

```yaml
definitions:
  VM:
    description: A Virtual Machine
paths:
  /vm: 
  ...
```

*image.yaml*

```yaml
definitions:
  Image:
    description: Image objects are typically...
paths:
  /image: 
  ...
```

In server code, object definitions and their associated paths can be included programatically:

```python
from specsynthase.specbuilder import SpecBuilder

spec = SpecBuilder()\
    .add_spec(spec_path.joinpath("cloud.yaml")) \
    .add_spec(spec_path.joinpath("vm.yaml")) \
    .add_spec(spec_path.joinpath("image.yaml"))

...

app.add_api(spec)
```

This creates a setup that is both easier to maintain and provides much greater flexibility when
considering which portions of the API should be active.


### Connexion's built in Swagger UI support

Connexion has built in support for a basic Swagger UI. By requiring/installing 
`connexion[swagger-ui]` instead of `connexion`, a basic Swagger UI is included at the URL
`{api}/ui` where `{api}` is your applicatin's base URL. In this example project the URL for the
Swagger UI is http://localhost:8080/api/ui.


### Serving a custom UI

As demonstrated in the [Real Python](https://github.com/realpython/materials/tree/master/flask-connexion-rest/version_4) example, flask/connexion can also serve up arbitrary HTML. We can use this to build a client application 
that is served along with our spec.

The technology used for the client appication is not important so long as its build/dist output 
is put into `index.html` and the `static` directory.
