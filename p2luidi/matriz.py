class Matriz():
    def __init__(self,n,m,v):
        referencial = 0
        self.mat = []
        if type(v) == list:
            for i in v:
                if type(i) != int:
                    raise ValueError
        else:
            raise ValueError
        if len(v) != m*n:
            raise ValueError
        for i in range(m):
            self.mat.append([])
            for j in range(n):
                self.mat[i].append(v[referencial+j])
            referencial += n
        self.n = len(self.mat)
        self.m = len(self.mat[0])
#     def __add__(self,other):
#         if len(self.mat) != len(other.mat) or len(self.mat[0]) != len(other.mat):
#             raise ValueError
#         copia = []
#         for i in range(len(self.mat)):
#             copia.append([])
#             for j in range(len(other.mat[0])):
#                 copia[i].append(0)
#         for i in range(len(self.mat)):
#             for j in range(len(self.mat[0])):
#                 copia[i][j] = self.mat[i][j] + other.mat[i][j]
#         return copia
#     def __sub__(self,other):
#         if len(self.mat) != len(other.mat) or len(self.mat[0]) != len(other.mat):
#             raise ValueError
#         copia = []
#         for i in range(len(self.mat)):
#             copia.append([])
#             for j in range(len(other.mat[0])):
#                 copia[i].append(0)
#         for i in range(len(self.mat)):
#             for j in range(len(self.mat[0])):
#                 copia[i][j] += self.mat[i][j] - other.mat[i][j]
#         return copia
#     def __mul__(self,other):
#         if len(self.mat[0]) != len(other.mat):
#             raise ValueError
#         copia = []
#         for i in range(len(self.mat)):
#             copia.append([])
#             for j in range(len(other.mat[0])):
#                 copia[i].append(0)
#         for i in range(len(self.mat)):
#             for j in range(len(other.mat[0])):
#                 for k in range(len(self.mat[0])):
#                     copia[i][j] += self.mat[i][k]*other.mat[k][j]
#         return copia
#     def __getitem__(self,key):
#         if type(key) != list or type(key) != tuple:
#             raise TypeError
#         i,j = key
#         return self.mat[i][j]
#     def __setitem__(self,key,x):
#         if type(key) != list or type(key) != tuple:
#             raise TypeError
#         i,j = key
#         self.mat[i][j] = x
#     def add_row(self,l):
#         self.mat.append(l)
#         self.n += 1
#     def add_col(self,c):
#         for i in range(len(self.mat)):
#             self.mat[i].append(c[i])
#         self.m += 1
#     def __repr__(self):
#         return str(self.mat)
#     def det(self):
#         if len(self.mat) == 1:
#             return self.mat[0][0]
#         elif len(self.mat) == 2:
#             return (self.mat[0][0]*self.mat[1][1]) - (self.mat[0][1]*self.mat[1][0])
#     def __linhas(self):
#         return self.n
#     def __col(self):
#         return self.m
# A = Matriz(2,2,[1,2,3,4])
# B = Matriz(2,2,[1,0,1,0])
# print(A)
# print(A+B)
# print(B-A)
# print(A*B)
# A.add_row([5,6])
# B.add_col([2,3])
# print(A,A.n,A.m)
# print(B,B.n,B.m)
#inputs
n = "(2,2,[1,2,3,4])+(2,2,[1,0,1,0])"
simbolo = n[n.index(")")+1]
salvaA = n[0:n.index(")")+1]
A = Matriz(*salvaA)
if simbolo == "+":
    pass

