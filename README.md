# MyStatusCare
Projeto com o objetivo de cuidar de uma pessoa com covid-19.

Funcionalidades
 - Gerenciamento perfil de usuário com as seguinte informações: nome, email, endereço, idade e cidade.
 - Sistema de pontuação: Criamos uma pontuação com base nos sintomas indicados pela tabela de sintomas, onde o sistema percebe quando a situação está grave e já recomenda a pessoa ir para o hospital.
 - Gerenciamento de sintoma: O usuário pode adicionar sintomas de acordo com a data, e então o sistema de pontuação é alterado de acordo com a gravidade do sintoma em questão.
 - Lista de hospitais: Fizemos uma lista de hospitais com base na lista do Ministério da Saúde, de hospitais que estão atendendo pessoas com o covid-19.
 - Registro de temperatura: há uma tabela para criação de um registro da temperatura corporal, que no Dashboard plota um gráfico com o histórico de temperatura.
 - Dashboard: Onde há um resumo sobre a situação do paciente registrado, aparecendo o histórico de temperatura, e a classificação de risco.
 
 Funcionalidades a se implementar:
 - Gerenciamento de localização: puxar o histórico de onde a pessoa esteve nos ultimos 15 dias depois que ela sentiu o primeiro sintoma, e depois fazer um mapeamento de foco onde as pessoas que contrairam a doença andaram.
 - Melhorar sistema de pontuação.
 - Implementar intensidade dos sintomas para uma pontuação mais precisa.
 - Melhorar segurança do usuário.
 - Gerar relatório em pdf sobre o paciente.
 
 Sobre o sistema:
 - Front end: O projeto visual foi feito em cima de uma ferramenta chamada Bootstrap Studio, depois foi implementado as requisições via AXIOS, onde foi feita toda conexao front-back-banco. Algumas funcionalidades a mais foram feitas com JavaScript Puro.
 - Back end: A ideia foi fazer uma API em python com a biblioteca flask, onde todos os selects, inserts foram feitos e o sistema de pontuação também.
 - Banco de dados: A escolha foi fazer em MySQL para uma seguridade e efetividade melhor, o sistema inteiro foi modelado a partir do esquema criado com o banco de dados, onde populamos cidades, estados, hospitais e sintomas.

Participantes e funções:
Felipe Queiroz - Front-end
Gabriel Rocha - API/Back-end
Felipe da Silva e Alex Moreira - Banco de dados.
