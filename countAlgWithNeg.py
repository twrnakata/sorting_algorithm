# Python program for counting sort
# which takes negative numbers as well

# The function that sorts the given arr[]
def count_sort(arr):
		max_element = int(max(arr))
		min_element = int(min(arr))
		range_of_elements = max_element - min_element + 1

		print("max ", max_element)
		print("min ", min_element)
		print("range_of_elements", range_of_elements)
		print("len(arr)", len(arr))
		# Create a count array to store count of individual
		# elements and initialize count array as 0
		count_arr = [0 for _ in range(range_of_elements)]
		output_arr = [0 for _ in range(len(arr))]

		# Store count of each character
		for i in range(0, len(arr)):
			#count same value to index[data]
			count_arr[arr[i]-min_element] += 1
			# print("arr[i]", arr[i])
			print(arr[i]-min_element)

		# Change count_arr[i] so that count_arr[i] now contains actual
		# position of this element in output array
		for i in range(1, len(count_arr)):
			#sum prev data
			print("i ", i)
			count_arr[i] += count_arr[i-1]
			print(count_arr[i])

		# Build the output character array
		for i in range(len(arr)-1, -1, -1):
			output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
			count_arr[arr[i] - min_element] -= 1

		# Copy the output array to arr, so that arr now
		# contains sorted characters
		for i in range(0, len(arr)):
			arr[i] = output_arr[i]

		return arr


# Driver program to test above function
# arr = [-5, -10, 0, -3, 8, 5, -1, 10]
arr = [10, 2, -3]
ans = count_sort(arr)
print("Sorted character array is " + str(ans))
