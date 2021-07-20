import psycopg2
from Model.Formulario import Formulario
from Model.Pergunta import Pergunta

class FormularioDAO:

    def __init__(self):
        pass


    def retornaFormulario(self):
        conn = psycopg2.connect("dbname=db_BemPromotora user=postgres password=postgres")
        cur = conn.cursor()
        query = '''SELECT tb_formulario.id_formulario,
                            tb_formulario.titulo,
                            tb_formulario.descricao,
                            tb_perguntas.id_pergunta,
                            tb_perguntas.texto,
                            tb_perguntas.opcao1,
                            tb_perguntas.opcao2,
                            tb_perguntas.opcao3,
                            tb_perguntas.opcao4 
                            from tb_formulario
	                JOIN tb_form_pergunta ON tb_form_pergunta.id_formulario = tb_formulario.id_formulario
	                JOIN tb_perguntas on tb_form_pergunta.id_pergunta = tb_perguntas.id_pergunta;'''
        
        cur.execute(query)
        vetTuplas = cur.fetchall()
        vetPerguntas = []

        for tupla in vetTuplas:
            id = tupla[0]
            titulo = tupla[1]
            descricao = tupla[2]
            pergunta = Pergunta(tupla[3],tupla[4],tupla[5],tupla[6],tupla[7],tupla[8])
            vetPerguntas.append(pergunta)

        formulario = Formulario(id,titulo,descricao,vetPerguntas)
        cur.close()
        conn.close()
        return formulario