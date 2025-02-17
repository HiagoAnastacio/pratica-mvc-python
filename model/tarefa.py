from ast import Param
from database import Database

class Tarefa:
    def __init__(self, id, titulo, data_conclusao):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao

    def salvarTarefa(self):
        """Esse método salva uma nova tarefa no banco de dados."""
        db = Database()
        db.conectar()
        sql = "insert into tarefa (titulo, data_conclusao) values (%s, %s)"
        params = (self.titulo, self.data_conclusao)
        db.executar(sql, params)
        db.desconectar()

    def listar_tarefas():
        """Esse método retorna uma lista com todas as tarefas cadastradas?!"""
        db = Database()
        db.conectar()
        sql = "select id, titulo, data_conclusao from tarefa"
        tarefas = db.consultar(sql)
        db.desconectar()
        return tarefas if tarefas else []
    
    def apagarTarefa(self):
        """Apaga uma tarega cadastrada no banco de dados."""
        db = Database()
        db.conectar()
        sql = "delete from tarefa where id = %s"
        params = (self.id,)
        db.executar(sql, params)
        db.desconectar()
    
    def atualizarTarefa(self):
        db = Database()
        db.conectar()
        sql = "update tarefa set titulo = 'nao sei o que', data_conclusao = 2024-08-04 where id = 1"
        params = (self.id, self.titulo, self.data_conclusao)
        db.executar(sql, params)
        db.desconectar()

tarefa = Tarefa(2, 'Teste de tarefa', None)
tarefa.apagarTarefa()