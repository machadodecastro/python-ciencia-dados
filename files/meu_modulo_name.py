# Conteúdo do arquivo meu_modulo_name.py

def saudacao(nome):
    return f"Olá, {nome}!"

if __name__ == "__main__":
    # Este código é executado apenas quando o módulo é executado como um programa principal
    mensagem = saudacao("Bob")
    print(mensagem)
