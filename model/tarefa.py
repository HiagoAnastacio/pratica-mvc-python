#Este arquivo é o "Model" da aplicação, onde a lógica de negócio e as interações com o banco de dados são definidas.
from model.database import Database
 
class Tarefa:
    def __init__(self, titulo, id=None,  data_conclusao=None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao
 
    def salvarTarefa(self):
        """Salva uma nova tarefa no banco de dados."""
        db = Database()
        db.conectar()
 
        sql = 'INSERT INTO tarefa (titulo, data_conclusao) VALUES (%s, %s)'
        params = (self.titulo, self.data_conclusao)
        db.executar(sql, params)
        db.desconectar()
 
    @staticmethod # decorador
    def listarTarefas():
        """Retornar uma lista com todas as tarefas cadastradas."""
        db = Database()
        db.conectar()
 
        sql = 'SELECT id, titulo, data_conclusao FROM tarefa'
        tarefas = db.consultar(sql)
        db.desconectar()
        return tarefas if tarefas else []

    @staticmethod
    def apagarTarefa(idTarefa):
        """Apaga uma tarefa cadastrada no banco de dados."""
        db = Database()
        db.conectar()
 
        sql = 'DELETE FROM tarefa WHERE id = %s'
        params = (idTarefa,) # Precisa passar como tupla? (a, b, c, ...) SIM!
        db.executar(sql, params)
        db.desconectar()


    def buscarTarefa(idTarefa):
        """Busca a tarefa pelo id"""
        db = Database()
        db.conectar()

        sql = 'SELECT id, titulo, data_conclusao FROM tarefa WHERE id = %s'
        params = (idTarefa,)
        tarefa = db.consultar(sql, params)
        db.desconectar() 
        
        return tarefa[0] if tarefa else None

    def atualizarTarefa(self):
        """Edita uma tarefa no próprio formulário da página de cadastro"""
        db = Database()
        db.conectar()

        sql = 'UPDATE tarefa SET titulo = %s, data_conclusao = %s WHERE id = %s '
        params = (self.titulo, self.data_conclusao, self.id)
        db.executar(sql, params)
        db.desconectar()