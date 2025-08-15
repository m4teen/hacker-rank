# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def camelCaseConverter(operations):
    h = None
    stuff = []

    for i in range(len(operations)):
        if operations[i][0] == "S":
            if operations[i][2] ==  'V':
                x = operations[i][4:]
                y = [i for i,val in enumerate(x) if val.isupper()]
                words = []
                for j in y:
                    words.append(x[:j])
                    words.append(x[j:])
                words = [w.lower() for w in words]
                h = ' '.join(words)
                stuff.append(h)
            
            if operations[i][2] ==  'M':
                x = operations[i][4:-2]
                y = [i for i,val in enumerate(x) if val.isupper()]
                words = []
                for j in y:
                    words.append(x[:j])
                    words.append(x[j:])
                words = [w.lower() for w in words]
                h = ' '.join(words)
                stuff.append(h)
                
            if operations[i][2] == 'C':
                x = operations[i][4:]
                y = [i for i,val in enumerate(x) if val.isupper()]
                words = [x[0:y[1]],x[y[1]:]]

                words = [w.lower() for w in words]
                h = ' '.join(words)
                stuff.append(h)


        if operations[i][0] == "C":
            if operations[i][2] == 'V':
                x = operations[i][4:]
                parts = x.split()  
                w = parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])
                stuff.append(w)

            if operations[i][2] == 'M':
                x = operations[i][4:]
                parts = x.split()
                w = parts[0].lower() + ''.join(word.capitalize() for word in parts[1:]) + '()'
                stuff.append(w)

            if operations[i][2] == 'C':
                x = operations[i][4:]
                parts = x.split()
                w = ''.join(word.capitalize() for word in parts)
                stuff.append(w)
    for item in stuff:
        sys.stdout.write(item + "\n")

                

camelCaseConverter(list(["S;M;plasticCup()", "C;V;mobile phone", "C;C;coffee machine"]))

