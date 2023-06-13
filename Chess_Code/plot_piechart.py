import matplotlib.pyplot as plt


plt.pie([90, 10], labels=['AI Win %', 'Human Win %'], shadow=True, explode=[0.1, 0.1])
plt.title('Win % of AI at depth 4')
plt.legend()
plt.show()
