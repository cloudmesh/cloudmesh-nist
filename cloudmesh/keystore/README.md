# Reproducible Cloud and Big Data Rest Service with Swagger 

## Acknowlegement: 
I cloned the repo owned by Chen Min (hid-sp18-405) and learned about the make 
file before I modified and created my own make file for this assignment

## About Service
Use pymongo as backend, profile is a general description of a user, which includes
uuid, username, context, description, firstname, lastname,publickey and email.
The service provide add a whole profile, get all profiles and get one profile by uuid.


## Notes For Instructors 
This is the directory for reproducable Reset Service with Swagger. 

* The reproducibility can be achieved by using the Make file:
    - make clean -- removes the code generated

    - make service -- creates the swagger service from the yaml file 
    and places the controllers in the appropriate directory

    - make start  -- starts the service

    - make stop -- stops the service

    - make test -- executes a number of tests against the service

    - make all -- creates and starts the service
    
    - make container -- creates a docker container that runs the service

* The yaml file I used is in 

        hid-sp18-508/swagger/cloudmesh/profile/profile.yaml
    
* The default_controller is at 

        hid-sp18-508/swagger/cloudmesh/profile/default_controller.py
  


## Server Generation Using Swagger Codegen

I followed the instruction from
[handbook](https://drive.google.com/file/d/1Mdd_TJcbXurJYRpG2gKCVqWmbhvED2Mp/view),
chapter 34: REST Service Generation with Swagger

## Start The Service

* clone the repository
* navigate to the directory 

        cd /hid-sp18-508/swagger/cloudmesh/profile
        
* creates the swagger service from the yaml file with correct controllers
        
        make service
        
* start the service by execute:

        make start

* The following will show

        Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
        
## Test The Service
* add one profile

        http://localhost:8080/cloudmesh/profile/addprofiles/135/nameYue/goodone/goodperson/yue/guo/public/yueguo@iu.com
	
	Get following response:
  
        "add a new profile successfully"

* get profile by uuid

        http://localhost:8080/cloudmesh/profile/profiles/135
	
	Get following response:
	
		{ "context": "goodone",
  		"description": "goodperson",
  		"email": "yueguo@iu.com",
  		"firstname": "yue",
  		"lastname": "guo",
  		"publickey": "public",
  		"username": "nameYue",
  		"uuid": "135"
		}

	
    
* get all profiles

        http://localhost:8080/cloudmesh/profile/profiles
	
	Get following response:
	
		[
  		{
		"context": "abc",
		"description": "aaa",
		"email": "gydbd@hotmail.com",
		"firstname": "yue",
		"lastname": "guo",
		"publickey": "puclin",
		"username": "name",
		"uuid": "13"
  		},
		{ "context": "goodone",
  		"description": "goodperson",
  		"email": "yueguo@iu.com",
  		"firstname": "yue",
  		"lastname": "guo",
  		"publickey": "public",
  		"username": "nameYue",
  		"uuid": "135"
		}
		]
    

## Stop The Service

* Stop the service by:

        make stop
        
* removes the code and directories generated:

        make clean
