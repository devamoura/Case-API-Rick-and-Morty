# Case API - Rick and Morty

Conforme solicitado, neste repositório está o script que realiza a requisição REST através da API do Rick and Morty e retorna um arquivo CSV contendo os dados de 50 personagens.

## Sobre o Desenvolvimento

Escrevi esse código pensando em deixá-lo o mais reutilizável possível. Separei as funções de requisição (`request_data`) e de exportação do arquivo (`export_csv`) para que, caso seja necessário no futuro, eu possa reaproveitar essas mesmas funções em outros casos ou contextos sem precisar desenvolver tudo do zero.

Além disso, fiz questão de armazenar informações como a URL, o nome do arquivo final e as colunas desejadas em variáveis separadas dentro do fluxo principal, deixando o código limpo e fácil de manter caso as regras mudem.

Durante o desenvolvimento, identifiquei que a API muda o contrato de resposta conforme a quantidade de personagens retornados: ao buscar vários personagens ela devolve uma lista de objetos, mas ao buscar apenas 1, devolve um dicionário direto. Para blindar a aplicação contra esse comportamento, adicionei a validação com `isinstance` para garantir que o dado seja sempre tratado como uma lista padronizada, evitando que o sistema quebre.

## Estrutura do Projeto
```
├── export_data_from_api_to_csv.py       # Script principal
├── README.md                             # Documentação do projeto
├── requirements.txt                      # Dependências
├── postman_print.png                     # Print do teste da API no Postman
```

## Exemplo de Saída (CSV)

```
id;name;status;species;type;gender
1;Rick Sanchez;Alive;Human;;Male
2;Morty Smith;Alive;Human;;Male
```

## Como Executar o Projeto

Clone o repositório:
```bash
git clone https://github.com/devamoura/Case-API-Rick-and-Morty.git
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

Execute o script principal:
```bash
python export_data_from_api_to_csv.py
```
