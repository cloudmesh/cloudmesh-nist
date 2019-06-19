define banner
	@echo
	@echo "###################################"
	@echo $(1)
	@echo "###################################"
endef

#	$(call banner, "use: make doc")

resources = \
	virtualcluster \
	flavor \
	image \
	vm \
	variables \
	virtualdirectory \
	alias \
	containers \
	database \
	default \
	deployment \
	filestore \
	filter \
	microservice \
	nic \
	publickeystore \
	replica \
	reservation \
	secgroup \
	stream \
	user \
	timestamp \
	scheduler \
	organization \
	non