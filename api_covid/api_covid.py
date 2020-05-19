from flask import Flask, request, jsonify
import pymysql
from flaskext.mysql import MySQL
from mysql_config import *

app = Flask(__name__)
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
	<a href="http://127.0.0.1:5000/api/v1/resources/usuarios?idt_usuario=1&city_id=1&address=rua+1&pto_user=5&nme_usuario=gabriel&ida_usuario=18">link</a><br>
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
		cur.execute("SELECT * FROM mydb.city;")
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
		cur.execute("SELECT * FROM mydb.country;")
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
		cur.execute("SELECT * FROM mydb.state;")
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

'''
@app.route('/api/v1/sintomas_usuario/all', methods=['GET'])
def user_symptoms():
	work in progress
'''

@app.route('/api/v1/resources/usuarios', methods=['GET'])
def api_filter_user():
	query_parameters = request.args

	idt_usuario = query_parameters.get("idt_usuario")
	nme_usuario = query_parameters.get("nme_usuario")
	ida_usuario = query_parameters.get("ida_usuario")
	address     = query_parameters.get("address")
	city_id     = query_parameters.get("city.id")
	pto_user    = query_parameters.get("pto_user")



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
	
	if address:
		query += ' address=%s AND'
		to_filter.append(address)

	if city_id:
		query += ' city_id=%s AND'
		to_filter.append(city_id)
	
	if pto_user:
		query += ' pto_user=%s AND'
		to_filter.append(pto_user)


	if not (idt_usuario or nme_usuario):
		return page_not_found(404)

	query = query[:-4] + ';'
	
	conn = mysql.connect()
	cur = conn.cursor(pymysql.cursors.DictCursor)
	cur.execute(query, to_filter)
	result = cur.fetchall()   

	resp=jsonify(result)
	return resp



@app.errorhandler(404)
def page_not_found(e):
	return "<h1>404</h1><p>The resource could not be found.</p>", 404




if __name__ == "__main__":
	app.run()