import random

pairs = []
children = []
count_lower = 0
count_upper = 0

# _________________________10th element
a = ('''
Аа аа аа Аа аа аа Аа Аа Аа Аа Аа Аа аа аа аа аа аа аа Аа аа Аа Аа Аа аа аа аа Аа аА аА аа аА Аа Аа аА аА аа АА аА АА аа аА Аа аА АА Аа Аа АА АА АА аА аа аА аА аа аА аа аА АА аа Аа аА АА аА АА АА АА аА аа аА аА АА АА АА АА АА АА Аа АА аА АА АА Аа аа Аа аа АА аа АА аа аа аА аа Аа АА Аа аа аА АА АА аА
''').split()

print(a)

for _ in range(len(a) // 2):
    b, c = random.sample(a, 2)
    pairs.append([b, c])

    a.remove(b)
    a.remove(c)

print(pairs)

for i in range(len(pairs)):
    gametes = [pairs[i][0][0], pairs[i][0][1], pairs[i][1][0], pairs[i][1][1]]
    for _ in range(10):
        children.append(random.sample(gametes, 1) + random.sample(gametes, 1))

print(children)

for i in range(len(children)):
    for j in range(2):
        cube = random.randint(1, 6)
        if cube == 6:
            if children[i][j] == 'А':
                children[i][j] = 'а'
                count_lower += 1
            else:
                children[i][j] = 'А'
                count_upper += 1
    children[i] = children[i][0] + children[i][1]

print(children)

AA = children.count('АА')
aA = children.count('Аа') + children.count('аА')
aa = children.count('аа')
print(AA, aA, aa)

cube = random.randint(1, 6)
print(cube)
if cube == 2:
    samples = random.sample(children, round(len(children) * 0.1))
    for x in samples:
        children.remove(x)
elif cube == 5:
    samples = random.sample(children, round(len(children) * 0.4))
    for x in samples:
        children.remove(x)

AA = children.count('АА')
aA = children.count('Аа') + children.count('аА')
aa = children.count('аа')
print(AA, aA, aa)

cube = random.randint(1, 6)
print(cube)
if not cube % 2:
    samples = random.sample(children, round(len(children) * 0.25))
    for x in samples:
        children.remove(x)

AA = children.count('АА')
aA = children.count('Аа') + children.count('аА')
aa = children.count('аа')
print(AA, aA, aa)

cube = random.randint(1, 6)
print(cube)
if cube == 1:
    samples = random.sample(children, round(len(children) * 0.5))
    for x in samples:
        children.remove(x)

AA = children.count('АА')
aA = children.count('Аа') + children.count('аА')
aa = children.count('аа')
print(AA, aA, aa)

if len(children) > 100:
    reserved = random.sample(children, len(children) - 100)
    for r in reserved:
        children.remove(r)

print(len(children))
print(*children)
print(count_lower, count_upper)
