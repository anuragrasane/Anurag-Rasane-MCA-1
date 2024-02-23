

str1 = 'PythonForPython'
# lambda returns a function object
rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str1))
#Output: NOHTYPROFNOHTYP
#Condition Checking Using Python lambda function
format_numeric = lambda
num: f"{num:e}"
if isinstance(num, int)
else f"{num:,.2f}"
print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))
#Output: Int formatting: 1.000000e+06
float formatting: 999,999.79

# using the lambda function
print("Using lambda function, cube:", lambda_cube(5))
