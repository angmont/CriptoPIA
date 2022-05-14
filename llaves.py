#    Python 3 program for
#    Generate all the binary strings of N bits
class BinaryText :
	def solution(self, record, start, last) :
		if (start == last) :
			print(record)
			return
		
		#  Find result using recursion
		self.solution(record + str('0'), start + 1, last)
		self.solution(record + str('1'), start + 1, last)
	
	def binaryString(self, n) :
		#  N indicate digit in binary
		if (n <= 0) :
			return
		
		print(" Digit : ", n ," ")
		self.solution("", 0, n)
	

def main() :
	task = BinaryText()
	task.binaryString(12)

if __name__ == "__main__": main()


