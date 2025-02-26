IN: u 

: odd-loop ( n -- n' )
    1 + factor-2s [ 3 swap ^ ] dip * 1 - ;

: even-loop ( n -- n' )
    factor-2s nip ;

: step ( n -- n' )
    dup even? [ even-loop ] [ odd-loop ] if ;

: collatz ( n -- ? )
    dup step [ 2dup < ] [ step ] while = ;

: find-exception ( lim -- )
    2 swap [a..b] [ collatz ] find nip . ;

1000000000 find-exception
