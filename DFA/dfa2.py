from models import DFA

#DFA accepts every string of {a, b} with the length at least 2
if __name__ == '__main__':
    obj = DFA(Q={'A', 'B', 'C'}, Sigma={'a', 'b'}, delta={
        ('A', 'a'): 'B', ('A', 'b'): 'B',
        ('B', 'a'): 'C', ('B', 'b'): 'C',
        ('C', 'a'): 'C', ('C', 'b'): 'C'
        }, q0='A', F={'C'})

    L = ["abaaaa", "ba", "ppap", "aab", "b"]
    for strings in L:
        print(obj.run(strings))