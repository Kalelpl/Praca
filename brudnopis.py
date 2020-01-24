Lista = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', 'h']

x = (len(Lista))
y = 0

# def rekur (Lista):
#     while y < x:
#         if y == x:
#             break
#         # print type(Lista[y])
#         if y == 0:
#             print Lista
#         elif isinstance(Lista[y], list):
#             lst = Lista[y]
#             rekur(lst)
#
#
# rekur(Lista)


def rekur(Lista):
    for iterator, i in enumerate(Lista):
        if iterator == 0 and Lista == globals()['Lista']:
            print Lista
        if isinstance(i, list):
            print i
            rekur(i)

rekur(Lista)
















