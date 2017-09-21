import sys
import hashlib

block="Qualsiasi testo"
nonce=0

zeron=int(sys.argv[1])
zeros='0'*zeron

while 1==1 :
    h = hashlib.sha256( hashlib.sha256( block+str(nonce) ).hexdigest()).hexdigest()
    print nonce, '\t',h
    head = h[:zeron]
    if (head == zeros):
        break
    nonce += 1;
