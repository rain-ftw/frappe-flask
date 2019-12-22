from flask import Flask
from flask import render_template
from flask import request
from flask_mysqldb import MySQL
from datetime import datetime
import sys

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'BHARAT12'
app.config['MYSQL_DB'] = 'inventory'

mysql = MySQL(app)

def productsFetch():
		cur = mysql.connection.cursor()
		cur.execute('''SELECT product_id from product''')
		products = cur.fetchall()
		cur.close()
		return products;

def locationsFetch():
		cur = mysql.connection.cursor()
		cur.execute('''SELECT location_id from location''')
		locations = cur.fetchall()
		cur.close()
		return locations;

def movementsFetch():
		cur = mysql.connection.cursor()
		cur.execute('''SELECT * from productmovement''')
		movements = cur.fetchall()
		cur.close()
		return movements;


@app.route("/", methods=['GET','POST'])
def manage():
	products = productsFetch()
	locations = locationsFetch()
	data = ['','','']
	if request.method == 'POST':
		if 'product' in request.form:
			details = request.form
			pid = details['p-id']
			cur = mysql.connection.cursor()
			cur.execute("INSERT INTO product(product_id) values(%s)",(int(pid),))
			mysql.connection.commit()
			data[0] = 'success'
		elif 'location' in request.form:
			details = request.form
			lid = details['location-id']
			cur = mysql.connection.cursor()
			cur.execute("INSERT INTO location(location_id) values(%s)",(int(lid),))
			mysql.connection.commit()
			cur.close()
			data[1] = 'success'
		elif 'movement' in request.form:
			from_ = ''
			to_ = ''
			details = request.form
			mid = details['movement-id']
			qty = details['qty']
			timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			pid = details['product-id']
			if 'from-location-id' in details:
				from_ = details['from-location-id']
			if 'to-location-id' in details:
				to_ = details['to-location-id']
			if from_ == '' and to_ == '':
				data[2] = 'Select Atleast One Location'
				return render_template('index.html',data = data,products = products,locations = locations)
			cur = mysql.connection.cursor()
			cur.execute("INSERT INTO productmovement(movement_id,timestamp,from_location,to_location,product_id,qty) values(%s,%s,%s,%s,%s,%s)",
				(int(mid),timestamp,from_,to_,int(pid),int(qty),))
			mysql.connection.commit()
			cur.close()
			data[2] = 'success'
	return render_template('index.html',data = data,products = products,locations = locations)


@app.route("/products")
def fetchP(): 
		products = productsFetch()
		return render_template('products.html',products = products)


@app.route("/locations")
def fetchL():
		locations = locationsFetch()
		return render_template('locations.html',locations = locations)


@app.route("/movements")
def fetchM():
		movements = movementsFetch()
		return render_template('movements.html',movements = movements)


class Warehouse:
	def __init__(self,name,products,qty):
		self.name = name
		self.products = products
		self.qty = qty

@app.route("/report")
def cal():
	movements = movementsFetch()
	locations = locationsFetch()
	products = productsFetch()
	
	wares=[]
	
	for l in locations:
		items = []
		qty = []
		for p in products:
			items.append(p[0])
			qty.append(150)
		wares.append(Warehouse(l[0],items,qty))

	for m in movements:
		product = int(m[4])
		q = int(m[5])
		if m[2] != '':
			fromLocation = int(m[2])
			wares[fromLocation-1].qty[product-1] -= q
		if m[3] != '':
			toLocation = int(m[3])
			wares[toLocation-1].qty[product-1] += q

	return render_template('report.html',wares= wares)


@app.route("/edit",methods=['GET','POST'])
def delete():
	products = productsFetch()
	locations = locationsFetch()
	movements = movementsFetch()
	data=['','','']
	if request.method == 'POST':
		if 'deleteP' in request.form:
			pid = request.form['product-id']
			cur = mysql.connection.cursor()
			cur.execute("DELETE FROM %s WHERE product_id = %s" % ('product',pid))
			mysql.connection.commit()
			data[0] = 'success'
		elif 'deleteL' in request.form:
			  lid = request.form['location-id']
			  cur = mysql.connection.cursor()
			  cur.execute("DELETE FROM %s WHERE location_id = %s" % ('location',lid))
			  mysql.connection.commit()
			  data[1] = 'success'
		elif 'deleteM' in request.form:
			  mid = request.form['movement-id']
			  cur = mysql.connection.cursor()
			  cur.execute("DELETE FROM %s WHERE movement_id = %s" % ('productmovement',mid))
			  mysql.connection.commit()
			  data[2] = 'success'
	return render_template('edit.html',data = data,products = products,locations = locations,movements=movements)


if __name__ == '__main__':
	app.run(debug=True)