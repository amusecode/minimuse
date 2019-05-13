from amuse.community import *
from amuse.test.amusetest import TestWithMPI

from .interface import c_exampleInterface
from .interface import c_example

class c_exampleInterfaceTests(TestWithMPI):
    
    def test1(self):
        instance = c_exampleInterface()
        result,error = instance.echo_int(12)
        self.assertEquals(error, 0)
        self.assertEquals(result, 12)
        instance.stop()
    
