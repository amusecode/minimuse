# standard amuse configuration include
# config.mk will be made after ./configure has run
AMUSE_DIR?=$(shell amusifier --get_amuse_dir)
-include $(AMUSE_DIR)/config.mk

MPICXX   ?= mpicxx

CFLAGS   += -Wall -g -I$(MUSE_PACKAGE_DIR)/lib/minilib
CXXFLAGS += $(CFLAGS) 
LDFLAGS  += -lm $(MUSE_LD_FLAGS) -L$(MUSE_PACKAGE_DIR)/lib/minilib -lminimuse_lib

OBJS = interface.o

CODELIB = src/libc_example.a

all: c_example_worker 

clean:
	$(RM) -rf __pycache__
	$(RM) -f *.so *.o *.pyc worker_code.cc worker_code.h 
	$(RM) *~ c_example_worker worker_code.cc
	make -C src clean

distclean: clean
	make -C src distclean

$(CODELIB):
	make -C src all

worker_code.cc: interface.py
	$(CODE_GENERATOR) --type=c interface.py c_exampleInterface -o $@

worker_code.h: interface.py
	$(CODE_GENERATOR) --type=H interface.py c_exampleInterface -o $@

c_example_worker: worker_code.cc worker_code.h $(CODELIB) $(OBJS)
	$(MPICXX) $(CXXFLAGS) $< $(OBJS) $(CODELIB) -o $@ $(LDFLAGS)

.cc.o: $<
	$(CXX) $(CXXFLAGS) -c -o $@ $< 
