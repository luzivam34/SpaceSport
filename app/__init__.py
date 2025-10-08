from flask import Flask # Importação da biblioteca Flask

# Função de criação do aplicativo
def create_app():
    app=Flask(__name__) # o Flask passa a se chamar app

    return app
