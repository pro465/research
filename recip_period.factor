USING: io formatting generalizations kernel math math.functions math.parser ;
IN: your-walls

: recip-period-fast ( b n m -- p )
        '[
            ! b n v i
            3dup
            [ _ * swap mod zero? ] 
            [ <= ] bi-curry* bi or
        ]
    pick 1 - 1 rot
        [ [ pick [ * ] [ + ] bi 1 - over mod ] [ 1 + ] bi* ] 
    until 3nip ;

: recip-period ( b n -- m p ) 
    2dup gcd nip [ / ] keep 1 = [ 1 0 ] [ over 1 ] if 
    [ recip-period-fast ] dip swap ;

: input ( s -- str/f ) "%s" printf readln ;

: main ( -- )
    "Enter number: " "Enter base: " [ input string>number ] bi@ swap recip-period 
    "initial non-period length = %d\nperiod length = %d\n" printf ;

MAIN: main
