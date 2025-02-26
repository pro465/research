IN: u
USING: sequences sequences.extras sequences.deep grouping.extras ;
! 
! : xi ( n -- n ) [ second 1 + ] [ first ] bi 4 mod { { 1 [ ] } { 3 [ 2 mod ] } [ 2drop 1 ] } case ;
! : num-sols ( n -- n ) group-factors [ xi ] map product 2/ ;
! : move ( n x y -- n x y ) [ 1 - ] dip [ 3dup [ dup * ] bi@ + > ] [ 1 + ] while ;
! : inner ( v n x y -- v n x y ) 
!     3dup [ dup * ] bi@ + = 
!     [ [ 2array swap [ suffix! ] dip ] 2keep ] when move ;
! : sols ( n -- seq ) V{ } clone swap dup integer-sqrt 1 + 0 [ 2dup > ] [ inner ] while 3drop ;
! 
: square? ( n -- ? ) dup 0 > [ dup integer-sqrt dup * = ] [ drop f ] if ;
! : condition ( n p1 p2 -- bool )
!     pick '[ first _ swap - ] bi@
!     { { -1 -1 } { 1 1 } }
!     [ first2 spin [ * ] 2bi@ + over + square? ] 2with all? nip ;
! 
! : find-pair ( n seq -- seq )
!     dup <enumerated> [ 
!         first2 [ dupd 1 + tail-slice ] dip
!         '[ _ 2array ] map pick
!         '[ first2 _ -rot condition ] filter
!     ] map concat 2nip ;
! 
! : grid ( n pair -- grid )
!     first2 pick '[ first _ swap - ] bi@
!     [ [ drop + ] [ + - ] [ nip + ] 3tri 3array ] 
!     [ [ - - ] [ 2drop ] [ - + ] 3tri 3array ]
!     [ [ nip - ] [ + + ] [ drop - ] 3tri 3array ] 
!     3tri 3array ;
! 
! 10 1000000 [a..b] [
!     dup * 
!     dup 2 * num-sols 3 >
!     [
!         dup 1000 mod 0 = [ dup . ] when
!         [ 2 * sols [ [ dup * ] map ] map ] keep
!         [ '[ [ _ + num-sols 2 > ] all? ] filter ] keep swap
!         dup length>> 1 >
!         [ dupd find-pair [ [ grid . ] with each 0 exit ] unless-empty drop ]
!         [ 2drop ] if
!     ] [ drop ] if
! ] each

: m ( -- m ) 128 ; inline
: lim ( -- l ) 1000 ; inline

: squares ( m -- set seq )
    dup [0..b) [ dup * swap mod ] with map deduplicate sort [ >hash-set ] keep ;

: mod-square? ( set n -- ? ) swap in? ;

: grid ( n a b -- seq )
    [ [ drop + ] [ + - ] [ nip + ] 3tri ] 
    [ [ - - ] [ 2drop ] [ - + ] 3tri ]
    [ [ nip - ] [ + + ] [ drop - ] 3tri ] 
    3tri 9 narray ;

: ?add ( set v n a b -- set v' )
    [ dupd - m rem ] bi@
    [ grid m [ rem ] curry map pick 
    swap [ mod-square? ] with all? ] 3keep 3array swap
    [ suffix! ] [ drop ] if ;

: inner ( set v n seq -- set v )
    <suffixes> [ [ first ] keep [ ?add ] 2with each ] with each ;

: find-triples ( set seq -- triples )
    V{ } clone swap dup [ inner ] curry each nip ;

: try-num ( arr -- arr )
    lim -1 * lim [a..b] dup [ [ 2array ] with map ] curry map flatten1
    [ [ first3 ] [ first2 ] bi* swapd [ m * + ] 2bi@ grid ] with map [ [ square? ] all? ] filter ;

m squares dup . find-triples dup . [ dup . try-num [ . ] unless-empty ] each 
