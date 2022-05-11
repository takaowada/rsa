Tamura et al.’s Technique

Similar to modified Khayat’s technique, the modification of
Tamura et al.’s technique also uses modular exponentiation
based on RSA cryptosystem. It considers two large primes Q1
and Q2 which are publicly known to all. The technique also
consists of four phases: (1) Setup, (2) Encryption, (3)
Decryption, and (4) Verification. Their roles are described
below.

Setup: A participant Cj has a secret encryption and
decryption key pair {Lj, Zj} though it is discretionary for this
modified technique. Each authority Ai also has two sets of
encryption and decryption key pairs: {Ki, Fi} for encryption
on modulo Q1 arithmetic and {Hi, Gi} for decryption on
modulo Q2 arithmetic. Similar to Khayat’s technique, the key
pairs are kept as Ai's secrets in order to enable each Ai to
securely use his key pairs in an environment where multiple
authorities share the same modulo arithmetic. Hi and Ki are
disclosed only in multiplied form(H* and K*) with respected
encryption keys of other authorities i.e. H* = PI(i=0, P) Hi
and K* = PI(i=1, P) Ki, where P is total number of authorities. When key Ki
or Hi is disclosed, it is easy for anyone to calculate Ai’s
decryption key Fi from the relation KiFi (mod (Q1-1)) = KjFj
(mod (Q1-1)) or HiGi (mod (Q2-1)) = HjGj (mod (Q2-1))
respectively. Here for any two integers u and w, it satisfies the
relation uKiFi (mod Q1) = u (mod Q1), wHiGi (mod Q2) = w (mod
Q2) and wLjZj (mod Q2) = w (mod Q2).

Encryption: In this phase, the participant Cj generates a
secret random number rj and encrypts her message mj by
calculating E({K*, H*}, {mj, rj}) = {E(K*, mjrj) = (mjrj)K*
(mod Q1) and E(H*, rj) = (rj)H* (mod Q2)} i.e. the encrypted
form consists of a data part E(Ki, mjrj) and a randomization
part E(Hi, rj). Here authorities cannot calculate mj from mjrj
and rjLj, because rj is the secret of Cj and the calculation of rj
from rjLj is a discrete logarithm problem.

Decryption: In this phase, the ciphertext E({K*, H*}, {mj,
rj}) is re-decrypted by the authorities {A1,---,AP} into (mjrj, rj)
by calculating E(K*, mjrj)(F1,---,FP) = (mjrj) K*(F1,---,FP) (mod Q1) =
mjrj and E(H*, rj)(G1,---,GP) = rj
H*(G1,---,GP) (mod Q2) = rj using
their decryption keys F1,---,FP and G1,---,GP; and finally rj
is used to retrive m from mjrj

Verification: For the confirmation of correct re-encryption
of the authorities {A1,---,AP}, Cj asks them to decrypt E(K*,
(mjrj)Uj) and E(H*, rjVj), where {Uj, Vj} are secret random
numbers of Cj. Dishonest authorities fail to complete the
operation correctly as they do not know Uj, Vj, mjrj or rj.
Therefore, although Ki and Hi of each Ai are secret, Cj can
confirm the correctness of the operations. However, this phase
is optional for Cj. It is apparent that this re-encryption
technique is probabilistic and commutative.