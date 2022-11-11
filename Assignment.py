


#header files to use the datafram and graphs in the code.
import pandas as pd
import matplotlib.pyplot as plt



#load the dataset into the df that is alias of the dataFrame. 
df = pd.read_csv("D:\\spyder_project\\washdash-download.csv")
df



#Function made to print the basic details of the dataframe 
#The function display details of every new dataframe that can be created in the whole document
def basic_details(x):
    #printing message to print the details of the dataframe with the help of describe function
    print("\n         ***** Details *****") 
    print(x.describe())
    #printing message to print the shape of the dataframe
    print("\n***** Shape *****\n")
    print(x.shape)
    #print the basic information of the dataframe 
    print("\n    ***** Information *****\n")
    print(x.info())
    #print the columns names
    print("\n***** Columns Names *****\n")
    print(x.columns)
    #print total of the null values that contain in the dataframe 
    print("\n***** Null values *****\n")
    print(x.isnull().sum())

#fuction call for the dataframe 1 
basic_details(df)


df1=df
#fuction call for the dataframe 2
basic_details(df1)


#groupby function use to merge the similar type of data and also using mean function 
df2 = df1.groupby(["Residence Type","Service Type","Year"]).mean()
df2 #show the dataframe 


#fuction call for the dataframe 3
basic_details(df2)


def linegraph():
    df2.plot()
    plt.suptitle("United Kingdom of Great Britain and Northern Ireland")
    plt.xlabel("Residence Type,Service Type,Year")    #xlabels asign the value year
    plt.ylabel("Population")   #ylabels asign the value Sales
    plt.xticks(rotation=45) 
    plt.yticks(rotation=45)
    plt.legend(["Coverage","Population"])
    
linegraph()



#groupby function use to merge the similar type of data and also using mean function 
df3= df1.groupby(["Year","Service Type"]).mean()
df3 #show the dataframe



#fuction call for the dataframe 4
basic_details(df3)


df3.plot(kind='bar' ) #ploting the bar graph
plt.suptitle("United Kingdom of Great Britain and Northern Ireland") #title of the graph
plt.xlabel("Year, Service Type")    #xlabels asign the value year
plt.ylabel("Population")   #ylabels asign the value Sales
plt.xticks(rotation=45)    #rotate the asix label using xticks
plt.yticks(rotation=45)    #rotate the axis label using yticks 
plt.legend(loc = 1)        #Uing the legend that help in describe the graph effectively 



#groupby function use to merge the similar type of data and also using mean function 
df4 = df1.groupby(["Year","Service level","Service Type"]).mean()
df4 #show the dataframe 


#fuction call for the dataframe 5
basic_details(df4)


axes = df4.plot(kind='area',subplots = True)    #ploting the area graph with
plt.suptitle("United Kingdom of Great Britain and Northern Ireland") #title of the graph              
plt.xlabel("Year, Service level, Service Type")    #xlabels asign the value year
plt.ylabel("Population")   #ylabels asign the value Sales4
plt.xticks(rotation=90)    #rotate the asix label using xticks
plt.yticks(rotation=90)    #rotate the axix label using yticks
plt.legend(loc = "upper left")   #legend of subplot second that show the legend in upper left side of the graph
axes[0].legend(loc = 1)          #legend of subplot one that show the legend in upper right side of the graph

