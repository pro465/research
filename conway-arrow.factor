IN: u

: unclip-last2 ( seq -- butlast2 penultimate ultimate )
    unclip-last [ unclip-last ] dip ; inline
: f ( seq -- num )
    dup length 3 <
    [ dup length 2 = [ first2 ^ ] [ first ] if ]
    [ unclip-last2 dup 1 >
        [
            over 1 >
            [ 3dup [ 1 - suffix ] dip suffix f spin drop 1 - [ suffix ] dip suffix ] 
            [ 2drop ] if
        ] [ drop suffix ] if f
    ] if ;

! 3 3 2 = 3 ( 3 2 2 ) 1 = 3 ( 3 ( 3 1 2 ) 1 ) 1 = 3 ( 27 ) = 3^27
{ 3 3 2 } f ...
