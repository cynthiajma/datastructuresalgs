
from typing import List 



def ones_counter(byte:int)-> int:
	# The byte is a 1-byte character bc first bit is 0
	if byte & 0b10000000 == 0:
		return 0
	count = 0
	mask = 0b10000000
	while byte & mask: 
		count += 1
		mask >>= 1
	return count


"""
UTF8 validation 
Character in UTF8 can be 1 to 4 characters long 
For a 1-byte character, the first bit is a 0, followed by its Unicode code.
For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, followed by n - 1 bytes with the most significant 2 bits being 10.


The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. 
This means each integer represents only 1 byte of data.
"""
def valid_utf8(data: List[int]) -> bool:
	i  = 0
	while i < len(data):
		ones_count = ones_counter(data[i])
		#1. when it is a single byte char, we move on to next char 
		if ones_count == 0:
			i += 1
			continue # continue will break the while loop and start it again 

		#2. when it is an invalid char
		if ones_count == 1 or ones_count > 4:
			return False 

		#3. If it is valid, then iterate through length of count
		for j in range(1, count):
			#if passed range of the array, then false 
			if i + j >= len(data):
				return False 
			# if the byte representation of the value doesn't start with 10, then false 
			if data[i+j] & 0b1100000 != 0b10000000:
				return False 
		i += 1
	return True


if __name__ == "__main__":
	int_array = [145]
	print(valid_utf8(int_array))

