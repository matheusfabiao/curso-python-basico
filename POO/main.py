from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('Rosa', 6, 'Ford', 10)
print(caminhao_rosa.cor, caminhao_rosa.rodas, caminhao_rosa.marca, caminhao_rosa.tanque)
caminhao_rosa.abastecer(10)
print(caminhao_rosa.tanque)

carro_azul = Carro('Azul',  'BMW', 30)
print(carro_azul.cor, carro_azul.rodas, carro_azul.marca, carro_azul.tanque)
carro_azul.abastecer(20)
print(carro_azul.tanque)
