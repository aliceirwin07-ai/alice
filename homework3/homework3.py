def say_goodbye(name):
    print("Hello,", name)

def areacircle(radius):
    area = 3.14*(radius**2)
    print(area)

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def whattowear(list):
    return (min(list),max(list))

def is_weekend(day):
    if day<=5:
        return "weekday :("
    elif day>=6:
        return "weekend :)"

def fuel_efficiency(distance,fuelused):
    fueleff = distance/fuelused
    return fueleff
    
def secret_code(code):
    encrypted_code = 0
    numdigits=len(str(code))
    for i in range(numdigits):
        digit = code%10 #take the last digit
        encrypted_code+=digit*(10**(numdigits-1-i)) #add last digit times 10^(n) so it becomes the first digit
        code//=10   #take away the last digit
    return encrypted_code

def power(x,y):
    xpowy=1
    for i in range(y):  #run loop y times
        xpowy*=x    #multiply xpowy by x y times
    return xpowy

def minimumfor(values):
    currentmin=values[0]    #set current min to the first element of the array
    for v in values:    #loop through array
        if v<currentmin:    #check if the current element is smaller than the current minimum
            currentmin=v    #replace it
    return currentmin   #return the current minimum after the loop is done

def maximumfor(values):
    currentmax=values[0]    #set current max to the first element of the array
    for v in values:    #loop through array
        if v>currentmax:    #check if the current element is bigger than the current minimum
            currentmax=v    #replace it
    return currentmax   #return the current max after the loop is done

def minimumwhile(values):
    currentmin=values[0]    #set current max to the first element of the array
    v=0     #start v at 0
    while v < len(values):  #while v is smaller than the len of array
        if values[v]<currentmin:    #check if the current element is bigger than the current minimum
            currentmin=values[v]    #replace it
        v+=1    #add 1 to v to move onto the next element
    return currentmin   #return min

def maximumwhile(values):
    currentmax=values[0]    #set current max to the first element of the array
    v=0     #start v at 0
    while v < len(values):  #while v is smaller than the len of array
        if values[v]>currentmax:    #check if the current element is bigger than the current minimum
            currentmax=values[v]    #replace it
        v+=1#add 1 to v to move onto the next element
    return currentmax   #return min

def digitsum(num):
    digsum=0    #set sum to 0
    numdigits=len(str(num)) #set number to loop through
    for i in range(numdigits):  #loop through
        digsum+=num%10  #add the last digit
        num//=10    #take away the last digit
    return digsum

x = 678
result = digitsum(x) # 2 raised to the power of 3
print(f"The result of digitsum(6.3) with x = {x} is {result}.")