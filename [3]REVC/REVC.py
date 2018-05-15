file = open('input.txt', 'r')
dna_seq = file.read()

def rev_comp_dna(dna):
    comp_dna = dna.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g')
    comp_dna = comp_dna.upper()
    rev_dna = comp_dna[::-1]
    return rev_dna.strip()

answer_file = open('answer.txt', 'w')
answer_file.write(rev_comp_dna(dna_seq))
