from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=('GET', 'POST'))
def formularioDeCompras():
    if request.method=='POST':
        nombre=request.form['nombre']
        edad=int(request.form['edad'])
        cantTarros=int(request.form['cantTarros'])
        precioTarro = 9000
        precio_sin_descuento=cantTarros*precioTarro
        total=precio_sin_descuento

        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        elif edad < 18:
            descuento = 0.0

        total=precio_sin_descuento*(1-descuento)
        cantDescuento=precio_sin_descuento-total

        return render_template('ejercicio1.html', total=total, precio_sin_descuento=precio_sin_descuento, nombre=nombre, edad=edad, cantTarros=cantTarros, cantDescuento=cantDescuento)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def inicioDeSesion():
    usuarios={
        "juan": "admin",
        "pepe": "user"
    }

    if request.method=='POST':
        nombre=request.form['nombre']
        contraseña=request.form['contraseña']

        if nombre in usuarios and usuarios[nombre] == contraseña:
            if nombre == 'juan':
                mensaje ='Bienvenido Administrador juan'
            elif nombre == 'pepe':
                mensaje ='Bienvenido Usuario pepe'
        else:
            mensaje ='Usuario o contraseña incorrectos'

        return render_template('ejercicio2.html',mensaje=mensaje)




    return render_template(('ejercicio2.html'))




if __name__ == '__main__':
    app.run(debug=True)