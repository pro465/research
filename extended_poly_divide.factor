USING: arrays formatting kernel math math.order math.vectors sequences vectors ;
IN: your-mom

: fmt ( v i -- ) swap "%d -> %d\n" printf ;

: multiply_and_subtract ( a b c -- a-b*c ) [ [ rest-slice ] bi@ ] dip v*n v- ;

: p_divmod ( dividend divisor -- remainder quotient ) 
    2dup [ first ] bi@ / [ multiply_and_subtract ] keep ;

: p_div_step ( dividend divisor i -- remainder ) 
    [ swap 2dup [ length ] bi@ - 0 max 0 <array> append! swap p_divmod ] dip fmt ;

: p_div ( dividend divisor i -- dividend divisor i ) 
    [ >vector ] 2dip 
    [ pick [ 0 = ] all? ]
    [ [ 2dup ] dip [ p_div_step nipd swap ] keep 1 - ] until ;

{ 4 8 12 } { 1 2 3 } 4 p_div
