from models import DFA

#DFA accepts every string of {0, 1} ends with string "101"
if __name__ == '__main__':
    obj = DFA(Q={'q0', 'q1', 'q2', 'q3'}, Sigma={0, 1}, delta={
        ('q0', 0): 'q0', ('q0', 1): 'q1',
        ('q1', 0): 'q2', ('q1', 1): 'q1',
        ('q2', 0): 'q0', ('q2', 1): 'q3',
        ('q3', 0): 'q0', ('q3', 1): 'q1'
        }, q0='q0', F={'q3'})

    L = ["101", "1101", "0010100101", "101001011", "001010010"]
    
    for strings in L:
        print(obj.run(strings))