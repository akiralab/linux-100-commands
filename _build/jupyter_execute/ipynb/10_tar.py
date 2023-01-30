#!/usr/bin/env python
# coding: utf-8

# ## tar コマンド
# - tape archiveから名称がきている
# - 複数ファイルを一つにまとめたアーカイブファイルを作成/展開するコマンド

# ---
# `tar -c  FILENAME.tar FILENAME` ： *FILENAME*を圧縮する(-cはcreateの意)

# In[1]:


get_ipython().system('tar -cf src/test.tar src/test.txt')
get_ipython().system('ls -la src/')


# ---
# `tar -x  FILENAME.tar FILENAME` ： *FILENAME*を解凍する(-xはextractの意)

# In[2]:


get_ipython().system('tar -x src/test.tar')
get_ipython().system('ls -la src/')


# ---
# `commands -options` *FILENAME*： *FILENAME*にxxxする

# In[5]:


get_ipython().system('xx -l')

# 

L
# In[ ]:





# In[ ]:





# In[ ]:




