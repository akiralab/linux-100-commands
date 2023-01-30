#!/usr/bin/env python
# coding: utf-8

# ## grepコマンド
# - Global regular expression printから名称がきている
# - ファイル中の文字列を検索するコマンド
# - [【 grep 】コマンド――特定の文字を含む行を抽出する](https://atmarkit.itmedia.co.jp/ait/articles/1604/07/news018.html)

# ---
# `grep *PATTERN* *FILENAME*`：*FILENAME*から*PATTERN*を検索する

# In[1]:


get_ipython().system('grep linux README.md')


# In[2]:


get_ipython().system('grep grep *')


# ---
# `grep -l *PATTERN* *FILENAME*`：*FILENAME*から*PATTERN*を検索する, <span style='background:blue'>検索結果にファイル名のみ表示する</span>

# In[3]:


get_ipython().system('grep -l linux README.md')


# `grep -c *PATTERN* *FILENAME*`：*FILENAME*から*PATTERN*を検索する, <span style='background:blue'>検索結果に一致した箇所から前後に指定した行数表示する</span>

# In[4]:


get_ipython().system('grep -c linux README.md')


# `grep -c *PATTERN* *FILENAME*`：*FILENAME*から*PATTERN*を検索する, <span style='background:blue'>検索結果に行番号を表示する</span>

# In[5]:


get_ipython().system('grep -n linux README.md')


# In[42]:





# `grep -e *PATTERN* *FILENAME*`：*FILENAME*から*PATTERN*を検索する, <span style='background:blue'>一致処理に指定した正規表現を使う</span>

# In[6]:


get_ipython().system('grep -e linux README.md')


# `grep -v *PATTERN* *FILENAME*`：*FILENAME*から*PATTERN*を検索する, <span style='background:blue'>一致しないものを検索する</span>

# In[7]:


get_ipython().system('grep -v linux README.md')


# In[ ]:





# `grep -r *PATTERN* *FILENAME*`：*FILENAME*から*PATTERN*を検索する, `<span style='background:blue'>ディレクトリ内も検索対象とする</span>`

# In[8]:


get_ipython().system('grep -r linux src/*')


# In[ ]:




