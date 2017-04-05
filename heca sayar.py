saitler=['a','e','ə','ı','i','o','ö','u','ü','A','E','Ə','I','İ','O','Ö','U','Ü']


while True:
    soz=str(input('Sozu daxil edin: '))

    hecasayi=0

    for i in soz:
    
        if i in saitler:
            hecasayi=hecasayi+1
    

    print('Daxil etdiyiniz sozde ', hecasayi,' heca var')
