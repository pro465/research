USING: kernel math prettyprint ;
IN: u

: f ( n -- n+1 ) 1 + ;
: g' ( m n -- n ) swap dup zero? [ drop f ] [ 1 - swap dup [ dupd g' dup 10000000 rem zero? [ dup . ] when ] times nip ] if ;
: g ( n -- n ) dup g' ;

3 g .
