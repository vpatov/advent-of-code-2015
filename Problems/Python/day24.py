"""
--- Day 24: It Hangs in the Balance ---
 It's Christmas Eve, and Santa is loading up the sleigh for this year's deliveries.  However, there's one small problem: he can't get the sleigh to balance.  If it isn't balanced, he can't defy physics, and nobody gets presents this year. No pressure. Santa has provided you a list of the weights of every package he needs to fit on the sleigh.  The packages need to be split into three groups of exactly the same weight, and every package has to fit.  The first group goes in the passenger compartment of the sleigh, and the second and third go in containers on either side.  Only when all three groups weigh exactly the same amount will the sleigh be able to fly.  Defying physics has rules, you know! Of course, that's not the only problem.  The first group - the one going in the passenger compartment - needs as few packages as possible so that Santa has some legroom left over.  It doesn't matter how many packages are in either of the other two groups, so long as all of the groups weigh the same. Furthermore, Santa tells you, if there are multiple ways to arrange the packages such that the fewest possible are in the first group, you need to choose the way where the first group has the smallest quantum entanglement to reduce the chance of any "complications".  The quantum entanglement of a group of packages is the product of their weights, that is, the value you get when you multiply their weights together.  Only consider quantum entanglement if the first group has the fewest possible number of packages in it and all groups weigh the same amount. For example, suppose you have ten packages with weights 1 through 5 and 7 through 11.  For this situation, some of the unique first groups, their quantum entanglements, and a way to divide the remaining packages are as follows: Group 1;             Group 2; Group 3
11 9       (QE= 99); 10 8 2;  7 5 4 3 1
10 9 1     (QE= 90); 11 7 2;  8 5 4 3
10 8 2     (QE=160); 11 9;    7 5 4 3 1
10 7 3     (QE=210); 11 9;    8 5 4 2 1
10 5 4 1   (QE=200); 11 9;    8 7 3 2
10 5 3 2   (QE=300); 11 9;    8 7 4 1
10 4 3 2 1 (QE=240); 11 9;    8 7 5
9 8 3      (QE=216); 11 7 2;  10 5 4 1
9 7 4      (QE=252); 11 8 1;  10 5 3 2
9 5 4 2    (QE=360); 11 8 1;  10 7 3
8 7 5      (QE=280); 11 9;    10 4 3 2 1
8 5 4 3    (QE=480); 11 9;    10 7 2 1
7 5 4 3 1  (QE=420); 11 9;    10 8 2
 Of these, although 10 9 1 has the smallest quantum entanglement (90), the configuration with only two packages, 11 9, in the passenger compartment gives Santa the most legroom and wins.  In this situation, the quantum entanglement for the ideal configuration is therefore 99.  Had there been two configurations with only two packages in the first group, the one with the smaller quantum entanglement would be chosen. What is the quantum entanglement of the first group of packages in the ideal configuration?
"""

import time
start_time = time.time()

package_list = sorted([int(pkg) for pkg in open('../Input/day24.txt','r').read().split('\n')])
package_set = set(package_list)
tot_weight = sum(package_list)
target_weight = tot_weight / 4
print tot_weight, target_weight
g1,g2,g3 = [],[],[]

def qe(l):
    prod = 1
    for el in l:
        prod *= el
    return prod

all_combos = []
count_combos = 0
def try_combo(index,total,combo):
    global count_combos,all_combos
    total += package_list[index]
    combo.append(package_list[index])
    if total == target_weight:
        all_combos.append(combo)
        return True
    if total > target_weight:
        return False
    else:
        for i in range(index+1,len(package_list)):
            res = try_combo(i,total,list(combo))
            if not res:
                break
        return True
            

for i in range(0,len(package_list)):
    try_combo(i,0,[])

min_qe = float('inf')
min_combo = None
for combo in all_combos:
    qe_ = qe(combo)
    if qe_ < min_qe:
        min_qe = qe_
        min_combo = combo

f = open('saved_from_24_2.txt','w')
for combo in all_combos:
    f.write(str(combo) + '\n')

print 'part II'
print min_qe





total_time = time.time() - start_time
print "Program Execution Time:", total_time, "seconds."
