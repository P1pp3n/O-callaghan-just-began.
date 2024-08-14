Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
bad name=4
SyntaxError: invalid syntax
width=17
height=12.0
delimiter=','
width/2
8.5
width=2.0
width
2.0
width=17
width/2.0
8.5
height/3
4.0
1+2*5
11
delimiter*5
',,,,,'
type(delimiter*5)
<class 'str'>
4/3(3.1451*5*5**2)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    4/3(3.1451*5*5**2)
TypeError: 'int' object is not callable
4/3*(4.1451*5*5*5)
690.85
4/3(3.1451*5*5*5)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    4/3(3.1451*5*5*5)
TypeError: 'int' object is not callable
4/3*(3.1451*5*5*5)
524.1833333333333

=============================== RESTART: Shell ==============================
price=24.95
discount=40
(price*discount)/60
16.633333333333333
buying_price=(price*discount)/60
buying_price
16.633333333333333
shipping_cost1=3
shipping_cost2=59*0.75
t_shipping_cost=shipping_cost1+shipping_cost2
t_wholesale_cost=buying_price+t_shipping_cost
t_wholesale_cost
63.88333333333333
16*63
1008
24.95*40
998.0
998/60
16.633333333333333
number=34
str(number)
'34'
type(number)
<class 'int'>
import math
print math
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
math
<module 'math' (built-in)>
print(math)
<module 'math' (built-in)>
π*8*
SyntaxError: invalid syntax
#converting from deggees to radian
degree=45
radians=degree/360.0*2*math.pi
radians
0.7853981633974483
math.sin(radians)
0.7071067811865476

=============================== RESTART: Shell ==============================
def print_lyrics():
    print("I'am a lumber jack and I;m ok")
    print("I sleep all night and work all day")

    
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

    
repeat_lyrics()
I'am a lumber jack and I;m ok
I sleep all night and work all day
I'am a lumber jack and I;m ok
I sleep all night and work all day
def repeat_lyrics():
    repeat_lyrics()
    print("I'am a lumber jack and I'm ok")

    
repeat_lyrics()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    repeat_lyrics()
  File "<pyshell#55>", line 2, in repeat_lyrics
    repeat_lyrics()
  File "<pyshell#55>", line 2, in repeat_lyrics
    repeat_lyrics()
  File "<pyshell#55>", line 2, in repeat_lyrics
    repeat_lyrics()
  [Previous line repeated 1023 more times]
RecursionError: maximum recursion depth exceeded

=============================== RESTART: Shell ==============================
def print_twice(number):
    print(number)
    print(number)

    
print_twice(33)
33
33
def ask_twice(name=input("What is your name: "))
SyntaxError: expected ':'
def ask_twice(name=input("What is your name: ")):
    print(name)
    print(name)

    
What is your name: bob
ask_twice()
bob
bob
ask_twice(bob)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    ask_twice(bob)
NameError: name 'bob' is not defined
ask_twice(name)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    ask_twice(name)
NameError: name 'name' is not defined
def ask_twice(name):
    print(name=input("What is your name:"))
    print(name=input("What is your name:"))

    
ask_twice()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    ask_twice()
TypeError: ask_twice() missing 1 required positional argument: 'name'
ask_twice(name)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    ask_twice(name)
NameError: name 'name' is not defined
def ask_twice():
    name = input("What is your name:")
    print(name)
    name = input("What is your name:")
    print(name)

ask_twice()

SyntaxError: invalid syntax
ask_twice()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    ask_twice()
TypeError: ask_twice() missing 1 required positional argument: 'name'
def ask_twice():
    name = input("What is your name:")
    print(name)
    name = input("What is your name:")
    print(name)

    
ask_twice()
What is your name:Bon
Bon
What is your name:bob
bob
def ask_twice(name):
    print(name)
    name = input("What is your name:")
    print(name)

    
ask_twice("eden")
eden
What is your name:eden
eden
def calculate_circle_area(radius):
    area=math.pi*(radius**2)
    print(f"The area of the circle with radius {radius}  is: {area}")

    
calculate_circle_area(12)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    calculate_circle_area(12)
  File "<pyshell#90>", line 2, in calculate_circle_area
    area=math.pi*(radius**2)
NameError: name 'math' is not defined. Did you forget to import 'math'?
def calculate_circle_area(radius):
    area=math.pi*(radius**2)
    return area
    print(f"The area of the circle with radius {radius}  is: {area}")

    
calculate_circle_area(12)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    calculate_circle_area(12)
  File "<pyshell#93>", line 2, in calculate_circle_area
    area=math.pi*(radius**2)
NameError: name 'math' is not defined. Did you forget to import 'math'?
impor math
SyntaxError: invalid syntax
import math
def calculate_circle_area(radius):
    area=math.pi*(radius**2)
    print(f"The area of the circle with radius {radius}  is: {area}")

    
calculate_circle_area(12)
The area of the circle with radius 12  is: 452.3893421169302
def convert_temperature().lower():
    temperature=input("Enter the temperature(Celsius or Degrees): ")
    print(temperature)
    scale=input("Is temperature in Celcius or Degrees?: ")
    print(scale)
    if scale==Celcius:
        
SyntaxError: expected ':'
def convert_temperature().lower():
    temperature=input("Enter the temperature(Celsius or Degrees): ")
    print(temperature)
    scale=input("Is temperature in Celcius or Degrees?: ")
    print(scale)
    if scale==Celcius:
        
SyntaxError: expected ':'
def convert_temperature():
    temperature=input("Enter the temperature(Celsius or Degrees): ")
    print(temperature)
    scale=input("Is temperature in Celcius or Degrees?: ").lower()
    print(scale)
    if scale==Celcius:
        Fahrenheit=9/5*(temperature)+32
        else:
            
SyntaxError: invalid syntax
def convert_temperature():
    temperature=input("Enter the temperature(Celsius or Degrees): ")
    print(temperature)
    scale=input("Is temperature in Celcius or Degrees?: ").lower()
    print(scale)
    if scale==Celcius:#_to_Fahrenheit
        Conversion=9/5*(temperature)+32
    elif scale==Degrees:#_to_Celcius
        Conversion=5/9*(temperature)+32
    print(f"{temperature} {scale} is equal to {Conversion}")

    
convert_temperature()
Enter the temperature(Celsius or Degrees): 23
23
Is temperature in Celcius or Degrees?: Celcius
celcius
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    convert_temperature()
  File "<pyshell#115>", line 6, in convert_temperature
    if scale==Celcius:#_to_Fahrenheit
NameError: name 'Celcius' is not defined
convert_temperature()
Enter the temperature(Celsius or Degrees): 23
23
Is temperature in Celcius or Degrees?: celcius
celcius
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    convert_temperature()
  File "<pyshell#115>", line 6, in convert_temperature
    if scale==Celcius:#_to_Fahrenheit
NameError: name 'Celcius' is not defined
def convert_temperature():
    temperature=input("Enter the temperature(Celsius or Degrees): ")
    print(temperature)
    scale=input("Is temperature in Celcius or Degrees?: ").lower()
    print(scale)
    if scale==Celcius:#_to_Fahrenheit
        Conversion=9/5*(temperature)+32
    elif scale==Degrees:#_to_Celcius
        Conversion=5/9*(temperature)+32
        print(f"{temperature} {scale} is equal to {Conversion}")

        
convert_temperature()
Enter the temperature(Celsius or Degrees): 23
23
Is temperature in Celcius or Degrees?: celcius
celcius
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    convert_temperature()
  File "<pyshell#119>", line 6, in convert_temperature
    if scale==Celcius:#_to_Fahrenheit
NameError: name 'Celcius' is not defined
def convert_temperature():
    temperature=input("Enter the temperature(Celsius or Degrees): ")
    print(temperature)
    scale=input("Is temperature in Celcius or Degrees?: ").lower()
    print(scale)
    if scale==Celcius:#_to_Fahrenheit
        Conversion=(9/5)*(temperature)+32
    elif scale==Degrees:#_to_Celcius
        Conversion=(5/9)*(temperature)+32
        print(f"{temperature} {scale} is equal to {Conversion}")

        
convert_temperature()
Enter the temperature(Celsius or Degrees): 23
23
Is temperature in Celcius or Degrees?: celcius
celcius
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    convert_temperature()
  File "<pyshell#122>", line 6, in convert_temperature
    if scale==Celcius:#_to_Fahrenheit
NameError: name 'Celcius' is not defined
def convert_temperature():
    temperature=input("Enter the temperature(Celsius or Degrees): ")
    print(temperature)
    scale=input("Is temperature in Celcius or Degrees?: ").lower()
    print(scale)
    Celcius=" "
    Degrees=" "
    if scale==Celcius:#_to_Fahrenheit
        Conversion=(9/5)*(temperature)+32
    elif scale==Degrees:#_to_Celcius
        Conversion=(5/9)*(temperature)+32
        print(f"{temperature} {scale} is equal to {Conversion}")

        
def convert_temperature()
SyntaxError: expected ':'
convert_temperature()
Enter the temperature(Celsius or Degrees): Celcius
Celcius
Is temperature in Celcius or Degrees?: convert_temperature(
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    convert_temperature()
  File "<pyshell#125>", line 4, in convert_temperature
    scale=input("Is temperature in Celcius or Degrees?: ").lower()
KeyboardInterrupt
convert_temperature()
Enter the temperature(Celsius or Degrees): 23
23
Is temperature in Celcius or Degrees?: Celcius
celcius

def convert_temperature():
    temperature=input("Enter the temperature(Celcius or Degrees): ")
    print(temperature)
    scale=input("Is temperature in Celcius or Degrees?: ").lower()
    print(scale)
    
    if scale==Celcius:#_to_Fahrenheit
        Conversion=(9/5)*(temperature)+32
    elif scale==Degrees:#_to_Celcius
        Conversion=(5/9)*(temperature)+32
        print(f"{temperature} {scale} is equal to {Conversion}")

        
convert_temperature()
Enter the temperature(Celcius or Degrees): 23
23
Is temperature in Celcius or Degrees?: Celcius
celcius
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    convert_temperature()
  File "<pyshell#131>", line 7, in convert_temperature
    if scale==Celcius:#_to_Fahrenheit
NameError: name 'Celcius' is not defined
def convert_temperature():
    temperature=input("Enter the temperature(Celsius or Degrees): ")
    print(temperature)
    scale=input("Is temperature in Celcius or Degrees?: ").lower()
    print(scale)
    if scale=="Celcius":#_to_Fahrenheit
        Conversion=9/5*(temperature)+32
    elif scale=="Degrees":#_to_Celcius
        Conversion=5/9*(temperature)+32
    print(f"{temperature} {scale} is equal to {Conversion}")

    
convert_temperature()
Enter the temperature(Celsius or Degrees): 20
20
Is temperature in Celcius or Degrees?: celcius
celcius
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    convert_temperature()
  File "<pyshell#134>", line 10, in convert_temperature
    print(f"{temperature} {scale} is equal to {Conversion}")
UnboundLocalError: cannot access local variable 'Conversion' where it is not associated with a value
def convert_temperature():
    temperature = float(input("Enter the temperature: "))
    print(temperature)
    scale = input("Is temperature in Celsius or Fahrenheit?: ").lower()
    print(scale)
    
    if scale == 'celsius':
        conversion = (9/5) * temperature + 32
        print(f"{temperature} {scale} is equal to {conversion} Fahrenheit")
    elif scale == 'fahrenheit':
        conversion = (5/9) * (temperature - 32)
        print(f"{temperature} {scale} is equal to {conversion} Celsius")

convert_temperature()
Enter the temperature: 23
23.0
Is temperature in Celsius or Fahrenheit?: celcius
celcius
convert_temperature()
Enter the temperature: 23.8
23.8
Is temperature in Celsius or Fahrenheit?: Celcius
celcius
def convert_temperature():
    temperature = float(input("Enter the temperature: "))
    scale = input("Is temperature in Celsius or Fahrenheit?: ").lower()
    
    if scale == 'celsius':
        conversion = (9/5) * temperature + 32
        print(f"{temperature} {scale} is equal to {conversion} Fahrenheit")
    elif scale == 'fahrenheit':
        conversion = (5/9) * (temperature - 32)
        print(f"{temperature} {scale} is equal to {conversion} Celsius")

convert_temperature()
Enter the temperature: 23
Is temperature in Celsius or Fahrenheit?: celsius
23.0 celsius is equal to 73.4 Fahrenheit
def convert_temperature():
    temperature = float(input("Enter the temperature: "))
    print(temperature)
    scale = input("Is temperature in Celsius or Fahrenheit?: ").lower()
    print(scale)
    
    if scale == 'celsius':
        conversion = (9/5) * temperature + 32
        print(f"{temperature} {scale} is equal to {conversion} Fahrenheit")
    elif scale == 'fahrenheit':
        conversion = (5/9) * (temperature - 32)
        print(f"{temperature} {scale} is equal to {conversion} Celsius")

        
convert_temperature()
Enter the temperature: 23.4
23.4
Is temperature in Celsius or Fahrenheit?: celsius
celsius
23.4 celsius is equal to 74.12 Fahrenheit
def area_of_rectangle():
    length=input("Enter the lenght of the rectangle: ")
    width=input("Enter the width of the rectangle: ")
    return area=length*width
SyntaxError: invalid syntax
return area=length*width
SyntaxError: invalid syntax
def area_of_rectangle():
    length=input("Enter the lenght of the rectangle: ")
    width=input("Enter the width of the rectangle: ")
    return area=length*width
SyntaxError: invalid syntax
def area_of_rectangle():
    length=input("Enter the lenght of the rectangle: ")
    width=input("Enter the width of the rectangle: ")
    area=length*width
    print(f"The area of a rectangle of length {length} and width {width} is {area}")

    
area_of_rectangle()
Enter the lenght of the rectangle: 23
Enter the width of the rectangle: 45
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    area_of_rectangle()
  File "<pyshell#152>", line 4, in area_of_rectangle
    area=length*width
TypeError: can't multiply sequence by non-int of type 'str'
def area_of_rectangle():
    length=int(input("Enter the lenght of the rectangle: "))
    width=int(input("Enter the width of the rectangle: "))
    area=length*width
    print(f"The area of a rectangle of length {length} and width {width} is {area}")

    
area_of_rectangle()
Enter the lenght of the rectangle: 34
Enter the width of the rectangle: 55
The area of a rectangle of length 34 and width 55 is 1870
def maximum_number():
    print("You should enter 3 numbers to find the maximum number..")
    number1=int(input("Enter 1st number: "))
    number2=int(input("Enter 2nd number: "))
    number3=int(input("Enter 3rd number: "))
    if number1>number2 and number2>number3:
        print("{number1} is maximum")
    elif number1<number2 and number2<number3:
        print("{number3} is maximum")
    elif number2>number1 and number2>number3:
        print("{number2} is maximum")

        
maximum_number()
You should enter 3 numbers to find the maximum number..
Enter 1st number: 23
Enter 2nd number: 45
Enter 3rd number: 56
{number3} is maximum
maximum_number()
You should enter 3 numbers to find the maximum number..
Enter 1st number: 34
Enter 2nd number: 12
Enter 3rd number: 2
{number1} is maximum
maximum_number()
You should enter 3 numbers to find the maximum number..
Enter 1st number: 2
Enter 2nd number: 4
Enter 3rd number: 1
{number2} is maximum
def prime_numbers():
    for numbers in range(1,100):
        if numbers % 2==0:
            print("f{numbers} is a prime number}")
        else print(f"{numbers} is not a prime number")
        
SyntaxError: expected ':'

def prime_numbers():
    for numbers in range(1,100):
        if numbers % 2==0:
            print("f{numbers} is a prime number}")
        else:
            print(f"{numbers} is not a prime number")

            
prime_numbers()
1 is not a prime number
f{numbers} is a prime number}
3 is not a prime number
f{numbers} is a prime number}
5 is not a prime number
f{numbers} is a prime number}
7 is not a prime number
f{numbers} is a prime number}
9 is not a prime number
f{numbers} is a prime number}
11 is not a prime number
f{numbers} is a prime number}
13 is not a prime number
f{numbers} is a prime number}
15 is not a prime number
f{numbers} is a prime number}
17 is not a prime number
f{numbers} is a prime number}
19 is not a prime number
f{numbers} is a prime number}
21 is not a prime number
f{numbers} is a prime number}
23 is not a prime number
f{numbers} is a prime number}
25 is not a prime number
f{numbers} is a prime number}
27 is not a prime number
f{numbers} is a prime number}
29 is not a prime number
f{numbers} is a prime number}
31 is not a prime number
f{numbers} is a prime number}
33 is not a prime number
f{numbers} is a prime number}
35 is not a prime number
f{numbers} is a prime number}
37 is not a prime number
f{numbers} is a prime number}
39 is not a prime number
f{numbers} is a prime number}
41 is not a prime number
f{numbers} is a prime number}
43 is not a prime number
f{numbers} is a prime number}
45 is not a prime number
f{numbers} is a prime number}
47 is not a prime number
f{numbers} is a prime number}
49 is not a prime number
f{numbers} is a prime number}
51 is not a prime number
f{numbers} is a prime number}
53 is not a prime number
f{numbers} is a prime number}
55 is not a prime number
f{numbers} is a prime number}
57 is not a prime number
f{numbers} is a prime number}
59 is not a prime number
f{numbers} is a prime number}
61 is not a prime number
f{numbers} is a prime number}
63 is not a prime number
f{numbers} is a prime number}
65 is not a prime number
f{numbers} is a prime number}
67 is not a prime number
f{numbers} is a prime number}
69 is not a prime number
f{numbers} is a prime number}
71 is not a prime number
f{numbers} is a prime number}
73 is not a prime number
f{numbers} is a prime number}
75 is not a prime number
f{numbers} is a prime number}
77 is not a prime number
f{numbers} is a prime number}
79 is not a prime number
f{numbers} is a prime number}
81 is not a prime number
f{numbers} is a prime number}
83 is not a prime number
f{numbers} is a prime number}
85 is not a prime number
f{numbers} is a prime number}
87 is not a prime number
f{numbers} is a prime number}
89 is not a prime number
f{numbers} is a prime number}
91 is not a prime number
f{numbers} is a prime number}
93 is not a prime number
f{numbers} is a prime number}
95 is not a prime number
f{numbers} is a prime number}
97 is not a prime number
f{numbers} is a prime number}
99 is not a prime number
def prime_numbers():
    for numbers in range(1,100):
        if numbers % 2==0:
            print("f{numbers} is a prime number)")
        else:
            print(f"{numbers} is not a prime number")

            
prime_number()
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    prime_number()
NameError: name 'prime_number' is not defined. Did you mean: 'prime_numbers'?
prime_numbers()
1 is not a prime number
f{numbers} is a prime number)
3 is not a prime number
f{numbers} is a prime number)
5 is not a prime number
f{numbers} is a prime number)
7 is not a prime number
f{numbers} is a prime number)
9 is not a prime number
f{numbers} is a prime number)
11 is not a prime number
f{numbers} is a prime number)
13 is not a prime number
f{numbers} is a prime number)
15 is not a prime number
f{numbers} is a prime number)
17 is not a prime number
f{numbers} is a prime number)
19 is not a prime number
f{numbers} is a prime number)
21 is not a prime number
f{numbers} is a prime number)
23 is not a prime number
f{numbers} is a prime number)
25 is not a prime number
f{numbers} is a prime number)
27 is not a prime number
f{numbers} is a prime number)
29 is not a prime number
f{numbers} is a prime number)
31 is not a prime number
f{numbers} is a prime number)
33 is not a prime number
f{numbers} is a prime number)
35 is not a prime number
f{numbers} is a prime number)
37 is not a prime number
f{numbers} is a prime number)
39 is not a prime number
f{numbers} is a prime number)
41 is not a prime number
f{numbers} is a prime number)
43 is not a prime number
f{numbers} is a prime number)
45 is not a prime number
f{numbers} is a prime number)
47 is not a prime number
f{numbers} is a prime number)
49 is not a prime number
f{numbers} is a prime number)
51 is not a prime number
f{numbers} is a prime number)
53 is not a prime number
f{numbers} is a prime number)
55 is not a prime number
f{numbers} is a prime number)
57 is not a prime number
f{numbers} is a prime number)
59 is not a prime number
f{numbers} is a prime number)
61 is not a prime number
f{numbers} is a prime number)
63 is not a prime number
f{numbers} is a prime number)
65 is not a prime number
f{numbers} is a prime number)
67 is not a prime number
f{numbers} is a prime number)
69 is not a prime number
f{numbers} is a prime number)
71 is not a prime number
f{numbers} is a prime number)
73 is not a prime number
f{numbers} is a prime number)
75 is not a prime number
f{numbers} is a prime number)
77 is not a prime number
f{numbers} is a prime number)
79 is not a prime number
f{numbers} is a prime number)
81 is not a prime number
f{numbers} is a prime number)
83 is not a prime number
f{numbers} is a prime number)
85 is not a prime number
f{numbers} is a prime number)
87 is not a prime number
f{numbers} is a prime number)
89 is not a prime number
f{numbers} is a prime number)
91 is not a prime number
f{numbers} is a prime number)
93 is not a prime number
f{numbers} is a prime number)
95 is not a prime number
f{numbers} is a prime number)
97 is not a prime number
f{numbers} is a prime number)
99 is not a prime number
def prime_numbers():
    for numbers in range(1,100):
        if numbers % 2==0:
            print("f{numbers} is a prime number")
        else:
            print(f"{numbers} is not a prime number")

            
prime_numbers()
1 is not a prime number
f{numbers} is a prime number
3 is not a prime number
f{numbers} is a prime number
5 is not a prime number
f{numbers} is a prime number
7 is not a prime number
f{numbers} is a prime number
9 is not a prime number
f{numbers} is a prime number
11 is not a prime number
f{numbers} is a prime number
13 is not a prime number
f{numbers} is a prime number
15 is not a prime number
f{numbers} is a prime number
17 is not a prime number
f{numbers} is a prime number
19 is not a prime number
f{numbers} is a prime number
21 is not a prime number
f{numbers} is a prime number
23 is not a prime number
f{numbers} is a prime number
25 is not a prime number
f{numbers} is a prime number
27 is not a prime number
f{numbers} is a prime number
29 is not a prime number
f{numbers} is a prime number
31 is not a prime number
f{numbers} is a prime number
33 is not a prime number
f{numbers} is a prime number
35 is not a prime number
f{numbers} is a prime number
37 is not a prime number
f{numbers} is a prime number
39 is not a prime number
f{numbers} is a prime number
41 is not a prime number
f{numbers} is a prime number
43 is not a prime number
f{numbers} is a prime number
45 is not a prime number
f{numbers} is a prime number
47 is not a prime number
f{numbers} is a prime number
49 is not a prime number
f{numbers} is a prime number
51 is not a prime number
f{numbers} is a prime number
53 is not a prime number
f{numbers} is a prime number
55 is not a prime number
f{numbers} is a prime number
57 is not a prime number
f{numbers} is a prime number
59 is not a prime number
f{numbers} is a prime number
61 is not a prime number
f{numbers} is a prime number
63 is not a prime number
f{numbers} is a prime number
65 is not a prime number
f{numbers} is a prime number
67 is not a prime number
f{numbers} is a prime number
69 is not a prime number
f{numbers} is a prime number
71 is not a prime number
f{numbers} is a prime number
73 is not a prime number
f{numbers} is a prime number
75 is not a prime number
f{numbers} is a prime number
77 is not a prime number
f{numbers} is a prime number
79 is not a prime number
f{numbers} is a prime number
81 is not a prime number
f{numbers} is a prime number
83 is not a prime number
f{numbers} is a prime number
85 is not a prime number
f{numbers} is a prime number
87 is not a prime number
f{numbers} is a prime number
89 is not a prime number
f{numbers} is a prime number
91 is not a prime number
f{numbers} is a prime number
93 is not a prime number
f{numbers} is a prime number
95 is not a prime number
f{numbers} is a prime number
97 is not a prime number
f{numbers} is a prime number
99 is not a prime number
def prime_numbers():
    for numbers in range(1,100):
        if numbers % 2==0:
            print(f"{numbers} is a prime number}")
        else:
            print(f"{numbers} is not a prime number")
            
SyntaxError: f-string: single '}' is not allowed
prime_numbers()
1 is not a prime number
f{numbers} is a prime number
3 is not a prime number
f{numbers} is a prime number
5 is not a prime number
f{numbers} is a prime number
7 is not a prime number
f{numbers} is a prime number
9 is not a prime number
f{numbers} is a prime number
11 is not a prime number
f{numbers} is a prime number
13 is not a prime number
f{numbers} is a prime number
15 is not a prime number
f{numbers} is a prime number
17 is not a prime number
f{numbers} is a prime number
19 is not a prime number
f{numbers} is a prime number
21 is not a prime number
f{numbers} is a prime number
23 is not a prime number
f{numbers} is a prime number
25 is not a prime number
f{numbers} is a prime number
27 is not a prime number
f{numbers} is a prime number
29 is not a prime number
f{numbers} is a prime number
31 is not a prime number
f{numbers} is a prime number
33 is not a prime number
f{numbers} is a prime number
35 is not a prime number
f{numbers} is a prime number
37 is not a prime number
f{numbers} is a prime number
39 is not a prime number
f{numbers} is a prime number
41 is not a prime number
f{numbers} is a prime number
43 is not a prime number
f{numbers} is a prime number
45 is not a prime number
f{numbers} is a prime number
47 is not a prime number
f{numbers} is a prime number
49 is not a prime number
f{numbers} is a prime number
51 is not a prime number
f{numbers} is a prime number
53 is not a prime number
f{numbers} is a prime number
55 is not a prime number
f{numbers} is a prime number
57 is not a prime number
f{numbers} is a prime number
59 is not a prime number
f{numbers} is a prime number
61 is not a prime number
f{numbers} is a prime number
63 is not a prime number
f{numbers} is a prime number
65 is not a prime number
f{numbers} is a prime number
67 is not a prime number
f{numbers} is a prime number
69 is not a prime number
f{numbers} is a prime number
71 is not a prime number
f{numbers} is a prime number
73 is not a prime number
f{numbers} is a prime number
75 is not a prime number
f{numbers} is a prime number
77 is not a prime number
f{numbers} is a prime number
79 is not a prime number
f{numbers} is a prime number
81 is not a prime number
f{numbers} is a prime number
83 is not a prime number
f{numbers} is a prime number
85 is not a prime number
f{numbers} is a prime number
87 is not a prime number
f{numbers} is a prime number
89 is not a prime number
f{numbers} is a prime number
91 is not a prime number
f{numbers} is a prime number
93 is not a prime number
f{numbers} is a prime number
95 is not a prime number
f{numbers} is a prime number
97 is not a prime number
f{numbers} is a prime number
99 is not a prime number
def prime_numbers():
    for numbers in range(1,100):
        if numbers % 2==0:
            print(f"{numbers} is a prime number")
        else:
            print(f"{numbers} is not a prime number")

            
prime_numbers()
1 is not a prime number
2 is a prime number
3 is not a prime number
4 is a prime number
5 is not a prime number
6 is a prime number
7 is not a prime number
8 is a prime number
9 is not a prime number
10 is a prime number
11 is not a prime number
12 is a prime number
13 is not a prime number
14 is a prime number
15 is not a prime number
16 is a prime number
17 is not a prime number
18 is a prime number
19 is not a prime number
20 is a prime number
21 is not a prime number
22 is a prime number
23 is not a prime number
24 is a prime number
25 is not a prime number
26 is a prime number
27 is not a prime number
28 is a prime number
29 is not a prime number
30 is a prime number
31 is not a prime number
32 is a prime number
33 is not a prime number
34 is a prime number
35 is not a prime number
36 is a prime number
37 is not a prime number
38 is a prime number
39 is not a prime number
40 is a prime number
41 is not a prime number
42 is a prime number
43 is not a prime number
44 is a prime number
45 is not a prime number
46 is a prime number
47 is not a prime number
48 is a prime number
49 is not a prime number
50 is a prime number
51 is not a prime number
52 is a prime number
53 is not a prime number
54 is a prime number
55 is not a prime number
56 is a prime number
57 is not a prime number
58 is a prime number
59 is not a prime number
60 is a prime number
61 is not a prime number
62 is a prime number
63 is not a prime number
64 is a prime number
65 is not a prime number
66 is a prime number
67 is not a prime number
68 is a prime number
69 is not a prime number
70 is a prime number
71 is not a prime number
72 is a prime number
73 is not a prime number
74 is a prime number
75 is not a prime number
76 is a prime number
77 is not a prime number
78 is a prime number
79 is not a prime number
80 is a prime number
81 is not a prime number
82 is a prime number
83 is not a prime number
84 is a prime number
85 is not a prime number
86 is a prime number
87 is not a prime number
88 is a prime number
89 is not a prime number
90 is a prime number
91 is not a prime number
92 is a prime number
93 is not a prime number
94 is a prime number
95 is not a prime number
96 is a prime number
97 is not a prime number
98 is a prime number
99 is not a prime number
def prime_numbers():
    for numbers in range(1,100):
        if numbers / 1==1 and numbers%numbers==1:
            print(f"{numbers} is a prime number")
        else:
            print(f"{numbers} is not a prime number")

            
prime_numbers()
1 is not a prime number
2 is not a prime number
3 is not a prime number
4 is not a prime number
5 is not a prime number
6 is not a prime number
7 is not a prime number
8 is not a prime number
9 is not a prime number
10 is not a prime number
11 is not a prime number
12 is not a prime number
13 is not a prime number
14 is not a prime number
15 is not a prime number
16 is not a prime number
17 is not a prime number
18 is not a prime number
19 is not a prime number
20 is not a prime number
21 is not a prime number
22 is not a prime number
23 is not a prime number
24 is not a prime number
25 is not a prime number
26 is not a prime number
27 is not a prime number
28 is not a prime number
29 is not a prime number
30 is not a prime number
31 is not a prime number
32 is not a prime number
33 is not a prime number
34 is not a prime number
35 is not a prime number
36 is not a prime number
37 is not a prime number
38 is not a prime number
39 is not a prime number
40 is not a prime number
41 is not a prime number
42 is not a prime number
43 is not a prime number
44 is not a prime number
45 is not a prime number
46 is not a prime number
47 is not a prime number
48 is not a prime number
49 is not a prime number
50 is not a prime number
51 is not a prime number
52 is not a prime number
53 is not a prime number
54 is not a prime number
55 is not a prime number
56 is not a prime number
57 is not a prime number
58 is not a prime number
59 is not a prime number
60 is not a prime number
61 is not a prime number
62 is not a prime number
63 is not a prime number
64 is not a prime number
65 is not a prime number
66 is not a prime number
67 is not a prime number
68 is not a prime number
69 is not a prime number
70 is not a prime number
71 is not a prime number
72 is not a prime number
73 is not a prime number
74 is not a prime number
75 is not a prime number
76 is not a prime number
77 is not a prime number
78 is not a prime number
79 is not a prime number
80 is not a prime number
81 is not a prime number
82 is not a prime number
83 is not a prime number
84 is not a prime number
85 is not a prime number
86 is not a prime number
87 is not a prime number
88 is not a prime number
89 is not a prime number
90 is not a prime number
91 is not a prime number
92 is not a prime number
93 is not a prime number
94 is not a prime number
95 is not a prime number
96 is not a prime number
97 is not a prime number
98 is not a prime number
99 is not a prime number
def prime_numbers():
    for numbers in range(1,100):
        if numbers % 2 == 0 or numbers % 3 == 0:
            print(f"{numbers} is a prime number")
        else:
            print(f"{numbers} is not a prime number")

            
primes_numbers()
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    primes_numbers()
NameError: name 'primes_numbers' is not defined. Did you mean: 'prime_numbers'?
prime_numbers()
1 is not a prime number
2 is a prime number
3 is a prime number
4 is a prime number
5 is not a prime number
6 is a prime number
7 is not a prime number
8 is a prime number
9 is a prime number
10 is a prime number
11 is not a prime number
12 is a prime number
13 is not a prime number
14 is a prime number
15 is a prime number
16 is a prime number
17 is not a prime number
18 is a prime number
19 is not a prime number
20 is a prime number
21 is a prime number
22 is a prime number
23 is not a prime number
24 is a prime number
25 is not a prime number
26 is a prime number
27 is a prime number
28 is a prime number
29 is not a prime number
30 is a prime number
31 is not a prime number
32 is a prime number
33 is a prime number
34 is a prime number
35 is not a prime number
36 is a prime number
37 is not a prime number
38 is a prime number
39 is a prime number
40 is a prime number
41 is not a prime number
42 is a prime number
43 is not a prime number
44 is a prime number
45 is a prime number
46 is a prime number
47 is not a prime number
48 is a prime number
49 is not a prime number
50 is a prime number
51 is a prime number
52 is a prime number
53 is not a prime number
54 is a prime number
55 is not a prime number
56 is a prime number
57 is a prime number
58 is a prime number
59 is not a prime number
60 is a prime number
61 is not a prime number
62 is a prime number
63 is a prime number
64 is a prime number
65 is not a prime number
66 is a prime number
67 is not a prime number
68 is a prime number
69 is a prime number
70 is a prime number
71 is not a prime number
72 is a prime number
73 is not a prime number
74 is a prime number
75 is a prime number
76 is a prime number
77 is not a prime number
78 is a prime number
79 is not a prime number
80 is a prime number
81 is a prime number
82 is a prime number
83 is not a prime number
84 is a prime number
85 is not a prime number
86 is a prime number
87 is a prime number
88 is a prime number
89 is not a prime number
90 is a prime number
91 is not a prime number
92 is a prime number
93 is a prime number
94 is a prime number
95 is not a prime number
96 is a prime number
97 is not a prime number
98 is a prime number
99 is a prime number
def prime_numbers():
    for numbers in range(1,100):
        if numbers % 2 == 0 or numbers % 3 == 0:
            print(f"{numbers} is not a prime number")
        else:
            print(f"{numbers} is a prime number")

            
prime_numbers()
1 is a prime number
2 is not a prime number
3 is not a prime number
4 is not a prime number
5 is a prime number
6 is not a prime number
7 is a prime number
8 is not a prime number
9 is not a prime number
10 is not a prime number
11 is a prime number
12 is not a prime number
13 is a prime number
14 is not a prime number
15 is not a prime number
16 is not a prime number
17 is a prime number
18 is not a prime number
19 is a prime number
20 is not a prime number
21 is not a prime number
22 is not a prime number
23 is a prime number
24 is not a prime number
25 is a prime number
26 is not a prime number
27 is not a prime number
28 is not a prime number
29 is a prime number
30 is not a prime number
31 is a prime number
32 is not a prime number
33 is not a prime number
34 is not a prime number
35 is a prime number
36 is not a prime number
37 is a prime number
38 is not a prime number
39 is not a prime number
40 is not a prime number
41 is a prime number
42 is not a prime number
43 is a prime number
44 is not a prime number
45 is not a prime number
46 is not a prime number
47 is a prime number
48 is not a prime number
49 is a prime number
50 is not a prime number
51 is not a prime number
52 is not a prime number
53 is a prime number
54 is not a prime number
55 is a prime number
56 is not a prime number
57 is not a prime number
58 is not a prime number
59 is a prime number
60 is not a prime number
61 is a prime number
62 is not a prime number
63 is not a prime number
64 is not a prime number
65 is a prime number
66 is not a prime number
67 is a prime number
68 is not a prime number
69 is not a prime number
70 is not a prime number
71 is a prime number
72 is not a prime number
73 is a prime number
74 is not a prime number
75 is not a prime number
76 is not a prime number
77 is a prime number
78 is not a prime number
79 is a prime number
80 is not a prime number
81 is not a prime number
82 is not a prime number
83 is a prime number
84 is not a prime number
85 is a prime number
86 is not a prime number
87 is not a prime number
88 is not a prime number
89 is a prime number
90 is not a prime number
91 is a prime number
92 is not a prime number
93 is not a prime number
94 is not a prime number
95 is a prime number
96 is not a prime number
97 is a prime number
98 is not a prime number
99 is not a prime number
