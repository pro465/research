def transform_sym(l,m):
    assert m in (0,1)
    return "(()"+"~>~,"*(l-1)+"~>,<"+'+'*m+")~>,<"+"~,"*m

def transform_seq(l,s):
    return "".join([transform_sym(l,i) for i in s])

# transform a table into an acceptable input encoding
def transform_table(l,table):
    return "".join([f"({transform_seq(l,i)})" for i in table])

# transform an cyclic tag system program into a mlatu-6 program
def transform_program(table, input):
    l=len(table)
    table=transform_table(l,table)
    input=transform_seq(l,input)
    end="(>+<,,()~<)+<"
    return table+"()"+input+end
"""
length is either 9 (for 0) or 32 (for 111)
assuming 50/50 probability...
3/4 1s, 1/4 0s
now in 1s, we have... (~+)~>,<~,
2 ",", 1 "+"
the 1 "+" leads to an increase by (9+32)/2=41/2 characters
the 2 ","s lead to a decrease by 2*2=4 characters
hence net change for 1 = 33/2

in 0 we get: (~)~>,<
1 ","
net change = -2
average active characters = (5+8*3)/4 = 29/4
so, expected difference = 4/29(33/2*3-2)/4 = (99/2-2)/29 = 95/58
subtract 1 to get a net difference of 37/58
"""
#print(transform_program([[1,1,1],[0]], [1]))
print(transform_program([[0],[0,1,1]], [1]).replace("()~>~,~>,<","~"))
