#!/usr/bin/env python
# coding: utf-8

# ## du コマンド
# - {名称の由来}から名称がきている
# - {コマンド内容}

# ---
# `du -s DIRNAME` *DIRNAME*： 指定したディレクトリの合計のみを表示する

# In[1]:


get_ipython().system('du -s src/')


# ---
# `du -hc DIRNAME`： ディレクトリ全体の合計も表示する

# In[2]:


get_ipython().system('du -ch src/')


# In[3]:


get_ipython().system('du -ch src/*')


# In[ ]:




