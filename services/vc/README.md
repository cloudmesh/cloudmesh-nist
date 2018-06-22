# Virtual Cluster Example 

# About Service
Use pymongo as backend. VC example stores Virtual Cluster objects.


## Notes For Instructors 
This is the directory for reproducable Reset Service with Swagger. 

* The reproducibility can be achieved by using the Makefile:
    - make clean -- removes the code generated

    - make service -- creates the swagger service from the yaml file 
    and places the controllers in the appropriate directory

    - make start  -- starts the service

    - make stop -- stops the service

    - make test -- executes a number of tests against the service

    - make all -- creates and starts the service
    
    - make container -- creates a docker container that runs the service

## Start The Service

* clone the repository
* navigate to the directory 

        cd nist/services/vc
        
* creates the swagger service from the yaml file with correct controllers
        
        make service
        
* start the service by execute:

        make start

* The following will show

        Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
        
## Test The Service
* Use the provided test script to populate test objects:

        make test

* list all VCs:

        http://localhost:8080/cloudmesh/vc/vcs
	
* get VC by name (nbdra):

	    http://localhost:8080/cloudmesh/vc/vcs/nbdra
    
* get front-end info of a VC (nbdra):

    	http://localhost:8080/cloudmesh/vc/vcs/nbdra/fe

* get info for a certain compute node (nbdra-node0) of a specified VC (nbdra):

        http://localhost:8080/cloudmesh/vc/vcs/nbdra/nbdra-node0

## Stop The Service

* Stop the service by:

        make stop
        
* removes the code and directories generated:

        make clean
