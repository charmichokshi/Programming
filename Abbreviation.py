def abbreviation(a, b):

    j=0
    c=0
    s=""
    temp=""
    for i in range(len(b)):
        if(j>=len(a)):
            break
        
        if(len(b)-i > len(a)-j):
            return "NO"
        
        if(b[i] != a[j]):
            k=1
            
            while(j < len(a) and b[i] != a[j] and k != 0):
                if(b[i] == a[j].upper()):
                    c+=1 
                    s+=a[j].upper()
                    temp+=a[j].upper()
                    j+=1
                    k=0
                else:
                    temp+=a[j]
                    print(temp)
                    j+=1
                    if(j<len(a) and b[i] == a[j]):
                        c+=1 
                        s+=a[j].upper()
                        temp+=a[j].upper()
                        j+=1
                        k=0
                        
                        break
        
        else:
            c+=1   
            s+=a[j]
            temp+=a[j]
            j+=1
    
    if(len(b) < len(a)):
        for i in range(j,len(a)):
            temp+=a[j]
            j+=1
    
    out = ""
    for c in temp:
        if c in temp and not c in s:
            out += c
    print(out)

    for i in range(len(out)):
        if(out[i].isupper()):
            return "NO"
        
    if(len(s) == len(b)):
        return "YES"
    else:
        return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        a = input()
        b = input()
        result = abbreviation(a, b)
        fptr.write(result + '\n')
    fptr.close()
