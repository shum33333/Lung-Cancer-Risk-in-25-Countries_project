import matplotlib
matplotlib.use('TkAgg')  # 或改成 'QtAgg' 試試
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [10, 20, 15])
plt.title("測試圖")
plt.show()
