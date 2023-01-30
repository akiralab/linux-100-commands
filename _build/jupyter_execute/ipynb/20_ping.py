#!/usr/bin/env python
# coding: utf-8

# ## ping コマンド
# - Packet Internet Groperから名称がきている
# - Networkの接続テストとして用いられる

# ---
# `ping DESTINATION` ： *DESTINATION*に接続する
# 
# - optionを何も指定しない場合、ずっと繰り返す
# - `-c 回数`のオプションを加えることで、指定回数繰り返す
# - ドメインをIPアドレスに変換後、ICMP()

# In[1]:


get_ipython().system('ping -c 5 google.com')


# ---
# `ping -p PATTERN`： 送信するパケット内容を指定することも可能

# In[2]:


get_ipython().system('ping -c 5 -p ff google.com')


# In[ ]:





# In[ ]:




