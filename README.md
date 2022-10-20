# askGPT-3
Demo code for OpenAI GPT-3 bot

## Como utilizar?
1. Acesse o portal do [OpenAI](https://beta.openai.com/signup) e crie uma conta caso ainda não tenha.
2. Acesso o sandbox [OpenAI](https://beta.openai.com/sign) e copie sua [API Key](https://beta.openai.com/account/api-keys)
3. Exporte a variável OPENAI_API_KEY usando sua chave de API (não compartilhe sua chave com ninguém!)

```
export OPENAI_API_KEY='xxxxxxxxxx'
```

4. Clone o repositório
```
git clone https://github.com/srebrasil/askGPT-3.git
```
5. Acesse o novo diretório
```
cd askGPT-3
```
6. Assumindo que você já tem o python3 instado, crie um ambiente virtual:

```
python3 -m venv openai
````
7. Ative o seu ambiente virtual
```
source openai/bin/activate
```
8. Instale os modulos necessários
```
pip3 install -r requirements.txt
```
9. Execute o programa e faça sua pergunta como no exemplo abaixo:
```
python3 askGPT-3.py "What are the 5 most important skills of SREs?"
```
A saída será algo do tipo:

![imagem](/images/output.png)