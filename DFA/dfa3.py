from models import DFA

#DFA accepts every string of {a, b} with the length at most 2
if __name__ == '__main__':
    obj = DFA(Q={'A', 'B', 'C', 'D'}, Sigma={'a', 'b'}, delta={
        ('A', 'a'): 'B', ('A', 'b'): 'B',
        ('B', 'a'): 'C', ('B', 'b'): 'C',
        ('C', 'a'): 'D', ('C', 'b'): 'D',
        ('D', 'a'): 'D', ('D', 'b'): 'D'
        }, q0='A', F={'A', 'B', 'C'})

    L = ["ba", "ppap", "aabaaaa", "b", ""]
    for strings in L:
        print(obj.run(strings))