from hash_table import HashTable


if __name__ == '__main__':
    print(12 % 11)
    t1 = HashTable()
    t1[1] = 'qwe1'
    t1[2] = 'qwe2'
    t1[12] = 'qwe3'
    print(t1)
    print(t1[1])
    print(t1[12])
    del t1[1]
    print(t1)
    del[t1[11]]
    print()
