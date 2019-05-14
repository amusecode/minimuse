FUNCTION echo_int(input, output)
    INTEGER echo
    INTEGER echo_int
    INTEGER input, output
    output = echo(input)
    echo_int = 0
END FUNCTION

FUNCTION add_one(output)
    use fortran_minilib
    INTEGER output
    call add1(output)
    add_one = 0
END FUNCTION
