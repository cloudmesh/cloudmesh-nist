OBJECTS=keystore profile


service:
	@for object in $(OBJECTS); do \
		cd $$object; make -f Makefile ;\
	done



mongo-start:
	make -f Makefile mongo_start


mongo-kill:
	make -f Makefile mongo_kill
