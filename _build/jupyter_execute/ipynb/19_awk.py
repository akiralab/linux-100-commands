#!/usr/bin/env python
# coding: utf-8

# ## awk コマンド
# - から名称がきている
# - テキストファイルに対して、行ごとに処理を行う
# - 空白などで区切られたテキストを処理するコマンド
# - 演算機能もある

# ---
# ### awk '/正規表現/' -> 正規表現

# In[1]:


# 偶数のみ表示する
get_ipython().system("seq 5 | awk '/[02468]/'")


# ---
# ### awk '条件{print(printしたい内容)}'

# In[2]:


get_ipython().system('seq 10 | awk \'$1%2==0{print($1"は偶数です")}\'')


# ---
# ### awk '{print(printしたい内容)}'
# - print内部で条件を作成することもできる

# In[3]:


get_ipython().system('seq 10 | awk \'{print $1%2==0 ? $1"は偶数です": $1"は奇数です"}\'')

!seq 10 | awk '{print $1%2==0 ? $1"は偶数です": $1"は奇数です"}'
# In[ ]:





# In[ ]:





# In[ ]:




