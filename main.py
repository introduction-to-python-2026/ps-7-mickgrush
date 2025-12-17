
import matplotlib.pyplot
import seaborn as sns
from sklearn.datasets import fetch_openml

data = fetch_openml(name='boston', version=1, as_frame=True,parser='pandas')

features = list(df.columns)
print("Available features:", features)
selected_features = ['CRIM' , 'RM', 'AGE', 'B', 'TAX']
print("Selected features: ", selected_features)

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, selected_features):
    ax.hist(data.frame[f], bins=5, color='blue', edgecolor='black')
    ax.set_xlabel(f)



reference_feature = selected_features[0]
comparison_feature = selected_features[3]


plt.figure(figsize=(5, 5))
plt.scatter(data.frame[reference_feature], data.frame[comparison_feature], alpha=0.6)
plt.xlabel(reference_feature)
plt.ylabel(comparison_feature)


plt.savefig('correlation_plot.png')

plt.show()
