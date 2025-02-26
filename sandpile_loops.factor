USING: arrays assocs combinators
grouping grouping.extras
kernel math math.extras math.matrices math.vectors prettyprint
random sequences sequences.rotated sequences.shifted vectors ;
IN: your-mom

: ?set-first ( seq first -- newseq ) 0 rot [ ?set-nth ] keep ; inline

: com ( 2darr -- c )
    { 0 0 } [ [ 2array n*v v+ ] curry swapd reduce-index ] reduce-index ;

: num-primitives ( n -- p )
    { 1 } swap <iota> [
        drop { 0 0 0 } [ prepend ] [ append ] bi 
        4 <clumps> [ sum ] map
    ] each ;

! 100 num-primitives ...

: spill ( matrix -- matrix' ) [ 4 >= 1 0 ? ] matrix-map ;

: step ( 2darr -- 2darr' )
    dup spill {
        [ 1 <rotated> ]
        [ -1 <rotated> ]
        [ [ 1 <rotated> ] map ]
        [ [ -1 <rotated> ] map ]
        [ -4 m*n ]
    } cleave m+ m+ m+ m+ m+ ;

: run ( arr -- trace )
    dup 1vector
    [ [ step ] dip dup [ pick = ] find drop not ]
    [ [ push ] 2keep ] while [ push ] keep ;

: cycle ( arr -- cycle ) run unclip-last [ = ] curry dupd find drop tail-slice ; inline

: matrix-by ( m n quot: ( ... -- ... newelt ) -- m )
    [ replicate ] 2curry replicate ; inline

: rand-partition ( k n -- p )
    [ dup <iota> dup pick [ swap - ] curry map zip weighted-random [ - ] keep ] replicate swap suffix randomize ;

: rand-matrix ( k h w -- m )
    [ * rand-partition ] 2keep [ unclip ] matrix-by nip ;

: rand-mat-step ( h w k -- h w k ? )
    3dup -rot rand-matrix dup cycle dup length 1 = 
    [ 2drop t ] [
        [ spill ] map unclip [ m+ ] reduce [ [ 2 > ] all? ] all? not 
        [ [ dup cycle . ] unless . ] keep
    ] if ;

: run-rand-matrix ( k w h -- ) 
    spin <iota> 0 swap
    [
        [ 1 + ] dip
        dup [ drop [ rand-mat-step ] dip swap ] all?
    ] loop 4drop ;

: map-last ( seq quot: ( ... a -- ... a ) -- seq' )
    [ unclip-last ] dip call suffix ; inline

: min-requirements ( h w -- n )
    2dup [ 1 ] <matrix-by> [ 4 m*n ] keep
    [ pick [ 0 ] replicate 1 swap <shifted> ]
    [ [ 1 0 <shifted> ] map ] bi m+
    [
      swap 1 = [ [ [ 1 - ] map-last ] map ] unless 
      swap 1 = [ [ 1 v-n ] map-last ] unless
    ] dip m-
    0 [ sum + ] reduce ;

2 3 min-requirements .

f
[ 1000 3 3
run-rand-matrix
 { { 2 3 2 2 1 }
  { 3 2 1 1 1 } 
  { 1 2 3 3 4 }
  { 3 3 3 2 0 }
  { 2 0 2 3 1 } }
run [ length . ] [ ... ] bi ] when

