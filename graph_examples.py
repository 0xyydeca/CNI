import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import plotly.express as px
import numpy as np
import pandas as pd

def create_basic_line_plot():
    """Create a simple line plot using matplotlib"""
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='sin(x)')
    plt.title('Simple Line Plot')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.grid(True)
    plt.legend()
    plt.savefig('line_plot.png')
    plt.close()

def create_network_graph():
    """Create a simple network graph using networkx"""
    G = nx.Graph()
    
    # Add nodes
    G.add_nodes_from([1, 2, 3, 4, 5])
    
    # Add edges
    G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3)])
    
    plt.figure(figsize=(10, 6))
    nx.draw(G, with_labels=True, node_color='lightblue', 
            node_size=1500, font_size=16, font_weight='bold')
    plt.title('Simple Network Graph')
    plt.savefig('network_graph.png')
    plt.close()

def create_interactive_scatter():
    """Create an interactive scatter plot using plotly"""
    # Generate random data
    np.random.seed(42)
    n_points = 100
    x = np.random.normal(0, 1, n_points)
    y = np.random.normal(0, 1, n_points)
    colors = np.random.randint(0, 3, n_points)
    
    df = pd.DataFrame({
        'x': x,
        'y': y,
        'color': colors
    })
    
    fig = px.scatter(df, x='x', y='y', color='color',
                     title='Interactive Scatter Plot')
    fig.write_html('interactive_scatter.html')

def create_heatmap():
    """Create a heatmap using seaborn"""
    # Generate random data
    data = np.random.rand(10, 10)
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(data, annot=True, cmap='viridis')
    plt.title('Heatmap Example')
    plt.savefig('heatmap.png')
    plt.close()

if __name__ == "__main__":
    print("Creating example graphs...")
    create_basic_line_plot()
    create_network_graph()
    create_interactive_scatter()
    create_heatmap()
    print("Done! Check the generated files:")
    print("- line_plot.png")
    print("- network_graph.png")
    print("- interactive_scatter.html")
    print("- heatmap.png") 