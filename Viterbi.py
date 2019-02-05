import sys
obs=sys.argv[1]
states=['H','F']
a={
    'Start':{'H': 0.6,'F': 0.4},
    'H':{'H':0.7,'F':0.3},
    'F':{'H': 0.5,'F':0.5}
}

b={
    'H':{'N':0.1, 'C':0.4, 'D':0.5},
    'F':{'N':0.6, 'C': 0.3, 'D': 0.1}
}

#initializing data structures for algorithm
viterbi={'H':[], 'F':[]}
backpointer={'H':[],'F':[]}

def getStateSequence(obs):
    #Filling the first column of the path probability matrix viterbi
    for state in states:
        temp=[]
        #print('The state is:', state)
        temp.append((a['Start'][state]*b[state][obs[0]]))
        viterbi[state]=temp

    #recursive step
    for t in range(1,len(obs)):
        for s in states:
            arrows={}
            for s_prime in states:
                arrows[s_prime]=viterbi[s_prime][t-1]*a[s_prime][s]*b[s][obs[t]]

            max_prob=-sys.maxsize-1
            for key in arrows:
                if(arrows[key]>max_prob):
                    max_prob=arrows[key]
                    max_state=key
            viterbi[s].append(max_prob)
            backpointer[s].append(max_state)
    #print(viterbi)
    #print(backpointer)

    best_path = []
    last=len(obs)-1
    max_value = -sys.maxsize - 1
    max_state=None

    for key in viterbi:
        if (viterbi[key][last] > max_value):
            max_value = viterbi[key][last]
            max_state = key
    best_path.append(max_state)

    count=0
    for index in range(len(obs)-2,-1,-1):
        state=backpointer[best_path[count]][index]
        best_path.append(state)
        count+=1

    return best_path


'''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''

print("\ninput:")
print(obs)
result=getStateSequence(obs)
print("\noutput:")
for i in range(len(result)-1,-1,-1):
    print(result[i],end='')
print('')