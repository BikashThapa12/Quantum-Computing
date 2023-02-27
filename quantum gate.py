#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import *


# In[2]:


from qiskit.tools.visualization import plot_bloch_multivector 


# In[6]:


circuit = QuantumCircuit(1, 1)
circuit.x(0)

simulator = Aer.get_backend('statevector_simulator')

result = execute(circuit, backend = simulator).result()

statevector = result.get_statevector()

get_ipython().run_line_magic('matplotlib', 'inline')

print(statevector)

circuit.draw(output = 'mpl')


# In[7]:


plot_bloch_multivector(statevector)


# In[8]:


circuit.measure([0], [0])
backend = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = backend, shots = 1024).result()

counts = result.get_counts()

from qiskit.tools.visualization import plot_histogram
plot_histogram(counts)


# In[ ]:




