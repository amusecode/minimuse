from amuse.test.amusetest import TestWithMPI

from .interface import fortran_exampleInterface
from .interface import fortran_example

class fortran_exampleInterfaceTests(TestWithMPI):
    
    def test1(self):
        instance = fortran_exampleInterface()
        result,error = instance.echo_int(12)
        self.assertEquals(error, 0)
        self.assertEquals(result, 12)
        instance.stop()
    
