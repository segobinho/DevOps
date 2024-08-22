from flask import Flask, send_file
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route("/")
def helloworld():
    
    # Dados do gráfico
    horarios = ['8h', '10h', '12h', '14h', '16h', '18h', '20h', '22h']
    quantidade_receba = [5, 8, 15, 10, 20, 18, 30, 25]

    # Criando o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(horarios, quantidade_receba, marker='o')
    plt.title('Quantidade de vezes que "Receba!" foi dito durante o dia')
    plt.xlabel('Horário')
    plt.ylabel('Quantidade de "Receba!"')
    plt.grid(True)

    # Salvando o gráfico em um objeto de bytes
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    # Enviando a imagem como resposta
    return send_file(img, mimetype='image/png')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

