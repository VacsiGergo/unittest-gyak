import unittest

szam = int(input("Adj meg egy számot: "))

def fibo(n:int):
    tmp = 1
    a = 0
    b = 0
    for i in range(0,n-1):
        b = a
        a = tmp
        tmp = a + b
    return tmp

print(fibo(szam))

class FiboTest(unittest.TestCase):
    def basicRun(self):
        self.assertEqual(fibo(4), 3)
    def minusGiven(self):
        self.minusGiven(fibo(-2), 0)
    def wrongNumber(self):
        self.assertGreater(fibo(0.2), 0)
    def lessEqual(self):
        self.assertLessEqual(fibo(4), 3)


if __name__ == '__main__':
  unittest.main()