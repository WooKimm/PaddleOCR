with open('train2.txt',encoding='utf-8') as reader, open('round1_train2.txt', 'w',encoding='utf-8') as writer1,open('test2.txt', 'w',encoding='utf-8') as writer:
    for index, line in enumerate(reader):
        if index % 10 == 0:
            writer.write(line)
        else:
            writer1.write(line)