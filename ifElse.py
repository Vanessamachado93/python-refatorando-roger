
velocidade = 60

if velocidade > 110:
    print('Acima da velocidade permitida')
    print('Favor reduzir a sua velocidade')
elif velocidade <= 60:
    print('Favor dirigir acima de 83km/h')
elif velocidade < 50:
    print('Favor dirigir acima de 80km/h')
else:
    print('Velocidade OK')