 
class code: 
    n = 0 
    k = 0 
    evals    = [] 
    G        = [] 
    H        = [] 
    messages = [] 

    def __init__(self, n: int, k: int):
        self.n = n
        self.k = k  

        # - let the evaluation points just be elements from Fq
        self.evals = [i for i in range(n)]  
        self.G     = self.genCode(k)  
        self.H     = self.genCode(n-k)
        self.genMessages([], k)

    def genCode(self, dim: int): 
        G = []  
        
        for i in range(dim):
            row = [0] * self.n

            for j, a in enumerate(self.evals):
                row[j] = (a ** i) % self.n 

            G.append(row)
        
        return G

    def encode(self, message: list):  
        # - obtain transpose of G to ease encoding
        gt = [[self.G[j][i] for j in range(len(self.G))] for i in range(len(self.G[0]))]
        codeword = [] 

        if len(message) != self.k: 
            print("Invalid message length")
            return 

        for row in gt: 
            elem = 0 

            for i in range(len(row)): 
                elem += (message[i] * row[i])
        
            codeword.append(elem % self.n)

        return codeword

    def check(self, codeword: list):  
        check_vector = [] 

        for row in self.H: 
            elem = 0 

            for i in range(self.n): 
                elem += row[i] * codeword[i]

            check_vector.append(elem % self.n) 

        return check_vector 

    def sum_vector(self, v: list): 
        s = 0 

        for e in v: 
            s += e 

        return s

    def genMessages(self, message: list, size: int): 
        if len(message) == size: 
            self.messages.append(message) 
        else: 
            for i in range(self.n): 
                self.genMessages(message + [i], size)

    def distance(self, c1: list, c2: list): 
        d = 0

        if len(c1) != len(c2) or c1 == c2: 
            return self.n + 1 # just return some invalid distance

        for i in range(len(c1)): 
            if c1[i] != c2[i]: 
                d += 1

        return d
