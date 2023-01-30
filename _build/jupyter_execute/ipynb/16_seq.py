#!/usr/bin/env python
# coding: utf-8

# ## seq コマンド
# - sequenceから名称がきている
# - 連続番号を出力する
# - 開始の数と間隔を指定することもできる
# - 逆順の指定も可能
# - 書式を指定して出力することもできる

# ---
# `seq number` 0からnumberまでの連続数字を出力する

# In[1]:


get_ipython().system('seq 10')


# ---
# `seq -w number` 0からnumberまでの連続数字を<font color=red>ゼロ埋めで</font>出力する

# In[2]:


get_ipython().system('seq -w 10')


# ---
# `seq start span end` 開始番号と差分、終了番号を指定することができる

# In[3]:


get_ipython().system('seq 1 2 3')


# In[4]:


get_ipython().system('seq 100 100 1000')


# In[5]:


get_ipython().system('seq 1 10')


# ---
# `seq -f number` 書式を指定できる
# - %e : 指数形式、大文字の時は%E
# - %f : 小数点形式
# - %g : 一般的な数字の形式

# In[6]:


get_ipython().system('seq -f "%.1e" 10')


# In[7]:


get_ipython().system('seq -f "%.1f" 10')


# In[8]:


get_ipython().system('seq -f "%04g" 10')


# In[9]:


get_ipython().system('seq -f "IMG_%04g.jpg" 10')


# In[ ]:




