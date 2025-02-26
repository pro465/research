# Universal Minsky Machine - By Proloy Mishra (May 2024)
# register # - function
# 0 - stores 0
# 1 - program part 1
# 2 - program part 2
# 3 - memory

# 4, 5, 6, etc. - scratch

# numbers in arguments (aka literals) are encoded using following method:
# b_0 b_1 b_2 ... b_n -> 1 b_0 1 b_1 1 b_2 ... 1 b_n 0
# where b_0 to b_n are the bits of the number (little endian)


# execution loop
# decode current instruction
# 00    - hlt
# 10... - inc
# 01... - decjz
# 11    - hlt
2 1000
2 6
2 70
2 1000
4
5
0 -5

# inc
# has 1 argument: reg

## restoring invariants
### restoring reg2
4 3
2
0 -2


## decode the literal (reg) and store it in reg4
5 28
5 3
6
0 -3

### reg4 *= 2
4 3
7
0 -2

7 4
4
4
0 -3

### reg1 = reg1*4 + 0b10
1 3
7
0 -2

7 6
1
1
1
1
0 -5

1
1

### reg5 = reg6/2
6 6
6 3
5
0 -3

### reg1 += reg6 & 1
1
### reg4 += reg6 & 1
4

0 -27

## reg1 = reg1*2
1 3
7
0 -2

7 4
1
1
0 -3

## reg2 = reg6
6 3
2
0 -2

## reg6 = reg5 = reg4
4 4
5
6
0 -3

## reg4 = reg3
3 3
4
0 -2

## reg3 = reg4 * reg5
4 12
5 3
3
0 -2

### restore reg5
6 4
5
7
0 -3

7 3
6
0 -2

0 -11

## cleanup scratches
5 2
0 -1
6 2
0 -1

## inc done (jump to start)
0 -72

# decjz
# has 2 arguments: reg, and addr
# addr is relative and signed
# also it denotes the number of bits to skip, not instructions

# restoring invariants
## reg2 = reg4
4 3
2
0 -2

## decode the literal (reg) and store it in reg4
5 28
5 3
6
0 -3

### reg4 *= 2
4 3
7
0 -2

7 4
4
4
0 -3

### reg1 = reg1*4 + 0b10
1 3
7
0 -2

7 6
1
1
1
1
0 -5

1
1

### reg5 = reg6/2
6 6
6 3
5
0 -3

### reg1 += reg6 & 1
1
### reg4 += reg6 & 1
4

0 -27

## reg1 = reg1*2
1 3
7
0 -2

7 4
1
1
0 -3

## reg2 = reg6
6 3
2
0 -2

## reg6 = reg5 = reg4
4 4
5
6
0 -3

## reg8 = reg4 = reg3
3 4
4
8
0 -3

## reg3 = reg4 / reg5
4 14
4

5 3
4 43
0 -2

3

### restore reg5
6 4
5
7
0 -3

7 3
6
0 -2

0 -13

## not zero
### ignore addr argument

#### reg1 *= 4
1 3
7
0 -2

7 6
1
1
1
1
0 -5

#### reg4 = reg2/2
2 12
2 3
4
0 -3

#### reg1 += (reg2 & 1)*2
1
1

4 5
4 3
2
0 -2

#### reg1 += reg4 & 1
1

0 -20

#### reg1 += reg2 & 1
2 5
2 3
4
0 -3

1

4 3
2
0 -2

### cleanup scratches
8 2
0 -1
5 2
0 -1
6 2
0 -1

### dec done (jump to start)
0 -172
## zero

### reg3 = reg8
8 3
3
0 -1

### reg5 = reg2
5 2
0 -1

2 3
5
0 -2

### decode the literal (addr) and store it in reg4
5 28
5 3
6
0 -3

#### reg4 *= 2
4 3
7
0 -2

7 4
4
4
0 -3

#### reg1 = reg1*4 + 0b10
1 3
7
0 -2

7

7 6
1
1
1
1
0 -5

#### reg5 = reg6/2
6 6
6 3
5
0 -3

#### reg1 += reg6 & 1
1
#### reg4 += reg6 & 1
4

0 -27

#### reg1 = reg1*4
1 3
7
0 -2

7 6
1
1
1
1
0 -5

#### reg2 = reg6/2
2 2
0 -1

6 19
6 3
2
0 -3

## copy reg4 bits from reg1 to reg2
### reg1 += 1
1

4 14

### reg2 *= 2
2 3
7
0 -2

7 4
2
2
0 -3

### reg6 = reg1/2
1 5
1 3
6
0 -3

### reg2 += reg1 & 1
2

### reg1 = reg6
6 3
1
0 -2

0 -13

0 15

## copy reg4 bits from reg2 to reg1
4 14

### reg1 *= 2
1 3
7
0 -2

7 4
1
1
0 -3

### reg6 = reg2/2
2 5
2 3
6
0 -3

### reg1 += reg2 & 1
1

### reg1 = reg6
6 3
1
0 -2

0 -13

### cleanup scratches
5 2
0 -1
6 2
0 -1

### jz done (jump to start)
0 -264
