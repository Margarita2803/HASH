from hash import HashTable

#тест метода resize
ht = HashTable(5)
for i in range(10):
    ht.insert(f"ключ {i}", i)

# Проверяем, что все элементы доступны
for i in range(10):
    print(f"ключ {i}: {ht.search(f'ключ {i}')}")

print(f"Текущий размер таблицы после изменения размера: {ht.size}")


