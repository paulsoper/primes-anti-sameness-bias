<p>This program explores the anti-samesness bias in the prime
numbers - i.e. the fact that for a prime number (base 10) that
ends in a 1, the next prime is less likely to end in a 1 than
in a 3, 7, or 9 - and the same thing for a prime that ends in a
3, or a 7 or a 9 - the successor is less likely to end in the
same digit.</p>

<p> The program uses a Miller-Rabin prime number generator,
which, with bases of [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
is a determinative test for primes less than
3,317,044,064,679,887,385,961,981. It is not the fastest test for
small primes, but lets one test the numbers in the range I am
using while being conservative with memory - no lists are necessary.</p>

<p>The reports are also included for the first 10^2, 10^3, 10^4, 10^5, 10^6,
10^7, and 10^8 primes.  The 10^8 prime report matches the table in
<a href=https://arxiv.org/pdf/1603.03720.pdf>this paper</a>.</p>








