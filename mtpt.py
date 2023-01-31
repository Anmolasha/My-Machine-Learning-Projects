


#first program with the help of matplotlib.


import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


#python-m pip install --upgrade pip

#How can we create a line plot

'''x= np.arange(1,11)
y=2*x
print(x)
print(y)
plt.plot(x,y)
plt.show()'''


#how can we add title and labels

'''x= np.arange(1,11)
y= 2*x
print(x)
print(y)
plt.plot(x,y)
plt.title("SimpleLine Plot")
plt.xlabel("Data on x-axis")
plt.ylabel("Data on y-axis")
plt.show() '''

#how can we change the colour, linestyle and linewidth 

'''x= np.arange(1,11)
y= 2*x
print(x)
print(y)
plt.plot(x,y,color="blue",linestyle=":",linewidth=5)
plt.title("SimpleLine Plot")
plt.xlabel("Data on x-axis")
plt.ylabel("Data on y-axis")
plt.show() '''


'''x= np.arange(1,11)
y1= 2*x
y2=3*x
print(y1)
print(y2)
plt.plot(x,y1,color="blue",linestyle=":",linewidth=5)
plt.plot(x,y2,color="orange",linestyle="-.",linewidth=5)
plt.title("Two Lines in one plot")
plt.xlabel("range")
plt.ylabel("two Lines")
plt.grid(True)
plt.show() '''


#How can we Create SUB PLOTS ROW WISE
#IF I WANT TO STACCK BOTH SUB PLOTS ROW WISE


#First parameter for row and second for columns and third parameter for fisrt sub plot


'''x= np.arange(1,11)
y1=2*x
y2=3*x
print(y1)
print(y2)
plt.subplot(1,2,1)
plt.plot(x,y1,color="green",linestyle=":",linewidth=2)
plt.subplot(1,2,2)
plt.plot(x,y2,color="orange",linestyle=":",linewidth=5)
plt.title("two plots in one table")
plt.show()'''

#IF I WANT TO STACK BOTH SUB PLOTS COLUMN WISE

'''x= np.arange(1,11)
y1= 2*x
y2=3*x
print(y1)
print(y2)

plt.subplot(2,1,1)
plt.plot(x,y1,color="brown",linestyle=":", linewidth= 3)
plt.subplot(2,1,2)
plt.plot(x,y2,color="blue", linestyle="-.", linewidth=5)
plt.show()'''





                                #BAR PLOT
                                   
#Now we create Bar plot

#we apply bar plot on the categorical values and we apply histogram for the numerical values


'''Student= {"kajal": 87,"Arun":56,"kiran": 27}
a= list(Student.keys())
b= list(Student.values())
print(a)
print(b)
plt.bar(a,b)
plt.show()'''

#HOW CAN WE MAKE A BASIC BAR PLOT.

#plt.bar(x[])


'''how can we add labels, x-axis and y-axis in the bar plot.
how can we add grid on the bar plot'''

#THIS IS VERTICAL BAR PLOT

'''Vegetables_basket= {"Brinjal":100,"Potatoes": 145, "Tomatoes": 123}
Vegetables_name= list(Vegetables_basket.keys())
Vegetables_cost= list(Vegetables_basket.values())
plt.bar(Vegetables_name,Vegetables_cost)
plt.title("Bar Plot")
plt.xlabel("Vegetables_name")
plt.ylabel("Vegetables_cost")
plt.grid(True)
plt.show()'''

# HORIZONAL BAR PLOT

'''Vegetables_basket= {"Brinjal":100,"Potatoes": 145, "Tomatoes": 123}
Vegetables_name= list(Vegetables_basket.keys())
Vegetables_cost= list(Vegetables_basket.values())
plt.barh(Vegetables_name,Vegetables_cost, color="yellow")
plt.title("Bar Plot")
plt.xlabel("Vegetables_name")
plt.ylabel("Vegetables_cost")
plt.grid(True)
plt.show()'''

                         #SCATTER PLOT


'''if we have only numerical values then we can create a scatter plot which shows the relationship between two
values, it shows the corelation between two values.what is the meaning of corelation
a mutual relationship or connection between two or more things...'''

'''x=[10,20,30,40,50,60,70,80,90,100]
y=[8,1,7,2,0,3,2,1,6,5]
plt.scatter(x,y)
plt.show()'''


'''x= [4,5,6,1,2,3,7,8]
y=[80,10,40,50,34,20,80,30]
plt.scatter(x,y,color='g')
plt.title('scatter.plot')
plt.xlabel('years from starting of entity')
plt.ylabel('revenue growth in percent(%)')
plt.grid(True)
plt.show()'''



'''x=[4,5,1,6,3,5,8]
y=[8,1,4,5,2,8,3]
plt.scatter(x,y,marker="*",color='b',s=150)
plt.title("scatter plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.show()'''


#ADDING TWO MARKER IN SAME PLOT

'''x= [10,20,30,40,50,60,70,80,90]
a=[8,1,7,2,0,3,7,3,2]
b=[7,2,5,6,9,1,4,5,3]
plt.scatter(x,a,marker="*",color="g",s=150)
plt.scatter(x,b,marker=".",color="orange",s=200)
plt.title("scatter plot")
plt.show()'''


#ADDING SUB-PLOTS
#STACK COLUMN-WISE


'''x=[10,20,30,40,50,60,70,80,90]
a=[10,23,70,56,78,89,90,24,59]
b=[34,89,90,78,68,46,34,23,14]
plt.subplot(1,2,1)
plt.scatter(x,a,marker="*",color="g",s= 150)
plt.title("Company Green")
plt.xlabel("years from entity origin")
plt.ylabel("revenue growth in percent(%)")
plt.grid(True)
plt.subplot(1,2,2)
plt.scatter(x,b,marker=".",color="red",s=300)
plt.title("company red")
plt.xlabel("years from entity origin")
plt.ylabel("revenue growth in percentage(%)")
plt.grid(True)
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.4,hspace=0.4)
plt.show()'''

#stack ROW wise

'''x=[10,20,30,40,50,60,70,80,90]
a=[10,23,70,56,78,89,90,24,59]
b=[34,89,90,78,68,46,34,23,14]
plt.subplot(2,1,1)
plt.scatter(x,a,marker="*",color="g",s= 150)
plt.title("Company Green")
plt.xlabel("years from entity origin")
plt.ylabel("revenue growth in percent(%)")
plt.grid(True)
plt.subplot(2,1,2)
plt.scatter(x,b,marker=".",color="blue",s=300)
plt.title("company red")
plt.xlabel("years from entity origin")
plt.ylabel("revenue growth in percentage(%)")
plt.grid(True)
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.4,hspace=0.4)
plt.show()'''




#........................#HISTOGRAM 

'''z=[1,1,2,2,2,3,3,3,3,4]
plt.hist(z,color="g")
plt.show()'''


'''z=[1,1,2,2,2,3,3,3,3,4]
plt.hist(z,color="r", bins=4)
plt.show()'''


'''iris=pd.read_csv("iris.csv")
print("iris")
print(iris.head())


plt.hist(iris['SepalLengthCm'],bins= 30, color="g")
plt.show()'''


#..........................PIE CHART


#USE OF PIE CHART: a pie vhart is a type of graph that represents the data in the circular path

#why we use pie chart: pie chart are used to represent the propotional data or relative data in a single pie chart.
#the concept of pie slices is used to show the percentage of a particular data from the whole pie.


'''Vegetables=["Potato","Tomato","Brinjal","Chilly"]
Cost=[64,34,100,56]
plt.pie(Cost,labels=Vegetables)
plt.show()'''


'''Vegetables=["Potato","Tomato","Brinjal","Chilly"]
Cost=[64,34,100,56]
plt.pie(Cost,labels=Vegetables,autopct='%0.1f%%',colors=['yellow','grey','green','red','blue'])
plt.show()'''



#...............USE OF DOUGHNUT: chart its looks like pie chart but it has ne hole in between of circle


'''Vegetables=["Potato","Tomato","Brinjal","Chilly","carrot"]
Cost=[64,34,100,56,78]
plt.pie(Cost,labels=Vegetables,radius=1)
plt.pie(Cost,labels=Vegetables,autopct='%0.1f%%',colors=["yellow","green","grey","red","blue"])
plt.pie([1],colors=['w'],radius=0.4)
plt.show()'''

Vegetables=["Potato","Tomato","Brinjal","Chilly","carrot"]
Cost=[64,34,100,56,78]
plt.pie(Cost,labels=Vegetables,radius=1)
plt.pie(Cost,labels=Vegetables,autopct='%0.1f%%',colors=["yellow","green","grey","red","blue"])
#plt.pie(Cost,labels=Vegetables,Cost=[64,34,100,56,78],colors=["yellow","green","grey","red","blue"])
plt.pie([1],colors=['w'],radius=2)
plt.show()











