girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letter_girls= {}
for g in girls:
    letter_girls.setdefault(g[0], []).append(g)
print([b+' & '+g for b in boys for g in letter_girls[b[0]]])
