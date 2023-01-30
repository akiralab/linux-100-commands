#!/usr/bin/env python
# coding: utf-8

# ## trap コマンド
# - try-catchのような処理ができる

# ```
# #!/bin/sh
# set -e
# trap catch ERR
# 
# function catch {
#     echo エラーを検知しました。エラー後の処理を開始します
#     
#     echo pkill python実行
#     pkill python
#     
#     echo pkill python後に待機中... 10sec
#     sleep 10s
#     echo 再スタートスクリプトの開始
#     
#     python -m trainer.py
# }
# 
# echo 正常フローを記載
# 
#     python -m trainer.py
# 
# exit 0
# ```

# In[ ]:




