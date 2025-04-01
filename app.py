# Este arquivo é o "Controller" da aplicação, onde as rotas são definidas e as interações com o modelo são realizadas.
from flask import Flask, render_template, request, redirect, url_for

from model.tarefa import Tarefa


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])

def index():

    if request.method == "POST":

        titulo = request.form["titulo"]

        data_conclusao = request.form["data_conclusao"]
        tarefa = Tarefa(titulo=titulo, data_conclusao=data_conclusao)

        tarefa.salvarTarefa()

        return redirect(url_for("index"))

    tarefas = Tarefa.listarTarefas()

    return render_template("index.html", tarefas=tarefas, title="Minhas Tarefas")


@app.route("/edit/<int:idTarefa>", methods=["GET", "POST"])

def edit(idTarefa):
    tarefas = Tarefa.listarTarefas()

    tarefa = next((info for info in tarefas if info.id == idTarefa), None)


    if not tarefa:

        return redirect(url_for("index"))


    if request.method == "POST":

        tarefa.titulo = request.form["titulo"]

        tarefa.data_conclusao = request.form["data_conclusao"]

        tarefa.atualizarTarefa()

        return redirect(url_for("index"))

    return render_template("index.html", tarefa=tarefa, tarefas=tarefas, title="Editar Tarefa")


@app.route("/delete/<int:idTarefa>")

def delete(idTarefa):

    Tarefa.apagartarefa(idTarefa)

    return redirect(url_for("index"))

