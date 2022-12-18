# Quantum-Simulator

To simulate a file, provide the file path  in the variable 'file' and the initial state in the variable 'init_state', for which the simulation is to be performed and just call the quantum_simulator function.

Number of qubits can be changed in the variable 'num_qubits' which for now is set to 16.

Input: 
      file - path of the file containing the QASM code 
      init_state - an array containing the amplitudes for the 2^(num_qubits) states (Examples have been shown in 
                  .ipynb notebook on how to create the state)
                   
Output:
       The output state after simulation in bra-ket notation
       
The output contains the state in Dirac notation after simulation with its amplitude rounded off to 3 decimal places. 
       
