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
