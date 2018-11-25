def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(10))

memo = {0:0,1:1}
def fibom(n):
    if n not in memo:
        memo[n] = fibom(n-1) + fibom(n-2)

    return memo[n]

print(fibom(10))

class Fiboc:

    def __call__(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return self.__call__(n - 1) + self.__call__(n - 2)

fiboc = Fiboc()
print(fiboc(10))

class Fibocm:
    def __init__(self):
        self.memo = {0:0, 1:1}

    def __call__(self, n):
        if n not in self.memo:
            self.memo[n] = self.__call__(n-1) + self.__call__(n-2)
        
        return self.memo[n]

fibocm = Fibocm()
print(fibocm(100))

# multiples of 3
# 3, 3+3, 3+
def mult(n):
    if n == 1:
        return 3
    else:
        return n + mult(n-1)

def sum_n(n):
    if n== 0:
        return 0
    else:
        return n + sum_n(n-1)

def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line

print(pascal(6))



def pascal(n):
    if n == 1:
        return [1]
    else:
        p_line = pascal(n-1)
        line = [ p_line[i]+p_line[i+1] for i in range(len(p_line)-1)]
        line.insert(0,1)
        line.append(1)
    return line

print(pascal(6))


def fib_pascal(n,fib_pos):
    if n == 1:
        line = [1]
        fib_sum = 1 if fib_pos == 0 else 0
    else:
        line = [1]
        (previous_line, fib_sum) = fib_pascal(n-1, fib_pos+1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
        if fib_pos < len(line):
            fib_sum += line[fib_pos]
    return (line, fib_sum)

def fib(n):
    return fib_pascal(n,0)[1]

# and now printing out the first ten Fibonacci numbers:
for i in range(1,10):
    print(fib(i))


from math import sqrt

def sieve(n):
	# returns all primes between 2 and n	
	primes = list(range(2,n+1))
	max = sqrt(n)
	num = 2
	while num < max:
		i = num
		while i <= n:
			i += num
			if i in primes:
				primes.remove(i)
		for j in primes:
			if j > num:
				num = j
				break			
	return primes
	
print(sieve(100))


from math import sqrt

def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = [j for i in p for j in range(i*2, n + 1, i)]
        p = [x for x in range(2, n + 1) if x not in no_p]
        return p


print(primes(100))



memo = {0:0, 1:1}
def fib(n):
    if not n in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

def find_index(*x):
	""" finds the natural number i with fib(i) = n """
	if len(x) == 1:
		# started by user
		# find index starting from 0
		return find_index(x[0],0)
	else:
		n = fib(x[1])
		m = x[0]
		if  n > m:
			return -1
		elif n == m:
			return x[1]
		else:
			return find_index(m,x[1]+1)