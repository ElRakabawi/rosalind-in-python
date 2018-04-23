file = open('input.txt', 'r')
dna_seq = file.read()

rna_seq = dna_seq.replace('T', 'U')

answer_file = open('answer.txt', 'w')
answer_file.write(rna_seq)
