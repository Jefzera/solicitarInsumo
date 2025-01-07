# solicitarInsumo
Calculadora de Duração de Ração para Aviário
Este aplicativo foi desenvolvido para calcular o tempo que a ração restante vai durar no aviário, ajudando a planejar o fornecimento de ração com base no número de aves, no sexo das aves e na quantidade de ração restante. Ele também fornece recomendações sobre quando solicitar mais ração para evitar que acabe inesperadamente.

Funcionalidades
Entrada de Dados:

Quantidade restante de ração (em quilogramas).
Número de aves no lote.
Sexo das aves (Macho, Fêmea ou Misto).
Cálculos:

O aplicativo converte a quantidade de ração de quilogramas para gramas.
O consumo diário é calculado considerando:
Macho: Consome 220 gramas por dia.
Fêmea: Consome 200 gramas por dia.
Misto: Consome 220 gramas por dia.
O tempo que a ração vai durar é calculado e exibido em dias e horas.
Recomendações:

Se a ração durar menos de 2 dias, o app recomenda:
"URGENTE: Peça ração agora, pois a ração durará menos de 2 dias!"
Se a ração durar 3 dias ou menos, ele sugere:
"Peça ração quando tiver apenas 3 dias restantes."
Como Usar
Instale o Python (caso não tenha instalado).
Baixe o código ou clone o repositório.
Execute o script Python na sua IDE ou terminal.
Insira os dados:
Quantidade restante de ração (em quilogramas).
Número de aves.
Sexo das aves (Macho, Fêmea ou Misto).
O aplicativo calculará a quantidade de dias e horas restantes para a ração e exibirá uma recomendação.
Exemplo de Uso
Entrada:
Quantidade restante de ração: 1 kg
Número de aves: 5
Sexo das aves: Macho (M)
Saída:
Quantidade Restante: 1 kg (1000 gramas)
Número de Aves: 5
Sexo: Macho
Consumo Diário Total: 1100 gramas
A ração durará: Menos de 1 dia.
Mensagem: "URGENTE: Peça ração agora, pois a ração durará menos de 2 dias!"
Tecnologias Usadas
Python
Tkinter (para interface gráfica)
