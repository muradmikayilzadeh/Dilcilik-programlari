saitler=['a','e','ə','ı','i','o','ö','u','ü','A','E','Ə','I','İ','O','Ö','U','Ü']

while True:

    mesaj=str(input('Mesaji daxil edin: '))

    for i in mesaj:

        if i not in saitler:

            print(i,end='')



    print('\n')
            
