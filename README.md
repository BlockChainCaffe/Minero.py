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

Posso aumentare il numero da 1 a 2 e vedere che ci mette molti più tentativi...

Successivamente aumento il numero, così da farmi un'idea di come funziona il processo di mining
