#!/usr/bin/env python
# coding: utf-8

# ## chmodコマンド
# - Change modeから名称がきている
# - ファイルの権限を変更する
# - [【 chmod 】コマンド――ファイル／ディレクトリのパーミッション（許可属性）を変更する](https://atmarkit.itmedia.co.jp/ait/articles/1605/23/news020.html)
# 
# - 権限の確認方法
# 
# ![Image from Gyazo](https://i.gyazo.com/eecb84d0016c2461a937440d81a728c8.png)<br>
# 
# 
# - 権限付与の数字の意味（755や777などの数字によってどのような違いがあるのか）
# <br>3つの数字は、{owner, group, others}に与えられた権限のこと
# <br>
# <br>r (read) = 4
# <br>w (write) = 2
# <br>x (execute) = 1
# <br>no permissions = 0
# <br>となっており、それぞれの数字にはこのような意味合いがある
# <br>0 (0+0+0) – No permission.
# <br>1 (0+0+1) – Only execute permission.
# <br>2 (0+2+0) – Only write permission.
# <br>3 (0+2+1) – Write and execute permissions.
# <br>4 (4+0+0) – Only read permission.
# <br>5 (4+0+1) – Read and execute permission.
# <br>6 (4+2+0) – Read and write permissions.
# <br>7 (4+2+1) – Read, write, and execute permission.

# ---
# `chmod +x *FILENAME*`：*FILENAME*に実行可能属性を追加する

# In[1]:


# まずは現在の参照権限を参照
get_ipython().system('ls -l src/sample.txt')


# In[2]:


get_ipython().system('chmod +x src/sample.txt')


# In[3]:


get_ipython().system('ls -l src/sample.txt')


# In[4]:


# !chmod -v src/sample.txt


# In[ ]:




