﻿📦 Automação de Cadastros em Python
Automatiza o cadastro de produtos (bolsas de luxo) em um sistema web, usando Python com PyAutoGUI e Pandas.

⚙️ Funcionalidades
Abertura automática do navegador e login no sistema
Preenchimento automático de campos (e-mail, senha e formulário de cadastro)
Leitura de dados de um arquivo .csv
Cadastro em loop de todos os produtos
Scroll automático após cada cadastro

📄 Formato do CSV
O arquivo deve estar codificado em Windows-1252 e conter as colunas:
Copiar
Editar
Codigo; Marca; Tipo; Categoria; Preco_unitario; Custo;Obs

⚠️ Certifique-se de que os nomes das colunas estejam exatamente como acima, sem espaços extras ou alterações.

🚀 Como Funciona
Abre o navegador com webbrowser.open()
Realiza login automático com pyautogui.write() e click()
Lê os dados do CSV com pandas.read_csv()
Preenche o formulário e cadastra os produtos em loop
Realiza scroll na página para exibir os registros após o envio

🧰 Tecnologias Utilizadas
Python 3
PyAutoGUI
Pandas
