from models import DFA

#DFA accepts every string of {a, b} that starts with "abb"
if __name__ == '__main__':
    obj = DFA(Q={'A', 'B', 'C', 'D', 'E'}, Sigma={'a', 'b'}, delta={
        ('A', 'a'): 'B', ('A', 'b'): 'E',
        ('B', 'a'): 'E', ('B', 'b'): 'C',
        ('C', 'a'): 'E', ('C', 'b'): 'D',
        ('D', 'a'): 'D', ('D', 'b'): 'D',
        ('E', 'a'): 'E', ('E', 'b'): 'E'
        }, q0='A', F={'D'})

    L = ["ababa", "abbaaaaaaaaa", "abb", "bbb"]
    for strings in L:
        print(obj.run(strings))