import seaborn as sns
import matplotlib.pyplot as plt

def plot_histogram(df, column, title):
    sns.histplot(df[column], kde=True)
    plt.title(title)
    plt.show()

def plot_correlation_matrix(df):
    correlation = df.corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()
