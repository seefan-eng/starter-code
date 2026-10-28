# 2D Array/List Practice

In today's in class, we will implement a number of different functions. Some of these functions purely use 2D Arrays, however, some of them also require the use of 1D Arrays and/or maybe dictionaries. These functions should help you develop your understanding of 2D Arrays and hopefully apply concepts we've covered before too.

## Provided Code

As you look at the code, you'll notice that there are three functions already implemented for you. The first is our common `num_input` function that takes in a prompt as the parameter, asks the user the prompt, checks if the value is a number, prints a message if it isn't, and returns the number if it is.

The second function is a new function. This function is the `str_to_num_list` function. It takes in a string as a parameter and returns a list containing the numbers in the string. For example, `str_to_num_list("1,2,3,4,5")` would give us `[1,2,3,4,5]`. This is used in the challenge problem in the main.

The third function is the main function itself. This means you only need to focus on implementing the functions and not how the main behaves. This also means you can test your code as you are working on each function.

## Task

For your task, you will implement 5 functions. There is a sixth function as a challenge that I suggest you attempt. I may or may not provide assistance on the challenge though, but that will be explained lower.

### Generate Grid

This function takes in a number `n`. You will create a `n` x `n` 2D Array filled with `"_"`. This function should return the 2D Array after.

#### Example Output

```python
grid = generate_grid(5)
print(grid)

>>
[['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_']]

```

### Print Grid

This function takes in a 2D array and prints out the rows without the list character. It will also print out a new line after each row. This function should not return anything.

#### Example Output

```python

grid = generate_grid(5)
print_grid(grid)

>>
_ _ _ _ _ 
_ _ _ _ _ 
_ _ _ _ _ 
_ _ _ _ _ 
_ _ _ _ _ 

```

### Split Parity

This function takes in a numeric parameter `n` that specifies the number it should go up to. The function will generate the numbers from 0 to n (exclusive of n). It will then split the list into a 2D array with the even values in one inner list and the odd numbers in another inner list. This function should return the 2D Array.

#### Example Output

```python

split = split_parity(10)
print(split) 

>> [[0, 2, 4, 6, 8], [1, 3, 5, 7, 9]]
```

### Print Sequence

This function takes in the 2D array created by the `split_parity` function and prints out the full sequence, taking the values from the even and odd portions and outputting the whole sequence. This function should not return anything.

#### Example Output

```python
split = split_parity(10)
print_sequence(split) 

>> 0 1 2 3 4 5 6 7 8 9 
```

### Sum Grid

This function is more involved and a bit more challenging. It takes in a numeric parameter `n` and creates a `n` x `n` 2D array of random numbers between 1 and 100.

After creating this grid, it should calculate the sum of the rows, producing a list containing the sums of each row.

After computing the sum of the rows, it should calculate the sum of the columns, producing a list containing the sums of each column.

Lastly, it should also compute the total of all the numbers in the list.

It should return a tuple containing all of these values.

#### Example Output

```python

sum_grid(3): 
    grid -> [[81, 96, 3], [4, 91, 52], [13, 65, 52]]
    rows = [180, 147, 130]
    cols = [98, 252, 107]
    all = 457
    returns: ([[81, 96, 3], [4, 91, 52], [13, 65, 52]], [180, 147, 130], [98, 252, 107], 457)

sums = sum_grid(3)
print(sums)

>> ([[81, 96, 3], [4, 91, 52], [13, 65, 52]], [180, 147, 130], [98, 252, 107], 457)
```

### Challenge: Find Dupes

This is the challenge I mentioned at the top. This function takes in a list of numbers and returns a list containing the duplicates from the original list.

This problem can also be quite involved, so it is one that I will not provide much assistance for. I think it's a good challenge to take, but I'd like to see what you're thinking.

However, I will provide this hint: How can we keep a count of how many times a number appears in the list?

#### Example Output

```python
l = [1,2,3,4,3,3,5,4]
print(find_dupes(l))

>> [3,4]
```

