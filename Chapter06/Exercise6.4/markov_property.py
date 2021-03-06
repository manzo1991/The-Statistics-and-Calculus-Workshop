
# Generate random letters from 4 states A B C D
import random
LEN_STR = 50
for i in range(LEN_STR):
    tokens.append(random.choice("ABCD"))
print(tokens)
LEN_TOKENS = len("ABCD")

# Finding the relative values with ordinal values of ASCII characters
ti = [(ord(t) - ord('A')) for t in tokens]
# print(T)
print(ti)

#create Matrix of zeros
m = [[0]*LEN_TOKENS for j in range(LEN_TOKENS)]
print(m)

# Building the frequency table(matrix) from the given data
for (i,j) in zip(ti,ti[1:]):
    m[i][j] += 1
print(zip(ti,ti[1:]))
print(m)

# Finding the Probabily
for state in m:
    total = sum(state)
    if total > 0:
        state[:] = [float(f)/sum(state) for f in state]

for state in m:
    print(state)
