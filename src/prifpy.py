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

import math
import sympy

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
	if not(isinstance(num, int)) or num <= 1:
		return list([-1, "[ERROR] Invalid number passed."])

	num = int(num)
	iterLimit = int(num)
	primeIter = int(2)
	primeFactors = list()
	primeFactors.append([num, -1])

	while primeIter <= iterLimit:
		if num % primeIter == 0:
			power = int(1)
			while num % int(pow(primeIter, power)) == 0:
				power = power + 1
			primeFactors.append([primeIter, power-1])
			iterLimit = int(iterLimit/pow(primeIter, power-1))
		if sympy.isprime(iterLimit):
			primeFactors.append([iterLimit, 1])
			break
		primeIter = sympy.nextprime(primeIter)

	if len(primeFactors) == 1:
		primeFactors.append([num, int(1)])
	return primeFactors

# Print the prime factorization list to STDOUT in expanded form
# Colors used in the print are set in the beginning
def printprifac(primeFactors):
	if len(primeFactors) < 2:
		print(ERRORCOLOR + "[ERROR] Ill formed prime factor list.\n" + LOSECOLOR)

	if len(primeFactors) == 2:
		print("[INFO] " + NUMCOLOR + str(primeFactors[0][0]) + LOSECOLOR + " is a prime number.")
	
	print(NUMCOLOR + str(primeFactors[0][0]) + LOSECOLOR + " = " + PRIMECOLOR + str(primeFactors[1][0]) + POWERSYM + "^" + POWERCOLOR + str(primeFactors[1][1]) + LOSECOLOR, end = '', flush = True)

	printIter = 2
	while printIter < len(primeFactors):
		print(" + " + PRIMECOLOR + str(primeFactors[printIter][0]) + POWERSYM + "^" + POWERCOLOR + str(primeFactors[printIter][1]) + LOSECOLOR, end = '', flush = True)
		printIter = printIter + 1
	print("\n")
	return