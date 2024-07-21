import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 生成示例数据
# 替换为实际数据
np.random.seed(0)
I_type_data = np.random.normal(loc=50, scale=10, size=1000)
S_type_data = np.random.normal(loc=60, scale=10, size=1000)
JH_data = np.random.normal(loc=55, scale=10, size=1000)

# 将数据转换为DataFrame
data = pd.DataFrame({
    'Element Concentration': np.concatenate([I_type_data, S_type_data, JH_data]),
    'Type': ['I-type']*1000 + ['S-type']*1000 + ['JH']*1000
})

# 使用Seaborn绘制KDE图
plt.figure(figsize=(10, 6))
sns.kdeplot(data=data[data['Type'] == 'I-type']['Element Concentration'], label='I-type')
sns.kdeplot(data=data[data['Type'] == 'S-type']['Element Concentration'], label='S-type')
sns.kdeplot(data=data[data['Type'] == 'JH']['Element Concentration'], label='JH')
plt.xlabel('Element Concentration')
plt.ylabel('Density')
plt.title('KDE Plot of Trace Element Data for I-type, S-type, and JH Zircon')
plt.legend()
plt.show()
