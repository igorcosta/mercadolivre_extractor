Mercadolivre Extractor de Listas
----------------

Algumas vezes você precisa extrair seus produtos dos eShops do Mercadolivre e para isso, ou você
usa o Scrapy ou cria um App no portal de desenvolvedores ou você faz isso de forma mais rápida e sem 
fazer nada disso.

Projeto é simples, pode ser melhorado como por exemplo, colocar Threads para vasculhar as paginações e tal
Só que ai, enfeitar isso, eu já mudaria para o Scrapy, se você quer fazer isso, faz um pull request ai.

Exportar para SQL

Um dos problemas que eu tinha era gerar um SQL insert para isso, ter que criar outro parse ou implementação e importar
em algum banco; Se você usa algum NoSQL, nem precisa disso ou até mesmo Hadoop, o json já funciona perfeitamente

Por quê?

Bom, existe muitos lojistas que estão partindo para lojas próprias ou marketplaces e muitos deles tem dezenas de centenas de itens
que estão lá e querem de alguma forma inserir rapidamente no site deles. Esse script é para esse tipo de pessoa, automatizar tarefas
do dia-a-dia facilmente e sem esforço.

Python


## Como instalar:

  1. Clone o projeto
  2. Instale os requisitos pip install -r requirements.txt
  3. Use as funções exportJSON() ou exportSQL()

## Como executar:

 ```yaml
    	python mercadolivre_extractor.py
 ```
## Suporte?

Adoraria! Só que não vou conseguir. Quer mudar o script? Você está no site certo.

Use com sabedoria, compartilhe conhecimento!

## Licença MIT

 Copyright (c) 2015 Igor Costa (igorcostaARROBAgmail.com)

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.

