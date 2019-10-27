# PRIFPY: A Python module for computing the prime factorization of numers.
It has dependency on [sympy](https://www.sympy.org/en/index.html) library. Please install sympy before using prifpy.
```pip3 install sympy```

## Usage:
Add PRIFPY to your application with `import prifpy`.
Use function `prifpy.prifac` to pass on the number to be prime factorized as an argument
`prifpy.prifac` returns a [Python dictionary](https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries) with prime factors as keys and respective powers as values.
This dictionary has the number that is factorized also stored in it as the value under a special key `-1`
Use function `prifpy.printprifac` to print the above dictionary of prime factors to `STDOUT`

## Copyright 2019 Kamesh Raghavendra
All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License [here](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.
