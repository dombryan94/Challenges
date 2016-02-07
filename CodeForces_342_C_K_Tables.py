if __name__=='__main__':
    n,k = map(int,input().split(' '))
    Sum = 0
    t,s =(),pow(n,2)
    for i in range(n):
        tmpt = ()
        for j in range(n-k+1):
            tmpt +=(s,)
            s -=1
        t += (tmpt,)
        Sum+=s
    print (Sum+n)
    #table
    s = 1
    for i in range(n):
        tn = ()
        for j in range(k-1):
            tn+=(s,)
            s+=1
        print (str(tn+t[i][::-1]).replace(',','').replace('(','').replace(')',''))
        
        
'''
C. K-special Tables
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

People do many crazy things to stand out in a crowd. Some of them dance, some learn by heart rules of Russian language, some try to become an outstanding competitive programmers, while others collect funny math objects.

Alis is among these collectors. Right now she wants to get one of k-special tables. In case you forget, the table n × n is called k-special if the following three conditions are satisfied:

    every integer from 1 to n2 appears in the table exactly once;
    in each row numbers are situated in increasing order;
    the sum of numbers in the k-th column is maximum possible. 

Your goal is to help Alice and find at least one k-special table of size n × n. Both rows and columns are numbered from 1 to n, with rows numbered from top to bottom and columns numbered from left to right.
Input

The first line of the input contains two integers n and k (1 ≤ n ≤ 500, 1 ≤ k ≤ n) — the size of the table Alice is looking for and the column that should have maximum possible sum.
Output

First print the sum of the integers in the k-th column of the required table.

Next n lines should contain the description of the table itself: first line should contains n elements of the first row, second line should contain n elements of the second row and so on.

If there are multiple suitable table, you are allowed to print any.
Sample test(s)
Input

4 1

Output

28
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Input

5 3

Output

85
5 6 17 18 19
9 10 23 24 25
7 8 20 21 22
3 4 14 15 16
1 2 11 12 13
'''
