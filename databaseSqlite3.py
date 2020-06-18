import sqlite3
class database:
    nomeTabela = "tabela-tcc"
    lista = [
        ["id", "INTEGER PRIMARY KEY AUTOINCREMENT"],
        ["nome", "TEXT NOT NULL"],
        ["idade", "INTEGER"],
        ["cpf", "TEXT"],
        ["fone", "TEXT"],
        ["cidade", "TEXT"],
        ["criado", "DATE NOT NULL"]
    ]
    
    criarTabela = ""
    inserirDados = ""
    lerDados = ""

    def __init__(self):
        pass
    

    def textCriarTabela(self):
        texto = "CREATE TABLE IF NOT EXISTS "
        texto += self.nomeTabela
        texto += ".db ("
        for data in self.lista:
            for d in data:
                # texto += " "
                texto += d
                texto += " "
            if data != self.lista[-1]:
                texto += " , "
        texto += ");"
        # print(texto)
        return texto

    def textInserirTabela(self):
        texto = "INSERT INTO " + self.nomeTabela + ".db ("
        for dados in self.lista:
            texto += dados[0]
            if dados != self.lista[-1]:
                texto += ", "
        texto += ") VALUES ("
        for i in range(0,len(self.lista)):
            texto += "?"
            if i != len(self.lista)-1 :
                texto+=","
        texto += ")"
        return texto

    def dbCriarTabela(self):
        try:
            conn = sqlite3.connect(self.nomeTabela+".db")
            cursor = conn.cursor()
            cursor.execute(self.textCriarTabela())
            print("Tabela Criado")

        except sqlite3.Error as error:
            print("Erro ocorrido:", error)

        finally:
            if (conn):
                conn.close()
                print("Desconectou Conexão com SQLite")

    def dbInserirDados(self,dados):
        try:
            conn = sqlite3.connect(self.nomeTabela+".db")
            cursor = conn.cursor()
            
            cursor.executemany(self.textInserirTabela(), dados)
            conn.commit()
            print("Dados Inseridos")

        except sqlite3.Error as error:
            print("Erro ocorrido:", error)

        finally:
            if (conn):
                conn.close()
                print("Desconectou Conexão com SQLite")
