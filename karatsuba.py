#2/7/2021 Javier Maldonado Rivera
#Karatsuba Multiplication Implementation

#Assuming equal lenght
def karatsuba(a, b):
    #verify if numbers given are double digit or more
    if((a > 10  and b > 10)):

        #implementation said function must be karatsuba(a,b) so we define r to be r = 10
        r = 10

        #get each first half of each number
        firstA = int(firstHalf(a,len(str(a))))
        secondA = int(secondHalf(a,len(str(a))))

        firstB = int(firstHalf(b,len(str(b))))
        secondB = int(secondHalf(b,len(str(b))))


        #find the exponential quantity
        expon = max(len(str(a)), len(str(a)))/2
        expon = int(expon)

        #start the multiplication process in parts
        delta = firstA * firstB
        alpha = secondA * secondB
        omega = (firstA + secondA) * (firstB + secondB) - delta - alpha
        karatAnswer = int(delta * r **(expon*2)+ omega * r**(expon) + alpha)

        #return answer found
        return karatAnswer
    else:
        return a * b

def firstHalf(a,l):
    split = str(a)
    final = ""
    z = 0
    for i in (split):
        if( z == l/2):
            return final
        final = final+split[z]
        z = z + 1

def secondHalf(a,l):
    split = str(a)
    final = ""
    z = 0
    for i in split:
        if (z == l / 2):
            return final
        final = final + split[int((l/2)+z)]
        z = z+1
    return int()
