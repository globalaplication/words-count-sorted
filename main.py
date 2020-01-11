
liste = dict()

#paragrafı oku, kelimelere ayır.

paragraf = open("paragraf").read().split()

#kelimeleri say, sozluge ekle {"bilgisayar":5}

[liste.update({kelime:paragraf.count(kelime)}) for kelime in paragraf  if kelime.startswith("b") ]

#alfabetik liste

alfabetik = [alfabetik for alfabetik in sorted(liste.items())]

#çıktı

print (alfabetik)
