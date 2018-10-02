# pyenv install

curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

# pyenv update

pyenv install 3.6.5
pyenv install 2.7.15

pyenv virtualenv 3.6.5 ENV3
pyenv virtualenv 2.7.15 ENV2


----

* <https://github.com/swagger-api/swagger-codegen/blob/master/CONTRIBUTING.md>

* <http://openapi.tools/>
* <https://github.com/APIs-guru/awesome-openapi3>
	* <https://apis.guru/awesome-openapi3/>


* <https://apimatic.io/>


* <https://nordicapis.com/top-specification-formats-for-rest-apis/>

spec -> generator -> ws

protrocol buffer - struct object
   -> openapi3.0 stub


#
# OpenAPI Documentation

* <https://sourcey.com/spectacle/>

```bash
$ npm install -g spectacle-docs
$ spectacle -d your_swagger_api.json
```

```
spectacle -h

  Usage: spectacle spactacle [options] <specfile>

  Options:

    -h, --help                output usage information
    -V, --version             output the version number
    -C, --disable-css         omit CSS generation (default: false)
    -J, --disable-js          omit JavaScript generation (default: false)
    -e, --embeddable          omit the HTML <body/> and generate the documentation content only (default: false)
    -d, --development-mode    start HTTP server with the file watcher and live reload (default: false)
    -s, --start-server        start the HTTP server without any development features
    -p, --port <dir>          the port number for the HTTP server to listen on (default: 4400)
    -t, --target-dir <dir>    the target build directory (default: public)
    -f, --target-file <file>  the target build HTML file (default: index.html)
    -a, --app-dir <dir>       the application source directory (default: app)
    -l, --logo-file <file>    specify a custom logo file (default: null)
    -c, --config-file <file>  specify a custom configuration file (default: app/lib/config.js)
```

# Swagger locally

```
$ npm install -g swagger
```

# Swagger editor

```bash
$ docker pull swaggerapi/swagger-editor
$ docker run -d -p 80:8080 swaggerapi/swagger-editor
```


# GO

Downlaod go

* <https://golang.org/dl/>

```
cd src/github.com/googleapis/gnostic/generate-gnostic
go install
cd ..
generate-gnostic --v2 # does not work

```

## Bootprint

npm install -g bootprint
npm install -g bootprint-openapi

## other html generators

* redoc <https://github.com/Rebilly/ReDoc>
* bootprint <https://bootprint.knappi.org/public-apis/petstore.swagger.io/v2/swagger.json.html>
* apidoc <http://apidocjs.com/>


swagger 2 markup

* <https://github.com/Swagger2Markup/swagger2markup>

