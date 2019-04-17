import pickle
input("press enter to start \n")

#this geneitc code table was taken from https://www.biostars.org/p/2903/ , all other functions are written by me
gen_code_table = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}


def read():
    # the dna sequence exists in a  dna.txt file
    with open("dna.txt", "r") as reader:
        text =reader.read()
        text = text.replace('\n','')
    return text



def write(text):
    #output the resulted protein to file
    with open("result.txt", "w") as writer:
        writer.write(text)
    writer.close()


def inverse(dna):
    # A to T ,  C to G
    rna = ""
    for i in dna:
        if i == 'A' or i == 'a':
            rna += 'T'
        elif i == 'T' or i == 't':
            rna += 'A'
        elif i == 'C' or i == 'c':
            rna += 'G'
        elif i == 'G' or i == 'g':
            rna += 'C'
        else:
            raise Exception('wrong input')
    return rna


def t_to_u(rna):
    #thymine to uracil
    sequence = ''
    for i in rna:
        if i == 't' or i == 'T':
            sequence += 'U'
        else:
            sequence += i
    return sequence


def to_triplets(sequence):
    #divide sequence into triplets
    triplets = ''
    j= 1
    for i in sequence:
        triplets+= i
        if (j %3 == 0):
            triplets+=  ' '
        j+=1
    return  triplets


def translate(triplets,table):
    #translate triplets into codons
    last = ''
    codon = ''
    j=0
    for i in triplets[::3]:
        try:
            codon = ''
            codon += triplets[j]
            codon += triplets[j+1]
            codon += triplets[j+2]
            last+=table[codon]
            j=j+4
        except:
            pass
    return last


dna  = read()
rna = inverse(dna)
print(rna)
sequence = t_to_u(rna)
print(sequence)
triplets = to_triplets(sequence)
print(triplets)
last = translate(triplets,gen_code_table)
print(last)
write(last)
