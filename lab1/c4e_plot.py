from matplotlib import pyplot

#1. prepare data
labels = ["Android","Ios","Web"]
values = [30,40,30]
colors = ["red",'blue','green']
explode = [0, 0.2, 0]
#plot
pyplot.pie(values, labels=labels,colors=colors,explode=explode,shadow=True)

pyplot.axis('equal')
#show
pyplot.show()
