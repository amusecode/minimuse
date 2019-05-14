# standard amuse configuration include
# config.mk will be made after ./configure has run
AMUSE_DIR?=$(shell amusifier --get_amuse_dir)
-include $(AMUSE_DIR)/config.mk

MPIFC ?= mpif90
FC      = $(MPIFC)

LDFLAGS  += -lm $(MUSE_LD_FLAGS)
FCFLAGS += -I$(MUSE_PACKAGE_DIR)/lib/minilib

FS_LIBS +=  -L$(MUSE_PACKAGE_DIR)/lib/minilib -lminimuse_lib

OBJS = interface.o

CODELIB = src/libfortran_example.a

all: fortran_example_worker 

clean:
	$(RM) -rf __pycache__
	$(RM) -f *.so *.o *.pyc worker_code.cc worker_code.h 
	$(RM) *~ worker_code worker_code.f90
	make -C src clean

distclean: clean
	make -C src distclean

$(CODELIB):
	make -C src all

worker_code.f90: interface.py
	$(CODE_GENERATOR) --type=f90 interface.py fortran_exampleInterface -o $@

fortran_example_worker: worker_code.f90 $(CODELIB) $(OBJS)
	$(MPIFC) $(FCFLAGS) $(FS_FLAGS) $< $(OBJS) $(CODELIB) $(FS_LIBS) -o $@

%.o: %.f90
	$(FC) $(FCFLAGS) -c -o $@ $<
