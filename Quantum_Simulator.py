# Quantum Simulator

# Importing libraries
import numpy as np

# Print the solution
def solution(res_state):
    sol = ''
    for iz in range(len(res_state)):
        if res_state[iz]!=0:
            sol += str(res_state[iz])+'|'+bin(iz)[2:].zfill(16)+'> + '

    k = len(sol)
    sol = sol[:k-2]
    print(sol)


# T gate
def T_gate(init_state, n):
    res_state = [0]*(2**16)
    for iz in range(len(init_state)):
        if init_state[iz] !=0:
            a = bin(iz)[2:].zfill(16)
            if a[n]=='1':
                res_state[iz] = np.exp(1.0j*np.pi/4)*init_state[iz]
            else:
                res_state[iz] = init_state[iz]
    
    print('After applying T gate on q[',n,']')
    solution(res_state=res_state)
    return res_state

# T dagger gate
def Tdg_gate(init_state, n):
    res_state = [0]*(2**16)
    for iz in range(len(init_state)):
        if init_state[iz] !=0:
            a = bin(iz)[2:].zfill(16)
            if a[n]=='1':
                res_state[iz] = np.exp(-1.0j*np.pi/4)*init_state[iz]
            else:
                res_state[iz] = init_state[iz]
    
    print('After applying Tdg gate on q[',n,']')
    solution(res_state=res_state)
    return res_state

# Hadamard Gate
def H_gate(init_state, n):
    res_state = [0]*(2**16)
    for iz in range(len(init_state)):
        if init_state[iz] !=0:
            a = bin(iz)[2:].zfill(16)
            
            if a[n] == '1':
                p1 = -1/np.sqrt(2)
                b = a[:n] + '0' + a[n+1:]

            else: 
                p1 = 1/np.sqrt(2)
                b = a[:n] + '1' + a[n+1:]
            
            p2 = 1/np.sqrt(2)
            res_state[iz] += p1*init_state[iz]
            b_int = int(b, 2)
            res_state[b_int] += p2*init_state[iz]

    print('After applying H gate on q[',n,']')
    solution(res_state=res_state)
    return res_state

# X gate            
def X_gate(init_state, n):
    res_state = [0]*(2**16)
    for iz in range(len(init_state)):
        if init_state[iz] !=0:
            a = bin(iz)[2:].zfill(16)

            if a[n] == '0':
                b = a[:n] + '1' + a[n+1:]
            else:
                b = a[:n] + '0' + a[n+1:]
        
            b_int = int(b, 2)
            res_state[b_int] = init_state[iz]
    
    print('After applying X gate on q[',n,']')
    solution(res_state=res_state)
    return res_state

# CNOT gate
def CX_gate(init_state, control, target):
    res_state = [0]*(2**16)
    for iz in range(len(init_state)):
        if init_state[iz] != 0:
            a = bin(iz)[2:].zfill(16)

            if a[control] == '1':
                if a[target] == '0':
                    b = a[:target] + '1' + a[target+1:]
                else:
                    b = a[:target] + '0' + a[target+1:]
        
                b_int = int(b, 2)
                res_state[b_int] = init_state[iz]
            
            else:
                res_state[iz] = init_state[iz]              
    
    print('After applying CX gate on q[',control,'], q[',target,']')
    solution(res_state=res_state)
    return res_state

# Quantum simulator

def quantum_simulator(file, init_state):

    initial_state = init_state

    file1 = open(file, 'r')
    lines = file1.readlines()

    for line in lines:
        l1 = line.strip()
        op, q_n = l1.split(' ')
        
        if op == 'h' or op=='t' or op=='tdg' or op=='x':
        
            if len(q_n) == 5:
                n = int(q_n[2])
            else:
                n = int(q_n[2:4])
            #print(op, n)
    
        if op == 'cx':
            m=0
            q_n1, q_m1 = q_n.split(',')
            
            if len(q_n1) == 4:
                n = int(q_n1[2])
            else:
                n = int(q_n1[2:4])
            
            if len(q_m1) == 5:
                m = int(q_m1[2])
            else:
                m = int(q_m1[2:4])
            #print(op, n,m)

        
        if op == 'cx':
            initial_state = CX_gate(initial_state, n, m)
        elif op == 'x':
            initial_state = X_gate(initial_state, n)
        elif op == 'h':
            initial_state = H_gate(initial_state, n)
        elif op == 't':
            initial_state = T_gate(initial_state, n)
        elif op == 'tdg':
            initial_state = Tdg_gate(initial_state, n)


# Simulating miller_11.qasm

init_state1 = [0]*(2**16)
init_state1[0] = 1
file1 = '/Users/payalkaushik/Downloads/con1_216.qasm'
quantum_simulator(file = file1, init_state = init_state1)


