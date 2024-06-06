from flask import Flask
from routes import init_routes

app = Flask(_nome_)
init_routes(app)

if _name_=="_main_":
    app.run(debug=true)
    