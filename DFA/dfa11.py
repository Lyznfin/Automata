from models import DFA

#DFA accepts every string of {a, b} with an odd number of 'a' and an even numbers of 'b'
    #perhaps one should remember, empty string of 'b' is an even number.
if __name__ == '__main__':
    obj = DFA(Q={'A', 'B', 'C', 'D'}, Sigma={'a', 'b'}, delta={
        ('A', 'a'): 'B', ('A', 'b'): 'D',
        ('B', 'a'): 'A', ('B', 'b'): 'C',
        ('C', 'a'): 'D', ('C', 'b'): 'B',
        ('D', 'a'): 'C', ('D', 'b'): 'A'
        }, q0='A', F={'B'})

    L = [
            "bba", "abb", "bab", "bbbbbba", "bbabaab", "abbbb", "aaabb", "bbaabab", "baaabbb", "bababab", "bbbabbbaa",
            "aabaaab", "aaabaab", "abaabaaabaaaaba"
        ]
    
    for strings in L:
        print(obj.run(strings))