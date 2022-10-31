class Solution:
	def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
		len_arr = len(arr)
		res = 0
		temp = arr[0 : k - 1]
		curr_sum = sum(temp)
		for r in range(k - 1, len(arr)):
			curr_sum += arr[r]
			print(curr_sum)
			if curr_sum / k >= threshold:
				res += 1
			curr_sum -= arr[r - k + 1]
		return res
