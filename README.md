# PRIFPY: A Python module for computing the prime factorization of numers.
It has dependencies on [sympy](https://www.sympy.org/en/index.html) and [numpy](https://numpy.org/) libraries. Please install them using `pip` before using `prifpy`.

## Usage:
Add PRIFPY to your application with `import prifpy`.

**`prifpy`** offers the following functions based on prime factorization methods:
1. `prifpy.primefac`: Prime factorizes the number sent as an argument and returns a [Python dictionary](https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries) with prime factors as keys and respective powers as values.
This dictionary has the number that is factorized also stored in it as the value under a special key `-1`.

2. `prifpy.printprifac`: Print the above created dictionary of prime factors to `STDOUT` by passing the `dict` to it.

3. `prifpy.lcm`: Computes the LCM of an array of number passed as an argument and returns the prime factorized `dict` object of the LCM. The LCM value can be accessed by the special key `-1`.

4. `prifpy.hcf`: Computes the HCF of an array of number passed as an argument and returns the prime factorized `dict` object of the HCF. The HCF value can be accessed by the special key `-1`.
<br>

**`prifpy-cmd`** is a command line wrapper script for the module. Please run it to see its options.

### Copyright:
**(c) 2019 Kamesh Raghavendra.** All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License [here](http://www.apache.org/licenses/LICENSE-2.0).

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.
