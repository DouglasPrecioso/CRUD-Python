from conexao import abrir_conexao, fechar_conexao, create, ler, atualizar, deletar

def main():
    conexao = abrir_conexao("localhost", "root", "", "crudtibia");

    # create(conexao, "Ferumbras", "Nenhuma", "Nenhuma", "Nenhuma");
    # atualizar(conexao, "Grand Master Oberon", 6);
    # deletar(conexao, 6);
    ler(conexao, "Behemoth");
  
    fechar_conexao(conexao);

if __name__ == "__main__":
    main()
