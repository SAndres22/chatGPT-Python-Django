from django.shortcuts import render
from chatGPT.models import ChatGpt

# Create your views here.

def index(request):
    return render(request, 'index.html')

def chat(request):
    # Inicializa la sesión de conversación si no existe
    if 'conversation_history' not in request.session:
        request.session['conversation_history'] = []

    if request.method == 'POST':
        pregunta = request.POST.get('message', '')
        mensj = ChatGpt.respuestaGPT(pregunta)
        
        # Recupera el historial de conversación de la sesión y agrega la pregunta y respuesta
        conversation_history = request.session['conversation_history']
        conversation_history.append((pregunta, mensj))
        
        # Actualiza la sesión con el nuevo historial de conversación
        request.session['conversation_history'] = conversation_history
        
    # Recupera el historial de conversación de la sesión para mostrarlo en la plantilla
    conversation_history = request.session['conversation_history']
    
    return render(request, "index.html", {"conversation_history": conversation_history})
