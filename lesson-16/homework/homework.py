# homework
# 1. Convert List to 1D Array
# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.
import numpy as np

my_list = [12.23, 13.32, 100, 36.32]
my_array = np.array(my_list)
print(my_array)

# 2. Create 3x3 Matrix (2?10)
# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
my_matrix = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
print(my_matrix)

# 3. Null Vector (10) & Update Sixth Value
# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.
null_vector = np.zeros(10)
null_vector[6] = 11
print(null_vector)
# 4. Array from 12 to 38
# Write a NumPy program to create an array with values ranging from 12 to 38.
n_range = np.arange(12, 38)
print(n_range)

# 5. Convert Array to Float Type
# Write a NumPy program to convert an array to a floating type.
int_array = np.array([1, 2, 3, 4])
float_array = np.array(int_array, dtype=float)
print(float_array)

# 6. Celsius to Fahrenheit Conversion
# Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.
celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = celsius * 9/5 + 32
print(f'Values in Celsius degrees: {celsius}')
print(f'Values in Fahrenheit degrees: {fahrenheit}')

# 7. Append Values to Array (Do self-tudy)
# Write a NumPy program to append values to the end of an array.
arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50, 60, 70, 80, 90])
appended_array = np.append(arr1, arr2)
print(appended_array)

# 8. Array Statistical Functions (Do self-tudy)
# Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.
m = np.random.randint(1, 101, size = 10)
mean = np.mean(m)
median = np.median(m)
standard_deviation = round(np.std(m), 2)
print(f'Mean: {mean}, Median: {median}, Standard Deviation: {standard_deviation}')

# 9 Find min and max
# Create a 10x10 array with random values and find the minimum and maximum values.
arr_10 = np.random.randint(1, 101, size = (10, 10))
min_value = arr_10.min()
max_value = arr_10.max()
print(f'Min: {min_value}, Max: {max_value}')

# 10
# Create a 3x3x3 array with random values.
arr3_3_3 = np.random.randint(1, 101, size = (3, 3, 3))
print(arr3_3_3)
