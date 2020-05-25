# MySQL configurations
'''def config_sql(app):
	app.config['MYSQL_DATABASE_USER'] = 'Root'
	app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
	app.config['MYSQL_DATABASE_DB'] = 'mydb'
	app.config['MYSQL_DATABASE_HOST'] = 'localhost:3306'
	mysql.init_app(app)'''

def config_sql(app):
	app.config['MYSQL_DATABASE_USER'] = 'root'
	app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
	app.config['MYSQL_DATABASE_DB'] = 'mydb'
	app.config['MYSQL_DATABASE_HOST'] = 'localhost'
	app.config['DEBUG'] = True



'''
metodo altenativo

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/api/v1/cidade', methods=['GET'])
def api_all():
    conn = mysql.connect()
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_citys = cur.execute('SELECT * FROM city;')
    all_citys = cur.fetchall()

    return jsonify(all_citys)

'''