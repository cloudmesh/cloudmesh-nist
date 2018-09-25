# nist

Spec will be hosted here:

https://cloudmesh-community.github.io/nist/spec/


## Requirements

We need more things which we have not yet written down here

```
$ npm install -g spectacle-docs
$ brew install ghc cabal-install
$ cabal update
$ cabal install pandoc-include-code
$ cabal install pandoc-include
```

## Get the code

```
git clone https://github.com/cloudmesh-community/nist.git

cd nist/cloudmesh/openapi/service
```

We assume all terminals are cd'ed to the directory `nist/cloudmesh/openapi/service`

## Running the test program

```
make service
make start # in one window
make test # in the other window
```

## Creating the spec in HTML 

```
make doc
```

viewing the doc

```
make view # or open public/index.html in your browser
```


## Publish the spec

make publish

## Create a new service

```
cm-openapi service init SERVICE
```

Example:

```
./bin/cm-openapi service init health
services/example -> services/health
```

## A Service Example

This example demonstrates two points. First, it adds security support of **http basic auth** and **apikey/secret auth**. Second it provides the concept of the virtualdirectory as a demonstration specification to showcase an example usage of a service with authentication, as well as showcasing the idea of virtualdirectory.

The source for this example is located in 

* https://github.com/cloudmesh-community/nist/tree/master/services/virtualdirectory

To run the demo:

1. Make sure the mongo container is running as required by the previous examples;
2. In the top level of nist git repo say  

       $ git clone git clone https://github.com/cloudmesh-community/nist.git
       $ cd nist
       $ make all
       
3. Then say 

       $ cd service; make all

This will run our new combined service `virtualdirectory`

In another terminal window, go also the the nist git repo directory.  The auth credential is configured in the file:

    services/secconf.yaml

---

:warning: Please make sure to set your own passwords. We will move the file in future to 

    ~/.cloudmesh/services/seccont.yaml

However we have not yet integrated this into the code. Thus be careful that when creating pull requests not to check in your version of secconf.yaml.

---

Then say 

    $ cd services/virtualdirectory/test
    $ ./test_virtualdirectory.sh

This will add an ftp endpoint as an entry of the virtualdirectory.
(currently ftp is the only supported protocol for the virtualdirectory).

Then run these from a terminal to test the two service endpoints.

    $ curl -u admin:secret http://localhost:8080/cloudmesh/virtualdirectories
    $ curl -u admin:secret http://localhost:8080/cloudmesh/virtualdirectory/UbuntuFTP

