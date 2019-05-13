from minimuse.community.c_example.interface import c_example
from minimuse.community.fortran_example.interface import fortran_example

if __name__=="__main__":
  

    print("instantiate a C code and a fortran code..")
    c_code=c_example()
    fortran_code=fortran_example()
    
    print("call to the codes to do some work")
    arg=123
    result1=c_code.echo_int(arg)
    result2=fortran_code.echo_int(arg)

    print("expected output: {0}".format(arg))
    print("c result:  {0}".format(result1))
    print("fortran results {0}".format(result2))
    
    c_code.stop()
    fortran_code.stop()
    
    print("done")
