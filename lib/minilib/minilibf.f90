module fortran_minilib

  interface
    subroutine add1(i) bind(c, name='add1')
      use iso_c_binding
      integer (c_int) :: i
    end subroutine
  
  end interface


end module
