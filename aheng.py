qalin=['a','ı','o','u']

ince=['ə','i','e','ö','ü']

while True:
    soz=str(input('Soz daxil edin: '))

    qalinnetice=[]

    incenetice=[]

    for i in soz:

        if i in qalin:

            qalinnetice.append(i)

        if i in ince:

            incenetice.append(i)

    if len(qalinnetice) == 0:

        print('Sozde ince saitlerin ahengi gozlenilib.')


    if len(incenetice) == 0:

        print('Sozde qalin saitlerin ahengi gozlenilib.')

    if len(qalinnetice) != 0 and len(incenetice) != 0:

        print('Sozde aheng qanunu pozulub.')
