# Set
# Unordered Data type
# Mutable

# you 'CANNOT' define empty set using literals
emptySet = set()

sampleSet = {1,'A', 'g', 3.86, 'Dayche', 'A', 'A'}

# for _ in range(10):
#     print(sampleSet)

print(sampleSet)

print('=' * 40)

odd = set(range(1, 50, 2))           # members: 25
power = {1, 4, 9, 16, 25, 36, 49}    # members: 7

print(len(odd))
print(odd.intersection(power))  # Eshterak

print(odd.union(power))
print(len(odd.union(power)))

print(odd.intersection_update(power))
print(odd)

print('=' * 40)

power_frozen = frozenset(power)
