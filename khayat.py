from math import gcd
from sympy import prime

import math
import random

# Function to find gcd
# of two numbers
def euclid(m, n):
	
	if n == 0:
		return m
	else:
		r = m % n
		return euclid(n, r)
	
	
# Program to find
# Multiplicative inverse
def exteuclid(a, b):
	
	r1 = a
	r2 = b
	s1 = int(1)
	s2 = int(0)
	t1 = int(0)
	t2 = int(1)
	
	while r2 > 0:
		
		q = r1//r2
		r = r1-q * r2
		r1 = r2
		r2 = r
		s = s1-q * s2
		s1 = s2
		s2 = s
		t = t1-q * t2
		t1 = t2
		t2 = t
		
	if t1 < 0:
		t1 = t1 % a
		
	return (r1, t1)

# Find the least common multiple.
def lcm(p, q):
  return (p * q) // gcd(p, q)

#  Generate a private and public key from two given prime numbers p and q.
def generate_keys(p, q, r):
  N = p * q
  L = lcm(p - 1, q - 1)

  # encryption key E
  for i in range(2, L):
    if gcd(i, L) == 1:
      E = i
      break
  # decryption key D
  for i in range(2, L):
    if (E * i) % L == 1:
      D = i
      break

  return (D, E)

'''
Setup
'''
# Two large prime
Q = prime(10**3)
#Q = 823
print('Q:', Q)

p = Q
q = 953
n = p * q
Pn = (p-1)*(q-1)
print('Pn:', Pn)
# Generate encryption key
# in range 1<e<Pn
keys = []

for i in range(2, Pn):	
	gcd = euclid(Pn, i)	
	if gcd == 1:
		keys.append(i)

# print(keys)
# Number of Authorities
P = 2
print('P:', P)

# Participant L:encryption Z:decryption
L = keys[100]
r, d = exteuclid(Pn, L)
if r == 1:
	Z = int(d)
else:
	print("Multiplicative inverse for\
	the given encryption key does not \
	exist. Choose a different encryption key ")
print('L:', L, 'Z:', Z)

# Authorities
# Encryption keys on Modulo Q
K = list()
F = list()
for i in range(P):
  k = keys[101 + i]
  r, d = exteuclid(Pn, k)
  if r == 1:
    f = int(d)
  else:
    print("Multiplicative inverse for\
    the given encryption key does not \
    exist. Choose a different encryption key ")
  K.append(k)
  F.append(f)
  print('key: ', k, f)
print('K:', K, 'F:', F)

# K*
Ks = math.prod(K)
print( 'Ks:', Ks)

'''
Encryption by Participant
t0 = E(Lj, mj) = mj^Lj (mod Q)
'''
# The message to be sent
mj = 123
print('mj:', mj)

t0 = pow(mj, L, Q)
print('t0:', t0)

'''
Re-encryption by Authorities [0]
E(K*, t0) = (t0)^(K1,---,KP) (mod Q)
'''
reencrypted = t0
for i in range(P):
  reencrypted = pow(reencrypted, K[i], Q)
  print('reencrypted: ', reencrypted)

'''
Decryption by Participant
D(E(K*, t0)) = E(K*, mj) = (t0)^Zj (mod Q)
'''
decrypted = pow(reencrypted, Z, Q)
print('decrypted:', decrypted)

'''
Re-decryption by Authorities [0]
mj = D(E(K*, mj)) = E(K*, mj)^(F1,---,FP) (mod Q)
'''
redecrypted = decrypted
for i in range(P):
  redecrypted = pow(redecrypted, F[i], Q)
  print('redecrypted: ', redecrypted)

'''
Verification
E(K*, mj^Bj)
Bj = random.randint(2, 100)
e1 = pow(pow(mj, Bj), Ks)
print('e1: ', e1)
'''
