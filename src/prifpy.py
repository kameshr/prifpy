# Copyright 2019 Kamesh Raghavendra
# All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# File: prfipy.py
# Description: Prime factorization of numbers

import sympy
import numpy

NUMCOLOR = "\033[1;90;40m"
PRIMECOLOR = "\033[1;94;40m"
POWERCOLOR = "\033[1;92;40m"
POWERSYM = "\033[1;33;40m"
LOSECOLOR = "\033[0m"
ERRORCOLOR = "\033[1;31;40m"

# Factorize the number passed and return a list of prime factors and powers
# The first item in the list will be the number itself with '-1' power
# Prime factors are loaded from the second item in the list onwards
def prifac(num):
	if not(isinstance(num, int)) or num < 1:
		return dict({-1: "[ERROR] Invalid number passed."})

	num = int(num)
	if num == 1:
		return dict({-1: 1, 1: 1})

	iterLimit = int(num)
	primeIter = int(2)
	primeFactors = dict()
	primeFactors[-1] = num

	if sympy.isprime(num):
		primeFactors[num] = 1
		return primeFactors

	while primeIter <= iterLimit:
		if num % primeIter == 0:
			power = int(1)
			while num % int(pow(primeIter, power)) == 0:
				power = power + 1
			primeFactors[primeIter] = power-1
			iterLimit = int(iterLimit/pow(primeIter, power-1))
		if sympy.isprime(iterLimit):
			primeFactors[iterLimit] = 1
			break
		primeIter = sympy.nextprime(primeIter)

	if len(primeFactors) == 1:
		primeFactors[num] = 1
	return primeFactors

# Print the prime factorization list to STDOUT in expanded form
# Colors used in the print are set in the beginning
def printprifac(primeFactors):
	if len(primeFactors) < 2:
		print(ERRORCOLOR + "[ERROR] Ill formed prime factor list.\n" + LOSECOLOR)

	if len(primeFactors) == 2 and primeFactors[-1] in primeFactors and primeFactors[-1] != int(1):
		print("[INFO] " + NUMCOLOR + str(primeFactors[-1]) + LOSECOLOR + " is a prime number.")
	
	first = False
	for prime, power in primeFactors.items():
		if prime == -1:
			print(NUMCOLOR + str(power) + LOSECOLOR + " = ", end = '', flush = True)
			first = True
		elif first:
			print(PRIMECOLOR + str(prime) + POWERSYM + "^" + POWERCOLOR + str(power) + LOSECOLOR, end = '', flush = True)
			first = False
		else:
			print(" * " + PRIMECOLOR + str(prime) + POWERSYM + "^" + POWERCOLOR + str(power) + LOSECOLOR, end = '', flush = True)
	print("\n")
	return

# Compute the lowest common multiple for a given array of numbers
# It takes an input argument of an array of positive integers > 1
# It returns an 'int' value of the LCM of the numbers in the input array
def lcm(numbers):
	pfarray = numpy.array([prifac(num) for num in numbers])
	lcm, lcmBuffer = dict(), dict()
	for pf in pfarray:
		lcmBuffer.update(pf)
		for prime, power in lcm.items():
			lcmBuffer[prime] = max(lcmBuffer[prime], power)
		lcm = lcmBuffer.copy()
	lcm[-1] = int(1)
	for prime, power in lcm.items():
		if prime > int(1):
			lcm[-1] = lcm[-1] * pow(prime, power)
	return lcm

# Compute the hishest common factor for a given array of numbers
# It takes an input argument of an array of positive integers > 1
# It returns an 'int' value of the HCF of the numbers in the input array
def hcf(numbers):
	pfarray = numpy.array([prifac(num) for num in numbers])
	hcf = dict()
	hvfPrimes = list()
	first = True
	for pf in pfarray:
		if first:
			hcf = pf.copy()
			hcfPrimes = list(hcf.keys())
			first = False
		else:
			for prime in hcfPrimes:
				if prime in pf.keys() and prime in hcf.keys():
					hcf[prime] = min(hcf[prime], pf[prime])
				elif prime not in pf.keys() and prime in hcf.keys():
					hcf.pop(prime)
	hcf[-1] = int(1)
	for prime, power in hcf.items():
		if prime > int(1):
			hcf[-1] = hcf[-1] * pow(prime, power)
	if len(hcf) == 1:
	  hcf[1] = int(1)
	return hcf
