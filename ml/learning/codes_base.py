from ml.classifier.retriever import embed
from db.scripts.operations_db import fill_law_base


def remove_headings(lst):
    new_lst = []
    for e in lst:
        if e and e.split()[0] not in ['Глава', '§', 'Раздел', 'Подраздел']:
            new_lst.append(e)

    return new_lst


civil = open('codes_RF/civil_code.txt', 'r', encoding='utf-8')

civil_lst = civil.read().split('\n\n')

civil.close()

new_civil_lst = remove_headings(civil_lst)
new_civil_lst = '\n\n'.join(new_civil_lst).split('Статья')

article_vectors = embed(new_civil_lst)
names = []
content = []
for article in new_civil_lst:
    tmp_article = article.split('\n')
    name, text = tmp_article[0], '\n'.join(tmp_article[1:])
    names.append('Статья' + name)
    content.append(text)
print(fill_law_base(names, content, article_vectors, 'Гражданский кодекс РФ'))


KoAP = open('codes_RF/KoAP_RF.txt', 'r', encoding='utf-8')

KoAP_lst = KoAP.read().split('\n\n')

KoAP.close()

new_KoAP_lst = remove_headings(KoAP_lst)
new_KoAP_lst = '\n\n'.join(new_KoAP_lst).split('Статья')
article_vectors = embed(new_KoAP_lst)
names = []
content = []
for article in new_KoAP_lst:
    tmp_article = article.split('\n')
    name, text = tmp_article[0], '\n'.join(tmp_article[1:])
    names.append('Статья' + name)
    content.append(text)
print(fill_law_base(names, content, article_vectors, 'Кодекс Российской Федерации об административных правонарушениях'))


labor = open('codes_RF/labor_code.txt', 'r', encoding='utf-8')

labor_lst = labor.read().split('\n\n')

labor.close()

new_labor_lst = remove_headings(labor_lst)
new_labor_lst = '\n\n'.join(new_labor_lst).split('Статья')
article_vectors = embed(new_labor_lst)
names = []
content = []
for article in new_labor_lst:
    tmp_article = article.split('\n')
    name, text = tmp_article[0], '\n'.join(tmp_article[1:])
    names.append('Статья' + name)
    content.append(text)
print(fill_law_base(names, content, article_vectors, 'Трудовой кодекс РФ'))


tax = open('codes_RF/tax_code.txt', 'r', encoding='utf-8')

tax_lst = tax.read().split('\n\n')

tax.close()

new_tax_lst = remove_headings(tax_lst)
new_tax_lst = '\n\n'.join(new_tax_lst).split('Статья')
article_vectors = embed(new_tax_lst)
names = []
content = []
for article in new_tax_lst:
    tmp_article = article.split('\n')
    name, text = tmp_article[0], '\n'.join(tmp_article[1:])
    names.append('Статья' + name)
    content.append(text)
print(fill_law_base(names, content, article_vectors, 'Налоговый кодекс РФ'))


personal = open('codes_RF/personal_data.txt', 'r', encoding='utf-8')

personal_lst = personal.read().split('\n\n')

personal.close()

new_personal_lst = remove_headings(personal_lst)
new_personal_lst = '\n\n'.join(new_personal_lst).split('Статья')
article_vectors = embed(new_personal_lst)
names = []
content = []
for article in new_personal_lst:
    tmp_article = article.split('\n')
    name, text = tmp_article[0], '\n'.join(tmp_article[1:])
    names.append('Статья' + name)
    content.append(text)
print(fill_law_base(names, content, article_vectors, 'О персональных данных'))
