#!/usr/bin/env python
# coding: utf-8

# ## rsync コマンド
# - remote syncから名称がきている
# - 別々のlinuxシステムからlocalにファイルをコピーもしくは同期する際に使用するコマンド
# - 送る専門。

# ---
# `# rsync options SOURCE DESTINATION` *SOURCE*から*DESTINATION*に同期する

# In[1]:


get_ipython().system('rsync -ac src/lm1/sample.txt src/lm2/sample.txt')


# In[ ]:




