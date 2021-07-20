import psycopg2
from Model.Resposta import Resposta

class RespostaDAO:

    def __init__(self):
        pass

    def adicionaResposta(self,resposta):
        conn = psycopg2.connect("dbname=db_BemPromotora user=postgres password=postgres")
        cur = conn.cursor()
        cur.execute("INSERT INTO tb_respostas (id_formulario,resposta1,resposta2,resposta3,resposta4) VALUES (%s,%s,%s,%s,%s);", [ str(resposta.getId_formulario()),str(resposta.getResposta1()),resposta.getResposta2(),resposta.getResposta3(),resposta.getResposta4() ])
        conn.commit()
        cur.close()
        conn.close()

