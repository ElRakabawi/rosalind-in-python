import sys
file = open('input.txt', 'r')

n_and_k = file.read()
num_n = int(n_and_k[0]+n_and_k[1])  # 33
num_k = int(n_and_k[3])             # 4


def rec_rel(n, k):
    if n < 2:
        return n
    else:
        return rec_rel(n-1, k) + k*rec_rel(n-2, k)


answer_file = open('answer.txt', 'w')
answer_file.write(str(rec_rel(num_n, num_k)))
