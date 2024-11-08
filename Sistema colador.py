def receber_arquivo_fonte():
    a = input("Digite o nome do arquivo que vai ser copiado: ")
    return a

def receber_arquivo_final():
    b = input("Digite o nome do arquivo que será gerado: ")
    return b

def abrir_arquivo_fonte(nome_arquivo):
    try:
        return open(nome_arquivo, 'r')
    except FileNotFoundError:
        print("Arquivo fonte não encontrado. Cancelando operação.")
        return None

def criar_arquivo_final(nome_arquivo):
    try:
        return open(nome_arquivo, 'x')
    except FileExistsError:
        print("Não pode ter outro arquivo com o mesmo nome do seu arquivo que você quer gerar. cancelando operação.")
        return None

def copiar_conteudo_arquivos(arquivo_fonte, arquivo_final):
    if arquivo_fonte and arquivo_final:
        while True:
            dados = arquivo_fonte.read()
            if not dados:
                break
            arquivo_final.write(dados)

def fechar_arquivos(arquivo_fonte, arquivo_final):
    if arquivo_fonte:
        arquivo_fonte.close()
    if arquivo_final:
        arquivo_final.close()


def main():
    
    arquivo_fonte = receber_arquivo_fonte()
    
    arquivo_final = receber_arquivo_final()

    arquivo_fonte = abrir_arquivo_fonte(arquivo_fonte)
    arquivo_final = criar_arquivo_final(arquivo_final)

    if arquivo_fonte is not None and arquivo_final is not None:
        copiar_conteudo_arquivos(arquivo_fonte, arquivo_final)
        fechar_arquivos(arquivo_fonte, arquivo_final)
        print("Seu arquivo foi copiado!")


main()
