file = open('input.txt', 'r')
dna_seq = file.read()


answer = str(dna_seq.count('A')) + ' ' + str(dna_seq.count('C')) + ' ' + str(dna_seq.count('G')) + ' ' + str(dna_seq.count('T')) + ' '  # Count A,C,G,T and printing their count seperated with  a space

answer_file = open('answer.txt', 'w')
answer_file.write(answer)
