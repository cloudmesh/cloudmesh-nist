
# Examples

* [../hid-sample/swagger](../hid-sample/swagger) Example


* integarte this ina a production wsgi server, uwsgi & nginx
  goal: can we place the spec somewhere call make production-server and it sets this up?

azure & aws & google

* [../hid-sp18-518/project-code/azure/azvm_controller.py](../hid-sp18-518/project-code/azure)
* [../hid-sp18-518/project-code/azure/azstorage_controller.py](../hid-sp18-518/project-code/azure)
* [../hid-sp18-518/project-code/google/google_storage_controller.py](../hid-sp18-518/project-code/google)
* [../hid-sp18-518/project-code/google/google_vm_controller.py](../hid-sp18-518/project-code/google)
* [../hid-sp18-518/project-code/aws/vm_controller.py](../hid-sp18-518/project-code/aws)
* [../hid-sp18-518/project-code/aws/s3_controller.py](../hid-sp18-518/project-code/aws)

openstack

* [../hid-sp18-503/project-code/default_controller.py](../hid-sp18-503/project-code)
* [../hid-sp18-516/project-code/default_controller.py](../hid-sp18-516/project-code)



drive - s3 vm

* [../hid-sp18-420/project-code/all_drive_operations_controller.py](../hid-sp18-420/project-code)
* [../hid-sp18-420/project-code/all_s3_operations_controller.py](../hid-sp18-420/project-code)
* [../hid-sp18-420/project-code/all_vm_operations_controller.py](../hid-sp18-420/project-code)
* [../hid-sp18-402/project-code/aws/vm_controller.py](../hid-sp18-402/project-code/aws)
* [../hid-sp18-402/project-code/aws/s3_controller.py](../hid-sp18-402/project-code/aws)


Data

* [../hid-sp18-503/swagger](../hid-sp18-503/swagger) virtual directory (arnav)


Services

* [../hid-sp18-518/swagger](../hid-sp18-518/swagger) flavor

* [../hid-sp18-408/swagger](../hid-sp18-408/swagger) networkinfo (similar to cpu, possibly incomplete)

	* [../hid-sp18-408/swagger-without-docker/network/flaskConnexion/swagger_server/test/test_default_controller.py](../hid-sp18-408/swagger-without-docker/network/flaskConnexion/swagger_server/test)
	* [../hid-sp18-408/swagger-without-docker/network/flaskConnexion/swagger_server/controllers/default_controller.py](../hid-sp18-408/swagger-without-docker/network/flaskConnexion/swagger_server/controllers)


* [../hid-sp18-402/swagger](../hid-sp18-402/swagger) aws vm (has only get info for vm)
* [../hid-sp18-420/swagger](../hid-sp18-420/swagger) aws s3 (only lists buckets, wrong name of OUTPUT in definitison?)
* [../hid-sp18-419/swagger](../hid-sp18-419/swagger) google compute (only lists the vms)

Local host

* [../hid-sp18-513/swagger](../hid-sp18-513/swagger) cpu info, disk info ram info (not follow template)
* [../hid-sp18-520/swagger](../hid-sp18-520/swagger) disk info
* [../hid-sp18-413/swagger](../hid-sp18-413/swagger) memory partial mem info
* [../hid-sp18-523/swagger](../hid-sp18-523/swagger) process run ps on localhost


SSH

* [../hid-sp18-516/swagger](../hid-sp18-516/swagger) localhost (ssh to host and execute command, not sure if this works, needs to be behind firewall)

list dir

* [../hid-sp18-502/project-code/default_controller.py](../hid-sp18-502/project-code)
* [../hid-sp18-502/cloudmesh/default_controller.py](../hid-sp18-502/cloudmesh)
* [../hid-sp18-502/cloudmesh/dir_controller.py](../hid-sp18-502/cloudmesh)
* [../hid-sp18-502/cloudmesh/swagger_example/server/dir/flaskConnexion/swagger_server/controllers/dir_controller.py](../hid-sp18-502/cloudmesh/swagger_example/server/dir/flaskConnexion/swagger_server/controllers)


* [../sav-hid-sp18-422/rest/codegenoutput/swagger_server/controllers/default_controller.py](../sav-hid-sp18-422/rest/codegenoutput/swagger_server/controllers) -- stream aggregator

---


# Issues

* [../hid-sp18-517/swagger](../hid-sp18-517/swagger) fileupload (has som unneded additional test in it), not sure if this works


* [../hid-sp18-507/swagger](../hid-sp18-507/swagger) replica - very incomplete only gets data not places data, data si not backed up with db

---

# Analysis & Application


* [../hid-sp18-409/swagger](../hid-sp18-409/swagger) crime finder


	* [../hid-sp18-409/project-code/crime_finder_swagger/data/data_controller.py](../hid-sp18-409/project-code/crime_finder_swagger/data)
	* [../hid-sp18-409/project-code/crime_finder_swagger/data/crimes_controller.py](../hid-sp18-409/project-code/crime_finder_swagger/data)

* [../hid-sp18-405/swagger](../hid-sp18-405/swagger) nlp
* [../hid-sp18-401/swagger](../hid-sp18-401/swagger) Mean square error
* [../hid-sp18-416/swagger](../hid-sp18-416/swagger) stream - twitter movie stream
* [../hid-sp18-521/project-code/default_controller.py](../hid-sp18-521/project-code) medicare aws service
* [../hid-sp18-521/swagger](../hid-sp18-521/swagger) AWS SQL database National Provider Identifier (NPI) records.
	* seems incomplete, as not all data is provided that is offered in NPI
	* https://npiregistry.cms.hhs.gov/api/?number=&enumeration_type=&taxonomy_description=&first_name=&last_name=&organization_name=&address_purpose=&city=Bloomington&state=IN&postal_code=47408&country_code=US&limit=&skip=
	* https://npiregistry.cms.hhs.gov/api/demo
	* https://npiregistry.cms.hhs.gov/registry/help-api
* [../hid-sp18-522/swagger](../hid-sp18-522/swagger) viz iris dataset - <https://archive.ics.uci.edu/ml/datasets/iris>

SNP price students worked together i gusee, eliminate duplicate

* [../hid-sp18-506/swagger](../hid-sp18-506/swagger) ? snp price -
* [../hid-sp18-514/swagger](../hid-sp18-514/swagger) ? snp price -
	
* [../hid-sp18-414/swagger](../hid-sp18-414/swagger) translate a phrase (maye not that interesting)


* [../hid-sp18-401/project-code/cloudmesh/svd/default_controller.py](../hid-sp18-401/project-code/cloudmesh/svd) MNIST SVD, hardcoded, unclear if useful

# other



kmeans - svc

* [../hid-sp18-416/project-code/kmeans-service/retrieve_k_means_model_controller.py](../hid-sp18-416/project-code/kmeans-service/)
* [../hid-sp18-416/project-code/kmeans-service/save_input_file_controller.py](../hid-sp18-416/project-code/kmeans-service)
* [../hid-sp18-416/project-code/kmeans-service/retrieve_predictions_for_input_data_controller.py](../hid-sp18-416/project-code/kmeans-service)
* [../hid-sp18-416/project-code/kmeans-service/execute_k_means_controller.py](../hid-sp18-416/project-code/kmeans-service)


cpu - example in class

* [../hid-sp18-601/cloudmesh/swagger_example/server/cpu/flaskConnexion/swagger_server/test/test_default_controller.py](../hid-sp18-601/cloudmesh/swagger_example/server/cpu/flaskConnexion/swagger_server/test)
* [../hid-sp18-601/cloudmesh/swagger_example/server/cpu/flaskConnexion/build/lib.linux-x86_64-2.7/swagger_server/test/test_default_controller.py](../hid-sp18-601/cloudmesh/swagger_example/server/cpu/flaskConnexion/build/lib.linux-x86_64-2.7/swagger_server/test)
* [../hid-sp18-601/cloudmesh/swagger_example/server/cpu/flaskConnexion/build/lib.linux-x86_64-2.7/swagger_server/controllers/default_controller.py](../hid-sp18-601/cloudmesh/swagger_example/server/cpu/flaskConnexion/build/lib.linux-x86_64-2.7/swagger_server/controllers)

CPU - example in class

* [../hid-sp18-524/cloudmesh/swagger_example/server/cpu/flaskConnexion/swagger_server/test/test_default_controller.py](../hid-sp18-524/cloudmesh/swagger_example/server/cpu/flaskConnexion/swagger_server/test)
* [../hid-sp18-524/cloudmesh/swagger_example/server/cpu/flaskConnexion/swagger_server/controllers/default_controller.py](../hid-sp18-524/cloudmesh/swagger_example/server/cpu/flaskConnexion/swagger_server/controllers)




# NOT RELEVANT for NIST PROJECT

* [../hid-sp18-526/swagger](../hid-sp18-526/swagger) mapreduce (has no real file based data upload)
* [../hid-sp18-511/swagger](../hid-sp18-511/swagger) filter (incomplete?)
* [../hid-sp18-524/swagger](../hid-sp18-524/swagger) converter (learning problem)
* [../hid-sp18-502/swagger](../hid-sp18-502/swagger)
	* variable (name, value, tyoe) store in mongo
	* get by name, should have used post not get
	* superseeded by our own keystors in mongodb 	
* [../hid-sp18-406/swagger](../hid-sp18-406/swagger) database info mongo
* [../hid-sp18-411/swagger](../hid-sp18-411/swagger) mongo db thing
* [../hid-sp18-418/swagger](../hid-sp18-418/swagger) virtual directory
* [../hid-sp18-421/swagger](../hid-sp18-421/swagger) logentry
* [../hid-sp18-508/swagger](../hid-sp18-508/swagger) profile, completely replaced
* AAA [../hid-sp18-417/swagger](../hid-sp18-417/swagger) strings (not relevant)
* [../hid-sp18-415/swagger](../hid-sp18-415/swagger) identity (incomplete)
* [../hid-sp18-410/swagger](../hid-sp18-410/swagger) timestamp of a file

	* [../hid-sp18-410/swagger-without-docker/flaskConnexion/swagger_server/test/test_default_controller.py](../hid-sp18-410/swagger-without-docker/flaskConnexion/swagger_server/test)
	* [../hid-sp18-410/swagger-without-docker/flaskConnexion/swagger_server/controllers/default_controller.py](../hid-sp18-410/swagger-without-docker/flaskConnexion/swagger_server/controllers)

* [../hid-sp18-412/swagger](../hid-sp18-412/swagger) key value store
* [../hid-sp18-406/old-swagger/flaskConnexion/swagger_server/test/test_default_controller.py](../hid-sp18-406/old-swagger/flaskConnexion/swagger_server/test) timestamp
* [../hid-sp18-406/old-swagger/flaskConnexion/swagger_server/controllers/default_controller.py](../hid-sp18-406/old-swagger/flaskConnexion/swagger_server/controllers) timestamp


Needs major cleanup

* [../hid-sp18-505/swagger](../hid-sp18-505/swagger) ? mongo - only eve server


* [../hid-sp18-510/swagger](../hid-sp18-510/swagger) ? machine learning -


Unclear - incomplete

* [../hid-sp18-601/swagger](../hid-sp18-601/swagger) subscribers (incomplete)
* [../hid-sp18-407/swagger](../hid-sp18-407/swagger) ??? -
* [../hid-sp18-501/swagger](../hid-sp18-501/swagger) ??? -
* [../hid-sp18-515/swagger](../hid-sp18-515/swagger) cpu example

* [../hid-sp18-512/swagger](../hid-sp18-512/swagger) --- nothing
* [../hid-sp18-602/swagger](../hid-sp18-602/swagger) --- incomplete
* [../hid-sp18-602/swagger-docker/openstack/default_controller.py](../hid-sp18-602/swagger-docker/openstack) openstac get images - superceeded by others

