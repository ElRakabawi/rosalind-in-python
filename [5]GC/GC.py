import sys

file = open('input.txt', 'r')
line = file.readline()
fasta_id = ''
seq = ''
gc_content = 0
cnt = 0
arr = []
gc_arr = []
linked_arr = []


while line:
    line = line.rstrip('\n')
    if '>' in line:
        fasta_id = line
        fasta_id = fasta_id[1:]
        if seq is not '':
            arr.append(seq)
        seq = ''
        arr.append(fasta_id)
    else:
        this_fasta = fasta_id
        seq += line

    line = file.readline()

if len(arr) % 2 is 1:
    arr.append(seq)

while cnt < len(arr):
    linked_arr.append([arr[cnt], arr[cnt+1]])
    cnt += 2

for i in range(len(arr)):
    if arr[i][:1] is not 'R':
        gc_content = ((arr[i].count('G') + arr[i].count('C')) / (arr[i].count('A') + arr[i].count('T') + arr[i].count('G') + arr[i].count('C'))) * 100  # (Gn + Cn)/Total * 100
        gc_arr.append(gc_content)

max_gc_index = gc_arr.index(max(gc_arr))
answer_data = linked_arr[max_gc_index][0] + "\n" + str(max(gc_arr));

answer_file = open('answer.txt', 'w')
answer_file.write(answer_data);
