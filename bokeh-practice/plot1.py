# Making basic Bokeh line graph

# Importing Bokeh
from bokeh.plotting import figure 
from bokeh.io import output_file, show 

# Prepare some data 
# These needs to be of the same length
x = [1,2,3,4,5]
y = [6,7,8,9,10]

# Prepare output file 
output_file("Line.html")

# Creating figure object 
f = figure()

# Creating line plot 
f.line(x,y)

# make the plot appear 
show(f)

# options can be found using dir(f), by passing the figure into it