from app import create_app # importação da função do arquivo principal

# chamado da Função para o loop
app = create_app()

# Começo do loop
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
