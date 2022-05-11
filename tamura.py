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
Q1 = prime(200)
Q2 = prime(201)
#Q1 = 823
#Q2 = 953
print('Q1:', Q1, 'Q2:', Q2)

N = Q1 * Q2
#Pn = (p-1)*(q-1)
Pn = (Q1-1) * (Q2-1)
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
# Encryption keys on Modulo Q1
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

# Decryption keys on Modulo Q2
H = list()
G = list()
for i in range(P):
  h = keys[101 + P + i]
  r, d = exteuclid(Pn, h)
  if r == 1:
    g = int(d)
  else:
    print("Multiplicative inverse for\
    the given encryption key does not \
    exist. Choose a different encryption key ")
  H.append(h)
  G.append(g)
  print('key: ', h, g)
print('H:', H, 'G:', G)

# K*
Ks = math.prod(K)
# H*
Hs = math.prod(H)
print( 'Ks:', Ks, 'Hs:', Hs)

'''
Encryption by Participant
E(Lj, {mj, rj}) = {mjrj, rj^Lj (mod Q2)}
'''
# The message to be sent
mj = 123
print('mj:', mj)
# Generate random
rj = 7 #random.randint(2, 100)
print('rj:', rj)

mjrj = mj * rj
print('mjrj:', mjrj)
rjLj = pow(rj, L, Q2)
print('rjLj:', rjLj)
encrypted = (mjrj, rjLj)
print('encrypted', encrypted)

'''
Re-encryption by Authorities [0]
E({K*, H*}, {mj, rj^Lj})
 = {E(K*, mjrj) = (mjrj)^(K1,---,KP) (mod Q1)
  and
   E(H*, rj^Lj) = (rj^Lj)^(H1,---,HP) (mod Q2)}
'''
reencrypted = encrypted
for i in range(P):
  enc1 = pow(reencrypted[0], K[i], Q1)
  enc2 = pow(reencrypted[1], H[i], Q2)
  reencrypted = (enc1, enc2)
  print('reencrypted: ', reencrypted)

'''
Decryption by Participant
D(E(H*, rj^Lj))
 = E(H*, rj^Lj)^Zj
 = E(H*, rj) (mod Q2)
'''
enc1 = reencrypted[0]
dec2 = pow(reencrypted[1], Z, Q2)
decrypted = (enc1, dec2)
print('decrypted:', decrypted)

'''
Re-decryption by Authorities [0]
D(E({K*, H*}, {mj, rj}))
 = {E(K*, mjrj)(F1,---,FP) (mod Q1) = mjrj
  and
   E(H*, rj)(G1,---,GP) (mod Q2) = rj}
 = {mjrj, rj}
'''
redecrypted = decrypted
for i in range(P):
  mjrj2 = pow(redecrypted[0], F[i]) % Q1
  rj2 = pow(redecrypted[1], G[i]) % Q2
  redecrypted = (mjrj2, rj2)
  print('redecrypted: ', redecrypted)

mj2 = int(redecrypted[0] / redecrypted[1])
print('mj2: ', mj2)

'''
Verification
{E(K*, (mjrj)^Uj), E(H*, rj^Vj)}
Uj = random.randint(2, 100)
e1 = pow(mj * rj, Uj) % Q1
Vj = random.randint(2, 100)
e2 = pow(rj, Vj) % Q2
print('e1: ', e1)
print('e2: ', e2)

# Decryption: (mjrj)^Uj, rj^Vj
d1 = pow(e2, e1) % Q1
print('d1: ', d1)
'''
