# Part B - The Turtle Library for Python

In addition to general purpose coding, Python has *libraries* that allow users to perform specialized tasks more easily. One of these libraries is called **Turtle**. The Turtle library consists of a set of predefined functions that let us draw pictures and shapes on a virtual canvas. We'll use this library to create the elements of our Pong game. Before we start with the game, we'll do a quick introduction to get everyone familiar with using the library.

To use any kind of Python library, we need to import it into the Python environment. We can import Turtle with the statement: `import turtle`. Import statements generally go at the top of a Python file. When we want to use functions from the Turtle library, we use the syntax `turtle.some_function()`. This lets Python know that `some_function` comes from the turtle library. 

To carry out any drawing commands, we need to open up a new window, called a **screen** that will be our canvas. To create the screen we initialize a new variable:

```python
import turtle
screen = turtle.getscreen() 
```
<!-- put a picture of the screen with turtle here -->

The black arrowhead in the middle of the screen is called the **turtle**. It is like our on-screen pen.

Let us now look at the screen. It can be divided into four quadrants, as below. The turtle is at the (0, 0) position. 

Our next step is to draw a shape, so we need to define a variable for the turtle. 

```python
my_turtle = turtle.Turtle() # remember, the first 'turtle' refers to the library!
```

If you want to draw a line in the turtle's path, you can use the command
```python
my_turtle.pendown()
```

To move the turtle without drawing a line, use
```python
my_turtle.penup()
```

We can use the commands *forward*, *backward*, *right*, and *left* to move my_turtle around the screen. Using commands *forward* and *backward* you can move the turtle in straight lines in the forward and backward directions. To turn right or left, we tell the turtle how far to rotate, with an angle specified in degrees. 

Note that on a virtual screen the distance is measured in pixels, like we measure distance in cm on using a ruler. 

For our first example, let’s say we want to draw a square of size 100x100 pixels. How can we do that?

**Step 1** - Move `my_turtle` in the forward direction 100 pixels
```python
my_turtle.forward(100)
```

**Step 2** - Turn `my_turtle` 90 degrees to the left
```python
my_turtle.left(90)
```

**Step 3** - Move `my_turtle` in the forward direction 100 pixels
```python
my_turtle.forward(100)
```

**Step 4** - Turn `my_turtle` 90 degrees to the left
```python
my_turtle.left(90)
```

**Step 5** - Move `my_turtle` in the forward direction 100 pixels
```python
my_turtle.forward(100)
```

**Step 6** - Turn `my_turtle` 90 degrees to the left
```python
my_turtle.left(90)
```

**Step 7** - Move `my_turtle` in the forward direction 100 pixels
```python
my_turtle.forward(100)
```

To clear what's been drawn on your screen, use: 
```python
screen.clear()
```

Now let’s say we want to draw a triangle that has equal sides (equilateral triangle), of length 100 pixels. How can we do that?

**Step 1** - Turn `my_turtle` 60 degrees to the left

**Step 2** - Move `my_turtle` in the forward direction 100 pixels

**Step 3** - Turn `my_turtle` 120 degrees to the right

**Step 4** - Move `my_turtle` in the forward direction 100 pixels

**Step 5** - Turn `my_turtle` 120 degrees to the right

**Step 6** - Move `my_turtle` in the forward direction 100 pixels

In code, this looks like:
```python
screen.clear()
my_turtle.left(60)
my_turtle.forward(100)
my_turtle.right(120)
my_turtle.forward(100)
my_turtle.right(120)
my_turtle.forward(100)
```

Another way to move my_turtle is by providing x and y coordinates. As we said earlier, the measurement we use on a virtual screen is pixels. So we can specify the x and y coordinate that we want `my_turtle` to go to. 
Let’s say we want `my_turtle` to move to (x,y) = (150,100).

```python
my_turtle.goto(150,100)
```

We can draw the above shapes using this type of command too.

Apart from these, there are so many commands that we can use. For example, we can change the colour or size of the screen. 

```python
screen.bgcolor("blue")  # Try "yellow", "green", "red", ...
sc.setup(width=1000, height=600)  # units are pixels
```

We can also change the size, shape, colour and speed of `my_turtle`:
```python
turtle.shape("circle")
right_pad.shapesize(stretch_len=6)  # stretches a circle into an oval
turtle.color("orange")
turtle.speed(5)  # can be an integer value from 0-10, with 10 being the fastest
```

>### *Coding Challenge #6*
>- Open up a *screen* and set the background colour to black
>- Create a turtle object called `my_marker`, and change its colour to violet
>- Use `my_marker` to draw a square or triangle using the *forward*, *backward*, *right*, *left* and *goto* commands. Feel free to use the code above to help!

___
>### *Coding Challenge #7*
>- Write the first letter of your name on the *screen*. (Or maybe even your first name!!)
