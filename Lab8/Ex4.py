# Create an algorithm to calculate the greatest common divisor (GCD)

# Name: Ava Puaatuua
# Date: Oct. 14, 2026


def GCD(num1,num2):
    for count in range(min(num1,num2),1,-1):
        if num1 % count == 0 and num2 % count == 0:
            return count
    
    return GCD_number

GCD_number = GCD(48, 18)
print("The GCD of 48 and 18 is:", GCD_number)


def Euclid(a,b):
    while b != 0:
        a,b = b, a%b
    return a
