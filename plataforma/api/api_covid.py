#Primeira versão da api, a medida que o banco de dados for sendo atualizado a api também será atualizada.
#import logging
from flask import Flask, request, jsonify
import pymysql
from flaskext.mysql import MySQL
from mysql_config import *
from flask_cors import CORS
#import requests

app = Flask(__name__)
CORS(app)
#logging.getLogger('flask_cors').level = logging.DEBUG

app.config["DEBUG"] = True

# Instanciar o objeto MySQL
mysql = MySQL()
# Ligar o MYSQL ao Flask
mysql.init_app(app)

config_sql(app)



@app.route('/')
def home():
	return '''<h1> API COVID</h1>
	<p>API criada para a aplicação MyStatusCare</p>
	<a href="http://127.0.0.1:5000/api/v1/resources/usuarios?idt_usuario=1">link</a><br>
	'''

#Rota table = City
@app.route('/api/v1/cidade/all', methods=['GET'])
def cities():
    #try:
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM mystatuscare.tb_cidade;")
    all_cities = cur.fetchall()
    cur.close()
    conn.close()
    resp=jsonify(all_cities)
    return resp

#Rota table = country
@app.route('/api/v1/pais/all', methods=['GET'])
def country():
	try:
		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("SELECT * FROM mystatuscare.tb_pais;")
		all_country = cur.fetchall()
		cur.close()
		conn.close()
		resp=jsonify(all_country)
		return resp
	except Exception as e:
		return "a"

#Rota table = state
@app.route('/api/v1/estado/all', methods=['GET'])
def state():
	try:
		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("SELECT * FROM mystatuscare.tb_estado;")
		all_states = cur.fetchall()
		cur.close()
		conn.close()
		resp=jsonify(all_state)
		return resp
	except Exception as e:
		return "a"

#Rota table = TB_hospital
@app.route('/api/v1/hospital/all', methods=['GET'])
def hospital():
	try:
		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("SELECT nme_hospital, nme_cidade, nme_estado FROM tb_hospital INNER JOIN tb_cidade ON tb_hospital.cod_cidade = idt_cidade INNER JOIN tb_estado ON tb_hospital.cod_estado = tb_estado.idt_estado;")
		all_hospital = cur.fetchall()
		resp=jsonify(all_hospital)
		cur.close()
		conn.close()
		return resp
	except Exception as e:
		return "a"
#Rota table = TB_patologia
@app.route('/api/v1/patologia/all', methods=['GET'])
def pathology():
	try:
		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("SELECT * FROM mystatuscare.tb_patologia;")
		all_pathology = cur.fetchall()
		cur.close()
		conn.close()
		resp=jsonify(all_pathology)
		return resp
	except Exception as e:
		return "a"

#Rota table = TB_sintomas
@app.route('/api/v1/sintomas/all', methods=['GET'])
def symptoms():
	try:
		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("SELECT * FROM mystatuscare.tb_sintomas;")
		all_symptoms = cur.fetchall()
		cur.close()
		conn.close()
		resp=jsonify(all_symptoms)
		return resp
	except Exception as e:
		return "a"


@app.route('/api/v1/resources/sintomas_usuario', methods=['GET'])
def user_symptoms():
	try:
		query_parameters = request.args
		idt_usuario = query_parameters.get("idt_usuario")

		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("SELECT tb_sintomas.nme_sintoma, tb_usuario.nme_usuario, tb_sintomas_usuario.dta_sintoma from tb_sintomas_usuario INNER JOIN tb_sintomas ON tb_sintomas_usuario.cod_sintoma = tb_sintomas.idt_sintoma INNER JOIN tb_usuario ON tb_sintomas_usuario.cod_usuario = tb_usuario.idt_usuario WHERE idt_usuario = %s;",(idt_usuario))
		all_user_symptoms = cur.fetchall()
		cur.close()
		conn.close()
		resp=jsonify(all_user_symptoms)
		return resp
	except Exception as e:
		return "a"



#filtro usuarios
@app.route('/api/v1/resources/usuarios', methods=['GET'])
def api_filter_user():
	query_parameters = request.args

	idg_usuario = query_parameters.get("idg_usuario")
	nme_usuario = query_parameters.get("nme_usuario")
	ida_usuario = query_parameters.get("ida_usuario")
	end_usuario = query_parameters.get("end_usuario")
	cod_cidade  = query_parameters.get("cod_cidade")
	pto_usuario = query_parameters.get("pto_usuario")



	query = "SELECT * FROM tb_usuario WHERE"
	to_filter=[]
	if idt_usuario:
		query += ' idg_usuario=%s AND'
		to_filter.append(idg_usuario)

	if nme_usuario:
		query += ' nme_usuario=%s AND'
		to_filter.append(nme_usuario)
	
	if ida_usuario:
		query += ' ida_usuario=%s AND'
		to_filter.append(ida_usuario)
	
	if end_usuario:
		query += ' end_usuario=%s AND'
		to_filter.append(end_usuario)

	if cod_cidade:
		query += ' cod_cidade=%s AND'
		to_filter.append(cod_cidade)
	
	if pto_usuario:
		query += ' pto_usuario=%s AND'
		to_filter.append(pto_usuario)


	if not (idt_usuario or nme_usuario or ida_usuario or end_usuario or cod_cidade or pto_usuario):
		return page_not_found(404)

	query = query[:-4] + ';'
	
	conn = mysql.connect()
	cur = conn.cursor(pymysql.cursors.DictCursor)
	cur.execute(query, to_filter)
	result = cur.fetchall()   

	resp=jsonify(result)
	return resp



@app.route('/api/v1/resources/hospital', methods=['GET'])
def api_filter_hospital():
	query_parameters = request.args

	idt_hospital = query_parameters.get("idt_hospital")
	nme_hospital = query_parameters.get("nme_hospital")
	end_hospital = query_parameters.get("end_hospital")
	bairro_hospital  = query_parameters.get("bairro_hospital")
	cod_cidade     = query_parameters.get("cod_cidade")

	query = "SELECT * FROM tb_hospital WHERE"
	to_filter=[]
	if idt_hospital:
		query += ' idt_hospital=%s AND'
		to_filter.append(idt_hospital)

	if nme_hospital:
		query += ' nme_hospital=%s AND'
		to_filter.append(nme_hospital)
	
	if end_hospital:
		query += ' end_hospital=%s AND'
		to_filter.append(end_hospital)
	
	if bairro_hospital:
		query += ' bairro_hospital=%s AND'
		to_filter.append(bairro_hospital)

	if cod_cidade:
		query += ' cod_cidade=%s AND'
		to_filter.append(cod_cidade)
	
	if cod_estado:
		query += ' cod_estado=%s AND'
		to_filter.append(cod_estado)

	if not (nme_hospital or end_hospital or bairro_hospital or cod_cidade or idt_hospital or cod_estado):
		return page_not_found(404)

	query = query[:-4] + ';'
	
	conn = mysql.connect()
	cur = conn.cursor(pymysql.cursors.DictCursor)
	cur.execute(query, to_filter)
	result = cur.fetchall()   

	resp=jsonify(result)
	return resp


@app.route('/api/v1/login', methods=['POST'])
def api_login():
	
    eml_usuario    =    request.json.get('eml_usuario')
    idg_usuario    =    request.json.get('idg_usuario')

    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT idg_usuario, idt_usuario FROM mystatuscare.tb_usuario WHERE eml_usuario=%s AND idg_usuario=%s;",(eml_usuario, idg_usuario))
    user = cur.fetchall()
    cur.close()
    conn.close()
	
    if user == None:
        return  -1
    else:
        return jsonify(user)


@app.route('/api/v1/insert/usuarios', methods=['POST'])
def api_insert_user():
	try:
		idt_usuario = 	request.json.get('idt_usuario') 
		nme_usuario = 	request.json.get('nme_usuario') 
		ida_usuario = 	request.json.get('ida_usuario')
		psw_usuario =	request.json.get('psw_usuario')
		end_usuario =	request.json.get('end_usuario')
		eml_usuario	= 	request.json.get('eml_usuario')
		cod_cidade	= 	request.json.get('cod_cidade')
		pto_usuario	= 	0
		
		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("INSERT INTO mystatuscare.tb_usuario(idt_usuario,nme_usuario,ida_usuario,end_usuario,psw_usuario,eml_usuario,cod_cidade,pto_usuario) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(idt_usuario,nme_usuario,ida_usuario,end_usuario,psw_usuario,eml_usuario,cod_cidade,pto_usuario))
		conn.commit()
		cur.close()
		conn.close()
		
		return "Registered"
	except Exception as e:
		return e

@app.route('/api/v1/insert/sintoma', methods= ['POST','GET'])
def api_insert_symptom():

    query_parameters = request.args

    idt_usuario = query_parameters.get("idt_usuario")
    idt_sintoma = request.json.get('idt_sintoma')
    dta_sintoma = request.json.get('dta_sintoma')

    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT tb_sintomas.idt_sintoma from tb_sintomas_usuario INNER JOIN tb_sintomas ON tb_sintomas_usuario.cod_sintoma = tb_sintomas.idt_sintoma INNER JOIN tb_usuario ON tb_sintomas_usuario.cod_usuario = tb_usuario.idt_usuario WHERE idt_usuario = %s",(idt_usuario))
    sintomas = cur.fetchall()
    close(cur,conn)

    result = filtro_sintoma(idt_sintoma,sintomas)

    if result == False:
        return -1
    else:

        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("INSERT INTO mystatuscare.tb_sintomas_usuario(cod_sintoma, cod_usuario, dta_sintoma) VALUES (%s,%s,%s)",(idt_sintoma, idt_usuario,dta_sintoma))
        conn.commit()
        close(cur,conn)


        pto_sint = sintinfo(idt_sintoma)
 

        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("UPDATE tb_usuario SET pto_usuario = pto_usuario + %s where idt_usuario = %s ;",(pto_sint, idt_usuario))
        conn.commit()
        close(cur,conn)

        return "Sintoma Registrado"


@app.route('/api/v1/insert/temperatura', methods=['POST', 'GET'])
def api_insert_usertemp():
    try:
        query_parameters = request.args
        idt_usuario = query_parameters.get('idt_usuario')

        dta_temperatura = request.json.get('dta_temperatura')
        vlr_temperatura = request.json.get('vlr_temperatura')




        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("INSERT INTO mystatuscare.tb_temperatura(dta_temperatura, vlr_temperatura, cod_usuario) VALUES (%s,%s,%s)",(dta_temperatura, vlr_temperatura,idt_usuario))
        conn.commit()
        cur.close()
        conn.close()

        return "Temp Registrada"
    except Exception as e:
    	return "a"


@app.route('/api/v1/resources/pontuacao', methods=['GET'])
def show_pto():
	idt_usuario = request.json.get('idt_usuario')

	conn = mysql.connect()
	cur = conn.cursor(pymysql.cursors.DictCursor)
	cur.execute("SELECT pto_usuario FROM mystatuscare.tb_usuario WHERE idt_usuario=%s",(idt_usuario))
	result = cur.fetchone()
	cur.close()
	conn.close()
	resp = jsonify(result)

	return resp

@app.route('/api/v1/resources/temperatura', methods=['GET'])
def show_temperature():
    query_parameters = request.args
    idt_usuario = query_parameters.get('idt_usuario')

    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT idt_usuario, dta_temperatura, vlr_temperatura FROM tb_usuario INNER JOIN tb_temperatura ON idt_usuario = cod_usuario WHERE idt_usuario=%s;",(idt_usuario))
    result = cur.fetchall()
    cur.close()
    conn.close()
    resp = jsonify(result)

    return resp

'''
@app.route('/api/v1/resources/attpontuacao', methods=['GET'])
def att_pto():
	try:
		idt_usuario = request.json.get('idt_usuario')



		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("SELECT SUM(pto_sintomas) from tb_sintomas_usuario INNER JOIN tb_sintomas ON tb_sintomas_usuario.cod_sintoma = tb_sintomas.idt_sintoma INNER JOIN tb_usuario ON tb_sintomas_usuario.cod_usuario = tb_usuario.idt_usuario WHERE idt_usuario = %s;",(idt_usuario))
		result = cur.fetchone()
		cur.close()
		conn.close()

		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("INSERT INTO mystatuscare.tb_usuario(pto_usuario,) VALUES (%s) WHERE idt_usuario=%s",(result,idt_usuario))
		conn.commit()
		cur.close()
		conn.close()
		
		return "ATT"
	except Exception as e:
		print(e)
'''

		
@app.errorhandler(404)
def page_not_found(e):
	return "<h1>404</h1><p>The resource could not be found.</p>", 404


#INSERT INTO mystatuscare.tb_sintomas_usuario(cod_sintoma, cod_usuario) VALUES (1,1);

if __name__ == "__main__":
	app.run()




'''
SELECT nme_hospital, nme_cidade, nme_estado FROM tb_hospital INNER JOIN tb_cidade ON tb_hospital.cod_cidade = idt_cidade
INNER JOIN tb_estado ON tb_hospital.cod_estado = tb_estado.idt_estado;'''


'''SELECT tb_sintomas.nme_sintoma, tb_usuario.nme_usuario from tb_sintomas_usuario INNER JOIN tb_sintomas
ON tb_sintomas_usuario.cod_sintoma = tb_sintomas.idt_sintoma
INNER JOIN tb_usuario ON tb_sintomas_usuario.cod_usuario = tb_usuario.idt_usuario;'''