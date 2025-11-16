from find_article import retrieve_law

a = retrieve_law('Как правильно оформить ИП или ООО?')

for e in a:
    print(e)
