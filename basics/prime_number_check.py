

def prime_check(user_input):
    #A prime number is greater than 1 and divisible only by 1 and itself
    if user_input <= 1:
        return False
    #check if the number is divisible from range 2 to square root of that number +1.if so its not prime
    for number in range(2,int(user_input**0.5)+1):
        if user_input%number == 0:
            return False
    # if nothing return false then number is prime , return true
    return True

user_input = int(input("Enter the number"))
result = prime_check(user_input)
if result :
    print(f"The number {user_input} is prime")
else :
    print(f" the number {user_input} is not prime")
