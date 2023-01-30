#!/usr/bin/env python
# coding: utf-8

# ## grep コマンド
# - {Global regular expression print}から名称がきている
# - 文字列に対して正規表現を使って検索するコマンド
# - 正規表現を勉強する必要がある

# ---
# `grep *検索したい正規表現* ファイル名` : 指定した表現を検索する

# In[1]:


get_ipython().system('seq 10 | grep 1')


# ---
# ### 正規表現の例
# - '^文字列' : 先頭を検索
# - '文字列$' : 末尾を検索
# - '文字列.' : 文字列 + 何か1文字（.の数によって文字数は変わってくる）

# In[2]:


get_ipython().system('seq 100 | grep "^5"')


# In[3]:


get_ipython().system('seq 100 | grep "5$"')


# In[4]:


get_ipython().system('seq 100 | grep "5."')


# ---
# ### 正規表現の例
# - '文字列2$' : 末尾に文字列が0個以上連続する
# - '文字列*$' : 末尾に文字列が0個以上連続する
# - '[文字列1、文字列2、文字列3]' : []内部のどれかの文字列を検索
# - '[^文字列1、文字列2、文字列3]' : []内部のどれかの文字列以外を検索

# In[5]:


get_ipython().system('seq 1000 | grep "^12*$"')


# In[6]:


get_ipython().system('seq 100 | grep "[02468]$" | xargs')


# In[7]:


get_ipython().system('seq 100 | grep "[^02468]$" | xargs')


# ---
# ### 正規表現の例
# - -E をつけることで、拡張正規表現ができる

# In[8]:


get_ipython().system("seq 100 | grep -E '^(.)\\1$'")


# In[9]:


get_ipython().system('echo 中村 山田 田代 上田 | grep -o "[^ ]田"')


# In[ ]:




