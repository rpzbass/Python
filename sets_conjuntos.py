# Sets para efetuar operacoes de conjuntos
# Sets são coleções não ordenadas de valores unicos serve para armazenar multiplos itens dentro de um objeto
# Sets não possui valores duplicados se colocar o python ignora e não repete

planeta_anao = {'Plutao','Ceres','Eris','Haumea','Makemake'}

print(len(planeta_anao))

contem = 'Ceres' in planeta_anao

print(f'{contem}')

print('Plutao' not in planeta_anao)

for planeta in planeta_anao:
     print(f'{planeta.lower()}', end='|')    # se não quiser que pule linha  so utilizar o end


astro = ['Lua','Vênus','']

