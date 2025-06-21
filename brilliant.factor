USING: math.primes.factors sequences.private ;
IN: brilliant
: ?first2 ( seq -- first/f second/f )
    dup length dup 1 >
    [ drop first2-unsafe ]
    [ 0 > [ first-unsafe f ] [ drop f f ] if ] if ;
: brilliant? ( n -- ? ) factors [ length 2 = ] [ ?first2 = ] bi and ;
: largest-below ( n -- n ) [ dup brilliant? ] [ 1 - dup . ] until ;
: main ( -- ) 175 10^ largest-below . ;
MAIN: main 
