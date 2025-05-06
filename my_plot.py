# coding=utf-8
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

# windws和linux设置字体
# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': 'larger'}
# matplotlib.rc("font", **font)

my_font = font_manager.FontProperties(fname="C:\\Windows\\Fonts\\华文宋体.ttf") #不会改中文 大问题靠靠靠

x = range(0, 120)  # 形成一个列表
y = [random.randint(20, 35) for i in range(120)]

# 设置图片的大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘图
plt.plot(x, y)

_x = list(x)
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
plt.xticks(_x[::3], _xtick_labels[::3], rotation=45,fontproperties=my_font)
# 保存
# plt.savefig("./t1.png")

# 展示图像
plt.show()