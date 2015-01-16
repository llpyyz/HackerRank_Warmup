"""
David Schonberger
Hackerrank.com
Warmpup - Topics known by 2-person teams
1/4/2015
"""
import itertools
def process_input(combs):
    curr_max = 0
    team_count = 0
    for comb in combs:
        z = zip(comb[0], comb[1])
        shared_task_sum = len([elt for elt in z if elt[0] == '1' or elt[1] == '1'])
        if(shared_task_sum == curr_max):
            team_count += 1
        elif(shared_task_sum > curr_max):
            curr_max = shared_task_sum
            team_count = 1
    print curr_max
    print team_count
    
s = raw_input()
s = s.split(' ')
N = int(s[0])
M = int(s[1])
ppl = []
for i in range(N):
    ppl.append(raw_input())
    
combs = list(itertools.combinations(ppl,2))
process_input(combs)

#bef = datetime.datetime.now()
#strlen = 500
#strs = []
#numstrs = 500
#for i in range(numstrs):
#    s = ""
#    for j in range(strlen):
#        s += str(random.randint(0,1))
#    strs.append(s)
#
#combs = list(itertools.combinations(strs,2))
#process_input(combs)
#aft = datetime.datetime.now()
#print "et:", aft - bef

##print combs

#
#bef = datetime.datetime.now()
#
#make_task_dict(combs, strlen)
#
#aft = datetime.datetime.now()
#print "et to make dict:", aft - bef, "\n\n"

#print "ord('0')", ord('0')
#print "ord('1')", ord('1')
#print zip('123','456')

#max_tasks = max([k for k in d.keys()])
#print max_tasks 
#print d[max_tasks]
#aft = datetime.datetime.now()
#print "et to solve rest:", aft - bef


#import itertools
#
#def make_task_dict(combs,m):
#    curr_max = 0
#    team_count = 0
#    for comb in combs:
#        z = zip(comb[0], comb[1])
#        shared_task_sum = m - sum([ord(elt[0]) | ord(elt[1]) == 48 for elt in z])
#        if(shared_task_sum == curr_max):
#            team_count += 1
#        elif(shared_task_sum > curr_max):
#            curr_max = shared_task_sum
#            team_count = 1
#    print curr_max
#    print team_count
#    
#s = raw_input()
#s = s.split(' ')
#N = int(s[0])
#M = int(s[1])
#ppl = []
#for i in range(N):
#    ppl.append(raw_input())
#
#combs = list(itertools.combinations(ppl,2))
#make_task_dict(combs, M)