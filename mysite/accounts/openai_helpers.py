import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_available_slots():
    """
    Usa OpenAI para generar horarios disponibles.
    """
    prompt = (
        "Genera horarios disponibles para citas de lunes a sábado. Cada cita dura 1 hora y 20 minutos, "
        "comenzando desde las 8:00 AM hasta las 6:00 PM. Devuelve los horarios en formato JSON con las horas disponibles."
    )
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text
