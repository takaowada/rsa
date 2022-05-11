'''
Base program by Python
https://qiita.com/QUANON/items/e7b181dd08f2f0b4fdbe
'''
from math import gcd
from sympy import prime

def lcm(p, q):
  '''
  Find the least common multiple.
  '''
  return (p * q) // gcd(p, q)


def generate_keys(p, q):
  '''
  Generate a private and public key from two given prime numbers p and q.
  '''
  N = p * q
  L = lcm(p - 1, q - 1)

  for i in range(2, L):
    if gcd(i, L) == 1:
      E = i
      break

  for i in range(2, L):
    if (E * i) % L == 1:
      D = i
      break

  return (E, N), (D, N)


def encrypt(plain_text, public_key):
  '''
  Encrypt plain_text using public_key.
  '''
  E, N = public_key
  plain_integers = [ord(char) for char in plain_text]
  encrypted_integers = [pow(i, E, N) for i in plain_integers]
  encrypted_text = ''.join(chr(i) for i in encrypted_integers)

  return encrypted_text


def decrypt(encrypted_text, private_key):
  '''
  Decrypt encrypted_text using private_key.
  '''
  D, N = private_key
  encrypted_integers = [ord(char) for char in encrypted_text]
  decrypted_intergers = [pow(i, D, N) for i in encrypted_integers]
  decrypted_text = ''.join(chr(i) for i in decrypted_intergers)

  return decrypted_text


def sanitize(encrypted_text):
  '''
  Avoid for UnicodeEncodeError.
  '''
  return encrypted_text.encode('utf-8', 'replace').decode('utf-8')


if __name__ == '__main__':
  p = 101 # prime(10**6)
  q = 3259 # prime(10**6+1)
  print('p:', p, 'q:', q)

  public_key, private_key = generate_keys(p, q)

  # public_key, private_key = generate_keys(101, 3259)

  plain_text = 'Welcome to RSA!'
  encrypted_text = encrypt(plain_text, public_key)
  decrypted_text = decrypt(encrypted_text, private_key)

  print(f'''
Public key: {public_key}
Private key: {private_key}

Plane text:
"{plain_text}"

Encrypted text:
"{sanitize(encrypted_text)}"

Decrypted text:
"{decrypted_text}"
'''[1:-1])