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

#Rota table = TB_usuario
@app.route('/api/v1/usuarios/all', methods=['GET'])
def users():
	try:
		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("SELECT * FROM mydb.tb_usuario;")
		all_users = cur.fetchall()
		resp=jsonify(all_users)
		return resp
	except Exception as e:
		print(e)
	finally:
		cur.close()
		conn.close()

#Rota table = City
@app.route('/api/v1/cidade/all', methods=['GET'])
def cities():
	try:
		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("SELECT * FROM mydb.tb_cidade;")
		all_cities = cur.fetchall()
		resp=jsonify(all_cities)
		return resp
	except Exception as e:
		print(e)
	finally:
		cur.close()
		conn.close()

#Rota table = country
@app.route('/api/v1/pais/all', methods=['GET'])
def country():
	try:
		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("SELECT * FROM mydb.tb_pais;")
		all_country = cur.fetchall()
		resp=jsonify(all_country)
		return resp
	except Exception as e:
		print(e)
	finally:
		cur.close()
		conn.close()

#Rota table = state
@app.route('/api/v1/estado/all', methods=['GET'])
def state():
	try:
		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("SELECT * FROM mydb.tb_estado;")
		all_states = cur.fetchall()
		resp=jsonify(all_state)
		return resp
	except Exception as e:
		print(e)
	finally:
		cur.close()
		conn.close()

#Rota table = TB_hospital
@app.route('/api/v1/hospital/all', methods=['GET'])
def hospital():
	try:
		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("SELECT * FROM mydb.tb_hospital;")
		all_hospital = cur.fetchall()
		resp=jsonify(all_hospital)
		return resp
	except Exception as e:
		print(e)
	finally:
		cur.close()
		conn.close()

#Rota table = TB_patologia
@app.route('/api/v1/patologia/all', methods=['GET'])
def pathology():
	try:
		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("SELECT * FROM mydb.tb_patologia;")
		all_pathology = cur.fetchall()
		resp=jsonify(all_pathology)
		return resp
	except Exception as e:
		print(e)
	finally:
		cur.close()
		conn.close()

#Rota table = TB_sintomas
@app.route('/api/v1/sintomas/all', methods=['GET'])
def symptoms():
	try:
		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("SELECT * FROM mydb.tb_sintomas;")
		all_symptoms = cur.fetchall()
		resp=jsonify(all_symptoms)
		return resp
	except Exception as e:
		print(e)
	finally:
		cur.close()
		conn.close()

@app.route('/api/v1/sintomas_usuario/all', methods=['GET'])
def user_symptoms():
	try:
		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("SELECT * FROM mydb.tb_sintomas_usuario;")
		all_user_symptoms = cur.fetchall()
		resp=jsonify(all_user_symptoms)
		return resp
	except Exception as e:
		print(e)
	finally:
		cur.close()
		conn.close()


#filtro usuarios
@app.route('/api/v1/resources/usuarios', methods=['GET'])
def api_filter_user():
	query_parameters = request.args

	idt_usuario = query_parameters.get("idt_usuario")
	nme_usuario = query_parameters.get("nme_usuario")
	ida_usuario = query_parameters.get("ida_usuario")
	end_usuario = query_parameters.get("end_usuario")
	cod_cidade  = query_parameters.get("cod_cidade")
	pto_usuario = query_parameters.get("pto_usuario")



	query = "SELECT * FROM tb_usuario WHERE"
	to_filter=[]
	if idt_usuario:
		query += ' idt_usuario=%s AND'
		to_filter.append(idt_usuario)

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


@app.route('/api/v1/resources/sintomas', methods=['GET'])
def api_filter_symptoms():
	query_parameters = request.args

	idt_sintoma = query_parameters.get("idt_sintoma")
	nme_sintoma = query_parameters.get("nme_sintoma")
	description = query_parameters.get("description")
	pto_sintomas  = query_parameters.get("pto_sintomas")
	cod_patologia = query_parameters.get("cod_patologia")
	ftr_risco     = query_parameters.get("ftr_risco")


	query = "SELECT * FROM tb_sintomas WHERE"
	to_filter=[]
	if idt_sintoma:
		query += ' idt_sintoma=%s AND'
		to_filter.append(idt_sintoma)

	if nme_sintoma:
		query += ' nme_sintoma=%s AND'
		to_filter.append(nme_sintoma)
	
	if description:
		query += ' description=%s AND'
		to_filter.append(description)
	
	if pto_sintomas:
		query += ' pto_sintomas=%s AND'
		to_filter.append(pto_sintomas)

	if cod_patologia:
		query += ' cod_patologia=%s AND'
		to_filter.append(cod_patologia)
	if ftr_risco:
		query += ' ftr_risco=%s AND'
		to_filter.append(ftr_risco)

	if not (nme_sintoma or description or pto_sintomas or cod_patologia or idt_sintoma or ftr_risco):
		return page_not_found(404)

	query = query[:-4] + ';'
	
	conn = mysql.connect()
	cur = conn.cursor(pymysql.cursors.DictCursor)
	cur.execute(query, to_filter)
	result = cur.fetchall()   

	resp=jsonify(result)
	return resp


@app.route('/api/v1/insert/usuarios', methods=['POST'])
def api_insert_user():
	try:
		nme_usuario = 	request.json.get('nme_usuario') 
		ida_usuario = 	request.json.get('ida_usuario')
		ida_usuario = str(ida_usuario)
		psw_usuario =	request.json.get('psw_usuario')
		end_usuario =	request.json.get('end_usuario')
		eml_usuario	= 	request.json.get('eml_usuario')
		cod_cidade	= 	request.json.get('cod_cidade')
		
		
		conn = mysql.connect()
		cur = conn.cursor(pymysql.cursors.DictCursor)
		cur.execute("INSERT INTO mydb.tb_usuario(nme_usuario,ida_usuario,end_usuario,psw_usuario,eml_usuario,cod_cidade) VALUES (%s,%s,%s,%s,%s,%s)",(nme_usuario,ida_usuario,end_usuario,psw_usuario,eml_usuario,cod_cidade))
		conn.commit()
		cur.close()
		conn.close()
		
		return "Registered"
	except Exception as e:
		return(str(e))

@app.errorhandler(404)
def page_not_found(e):
	return "<h1>404</h1><p>The resource could not be found.</p>", 404




if __name__ == "__main__":
	app.run()