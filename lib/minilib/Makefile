AMUSE_DIR?=$(shell amusifier --get_amuse_dir)
include ${AMUSE_DIR}/config.mk

MPICC ?= mpicc

LIBNAME = libminimuse_lib.a

OBJS = minilib.o minilibf.o

all:$(LIBNAME)

CFLAGS += -fPIC

$(LIBNAME): $(OBJS)
	ar -r  $(LIBNAME) $^
	ranlib $(LIBNAME)
	
%.o: %.c
	$(MPICC) $(CFLAGS) -c -o $@ $<
	
%.o: %.f90
	$(MPIFC) $(FCFLAGS) -c -o $@ $<

clean:
	rm -Rf *.o *.a *.mod

distclean: clean