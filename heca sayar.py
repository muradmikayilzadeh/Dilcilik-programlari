saitler=['a','e','ə','ı','i','o','ö','u','ü','A','E','Ə','I','İ','O','Ö','U','Ü']


while True:
    soz=str(input('Sozu daxil edin: '))

    sozlist=list(soz)


    hecasayi=0

    for i in sozlist:
    
        if i in saitler:
            hecasayi=hecasayi+1
    

    print('Daxil etdiyiniz sozde ', hecasayi,' heca var')
