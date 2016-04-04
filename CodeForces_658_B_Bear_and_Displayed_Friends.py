from sys import stdin as Si
from operator import itemgetter as ig 
if __name__=='__main__':
    n,k,q = map(int,Si.readline().split())
    T = tuple(map(int,Si.readline().split()))
    stack = {}
    for i in range(q):
        a,b = map(int,Si.readline().split())
        #print(a,b,stack)
        if a==1:
            if len(stack)<k:    stack[b]=T[b-1]
            else:
                stack[b]=T[b-1]
                while len(stack)>k:
                    x,y = min(stack.items(),key=ig(1))
                    del stack[x]
                #stack[b] = T[b-1]
        elif a==2:
            if b in stack:  print('YES')
            else:   print('NO')
            
    
'''
B. Bear and Displayed Friends
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

Limak is a little polar bear. He loves connecting with other bears via social networks. He has n friends and his relation with the i-th of them is described by a unique integer ti. The bigger this value is, the better the friendship is. No two friends have the same value ti.

Spring is starting and the Winter sleep is over for bears. Limak has just woken up and logged in. All his friends still sleep and thus none of them is online. Some (maybe all) of them will appear online in the next hours, one at a time.

The system displays friends who are online. On the screen there is space to display at most k friends. If there are more than k friends online then the system displays only k best of them — those with biggest ti.

Your task is to handle queries of two types:

    "1 id" — Friend id becomes online. It's guaranteed that he wasn't online before.
    "2 id" — Check whether friend id is displayed by the system. Print "YES" or "NO" in a separate line. 

Are you able to help Limak and answer all queries of the second type?
Input

The first line contains three integers n, k and q (1 ≤ n, q ≤ 150 000, 1 ≤ k ≤ min(6, n)) — the number of friends, the maximum number of displayed online friends and the number of queries, respectively.

The second line contains n integers t1, t2, ..., tn (1 ≤ ti ≤ 109) where ti describes how good is Limak's relation with the i-th friend.

The i-th of the following q lines contains two integers typei and idi (1 ≤ typei ≤ 2, 1 ≤ idi ≤ n) — the i-th query. If typei = 1 then a friend idi becomes online. If typei = 2 then you should check whether a friend idi is displayed.

It's guaranteed that no two queries of the first type will have the same idi becuase one friend can't become online twice. Also, it's guaranteed that at least one query will be of the second type (typei = 2) so the output won't be empty.
Output

For each query of the second type print one line with the answer — "YES" (without quotes) if the given friend is displayed and "NO" (without quotes) otherwise.
Examples
Input

4 2 8
300 950 500 200
1 3
2 4
2 3
1 1
1 2
2 1
2 2
2 3

Output

NO
YES
NO
YES
YES

Input

6 3 9
50 20 51 17 99 24
1 3
1 4
1 5
1 2
2 4
2 2
1 1
2 4
2 3

Output

NO
YES
NO
YES

Note

In the first sample, Limak has 4 friends who all sleep initially. At first, the system displays nobody because nobody is online. There are the following 8 queries:

    "1 3" — Friend 3 becomes online.
    "2 4" — We should check if friend 4 is displayed. He isn't even online and thus we print "NO".
    "2 3" — We should check if friend 3 is displayed. Right now he is the only friend online and the system displays him. We should print "YES".
    "1 1" — Friend 1 becomes online. The system now displays both friend 1 and friend 3.
    "1 2" — Friend 2 becomes online. There are 3 friends online now but we were given k = 2 so only two friends can be displayed. Limak has worse relation with friend 1 than with other two online friends (t1 < t2, t3) so friend 1 won't be displayed
    "2 1" — Print "NO".
    "2 2" — Print "YES".
    "2 3" — Print "YES".
'''
        
        
