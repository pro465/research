# pick m'th (0-indexed) entry in (n+1)-tag system
def transform_sym(l,n,m):
    assert m<l
    return "(()"+"~>~,"*n+"~>,<+)~>,<~<"+"-"*m+"~-"*(l-m-1)+","

def transform_seq(l,n,s):
    return "".join([transform_sym(l,n,i) for i in s])

# transform a table into an acceptable input encoding
def transform_table(table,n):
    l=len(table)
    t="".join([f"({transform_seq(l,n,i)})" for i in table])
    return f"({t})"+f"({'()'*l})"*n

# transform an (n+1)-tag system program into a mlatu-6 program
def transform_program(n, table, input):
    l=len(table)
    table=transform_table(table,n)
    input=transform_seq(l,n,input)
    end="(>+<,,()~<)+<"
    return table+"()"+input+end

print(transform_program(1, [[0,1],[2],[2,0,1,0]], [2,2]))
