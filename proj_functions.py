def sum_two(m,n):
    sum=m+n
    return sum
def swap1(num1,num2):
    temp=num1+num2
    num1=temp-num1
    num2=temp-num1
    return num1,num2

def swap2(num1,num2):
    num1=num1+num2
    num2=num1-num2
    num1=num1-num2
    return num1,num2
# control statements

def odd_even(num):
    if num % 2==0:
        return (f'the {num} is even number')
    else:
        return (f'the {num} is odd number ')
    
def pos_or_neg(num):
    if num > 0:
        return(f'{num} is positive number')
    else:
        return(f'{num} is negative number')
    
def big_from_two(num1,num2):
    if num1 >=num2:
        return num1
    else:
        return num2
    
def big_from_three(num1,num2,num3):
    if num1>=num2 and num1 >=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

def check(num1):
    if num1==0:
        return "zero"
    elif num1 > 0:
        return "positive"
    else:
        return "negative"
    
def pr_1_to_10():
    for i in range(1,11):
        print(i)

def pr_100_to_1():
    for i in range(100,0,-1):
        print(i)



def even(limit):
    for i in range(0,limit+1):
        if i%2==0:
            print(i)

def odd(limit):
    for i in range(0,limit+1):
        if i%2!=0:
            print(i)

def sum_of_range(num1,num2):
    sum=0
    for i in range(num1,num2+1):
        sum+=i
    return sum

def sum_of_even(num1,num2):
    sum=0
    for i in range(num1,num2+1):
        if i%2==0:
            sum+=i
    return sum

def sum_of_even(num1,num2):
    sum=0
    for i in range(num1,num2+1):
        if i%2!=0:
            sum+=i
    return sum
def factorial(num1):
    fact=1
    for i in range(num1,0,-1):
        fact*=i
    return fact
def factors(x):
    factors=[]
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    
    return factors

def prime(num1):
    count=0
    for i in range(1,num1//2):
        if num1%i==0:
            count+=1
    if count >1:
        print("not prime")
    else:
        print("prime")

def fabonacci(num1):
    a=0
    b=1
    for i in range(0,num1+1,+1):
        if i==0:
            print(0)
        elif i==1:
            print(1)
        else:
            c=a+b
            a=b
            b=c
            print(c)

def sum_of_digit(num1):
    temp=num1
    sum=0
    while temp>=1:
        res=temp%10
        temp=temp//10
        sum=sum+res
    return sum

def count_of_digit(num1):
    temp=num1
    count=0
    while temp>=1:
        res=temp%10
        temp=temp//10
        count+=1
    return count

def reverse_of_number(num1):
    temp=num1
    rev_no=0
    while temp>=1:
        res=temp%10
        temp=temp//10
        rev_no=rev_no*10+res
    return rev_no

def check_for_pal(num1):
    temp=num1
    s=reverse_of_number(temp)
    if num1==s:
        return print("its pallindrome")
    else:
        return print("not pallindrome")
    
def amstrong(num1):
    temp=num1
    len=count_of_digit(temp)
    num2=0
    while temp>=1:
        rem=temp%10
        temp=temp//10
        num2=num2+rem**len
    
    if num1==num2:
        return "amstrong number"
    else:
        return "not amstrong number"
    

"""
25. print sum of given array
26. print smallest number from an array.
27. print reverse numbers of array elements.
28. generate the reverse array from given array.
29. find the count[occurance] of array elements.
30. sort array in ascending order

here array is list
"""
def sum_of_list(list1):
    sum =0
    for i in list1:
        sum+=i
    return sum

def smallest_no(list1):
    min=list1[0]
    for i in list1:
        if min > i:
            min,i=i,min
    return min
l=[10,20,30,40,50,60,-20,10,10,30]

def reverse_list(list1):
    list2=[]
    for i in range(len(list1)):
        list2.append(list1[-1-i])

    return list2

def count_element(list1):
    l=set(list1)
    dict={}
    for i in l:
        count=0

        for j in list1:
            if i==j:
                count+=1
        dict[i]=count
    return dict

# def sort_list_ascending(list2):
#     list1=list2

#     for i in range(len(list1)):
#         min=list1[0]

#         for j in range(len(list1)-i):
#             if min > list1[j]:
#                 min,list1[j]=list1[j],min

#     return list1

# print(sort_list_ascending(l))
"""
31. print Vowels from given String.
32. compare the both of String which is Max.
33. reverse the String
34. check given string is pallindrome or not.
35. check given both string are anagram String or not
"""

def find_vowels(s):
    for i in range(len(s)):
        if s[i] in ['a','e','i','o','u']:
            print(s[i])

def rev_string(s):
    return s[::-1]

#check given both string are anagram String or not
def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        print("its anagram")
    else:
        print("its not anagram")











