#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import *
import matplotlib as plt 


# In[2]:


qr = QuantumRegister(2)


# In[3]:


cr = ClassicalRegister(2)


# In[4]:


circuit = QuantumCircuit(qr, cr)


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


circuit.draw()


# In[7]:


#Creating hadamard gate

circuit.h(qr[0])


# In[8]:


circuit.draw(output='mpl')


# In[11]:


circuit.cx(qr[0], qr[1])


# In[12]:


circuit.draw(output='mpl')


# In[13]:


#Using these Qbits we can generate Entanglement
#Now we're going to measure and those measurement into the classical bits


circuit.measure(qr, cr)


# In[14]:


circuit.draw(output='mpl')


# In[15]:


#We're going to first run this circiut on classical computer, see what happened 

simulator = Aer.get_backend('qasm_simulator')


# In[17]:


execute(circuit, backend = simulator)


# In[22]:


#Now we executed our circuit what are the results came out of the circuit?

result = execute(circuit, backend = simulator).result()


# In[23]:


from qiskit.tools.visualization import plot_histogram


# In[24]:


plot_histogram(result.get_counts(circuit))


# In[25]:


IBMQ.load_account()


# In[26]:


provider = IBMQ.get_provider('ibm-q')


# In[29]:





# In[ ]:




