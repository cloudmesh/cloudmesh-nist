# NIST Big Data Reference Architecture Interfaces


The working draft of the specification is in 

* https://github.com/cloudmesh-community/nist/blob/master/docs/nistvol8-2.md

It is easy to contribute to the document with the help of pull requests that allow eddits that will be addressed by the editor of this Volume (Gregor von Laszewski). Pull request can even be created via the GUI features of Github. YOu will need a github.com account and login into github to make use of this. 

With Pandoc a version in MS Word can be created and formating changes can be applied. However all editorial non look and feel changes must not be conducted in the docx version but in the markdown version so we have a record of the changes in the github history. The look and feel, can be managed by a professional editor. 

Once finalized, the Spec Draft will be hosted here in word format

https://cloudmesh-community.github.io/nist/spec/

and uploaded to NIST.

The document workflow is as follows:

1. contributor gets github account
2. contributor logs into github
3. contributor eidts the md document and creates a pull request
4. pull request is reviewed by Gregor von LAszewski and others 
   while discussing it in the working group meetings if needed
5. pull request is either rejected, accepted, or accepted with changes
6. Once a number of changes are accepted a new version is created, 
   however the most up to date version is always avalaible as 
   markdown document
7. The version number of the document is increased.

Super old:

* Outdated document: https://github.com/cloudmesh/nist-volume8
* On Gregors Computer ~/Desktop/Documents/OneDrive/nist-volume-8

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

Start mongo

    $ cd mongo
    $ make start

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


## One line Convenient Demo Script

We assume that you have docker installed on your machine. This demo
works at this time only on macOS

To execute the demo do the following

      $ git clone git clone https://github.com/cloudmesh-community/nist.git
      $ cd nist
      $ make demo

In case you do not have an macOS machine we have shot a convenient
video that explains how simple it is to run our services.


* <https://www.youtube.com/watch?v=fl-4PGPzwsM>

 Please note
that the service here is build from an open API specification that is
includes in

*
<https://github.com/cloudmesh-community/nist/tree/master/services/virtualdirectory>

The code for the service backend is located at

*
<https://github.com/cloudmesh-community/nist/blob/master/services/virtualdirectory/virtualdirectory_controller.py>

The password configuration file is located at

*
<https://github.com/cloudmesh-community/nist/blob/master/services/secconf.yaml>

As this is only a demonstration, we have used the most simple security
possible. We assume the server runs only on the local host. Please
make sure to properly secure it.
