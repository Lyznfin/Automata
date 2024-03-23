from models import DFA

#DFA accepts every string of {a, b} with an odd number of 'a' and an even numbers of 'b' with minimum length of 3
    #meaning, just 'a' is not gonna cut it. Please send help, Im confused
if __name__ == '__main__':
    obj = DFA(Q={'A', 'B', 'C', 'D', 'E', 'F', 'G'}, Sigma={'a', 'b'}, delta={
        ('A', 'a'): 'B', ('A', 'b'): 'E',
        ('B', 'a'): 'A', ('B', 'b'): 'C',
        ('C', 'a'): 'E', ('C', 'b'): 'D',
        ('D', 'a'): 'G', ('D', 'b'): 'C',
        ('E', 'a'): 'C', ('E', 'b'): 'F',
        ('F', 'a'): 'D', ('F', 'b'): 'E',
        ('G', 'a'): 'D', ('G', 'b'): 'D'
        }, q0='A', F={'D', 'G'})

    L = [
            "bba", "abb", "bab", "bbbbbba", "bbabaab", "abbbb", "aaabb", "bbaabab", "baaabbb", "bababab", "bbbabbbaa",
            "aabaaab", "aaabaab", "abaabaaabaaaaba"
        ]
    
    for strings in L:
        print(obj.run(strings))