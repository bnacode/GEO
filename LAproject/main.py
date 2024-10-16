import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

names_array = [
    "granit/granodiorit",
    "gabro",
    "dacit/andezit",
    "dijabaz/spilit",
    "peridotit (serpent.)",
    "konglomerat",
    "peščar",
    "krečnjak/dolomit",
    "rožnac",
    "kvarcit",
    "gnajs/migmatit",
    "škriljci",
    "mikašisti"
]

def init():
    global data, X, Y

    # Load the data
    data = pd.read_csv('./LA vrednosti.csv', header=None)
    X = data.iloc[:-1, :].values  # Concentrations
    Y = data.iloc[-1, :].values    # Output vector

def calculate_pearson_correlation():
    # Calculate the Pearson correlation coefficient for each stone with Y
    correlations = {}
    for i in range(X.shape[0]):
        stone_concentration = X[i]
        correlation = pd.Series(stone_concentration).corr(pd.Series(Y))
        correlations[names_array[i]] = float(correlation)
    return correlations

def calculate_spearman_correlation():
    # Calculate the Pearson correlation coefficient for each stone with Y
    correlations = {}
    for i in range(X.shape[0]):
        stone_concentration = X[i]
        correlation = pd.Series(stone_concentration).corr(pd.Series(Y), method='spearman')
        correlations[names_array[i]] = float(correlation)
    return correlations

def plot_absolute_correlation(correlation_results):
    # Extract the names and values for plotting
    names = list(correlation_results.keys())
    values = list(map(abs, correlation_results.values()))  # Convert to absolute values


    df = pd.DataFrame({'Names': names, 'Correlation': values})

    # Sort the DataFrame by correlation values
    df = df.sort_values(by='Correlation', ascending=False)

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(df['Names'], df['Correlation'], color='skyblue')
    plt.ylabel('Pearson Correlation Coefficient')
    plt.title('Correlation of Stone Concentrations with Y')
    plt.axhline(0, color='gray', linestyle='--')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def plot_correlation(correlation_results):
    # Extract names and values
    names = list(correlation_results.keys())
    values = list(correlation_results.values())

    # Create a DataFrame for easier sorting
    df = pd.DataFrame({'Names': names, 'Correlation': values})

    # Add a column for absolute values for sorting
    df['Absolute Correlation'] = df['Correlation'].abs()

    # Sort the DataFrame by absolute correlation values
    df = df.sort_values(by='Absolute Correlation', ascending=False)

    # Create a bar plot
    plt.figure(figsize=(10, 6))

    # Plotting
    colors = ['salmon' if val >= 0 else 'skyblue' for val in df['Correlation']]
    plt.bar(df['Names'], df['Correlation'], color=colors)
    plt.ylabel('Correlation Coefficient')
    plt.title('Correlation of Stone Concentrations with LA')
    plt.axhline(0, color='gray', linestyle='--')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    init()
    correlation_results = calculate_pearson_correlation()
    plot_correlation(correlation_results)


