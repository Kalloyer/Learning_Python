# Dentro do módulo dado crie a função leiaDinheiro que seja capaz de funcionar como input mas com a validação dos dados
from UtilidadesCeV import Moeda
from UtilidadesCeV import Dado

p = Dado.leiDinheiro("Digite o preço R$ ")
Moeda.resumo(p, 80, 20)
