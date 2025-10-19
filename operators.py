#Types of Operators in Python
#An operator is a special symbol that performs a specific operation
#between two operands.

#1. Arithmetic Operators(+, -, *, /, %, **, //)
a = 10
b = 3
print("Addition:", a + b)          #Addition: 13
print("Subtraction:", a - b)       #Subtraction:7
print("Multiplication:", a * b)    #Multiplication:30
print("Division:", a / b)          #Division:3.3333333333333335
print("Modulus:", a % b)           #Modulus:1
print("Exponentiation:", a ** b)   #Exponentiation:1000
print("Floor Division:", a // b)   #Floor Division:3     Normally, 10 / 3 = 3.333..., but floor division gives the largest integer less than or equal to the result.

#2. Relational/Comparison Operators (==, !=, >, <, >=, <=)
x = 5
y = 8
print("Equal to:", x == y)          #Equal to: False
print("Not equal to:", x != y)      #Not equal to: True 
print("Greater than:", x > y)       #Greater than: False
print("Less than:", x < y)          #Less than: True
print("Greater than or equal to:", x >= y)  #Greater than or equal to: False
print("Less than or equal to:", x <= y)     #Less than or equal to: True

#complex comparison
z = 5
print("x == z and x < y:", x == z and x < y)  #x == z and x < y: True
print("x == z or x > y:", x == z or x > y)  #x == z or x > y: True

#camparison coplex (characters)
char1 = 'a'
char2 = 'b'
print("char1 < char2:", char1 < char2)  #char1 < char2: True (because 'a' comes before 'b' in ASCII)
print("char1 == char2:", char1 == char2)  #char1 == char2: False    
print("char1 != char2:", char1 != char2)  #char1 != char2: True 

#complex use of comparison
age = 25
is_teenager = age >= 13 and age <= 19
print("Is teenager:", is_teenager)  #Is teenager: False 

#use of comparison with strings
str1 = "apple"  
str2 = "banana"
print("str1 < str2:", str1 < str2)  #str1 < str2: True (because 'a' comes before 'b' in alphabetical order) it only chackes first character
print("str1 == str2:", str1 == str2)  #str1 == str2: False  
print("str1 != str2:", str1 != str2)  #str1 != str2: True

#another complex comparison
name1 = "Alice"
name2 = "Alice"
print("name1 == name2:", name1 == name2)  #name1 == name2: True
print("name1 != name2:", name1 != name2)  #name1 != name2: False
print("name1 < name2:", name1 < name2)    #name1 < name2: False
print("name1 <= name2:", name1 <= name2)  #name1 <= name2: True
print("name1 > name2:", name1 > name2)    #name1 > name2: False
print("name1 >= name2:", name1 >= name2)  #name1 >= name2: True 

#3.Assignment Operators (=, +=, -=, *=, /=, %=, **=, //=)
num = 10
print("Initial value:", num)  #Initial value: 10
num += 5
print("After += 5:", num)     #After += 5: 15
num -= 3
print("After -= 3:", num)     #After -= 3: 12
num *= 2
print("After *= 2:", num)     #After *= 2: 24
num /= 4
print("After /= 4:", num)     #After /= 4: 6.0
num %= 4
print("After %= 4:", num)     #After %= 4: 2.0
num **= 3
print("After **= 3:", num)     #After **= 3: 8.0
num //= 3
print("After //= 3:", num)     #After //= 3: 2.0

#use case of assignment operators
counter = 0 # Initializing counter
for i in range(1, 6):
    counter += i  # Incrementing counter by i
print("Final counter value:", counter)  #Final counter value: 15 

#use case of assignment operators with strings
greeting = "Hello"
greeting += ", World!"  # Concatenating strings
print(greeting)  #Hello, World!

#4. Logical Operators (and, or, not)
a = True
b = False
print("a and b:", a and b)  #a and b: False
print("a or b:", a or b)    #a or b: True
print("not a:", not a)      #not a: False   
print("not b:", not b)      #not b: True
#complex use of logical operators
x = 10
y = 5
z = 15
print("x > y and x < z:", x > y and x < z)  #x > y and x < z: True
print("x < y or x < z:", x < y or x < z)    #x < y or x < z: True
print("not (x > y):", not (x > y))          #not (x > y): False
#another complex use of logical operators
is_raining = True
has_umbrella = False
can_go_outside = not is_raining or has_umbrella
print("Can go outside:", can_go_outside)  #Can go outside: False    
#5. Bitwise Operators (&, |, ^, ~, <<, >>)
p = 5  # In binary: 0101
q = 3  # In binary: 0011
print("Bitwise AND:", p & q)   #Bitwise AND: 1   (In binary: 0001)
print("Bitwise OR:", p | q)    #Bitwise OR: 7    (In binary: 0111)  
print("Bitwise XOR:", p ^ q)   #Bitwise XOR: 6   (In binary: 0110)
print("Bitwise NOT p:", ~p)    #Bitwise NOT p: -6  (In binary: ...11111010)
print("Left Shift p by 1:", p << 1)  #Left Shift p by 1: 10  (In binary: 1010) adding 0 at right
print("Right Shift q by 1:", q >> 1) #Right Shift q by 1: 1   (In binary: 0001) removing 1 from right
#complex use of bitwise operators
a = 12  # In binary: 1100
b = 5   # In binary: 0101
print("a & b:", a & b)   #a & b: 4   (In binary: 0100)
print("a | b:", a | b)   #a | b: 13  (In binary: 1101)
print("a ^ b:", a ^ b)   #a ^ b: 9   (In binary: 1001)
print("~a:", ~a)         #~a: -13  (In binary: ...11110011)
print("a << 2:", a << 2) #a << 2: 48  (In binary: 110000)
print("a >> 2:", a >> 2) #a >> 2: 3   (In binary: 0011)
#another complex use of bitwise operators
# flags = 0b1010  # Binary representation of flags
# READ = 0b0001   # Read permission
# WRITE = 0b0010
# EXECUTE = 0b0100
# # Check if WRITE permission is set  
# has_write_permission = (flags & WRITE) != 0
# print("Has WRITE permission:", has_write_permission)  #Has WRITE permission: True   
# # Set EXECUTE permission    
# flags |= EXECUTE
# print("Updated flags after setting EXECUTE:", bin(flags))  #Updated flags after setting EXEC    

#how this operators are used in machine learning and data science
# Arithmetic operators are used in various calculations, such as computing loss functions, gradients, and updates to model parameters.
# Comparison operators are used to evaluate conditions, such as checking for convergence during training or filtering data based on certain criteria.
# Assignment operators are used to update variables, such as weights and biases in neural networks. 
# Logical operators are used in decision-making processes, such as implementing activation functions or conditional statements in algorithms.UTE: 0b1110
# Bitwise operators are used in low-level data manipulation, such as optimizing memory usage or implementing certain algorithms that require bit-level operations.
# For example, bitwise operations can be used in hashing functions or in certain image processing techniques.
# Overall, operators play a crucial role in implementing algorithms and performing computations in machine learning and data    science tasks.  
#Note: This is just a basic overview of operators in Python. There are more operators and advanced concepts that can be explored further.   

#bitwise operators in detailed
# Bitwise AND (&)
a = 6  # In binary: 0110
b = 3  # In binary: 0011
result_and = a & b  # Result: 0010 (2 in decimal)
print("Bitwise AND of", a, "and", b, "is:", result_and)
#what actually happens
#  0110  (6 in binary)    
#& 0011  (3 in binary) 
# -----
#  0010  (2 in binary)

# Bitwise OR (|)
result_or = a | b  # Result: 0111 (7 in decimal)
print("Bitwise OR of", a, "and", b, "is:", result_or)
#what actually happens
#  0110  (6 in binary)
#| 0011  (3 in binary)
# -----
#  0111  (7 in binary)
# Bitwise XOR (^)
result_xor = a ^ b  # Result: 0101 (5 in decimal)
print("Bitwise XOR of", a, "and", b, "is:", result_xor)
#what actually happens
#  0110  (6 in binary)
#^ 0011  (3 in binary)
# -----
#  0101  (5 in binary)
# Bitwise NOT (~)
result_not_a = ~a  # Result: 1001 (-7 in decimal, two's complement)
print("Bitwise NOT of", a, "is:", result_not_a)
#what actually happens
#  0110  (6 in binary)
# -----
#  1001  (-7 in binary, two's complement)
# Left Shift (<<)
result_left_shift = a << 1  # Result: 1100 (12 in decimal)
print("Left Shift of", a, "by 1 is:", result_left_shift)
#what actually happens
#  0110  (6 in binary)
#<< 1
# -----
#  1100  (12 in binary)
# Right Shift (>>)
result_right_shift = a >> 1  # Result: 0011 (3 in decimal)
print("Right Shift of", a, "by 1 is:", result_right_shift)
#what actually happens
#  0110  (6 in binary)
#>> 1
# -----
#  0011  (3 in binary)
# Note: Bitwise operators work on the binary representations of integers. They perform operations at the bit level, which can be useful for low-level programming tasks, such as manipulating flags or optimizing memory usage.
# Bitwise operators are not typically used with floating-point numbers or non-integer types, as they operate on the binary representation of integers.
# In summary, bitwise operators allow you to perform operations on individual bits of integers, enabling efficient manipulation of binary data.
