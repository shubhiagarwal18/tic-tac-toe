
class iterator(object):
	def __init__(self, n):
		super(iterator, self).__init__()
		self.n = n
		
	def divByChecker(self):
		for i in range(0, self.n):
			if i % 7 == 0:a
				yield i

for number in iterator(70).divByChecker():
	print(number)
