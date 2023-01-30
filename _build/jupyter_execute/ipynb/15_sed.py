#!/usr/bin/env python
# coding: utf-8

# ## sed コマンド
# - {Stream EDitor}からきている
# - 文字を置換するコマンド
# - パイプとリダイレクトを活用するのが一般的
# - ファイル名を省略した場合は、標準入力からのデータを処理する

# ---
# `sed "s/置換前の文字列/置換後の文字列/"` 入力に対して、置換前の文字列を置換後の文字列に置換する

# In[1]:


get_ipython().system('ls  src/')


# In[2]:


get_ipython().system('ls src/ | sed "s/.txt/.py/"')


# `sed -e` もしくは `sed -r` : 拡張正規表現（練習中）

# In[3]:


get_ipython().system("echo クロロメチルエチルエーテル | sed -E 's/(メ..)(...)/\\2\\1/'")


# In[ ]:




