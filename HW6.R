# Question 1
x <- matrix(c(7, 2, 9, 4, 12, 13), nrow = 2, ncol = 3)
y <- matrix(c(1, 2, 3, 7, 8, 9, 12, 13, 14,19, 20, 21), nrow = 3, ncol = 4)
x %*% y

# Question 2
# part a
Data_Frame <- data.frame (
  id = c(1, 2, 3, 4, 5),
  name = c('Peter', 'Amy', 'Ryan', 'Gary', 'Michelle'),
  salary = c(623.30, 515.20, 611.00, 729.00, 843.25)
)

# part b
department <- c('Human Resources', 'Sales', 'Marketing', 'Accounting', 'Wellness')
Data_Frame$department <- department

# part c
Data_Frame <- Data_Frame[-c(1, 3, 5), -c(2, 3)]

# part d
x2 <- c("Peter", "Gary", "Michelle")
y2 <- c(623.30, 729.00, 843.25)
barplot(y2, names.arg = x2)

# part e
Data_Frame <- data.frame (
  id = c(1, 2, 3, 4, 5),
  name = c('Peter', 'Amy', 'Ryan', 'Gary', 'Michelle'),
  salary = c(623.30, 515.20, 611.00, 729.00, 843.25)
)

mylabel <- c("highest salary", "lowest salary", "median salary")
colors <- c("blue", "yellow", "green", "black")

maxS <- max(Data_Frame$salary)
minS <- min(Data_Frame$salary)
medianS <- median(Data_Frame$salary)
x3 <- c(maxS, minS, medianS)

# Display the pie chart with colors
pie(x3, label = mylabel, main = "Salary Statistics", col = colors)

# Display the explanation box
legend("topleft", mylabel, fill = colors)

# Question 3
# if/else 
get_color <- function(a) {
  if (a == 'red'){
      return (col=c("#FF3300"))
  } else if (a == 'white'){
      return (col=c("#FFFFFF"))
  } else if (a == 'blue'){
      return (col=c("#3333FF"))
  } else {
      return (col=c("#000000"))
  }
}
get_color('red')
get_color('white')
get_color('blue')
get_color('black')

#for loop
install.packages("TurtleGraphics")
library("TurtleGraphics")

x4 = -(height/20)-(0.75*height)
y4 = 0.75*height 
draw_starrows <- function(a, b) {
  turtle_init()
  for (i in 1:5) {
    x4 = x4 + (a/8.696)
    turtle_up()
    turtle_col(col="white")
    turtle_down()
    turtle_forward(a/32.5)
    turtle_left(144)
    turtle_forward(a/32.5)
    turtle_left(144)
    turtle_forward(a/32.5)
    turtle_left(144)
    turtle_forward(a/32.5)
    turtle_left(144)
    turtle_forward(a/32.5)
    turtle_left(144)
    }
  }

draw_starrows(height, height/1.43)