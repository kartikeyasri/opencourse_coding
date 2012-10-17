def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''
    return len(dna)


def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''
    return len(dna1)>len(dna2)



def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    numbers=0
    for n in dna:
        if n==nucleotide:
            numbers+=1
    return numbers



def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''
    return dna2 in dna1 

def is_valid_sequence(dna):
    '''(str) -> bool

    Return True if and only if the DNA sequence is valid.

    >>>is_valid_sequence('ATDGDRTD')
    False
    >>>is_valid_sequence('AAATCGTTAC')
    True
    '''
    for n in dna:
        if n not in ['A','T','C','G']:
            return False
    return True

def insert_sequence(dna1,dna2,index):
    ''' (str,str,int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.

    >>>insert_sequence('CCGG','AT',2)
    CCATGG

    '''
    return dna1[:index]+dna2+dna1[index:]

def get_complement(n):
    ''' (str) -> str

    Return the complement of a nucleotide.

    >>>get_complement('A')
    T
    >>>get_complement('C')
    G

    '''
    if n=='A':
        return 'T'
    elif n=='T':
        return 'A'
    elif n=='C':
        return 'G'
    elif n=='G':
        return 'C'

def get_complementary_sequence(dna):
    ''' (str) -> str

    Return the complement of a given DNA sequence.

    >>>get_complementray_sequence('ATCGGACT')
    TAGCCTGA
    >>>get_complementray_sequence('GCACTCC')
    CGTGAGG
    '''
    com_seq=''
    for n in dna:
        com_seq+=get_complement(n)
    return com_seq

