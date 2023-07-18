def factors(num):
    cnt,i=0,1
    while i*i<=num:
        if num%i==0:
            if i==num//i:cnt+=1
            else:cnt+=2
        i+=1
    return cnt
def FactorsSort(Array):
    return sorted(Array,key=lambda x:(factors(x),x))
if __name__ == '__main__':
     array=list(map(int,input().split()))
     print(*FactorsSort(array))
"""
Factors Sort
You are given an array A of N elements. Sort the given array in increasing order of number of distinct 
factors of each element, i.e., element having the 
least number of factors should be the first to be displayed and
 the number having highest number of factors should be the last one. If 2 elements have same number of factors, then number with less value should come first.
Example Input

Input 1:
A = [6, 8, 9]
Input 2:
A = [2, 4, 7]


Example Output

Output 1:
[9, 6, 8]
Output 2:
[2, 7, 4]
"""