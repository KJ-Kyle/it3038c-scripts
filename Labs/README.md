# Lab 7 Example

This is how to run a python script with python Numpy 

To start, we need to install Numpy. to do so, run the following command in the terminal.

```bash
pip install numpy
```

now that numpy is installed, lets make an array and print it.

```python
import numpy as np

a = np.array([10,20,30,40])
print(a)
```

There is actully an easier way to creat an array using .arange

```python
b = np.arange(5)
print(b)
```

The .arange function alows for the simple creation of an in-order array 

we can now create multiple arrays using the .reshape function 

```python
c = np.arrange(15).reshape(3,5)
print(c)
```

we can also do math with the above array with the .sum function 

```python 
print(c.sum(axis=0))
```

This function takes the sum of each column 
