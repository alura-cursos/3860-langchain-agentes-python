![Capa do curso LangChain: desenvolva agente de inteligência artificial em Python](https://github.com/alura-cursos/3860-langchain-agentes-python/assets/3330769/baa2a716-78a4-4746-acb6-5714aced2612)


![](https://img.shields.io/github/license/alura-cursos/android-com-kotlin-personalizando-ui)

# Titulo do projeto

3860 - LangChain: desenvolva agentes de inteligência artificial

## 🔨 Funcionalidades do projeto

Neste projeto desenvolvemos um conjunto de assistentes que permitem auxiliar no processo de identificação de universidades para perfis específicos de estudantes. Para isso, implementamos uma solução em Python, utilizando LangChain e a LLM da OpenAI. Nesta abordagem, criamos um conjunto de agentes para (i) recuperar dados do usuário (ii) gerar um perfil do usuário e (iii) identificar universidades que combinam com este perfil. Além disso, implementamos um hub par agestão dos agentes e ferramentas criadas.

![](img/amostra.gif)

## ✔️ Técnicas e tecnologias utilizadas

As técnicas e tecnologias utilizadas pra isso são:

- Programação Orientada à Objetos em Python
- Uso de API GPT OpenAI
- Uso de cadeias, com LangChain
- Uso de agentes OpenAI
- Uso de Agentes ReAct
- Leitura de arquivos CSV e manipulação de dados


## 🛠️ Abrir e rodar o projeto

Após baixar o projeto, você pode abrir com Visual Studio Code. Em seguida, é necessário que você prepare seu ambiente. Para isso:

### venv no Windows:

```bash
python -m venv venv-langchain2
venv-langchain2\Scripts\activate
```

### venv no Mac/Linux:

```bash
python3 -m venv venv-langchain2
source venv-langchain2/bin/activate
```

Em seguida, instale os pacotes utilizando:

```bash
pip install -r requirements.txt
```

## 🔑 Gerar API_KEY e associar ao .env

```python
OPENAI_API_KEY = "SUA_CHAVE_AQUI"
```

