USING: arrays kernel math math.primes.factors sequences ;
IN: partition-numbers

: dupdd ( x y z -- x x y z ) [ dupd ] dip ;

: find-nonzero ( seq -- n )
    [ zero? not ] find drop ;

: sum-so-far ( a b n -- sum )
    [ divisors [ over length <= ] filter -rot ] keep
    [ roll [ / ] keep [ 1 - [ nth ] curry ] bi@ bi* * ] 3curry map sum ;

: find-term ( partial-q dividend divisor nonzero -- partial-q' )
    [ swap ] 2dip [ swapd sum-so-far ] 3keep swap nth [ -rot - ] dip /i suffix ;

: divide ( dividend divisor -- quotient )
    dup find-nonzero [ find-term ] 2curry { } swap reduce ;

: remaining ( num prev -- remaining )
    dup length dup divisors [ [ = ] keep 1 = or ] with reject
    [ [ dup length ] dip [ /i ] keep
        [ 1 - swap nth ] bi-curry@ bi [ first ] [ second ] bi* *
    ] with map sum - ;

: solve ( remaining a b -- solutions )
    swapd 2dup / [0..b] -roll
    [ roll * - [ nip 0 >= ] [ swap rem 0 = ] [ over /i 2array ] 2tri and and ] 
    3curry map [ not ] reject ;

: find-factors ( num -- factors )
    unclip divisors dup reverse zip [ 1array ] map
    [ { } spin [
        [ remaining ] keep
        [ first first2 solve ] keep
        swap [ suffix ] with map append
    ] with each ] reduce [ [ first ] map ] map ;

0 1 1 solve ...
{ 1 0 1 } find-factors ...
! { 1 0 1 } { 2 } divide
