from sys import stdin as Si
from collections import defaultdict as dt
from operator import itemgetter as ig 
if __name__=='__main__':
    n,m = map(int,Si.readline().split())
    h = dt(dict)

    for i in range(n):
        s,r,p = map(str,Si.readline().split())
        r,p = map(int,(r,p))
        if p in h[r]:   h[r][p]+=[s]
        else:   h[r][p]=[s]
    for da in h:
        d = sorted(h[da].items(),key=ig(0),reverse=True)
        #print(d)
        ns,i = [],0
        while len(ns)<2:
            if len(d[i][1])+len(ns)>=3:
                ns='?'
                break
            else:
                ns+= d[i][1][:2-len(ns)]
            i+=1
            if i>=len(d):   break
        print(' '.join(ns))
'''
Very soon Berland will hold a School Team Programming Olympiad. From each of the m Berland regions a team of two people is invited to participate in the olympiad. The qualifying contest to form teams was held and it was attended by n Berland students. There were at least two schoolboys participating from each of the m regions of Berland. The result of each of the participants of the qualifying competition is an integer score from 0 to 800 inclusive.

The team of each region is formed from two such members of the qualifying competition of the region, that none of them can be replaced by a schoolboy of the same region, not included in the team and who received a greater number of points. There may be a situation where a team of some region can not be formed uniquely, that is, there is more than one school team that meets the properties described above. In this case, the region needs to undertake an additional contest. The two teams in the region are considered to be different if there is at least one schoolboy who is included in one team and is not included in the other team. It is guaranteed that for each region at least two its representatives participated in the qualifying contest.

Your task is, given the results of the qualifying competition, to identify the team from each region, or to announce that in this region its formation requires additional contests.
Input

The first line of the input contains two integers n and m (2 ≤ n ≤ 100 000, 1 ≤ m ≤ 10 000, n ≥ 2m) — the number of participants of the qualifying contest and the number of regions in Berland.

Next n lines contain the description of the participants of the qualifying contest in the following format: Surname (a string of length from 1 to 10 characters and consisting of large and small English letters), region number (integer from 1 to m) and the number of points scored by the participant (integer from 0 to 800, inclusive).

It is guaranteed that all surnames of all the participants are distinct and at least two people participated from each of the m regions. The surnames that only differ in letter cases, should be considered distinct.
Output

Print m lines. On the i-th line print the team of the i-th region — the surnames of the two team members in an arbitrary order, or a single character "?" (without the quotes) if you need to spend further qualifying contests in the region.
Examples
Input

5 2
Ivanov 1 763
Andreev 2 800
Petrov 1 595
Sidorov 1 790
Semenov 2 503

Output

Sidorov Ivanov
Andreev Semenov

Input

5 2
Ivanov 1 800
Andreev 2 763
Petrov 1 800
Sidorov 1 800
Semenov 2 503

Output

?
Andreev Semenov

Note

In the first sample region teams are uniquely determined.

In the second sample the team from region 2 is uniquely determined and the team from region 1 can have three teams: "Petrov"-"Sidorov", "Ivanov"-"Sidorov", "Ivanov" -"Petrov", so it is impossible to determine a team uniquely.
'''
            
        