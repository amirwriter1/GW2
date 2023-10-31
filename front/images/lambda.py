def kir(item: str):
    return item.upper()

result = list(map(kir, ['ali', 'sara', 'mmd']))
print(result)

result = list(map(lambda i: i.upper(), ['ali', 'sara', 'mmd']))
print(result)
