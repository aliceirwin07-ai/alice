five_favorite_foods = ["wagyu","raspberry chocolate ice cream","eggs and rice","burrito","fish"]
print(five_favorite_foods[1])
print(five_favorite_foods[-1])
five_favorite_foods.append("chocolate")
five_favorite_foods.insert(0,"apple")
del five_favorite_foods[2]

for i in five_favorite_foods:
    print(i.upper())  #<built-in method upper of str object at 0x100956a70>, I forgot to use .upper(), fixed by adding ()

first_last_food = five_favorite_foods[:1] + five_favorite_foods[-1:]

if "potato" in five_favorite_foods:
    print("A potato!")
else:
    print("No potato!")

numbers = list(range(21))

def get_first_15(numbers):
    return numbers[0:15]

def get_every_5th(lst):
    return lst[0::5]

def reverse_and_stride(lst):
    lst.reverse()    #ran into TypeError: 'NoneType' object is not subscriptable, tried to set a variable = to lst.reverse() instead of just calling it
    return lst[0::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)
print(step1,step2,step3)

numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
print(numbers[2])
print(numbers[1][1])
numbers.append([10,11,12])

def sum_nested(numbers):
    total = 0
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            total+=numbers[i][j]
    return total
sum_nested(numbers)

def create_5x5():
    list5x5=[]
    for i in range(5):
        list5x5.append([])  #TypeError: list.append() takes exactly one argument (0 given), typo I was trying to append to list which didn't exist, fixed by fixing list to list5x5
        for j in range(5):
            list5x5[i].append(5*i+j+1)
    return list5x5

list5x5 = create_5x5()

def replace3s(list5x5):
    for i in range(5):
        for j in range(5):
            if list5x5[i][j]%3==0:
                list5x5[i][j]="?"
    return list5x5

list5x5no3 = replace3s(list5x5)

def sumlist5x5(listno3):
    total=0
    for i in range(5):
        for j in range(5):
            if listno3[i][j]!="?":
                total+=listno3[i][j]
    return total
sumlist = sumlist5x5(list5x5no3)

ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

print(ages["Katie"])
ages["Mira"]=100
ages["Milana"]=52
ages.pop("Mariam")
for i in ages:
    print(i,ages[i])

print("calling create5x5()",create_5x5())