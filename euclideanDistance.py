##iki noktanın oklit mesafesini hesaplayan fonksiyon
def euclideanDistance(m1,m2):
    oklid = 0
    
    for points in range(len(m1)):
        oklid += (m1[points]- m2[points])*(m1[points]- m2[points])
    oklid **= (1/2)
    return oklid

##verilerin hazırlandığı ve oklitMesafesi fonksiyonunun çağrıldığı yer 
matris = [-1, 2, 1]#matris=[x1,y1,z1] üç boyutlu bir nokta demektir.
matris1 = [-1, 4, 6]
sonuc = euclideanDistance(matris,matris1)
print(sonuc)