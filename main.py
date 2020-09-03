# Jack Scallan jgs5472@psu.edu
#Jeffery Shi jjs7487@psu.edu
#Ishan Behoorna 
#Alessandro Preito Brostamante asp5586@psu.edu

#Enter value
number = input("Enter temperature: ")
number = float(number)

#Enter unit 
unit = input("Enter unit in F/f or C/c: ")

#Calculations 
fahrenheit = ((9/5) *number)+32
celsius = (number -32)* (5/9)

#Celsius to fahrenheit
if unit == "C" or unit == "c":
  {
    print(f"{number}° in Celsius is equivalent to {fahrenheit}° Fahrenheit.")
  }

#Celsius to Fahrenheit 
elif unit == "F" or unit == "f":
  {
    print(f"{number}° in Fahrenheit is equivalent to {celsius}° Celsius.")
  }

#Error 
else:
  {
    print(f"Invalid unit({unit}).")
  }