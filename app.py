from flask import Flask, render_template, request, jsonify, url_for
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Banco de preguntas y respuestas del chatbot
banco_preguntas = [
    [
        r"(hola|buenos dias|buenas tardes|buenas noches|que tal)",
        ["Hola, ¿Cómo estás?", "Hola, en qué puedo ayudarte", "Hola, ¿cómo te va?"]
    ],
    [
        r"(quiero presentar un reclamo|cómo presento un reclamo|deseo presentar un reclamo)",
        ["Por favor, proporcióname los detalles del reclamo que deseas presentar."]
    ],
    [
        r"(mi reclamo fue recibido\?|ya recibieron mi reclamo\?|está mi reclamo en proceso\?)",
        ["Estamos evaluando tu reclamo. Te notificaremos si es válido para continuar con el proceso."]
    ],
    [
        r"(mi reclamo es válido\?|aceptaron mi reclamo\?)",
        ["Tu reclamo ha sido aceptado y se está procesando. Recibirás una respuesta en breve."]
    ],
    [
        r"(cuál es el estado de mi reclamo\?|puedes actualizarme sobre mi reclamo\?)",
        ["Tu reclamo está siendo revisado. Te informaremos tan pronto como tengamos una actualización."]
    ],
    [
        r"(mi reclamo fue rechazado\?|por qué rechazaron mi reclamo\?)",
        ["Lamentablemente, tu reclamo no cumple con los criterios necesarios y ha sido rechazado. Puedes intentar presentar nuevamente si tienes más información."]
    ],
    [
        r"(gracias|muchas gracias|te lo agradezco)",
        ["De nada", "Estoy para ayudarte", "No hay de qué", "Cuando desees puedes consultarme"]
    ],
    [
        r"(chau|adios|hasta luego|good bye|eso es todo)",
        ["Adiós", "Cuídate", "Hasta luego", "Que tengas un buen día", "Nos vemos la próxima"]
    ]
]

chatbot = Chat(banco_preguntas, reflections)

@app.route('/')
def index():
    return render_template('Portal.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get("message")
    response = chatbot.respond(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
