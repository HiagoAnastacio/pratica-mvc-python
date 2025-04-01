#Este arquivo é o "Model" da aplicação, onde a lógica de negócio e as interações com o banco de dados são definidas.

from model.database import Database


class Tarefa:

    def __init__(self, titulo, id=None, data_conclusao=None):
        self.id = id
        self.titulo = titulo

        self.data_conclusao = data_conclusao


    def salvarTarefa(self):

        db = Database()
        db.conectar()

        sql = "insert into tarefa (titulo, data_conclusao) values (%s, %s)"

        params = (self.titulo, self.data_conclusao)

        db.executar(sql, params)
        db.desconectar()


    @staticmethod

    def listarTarefas():

        db = Database()
        db.conectar()

        sql = "select id, titulo, data_conclusao from tarefa"

        tarefas = db.consultar(sql)
        db.desconectar()

        return [Tarefa(titulo=info['titulo'], id=info['id'], data_conclusao=info['data_conclusao']) for info in tarefas] if tarefas else []


    @staticmethod

    def apagartarefa(idTarefa):

        db = Database()
        db.conectar()

        sql = "delete from tarefa where id = %s"

        params = (idTarefa,)

        db.executar(sql, params)
        db.desconectar()


    def atualizarTarefa(self):

        db = Database()
        db.conectar()

        if self.id:

            sql = "update tarefa set titulo = %s, data_conclusao = %s where id = %s"

            params = (self.titulo, self.data_conclusao, self.id)

            db.executar(sql, params)
        db.desconectar()



