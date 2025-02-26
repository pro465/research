USING: kernel math math.primes math.primes.erato.fast prettyprint sequences ;
IN: your-walls 

: eval ( c n -- n' ) [ 1 - ] keep * + ; inline
: caboose? ( c -- ? ) dup <iota> [ eval prime? ] with all? ; inline
: c ( lim -- ) sieve [ dup caboose? [ . ] [ drop ] if ] each ;

[ 100000000 >fixnum c ] benchmark .
