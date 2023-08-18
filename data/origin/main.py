
csv_path = './df_1_re.csv'

with open(csv_path, 'r', encoding='utf-8') as f:
    context = f.read().split('\n')

with open('train.csv', 'w', encoding='utf-8') as tr:
    print(context[0], file=tr)
    with open('valid.csv', 'w', encoding='utf-8') as v:
        print(context[0], file=v)
        with open('test.csv', 'w', encoding='utf-8') as ts:
            print(context[0], file=ts)
            for i in range(1, len(context)):
                if i % 10 == 0:
                    print(context[i], file=ts)
                elif i % 10 == 9:
                    print(context[i], file=v)
                else:
                    print(context[i], file=tr)
