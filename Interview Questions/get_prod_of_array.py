# given arr[N]
# prod[i] = prod of all ele of arr except arr[i]
# i/p: [10, 3, 5, 6, 1]
# o/p: [90, 300, 180, 150, 900]
# time complexity: O(n)


def get_prod_with_div(arr):
	prod = []
	all_prod = 1
	for ele in arr:
		all_prod = all_prod * ele
	for ele in arr:
		prod.append(all_prod // ele)
	return prod


def get_prod_without_div(arr):
	prod = []
	all_prod = 1
	for ele in arr:
		all_prod = all_prod * ele
	for ele in arr:
		prod.append(int(all_prod * pow(ele, -1)))
	return prod


arr = [10, 3, 5, 6, 1]

print("get_prod_with_div: ", get_prod_with_div(arr))
print("get_prod_without_div: ",get_prod_without_div(arr))
