import mysql.connector

def abrir_conexao(host, usuario, senha, banco):
    return mysql.connector.connect(host= host, user= usuario, password= senha, database= banco);

def fechar_conexao(conexao):
    conexao.close();

def create(conexao, nome_monstro, fraquezas, neutro, forte):
    cursor= conexao.cursor();
    sql= "INSERT INTO monstros (nome_monstro, fraquezas, neutro, forte) VALUES (%s, %s, %s, %s)";
    valores= (nome_monstro, fraquezas, neutro, forte);
    cursor.execute(sql, valores);
    cursor.close();
    conexao.commit();

def ler(conexao, nome_monstro):
    cursor= conexao.cursor();
    sql= "SELECT * FROM monstros WHERE nome_monstro=%s";
    valores= (nome_monstro,);
    cursor.execute(sql, valores);
    for(id_monstro, nome_monstro, fraquezas, neutro, forte) in cursor:
        print(id_monstro, nome_monstro, fraquezas, neutro, forte)
    cursor.close();

def atualizar(conexao, nome_monstro, id_monstro):
    cursor= conexao.cursor();
    sql= "UPDATE monstros SET nome_monstro=%s where id_monstro=%s";
    valores= (nome_monstro, id_monstro);
    cursor.execute(sql, valores);
    cursor.close();
    conexao.commit();

def deletar(conexao, id_monstro):
    cursor= conexao.cursor();
    sql= "DELETE FROM monstros WHERE id_monstro=%s"
    valores= (id_monstro,);
    cursor.execute(sql, valores);
    cursor.close();
    conexao.commit();