from flask import Flask # Importação da biblioteca Flask

# Função de criação do aplicativo
def create_app():
    app=Flask(__name__) # o Flask passa a se chamar app

    from .routes.main_route import main_bp # importação do arquivo routes

    # registro de routes
    app.register_blueprint(main_bp)

    return app
