

string = """bir internet sitesinin ihtiyaçlarını karşılamak bu isteyen hosting firmalarının olması ve bu firmaların, isteklerinize en doğru cevapları veriyor olmaları nedeni ile sizlerde siteleriniz için en iyi sunuculardan yerinizi alabilir"""

liste = dict()

[liste.update({kelime:string.count(kelime)}) for kelime in string.split()]

test = [test for test in sorted(liste.items(), key = lambda x : x[1], reverse=True)]

#print( help( sorted(liste.items()) ))

print(liste.items())
