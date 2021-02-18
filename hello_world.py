print('hello world')

a = 3+4
b = 3-4
c = 3%4
d = 3/4

print(a,b,c,d)

#f-strings
print(f"value of a is: {a}")

# equivalent cpp code
# cout<<"value of a is:"<<a<<endl;
# relational: <,>,<=,>=

print(a**2)
# cout<< pow(a,2)<<endl;

#logical and, or, not
#cpp comments // py me #
a=17
b=15
c=16

maximum = -1
#py me indentation is strictly required
if a > b and a > c:
    maximum = a
else:
    maximum = b
print(maximum)

"""
if (a>b && a>c){
    maximum=a;
}
"""
#loops
counter = 0
while counter < 10:
    print(counter)
    counter += 1
