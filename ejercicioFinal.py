"""
Hacer un analizador de sentimientos.
"""
# from textoblob import TextBlob

# class AnalizadorDeSentimiento:
#     def analizar_sentimientos(self, texto):
#         analisis = TextBlob(texto)
#         if analisis.sentiment.polarity > 0:
#             return "positivo"
#         elif analisis.sentiment.polarity == 0:
#             return "neutral"
#         else:
#             return "negativo"
        
import openai 

openai.api_base = 