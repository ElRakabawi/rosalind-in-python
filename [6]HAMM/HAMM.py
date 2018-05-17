file = open('input.txt', 'r')
file_data = file.readlines()

seq_one = file_data[0]
seq_two = file_data[1]


def hamming_dist(u, v):
    cnt = 0
    for base in range(len(v)):
        if u[base] is not v[base]:
            cnt += 1
    return cnt


answer_file = open('answer.txt', 'w')
answer_file.write(str(hamming_dist(seq_one, seq_two)))
