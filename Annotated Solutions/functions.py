import math

def check_prime(n):
    if n==2:
        return True
    elif n==1:
        return False
    else:
        for i in range(2,math.ceil(math.sqrt(n+1))):
            if n%i==0:
                return False
        return True

def lower_factors_of_n(n):
    factor_list = []
    for i in range(2,math.ceil(math.sqrt(n))):
        if n%i==0:
            factor_list+=[i]
    return factor_list

def prime_factors_of_n(n):
    prime_factors=[]
    list1 = lower_factors_of_n(n)
    for element in list1:
        if check_prime(element)==True:
            prime_factors+=[element]
    return(prime_factors)

def ispalindrome(input1):
    alpha=str(input1)
    i=0
    while i<(len(alpha)/2):
        if alpha[i]!=alpha[len(alpha)-(i+1)]:
            return False
        else:
            i+=1
    return True

def proper_divisors(i):
    if i==1:
        return [1]
    factor_list=[1]
    if int(math.sqrt(i))**2==i:
        factor_list+=[int(math.sqrt(i))]
    for x in range(2,int(math.sqrt(i)+1)):
        if i%x==0:
            factor_list+=[x]
            factor_list+=[int(i/x)]
    factor_list = list(set(factor_list))
    return sorted(factor_list)

def prime_factorization(n):
    factor_list = []
    while check_prime(n)==False:
        for i in range(2,math.ceil(math.sqrt(n+1))):
            if n%i==0:
                factor_list+=[i]
                n = int(n/i)
                break
    factor_list+=[n]
    return(factor_list)

def divisor_count(input1):
    output=0
    if int(math.sqrt(input1))**2==input1:
        output+=1
    i=1
    while i<math.sqrt(input1):
        if input1%i==0:
            output+=2
        i+=1
    return output

def generate_triangle_number(input1):
    i=1
    output = 0
    while i<=input1:
        output+=i
        i+=1
    return output