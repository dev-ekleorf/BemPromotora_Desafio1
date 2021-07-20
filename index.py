from flask import Flask,render_template,request,redirect,url_for
from DAO.FormularioDAO import FormularioDAO
from Model.Formulario import Formulario
from Model.Pergunta import Pergunta
from Model.Resposta import Resposta
from DAO.RespostaDAO import RespostaDAO
app = Flask("index")


@app.route("/resultados",methods=['POST'])
def resultados():
    
    return "Obrigado por responder!"

@app.route("/")
def index():
    fDAO = FormularioDAO()
    formulario = fDAO.retornaFormulario()
    titulo = formulario.getTitulo()
    descricao = formulario.getDescricao()
    perguntas = Pergunta()
    perguntas = formulario.getPerguntas()
    return render_template('index.html', titulo=titulo,descricao=descricao,perguntas=perguntas)

@app.route("/gravarResposta",methods=['POST'])
def gravarResposta():
    print("esta vindo do request.form: \n")
    vetRespostas=[]
    f = request.form
    for key in f.keys():
        for value in f.getlist(key):
            print(key,":",value)
            vetRespostas.append(value)


    resposta = Resposta("1",vetRespostas[0],vetRespostas[1],vetRespostas[2],vetRespostas[3])
    respostaDAO = RespostaDAO()
    respostaDAO.adicionaResposta(resposta)

    mensagem = "Muito Obrigado por responder!"
    return render_template("sucesso.html",mensagem=mensagem)

    