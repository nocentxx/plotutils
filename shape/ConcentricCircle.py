import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

ChineseFont1 = FontProperties(fname = 'C:\\Windows\\Fonts\\simsun.ttc')
ChineseFont2 = FontProperties('SimHei')
fontSize = 16

# figure property
plt.figure(figsize=(12, 12))
plt.figtext(0.5, 0.9,  u'现代公共组织的核心能力', fontproperties = ChineseFont1,  fontsize=fontSize+2, horizontalalignment='center', verticalalignment='center')

# circle
circle0 = plt.Circle((1, 1), radius=0.5, fc='r')
plt.text(1, 1, u'理念', fontproperties = ChineseFont1,  fontsize=fontSize, horizontalalignment='center', verticalalignment='center')

circle1 = plt.Circle((1, 1), radius=1, fc='orangered')
plt.text(1, 1.75, u'体制', fontproperties = ChineseFont1,  fontsize=fontSize, horizontalalignment='center', verticalalignment='center')

circle2 = plt.Circle((1, 1), radius=1.5, fc='darkorange')
plt.text(1, 2.25, u'机制', fontproperties = ChineseFont1,  fontsize=fontSize, horizontalalignment='center', verticalalignment='center')

circle3 = plt.Circle((1, 1), radius=2, fc='goldenrod')
plt.text(1, 2.75, u'团队', fontproperties = ChineseFont1,  fontsize=fontSize, horizontalalignment='center', verticalalignment='center')

circle4 = plt.Circle((1, 1), radius=2.5, fc='y')
plt.text(1, 3.25, u'人才', fontproperties = ChineseFont1,  fontsize=fontSize, horizontalalignment='center', verticalalignment='center')

circle5 = plt.Circle((1, 1), radius=3, fc='darkolivegreen')
plt.text(1, 3.75, u'管理与技术', fontproperties = ChineseFont1,  fontsize=fontSize, horizontalalignment='center', verticalalignment='center')

circle6 = plt.Circle((1, 1), radius=3.5, fc='skyblue')
plt.text(1, 4.25, u'产品与服务', fontproperties = ChineseFont1,  fontsize=fontSize, horizontalalignment='center', verticalalignment='center')

plt.gca().add_patch(circle6)
plt.gca().add_patch(circle5)
plt.gca().add_patch(circle4)
plt.gca().add_patch(circle3)
plt.gca().add_patch(circle2)
plt.gca().add_patch(circle1)
plt.gca().add_patch(circle0)

plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.axis('equal')
plt.axis('image')
plt.axis('off')

plt.show()
