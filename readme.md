# 猫叫翻译机！

能把中文翻译成猫叫的翻译机！
灵感来自https://github.com/RimoChan/yinglish.git(<sub>其实就是搜索替换了字符串</sub>)


## 样例

```python
import miaolish

print(miaolish.chs2miao('你好吖！'))
#你，喵，喵，你好猫猫吖，喵喵喵！
```


## 接口说明

```python
def chs2miao(s, 猫叫率=0.5):
```

s是原字符串，猫叫率是0~1的实数，越大越容易猫叫，表示每个词语被转化的概率。


## 安装

首先，你需要安装一个Python(3.6以上版本)。

然后——
```bash 
pip install git+https://github.com/DreamOneX/miaolish.git
```

最后`import miaolish`就行了。


## 结束

就这样，大家88<sub>(溜了溜了)</sub>。
