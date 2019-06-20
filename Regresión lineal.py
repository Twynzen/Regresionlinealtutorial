#!/usr/bin/env python
# coding: utf-8

# In[1]:


import  numpy as np #Calculo nùmerico, funcionalidades con arrays, matrices operaciones de convertir matriz transpuesta etc...
import scipy as sc  #Lo mismo que numpy pero agrega màs funcionalidades de tratamiento de imagenes y datos


import matplotlib.pyplot as plt # libreria de visualizacion grafica


# In[2]:


print("probando")


# In[3]:


from sklearn.datasets import load_boston


# In[5]:


#cargamos la libreria
boston = load_boston()

boston.


# In[6]:


print(boston.DESCR)


# In[16]:


x = np.array(boston.data[:, 5])
y = np.array(boston.target)

plt.scatter(x, y)

plt.show()

