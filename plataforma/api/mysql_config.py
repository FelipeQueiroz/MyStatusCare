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


def filtro_sintoma(idt_sintoma,sintomas):
    for idt_sintoma in sintomas:
        if idt_sintoma == ("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10" or "11" or "12" or "13" or "14" or "15"):
            return False
        else:
            return idt_sintoma


def close(cur,conn):
        cur.close()
        conn.close()
        return

def sintinfo(sintoma):
    if sintoma == 1 or 2 or 6 or 8:
        return 1
    elif sintoma == 4 or 5 or 7 or 10 or 13 or 14:
        return 2
    else:
        return 3

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