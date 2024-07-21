from typing import *


def find_celebrity(n: int) -> int: # n = total number of candidates
	
	candidate = 0

	for i in range(1, n):
		if knows(candidate, i):
			candidate = i


	for i in range(n):
		if i != candidate && knows(candidate, i):
			if !knows(i, candidate): # candidate knows someone
			return -1
	
	return candidate



if __name__ == "__main__":