from amuse.community import *

class c_exampleInterface(CodeInterface):
    
    include_headers = ['worker_code.h']
    
    def __init__(self, **keyword_arguments):
        CodeInterface.__init__(self, name_of_the_worker="c_example_worker", **keyword_arguments)
    
    @legacy_function
    def echo_int():
        function = LegacyFunctionSpecification()  
        function.addParameter('int_in', dtype='int32', direction=function.IN)
        function.addParameter('int_out', dtype='int32', direction=function.OUT)
        function.result_type = 'int32'
        function.can_handle_array = True
        return function
    
    @legacy_function
    def add_one():
        function = LegacyFunctionSpecification()  
        function.addParameter('int_inout', dtype='int32', direction=function.INOUT)
        function.result_type = 'int32'
        function.can_handle_array = True
        return function

    
class c_example(InCodeComponentImplementation):

    def __init__(self, **options):
        InCodeComponentImplementation.__init__(self,  c_exampleInterface(**options), **options)
    
