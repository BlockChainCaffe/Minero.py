# Minero.py
Minero.py è un semplice programma in python che serve a dare una spiegazione semplificata del processo di mining di cryptovalute basato su PoW (proof of work).


# Links
Youtube:  https://www.youtube.com/c/BlockchainCaffe

Facebook: https://www.facebook.com/BlockchainCaffe/


# Python
Per accertarvi di avere python installato sulla vostra macchina usate il comando
```
python --version
```
Se ottenete come risposta una versione superiore alla 2.7 siete a posto. Se ottenete un errore dovete prima installare correttamente python

# Scaricare il programma

## Da web
Usate il pulsante verde sopra "Clone or Download"
## Con git
usate il comando 
```
git clone https://github.com/BlockChainCaffe/Minero.py.git
```

## Cut & Paste
Aprite il file minero.py e fate copia incolla delle poche righe in un editor locale e salvate

# Lanciare il programma e provare
Il programma simula il processo di mining, il cui scopo è trovare un numero "nonce" che aggiunto al blocco fa si che la HASH di [blocco+nonce] inizi con un certo numero di zeri.

Per avere un solo zero iniziale lancio il programma con:
```
python minero.py 1
```
Come output ottengo una lista di tentativi: l'incremento progressivo del nonce (prima colonna) e l'hash calcolata (seconda).

Esempio:

``` 
Nonce |  Hash
------------------------------------------------------------------------
0 	caf0227ddedd9cfa1c94b040b662b90d57b94975ee62b1d6ad4864e4979ab87d
1 	7db4b25cafb38bd23c477bfe7cc7e6da5f82cb27d0ed6d4f7518ad51cb91089f
2 	d40afca9419679080b4d048e230654d07cd22a350611490b50c4d0315d193edd
...
28 	d147f888e28f171bc7e1d827d309070695bed52509b219c1468c054cd4f48408
29 	58049ed61d152b3e6457403cc6ee59b2430c10726ebd5954817f8be3fcb7cb00
30 	06806a11e4471a3dfad62bff4a054c01ba0fb5ed591a4552aa02b75010530ec1
```


Posso aumentare il numero da 1 a 2 e vedere che ci mette molti più tentativi...

Successivamente aumento il numero, così da farmi un'idea di come funziona il processo di mining

# Risultati

|Zeri | Tentativi|
|-----|----------------|
|1 | 30|
|2 | 912|
|3 | 8.077|
|4 | 11.667|
|8 | ... si vabbeh, mi fermo a **7.000.000** che il concetto è chiaro|

Tenete presente che i blocchi, mediamente, **hanno 18/19 zeri** iniziali
