That was easy wasn't it? Now for pattern matching:

Consider the axiom
```
axiom a :: [f(X) |- g(X)]
```

Suppose we passed it `f(h(P))`. Then, the nyaya checker would first 
check that `f(h(P))` really matches the `f(X)` in the condition of 
the axiom for some value of `X`.

It would find that it really does match the condition with `X=h(P)`.

Then, it derives `g(X)` with `X=h(P)`, thus resulting in `g(h(P))`. 
we have proved `g(h(P))` from `f(h(P))`.

On the other hand, the nyaya checker would error out if we passed to
`a` the expression `impl(h(P))` because it cannot match `f(X)` for any value of `X`.
Passing `f()` or `f(d, J)` also don't work because the axiom 
expects a "function"/"property" with arity of exactly 1.

for a more complex example, let's take the axiom `modus_ponens` defined earlier.
If we pass it two expressions: `impl(impl(P, P), P)` and `impl(P, P)`, 
the checker works out that they actually match `impl(P, Q)` and `P` respectively
with `P=impl(P, P)` and `Q=P`. It's important to know that the `P` being assigned is the axiom's 
and not the same as the `P`s appearing in the RHS, which are there only because we passed an 
expression with `P` in it.

Let's pass `modus_ponens` a pair of expressions that we intuitively know it should not accept:
`impl(not(X), Y)` and `X`. If it accepts it and gives us `not(Y)`, then it has committed a logical 
fallacy known as "denying the antecendent". But will it?

the nyaya checker first checks the first condition and finds that it indeed matches, with `P=not(X)`
and `Q=Y`. However, when it checks the second condition, it sees that the only way it could be fulfilled 
is if `P=X`, but that is not consistent with what it previously derived (i.e., `P=not(X)`). 
Hence, it rejects our proof.


