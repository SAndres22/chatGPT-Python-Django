from django.db import models
import openai
# Indica el API Key
openai.api_key = "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"

# Create your models here.

class ChatGpt(models.Model):
    pregunta = models.TextField()

    def respuestaGPT(pregunta):
        # Define el motor del modelo GPT-3
        model_engine = "text-davinci-003"

        # Llama a la API de OpenAI para generar una respuesta basada en la pregunta
        completion = openai.Completion.create(
        engine=model_engine,
        # Usar la pregunta almacenada en la instancia del modelo
        prompt=pregunta,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7)

        # Extrae la respuesta generada por el modelo
        response = completion.choices[0].text
        print(response)

        # Devuelve la respuesta generada
        return response
