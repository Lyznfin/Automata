from models import DFA

#DFA accepts every string of {a, b} that ends with "abb"
if __name__ == '__main__':
    obj = DFA(Q={'A', 'B', 'C', 'D'}, Sigma={'a', 'b'}, delta={
        ('A', 'a'): 'B', ('A', 'b'): 'A',
        ('B', 'a'): 'B', ('B', 'b'): 'C',
        ('C', 'a'): 'B', ('C', 'b'): 'D',
        ('D', 'a'): 'B', ('D', 'b'): 'A'
        }, q0='A', F={'D'})

    L = ["bb", "bbaabb", "abb", "aaabba"]
    for strings in L:
        print(obj.run(strings))