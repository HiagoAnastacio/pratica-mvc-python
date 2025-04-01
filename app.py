# Este arquivo é o "Controller" da aplicação, onde as rotas são definidas e as interações com o modelo são realizadas.
from flask import Flask, redirect, render_template, request, url_for
from model.tarefa import Tarefa

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        titulo = request.form['titulo']
        data_conclusao = request.form['data_conclusao']
        tarefa = Tarefa(titulo=titulo, data_conclusao=data_conclusao)
        tarefa.salvarTarefa()
        return redirect(url_for('index'))

    tarefas = Tarefa.listarTarefas()
    return render_template('index.html', tarefas=tarefas, title='Minhas Tarefas')

@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
    Tarefa.apagarTarefa(idTarefa)
    return redirect(url_for('index'))


@app.route('/update/<int:idTarefa>', methods=['GET', 'POST'])
def update(idTarefa):
    if request.method =='GET': 
        tarefa = Tarefa.buscarTarefa(idTarefa)
        tarefas = Tarefa.listarTarefas()
        return render_template('index.html', tarefa=tarefa, title='Editar Tarefa')

    elif request.method == 'POST':
        idTarefa = request.form.get('idTarefa')
        titulo = request.form['titulo']
        data_conclusao = request.form['data_conclusao']
        tarefa = Tarefa(titulo=titulo, data_conclusao=data_conclusao, id=idTarefa)
        tarefa.atualizarTarefa()
        return redirect(url_for('index'))