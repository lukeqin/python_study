#-*- coding: UTF-8 -*-
'''
Created on 2017年3月11日
@author: luke
'''

'''
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))
plt.show()
'''
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-100, 100, 100)
y = x*x*x

myfont = matplotlib.font_manager.FontProperties(fname=r'Light.ttc')
plt.plot(x, y, "b--",label="$y=x3$",  linewidth=2)
plt.title(u"y=x3的散点图", fontproperties=myfont)
plt.legend()
plt.show()

