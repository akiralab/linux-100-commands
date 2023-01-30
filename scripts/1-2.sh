# 計算させる
echo '---1.2.c---'
echo '1+1' | bc
#  2

echo '28*43' | bc
# 1204

# 計算結果をファイルに保存する
echo '---1.2.d---'
echo '1+1' | bc > a.txt
cat a.txt
# 2

echo '---1.2.e(skip)---'
# nautilus

echo '---1.2.f---'
chmod -r a.txt
cat a.txt
whoami
chmod +r a.txt
cat a.txt
sudo whoami

echo '---1.2.g---'
man ls