seq="AAAAAAA"
seq1="AAAAAAA"
def score(seq,seq1): #definisco una funzione per due stringhe
    s=0 #inizializzo lo score
    for base in range(len(seq)): #inizio un ciclo che mi itera tutti gli elementi della stringa
        if seq[base]==seq1[base]: #condizione
            s+=1 #incremento lo score di 1
        else:
            s=s-1 #diminuisco lo score di 1
    return(s)
print(score(seq,seq1))
