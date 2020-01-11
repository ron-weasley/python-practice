import numpy as np

arr = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
bool_arr = arr > 3
print("bool\n", bool_arr)
print("true values\n", arr[bool_arr])
# or in sigle way
print("true values\n", arr[arr>3])

arr1 = np.array([[1, 2, 3.23],[4, 5, 6],[7, 8, 9]], dtype=np.float64)
print("arr1\n", arr1) # or np .add .subtract .multiply .divide .sqrt
print("add\n", arr1+arr)
print("sub\n", arr1-arr)
print("div\n", arr1/arr)
print("mul\n", arr1*arr)
print("exp\n", arr**arr1)
print("sqrt\n", np.sqrt(arr))