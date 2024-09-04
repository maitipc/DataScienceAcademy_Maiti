# Lab 4 - Deploy de Infraestrutura e API Para Aplicação de Data Science na AWS com Terraform
# Criação da API para o Modelo de Machine Learning

# Imports
from flask import Flask, request, render_template # Estruturas para criar o site
import joblib

# Criação do objeto app do tipo Flask
app = Flask(__name__)

# Carregar o modelo treinado que está em disco e coloca na memória, em modelo_dsa_final
modelo_dsa_final = joblib.load('modelo_dsa_treinado.pkl')

# Rota da página de entrada
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():

    # Recebe os novos dados de entrada
    features = [float(x) for x in request.form.values()]

    # Prepara a lista dos atributos
    final_features = [features]

    # Previsão com o modelo treinado
    prediction = modelo_dsa_final.predict(final_features)
    
    return render_template('index.html', prediction_text = f'Previsão do Modelo (1 - Cliente Fará Outra Compra / 0 - Cliente Não Fará Outra Compra): {prediction[0]}')

# Executa o programa 
if __name__ == "__main__":
    app.run(debug = True)
