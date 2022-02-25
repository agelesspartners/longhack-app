#Importing the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')
#plt.grid()
#%matplotlib inline


class Viz():
    """A class to create different kinds of visualizations for both numerical and categorical variables."""
    
    def __init__(self, data, variable, title, ylabel, xlabel):
        #Initializing the attributes of the class.
        self.data = data
        self.variable = variable
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
    
    #UNIVARIATE ANALYSIS (NUMERICAL)
    #Visualization for numerical variables
    
    #DISTRIBUTION PLOT
    def distributionplot_viz(self, color, bins = 10):
        #Making a distribution plot of the numerical variable
        plt.figure (figsize = (13, 8))

        sns.histplot(self.data[self.variable], color =  color, bins = bins)
        plt.title(self.title, fontsize = 35)
        plt.ylabel(self.ylabel, fontsize = 30)
        plt.xlabel(self.xlabel, fontsize = 30)

        plt.xticks(fontsize = 15)
        plt.yticks(fontsize = 15)
        
        plt.show()

    #BOX PLOT
    def boxplot_viz(self, color, btitle):       
        #BOX PLOT.
        plt.figure (figsize = (10, 6))
        sns.boxplot(data = self.data, y = self.variable, color = color, showmeans=True)
        plt.title(btitle, fontsize = 25)
        
        plt.xticks(fontsize = 15)
        plt.yticks(fontsize = 15)
       
        plt.show()

    
    #BIVARIATE ANALYSIS (NUMERICAL)
    
    #SCATTER PLOT
    def scatterplot_viz(self, variable2, color, size):
        plt.figure(figsize = (16, 10))
        
        plt.scatter(self.data[self.variable], self.data[variable2], c = color, alpha = 0.4, s = size)

        plt.title(self.title, fontsize = 40)
        plt.xlabel(self.xlabel, fontsize = 35)
        plt.ylabel(self.ylabel, fontsize = 35)

        plt.xticks(fontsize = 15)
        plt.yticks(fontsize = 20)

  
        plt.show()

    #UNIVARIATE ANALYSIS(CATEGORICAL)
    #Visualization for categorical variable.
    
    #COUNT PLOT
    def countplot_viz(self, palette):
        plt.figure(figsize=[20, 10])
        sns.countplot(x = self.variable, palette = palette, data = self.data)
        plt.title(self.title, fontsize = 35)
        plt.ylabel(self.ylabel, fontsize = 30)
        plt.xlabel(self.xlabel, fontsize = 30)

        plt.xticks(fontsize = 15)
        plt.yticks(fontsize = 15)
       
        plt.show()