## Recomendação de Vinhos

Este projeto foi desenvolvido como parte do [Curso de Sistema de Recomendação Inteligente](https://drive.google.com/file/d/17K87LtU9j7mQbs0Mdq08r84zq6Y0kNEk/view?usp=sharing) na Universidade Federal do Tocantins. Ele tem como objetivo criar um sistema de recomendação de vinhos personalizado usando o conjunto de dados XWines. O sistema utiliza técnicas de filtragem colaborativa e recomendação baseada em conteúdo para sugerir vinhos com base nas preferências do usuário.

O projeto se inspira no trabalho de [salimkilinc](https://github.com/salimkilinc), cujo código no GitHub serviu como referência para a implementação dos modelos de recomendação.

## Summary

- [Quais recomendação foram utilizadas?](#quais-recomendação-foram-utilizadas)
- [Tecnologias](#tecnologias)
- [How to Install](#how-to-install)

## Quais recomendação foram utilizadas?

**Collaborative Filtering:** Este modelo utiliza interações entre usuários e itens para recomendar vinhos com base nas preferências de usuários similares. Ao identificar padrões no comportamento dos usuários, pode-se gerar recomendações personalizadas para cada usuário.

**Content-based:** Em contraste com a filtragem colaborativa, este modelo foca nos atributos dos vinhos como variedade de uva, região e safra. Ao entender as características de cada vinho, podemos recomendar vinhos similares com base na similaridade de conteúdo.

## Tecnologias

* **Python:** uma linguagem de programação versátil amplamente utilizada em ciência de dados, desenvolvimento web e automação.
* **Numpy e Pandas:** usados para pré-processamento de dados, engenharia de recursos e manipulação de conjuntos de dados.
* **Jupyter Notebook e VSCode:** ambientes de desenvolvimento comumente usados para codificação em Python, com o Jupyter Notebook focando em análise de dados interativa e o VSCode sendo um editor de código de propósito geral.
* **Scikit-learn:** uma biblioteca para aprendizado de máquina, oferecendo uma variedade de algoritmos e ferramentas para análise de dados.
    * **TfidfVectorizer:** classe do sklearn que transforma texto em representações numéricas usando a técnica TF-IDF.
    * **linear_kernel:** função que calcula a similaridade linear entre dois conjuntos de dados.
    * **cosine_similarity:** função para calcular a similaridade entre vetores usando a medida cosseno.
    * **euclidean_distances:** função para calcular a distância euclidiana entre pontos em um espaço n-dimensional.

## Como posso testar?

1. Clona o repositório
```
git clone https://github.com/Anotherafael/STUDY_WineRecommendation.git
```
2. Instale o [Python](https://www.python.org/) ou copie o projeto para o ambiente do [Google Collab](https://colab.google/)
3. Instale as dependências
```
pip install -r requirements.txt
```
or
```
%pip install -r requirements.txt
```
4. Divirta-se! 😊