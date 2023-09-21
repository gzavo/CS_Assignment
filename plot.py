import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
data = pd.read_csv("istherecorrelation.csv")

# 假设数据集有两列: 'column1' 和 'column2'，您可以根据实际列名修改
plt.figure(figsize=(8, 6), dpi=300)
plt.plot(data['column1'], data['column2'], marker='o')  # 假设你想绘制点和线

# 添加标题和轴标签
plt.title("Title of Your Plot")
plt.xlabel("Name of X-axis")
plt.ylabel("Name of Y-axis")

# 保存图像
plt.savefig("output_image.png", dpi=300)

# 显示图像
plt.show()
