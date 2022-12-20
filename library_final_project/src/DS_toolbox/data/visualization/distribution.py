import matplotlib.pyplot as plt

def density_histogram(data, bins, density=True):
    """This function displays the statistical information using rectangles for showing
    the frequency of data items in successive numerical intervals of equal size  
     
    Parameters
    ----------
    data =  a list or array of numerical values that you want to create a histogram for
    bins =  the number of bins to use in the histogram
    density = a boolean value indicating whether the histogram should be normalized to show probability density (True) or raw counts (False). The default value is True.
     
    Returns:
    ---------- 
    The function uses the hist function from the matplotlib library to return a histogram of the data and displays it using show. 
    The ylabel function is used to label the y-axis as "Probability"."""
    
    plt.hist(data, bins=bins, density=density)
    plt.ylabel('Probability')
    plt.show()

