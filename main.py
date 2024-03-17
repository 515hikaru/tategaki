def main():
    string = input()
    col = 3
    row = 10
    p = { i: [] for i in range(row)}
    for i, w in enumerate(string):
        p[i % row].append(w)
    l = len(p[0])
    for w in p.values():
        if len(w) < l:
            diff = l - len(w)
            w.append('　' * diff)
        print(' '.join(reversed(w)))

if __name__ == '__main__':
    main()
