from flask import Flask, request, render_template_string, redirect, url_for 
app = Flask(__name__) 

USUARIO_CORRECTO = "Cesar Huanca" 
PASSWORD_CORRECTO = "Huanquita15." 

# Contador de intentos 
intentos = 0 

# Página principal (Login) con estilo empresarial
login_html = """ 
<!DOCTYPE html> 
<html lang="es"> 
<head> 
    <meta charset="UTF-8"> 
    <title>Login</title> 
    <style>
        body {
            background: url('/static/fondo.jpg') no-repeat center center fixed;
            background-size: cover;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .login-box {
            background: rgba(255, 255, 255, 0.6); /*blanco con 60% de transparencia*/
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 6px 20px rgba(0,0,0,.3);
            text-align: center;
            width: 320px;
        }
        .login-box img {
            height: 80px;
            margin-bottom: 20px;
        }
        h2 {
            margin-bottom: 20px;
            color: background: rgba(0,0,0,0.6); /* negro con 60% transparencia */
        }
        label {
            display: block;
            text-align: left;
            margin: 8px 0 4px;
            font-weight: bold;
        }
        input {
            width: 100%;
            padding: 10px;
            margin-bottom: 14px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }
        .btn {
            width: 48%;
            padding: 10px;
            border: none;
            border-radius: 6px;
            font-weight: bold;
            cursor: pointer;
        }
        .btn-green {
            background: #2e7d32;
            color: #fff;
        }
        .btn-red {
            background: #c62828;
            color: #fff;
        }
        .mensaje {
            color: red;
            margin-top: 10px;
        }
    </style>
</head> 
<body> 
    <div class="login-box">
        <!-- Logo arriba -->
        <img src="/static/logo_1.png" alt="logo_1">
        <h2>¡Bienvenido!</h2>
        <h2>Ingresa para comprar y ver tus pedidos</h2>
        <form method="POST"> 
            <label>Usuario:</label> 
            <input type="text" name="usuario" required> 
            <label>Password:</label> 
            <input type="password" name="password" required> 
            <div style="display:flex; justify-content:space-between; margin-top:10px;">
                <button type="submit" class="btn btn-green">Acceder</button> 
                <button type="reset" class="btn btn-red">Cancelar</button> 
            </div>
        </form> 
        <h3 class="mensaje">{{ mensaje }}</h3> 
        <h4>Intentos restantes: {{ restantes }}</h4> 
    </div>
</body> 
</html> 
""" 

# Página de bienvenida
bienvenida_html = """ 
<!DOCTYPE html> 
<html lang="es"> 
<head> 
    <meta charset="UTF-8"> 
    <title>Bienvenido</title> 
    <style>
        body {
            background: #f0f0f0;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
        }
        h1 {
            color: #1b5e20;
        }
        a {
            margin-top: 20px;
            color: #2e7d32;
            font-weight: bold;
            text-decoration: none;
        }
    </style>
</head> 
<body> 
    <h1>Autenticación Exitosa</h1> 
    <h2>Bienvenido al Sistema</h2> 
    <a href="/">Volver al inicio</a>
</body> 
</html> 
""" 

# Página de bloqueo
bloqueado_html = """ 
<!DOCTYPE html> 
<html lang="es"> 
<head> 
    <meta charset="UTF-8"> 
    <title>Sistema Bloqueado</title> 
    <style>
        body {
            background: #ffdddd;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
        }
        h1 {
            color: #c62828;
        }
    </style>
</head> 
<body> 
    <h1>Sistema Bloqueado</h1> 
    <h2>Ha superado el máximo de intentos permitidos.</h2> 
    <a href="/">Volver al inicio</a>
</body> 
</html> 
""" 

# Ruta principal
@app.route("/", methods=["GET", "POST"]) 
def login(): 
    global intentos 
    mensaje = "" 
    restantes = 3 - intentos 

    if intentos >= 3: 
        return redirect(url_for("bloqueado")) 

    if request.method == "POST": 
        usuario = request.form["usuario"] 
        password = request.form["password"] 

        if usuario == USUARIO_CORRECTO and password == PASSWORD_CORRECTO: 
            return redirect(url_for("bienvenida")) 
        else: 
            intentos += 1 
            restantes = 3 - intentos 
            mensaje = "Usuario o contraseña incorrectos" 
            if intentos >= 3: 
                return redirect(url_for("bloqueado")) 

    return render_template_string(login_html, mensaje=mensaje, restantes=restantes) 

@app.route("/bienvenida") 
def bienvenida(): 
    return render_template_string(bienvenida_html) 

@app.route("/bloqueado") 
def bloqueado(): 
    return render_template_string(bloqueado_html) 

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=8080) 