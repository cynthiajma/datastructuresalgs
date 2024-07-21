from typing import * 

class Solution: 

		def longest_common_subsequence(text1: str, text2: str) -> int:
		# 0 a b c d e 
		# a 1 1 1 1 1
		# c 1 1 2 2 2
		# e 1 1 2 2 3

			dp = [[0] * (len(text1)+1) for _ in range(len(text2)+1)]
			for i in range(1, len(text2) + 1):
				for j in range(1, len(text1) + 1):
					# equal
					if text2[i-1] == text1[j-1]: 
						dp[i][j] = dp[i-1][j-1] + 1
					# not subsequence
					else:
						dp[i][j] = max(dp[i-1][j], dp[i][j-1])
			return dp[len(text2)][len(text1)]



		"""
		Continually finds the longest subsequence from (i,j)
		"""
		def longest_increasing_subsequence(nums: List[int]) -> int:
			dp = [1] * len(nums) # holds the longest subsequence up from (i,j) 
			for i in range(len(nums)): 
				for j in range(i):
					# if less, increment subsequence length 
					if nums[i] > nums[j] and dp[i] < dp[j] + 1:
						dp[i] = dp[j] + 1 # dp[j] is the last longest subsequence 
			return max(dp)
			# dp = [1, 2, 3, 4, 5, 3, 6, 4, 5]




		"""
		Memoization: used to store results of subproblems to avoid redundant calculations
		This will find all substrings of the current string without repeats because of the cache 
		1) check if boundaries match
		2) if boundaries match, check if string in between is a palindrome
		"""
		def longest_palindrome_subsequence(s: str) -> int: 
			cache = {} 
			reversed_s = s[::-1]

			def dp(i,j): # dp will return the length of the palindrome of the string
				# base case: 
				if (i,j) in cache:
					return cache[(i,j)]
				# reached end of either string 
				elif i >= len(s) or j >= len(reversed_s):
					return 0
				if s[i] == reversed_s[i]:
					cache[i,j] = 1 + dp(i+1, j+1) # gets length of the palindrome inside the boundary 
				else:
					# take the max of skipping a character in either string 
					cache[i,j] = max(dp(i, j+1), dp(i+1,j)) 
				return cache[(i,j)]

			return dp(0,0)



		"""
		dp[start][end] = dp[start + 1][end - 1] + 2
		This includes both matching characters and adds 2 to the length of the longest palindromic subsequence within the inner substring.
		When Characters Do Not Match (s[start] != s[end]):

		dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
		This considers the maximum length obtained by either skipping the character at the start or the end.
		"""
		def longest_palindrome_subsequence_with_array(s: str) -> int:
			n = len(s)
			grid = [[0] * n for _ in range(n)]

			# strs of length 1 are palindromes
			for i in range(n):
				grid[i][i] = 1

			for length in range(2, n + 1):
				for start in range(n-length + 1):
					end = start + length -1
					# check if boundary is equal:
					if s[start] == s[end]:
						grid[start][end] = grid[start+1][end-1] + 2 # get length of str in between boundary

					else:
						grid[start][end] = max(grid[start+1][end], grid[start][end-1]) # find max length of strs skipping start and end
			return grid[0][n-1] # entire string s


		def longest_palindrome_subsequence_string(self, s: str) -> str:
		    n = len(s)
		    grid = [[0] * n for _ in range(n)]
		    subsequence = [[""] * n for _ in range(n)]

		    if n == 1:
		        return s

		    # check for strs with length 1
		    for i in range(n):
		        grid[i][i] = 1
		        subsequence[i][i] = s[i]

		    for length in range(2, n+1):
		        for start in range(n - length + 1): 
		            end = start + length -1 
		            # check boundary
		            if s[start] == s[end]:
		                if length == 2:
		                    grid[start][end] = 2
		                    subsequence[start][end] = s[start] + s[end]
		                else:
		                    grid[start][end] = grid[start+1][end-1] + 2
		                    subsequence[start][end] = s[start] + subsequence[start+1][end-1] + s[end]
		            else:
		                if grid[start+1][end] > grid[start][end-1]:
		                    grid[start][end] = grid[start+1][end]
		                    subsequence[start][end] = subsequence[start+1][end]
		                else:
		                    grid[start][end] = grid[start][end-1]
		                    subsequence[start][end] = subsequence[start][end-1]
		    return subsequence[0][n-1]



		def longest_palindrome_substring(self, s: str) -> str:
			n = len(s)
			grid = [[False] * n for _ in range(n)]

			# length 0 and 1
			if n == 0: 
				return ""
			if n == 1:
				return s

			start_idx = 0
			max_length = 1

			# length 1
			for i in range(n):
				grid[i][i] = True
			# length 2
			for i in range(n-1):
				if s[i] == s[i+1]:
					grid[i][i+1] = True 
					max_length = 2
					start_idx = i

			# length 3 and above
			for length in range(3, n):
				for start in range(n-length + 1):
					end = start+length-1
					if s[start] == s[end] and grid[start+1][end-1]:
						grid[start][end] = True 
						start_idx = start
						max_length = length

			return s[start_idx: start_idx+max_length]



if __name__ == "__main__":
	text1 = "abcde"
	text2 = "ace"
	self = Solution()
	

	print(self.longest_palindrome_substring("babad"))
