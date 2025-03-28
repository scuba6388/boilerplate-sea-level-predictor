import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', dtype={'Year': 'int32', 'CSIRO Adjusted Sea Level': 'float64'})

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    linReg = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    m = linReg.slope
    b = linReg.intercept
    fillX = pd.Series(range(df['Year'].max() + 1, 2051))
    lineX = pd.concat([df['Year'], fillX])
    lineY= m * lineX + b

    plt.plot(lineX, lineY, color='Blue')

    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    linReg2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    m2 = linReg2.slope
    b2 = linReg2.intercept
    fillX2 = pd.Series(range(df2['Year'].max() + 1, 2051))
    line2X = pd.concat([df2['Year'], fillX2])
    line2Y = m2 * line2X + b2

    plt.plot(line2X, line2Y, color='Red')

    # print(plt.gca().get_lines()[0].get_ydata().tolist())

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()