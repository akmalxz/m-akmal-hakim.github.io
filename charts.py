import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# General style tweaks
rcParams['font.family'] = 'sans-serif'
rcParams['font.size'] = 8
rcParams['axes.edgecolor'] = '#333'
rcParams['axes.linewidth'] = 0.5
rcParams['axes.spines.top'] = False
rcParams['axes.spines.right'] = False
rcParams['xtick.color'] = '#333'
rcParams['ytick.color'] = '#333'

# Bar Chart
x = np.arange(4)
y = [3, 7, 5, 4]

fig, ax = plt.subplots(figsize=(4,3))
ax.bar(x, y, color='gray')
ax.set_xticks(x)
ax.set_xticklabels(['Q1', 'Q2', 'Q3', 'Q4'])
ax.set_ylabel('Sales')
ax.set_title('Sales by Quarter', fontsize=10, pad=10)
ax.tick_params(axis='both', which='major', length=0)
[spine.set_visible(False) for spine in ax.spines.values()]
fig.tight_layout()
plt.savefig('bar_chart.png', dpi=100)
plt.close()

# Pie Chart
labels = ['A', 'B', 'C', 'D']
sizes = [30, 20, 35, 15]

fig, ax = plt.subplots(figsize=(3,3))
wedges, texts = ax.pie(
    sizes, 
    labels=labels, 
    colors=['lightgray','silver','darkgray','gray'], 
    startangle=90,
    textprops={'fontsize':8}
)
for w in wedges:
    w.set_linewidth(0.5)
    w.set_edgecolor('#333')

ax.set_title('Market Share', fontsize=10, pad=10)
fig.tight_layout()
plt.savefig('pie_chart.png', dpi=100)
plt.close()

# Dual Axis Chart
months = np.arange(1,13)
values1 = np.random.randint(10, 20, size=12)
values2 = np.random.randint(50, 100, size=12)

fig, ax1 = plt.subplots(figsize=(4,3))
ax2 = ax1.twinx()

ax1.plot(months, values1, color='gray', marker='o', linewidth=1, markersize=3)
ax1.set_xlabel('Month')
ax1.set_ylabel('Metric A', color='gray')
ax1.tick_params(axis='y', labelcolor='gray', length=0)
ax1.tick_params(axis='x', length=0)
[spine.set_visible(False) for spine in ax1.spines.values()]

ax2.bar(months, values2, color='silver', alpha=0.7, width=0.6)
ax2.set_ylabel('Metric B', color='silver')
ax2.tick_params(axis='y', labelcolor='silver', length=0)
for spine in ax2.spines.values():
    spine.set_visible(False)

plt.title('Dual Axis Chart', fontsize=10, pad=10)
fig.tight_layout()
plt.savefig('dual_axis_chart.png', dpi=100)
plt.close()
