from typing import Text, List, Optional, Dict, Any
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker, Action


def calcular_estilo(respuestas):
    puntajes = [0, 0, 0]  # visual, auditivo, kinestesico
    for i in range(0, 5):
        puntajes[0] = puntajes[0] + respuestas[i]
    for i in range(5, 10):
        puntajes[1] = puntajes[1] + respuestas[i]
    for i in range(10, 15):
        puntajes[2] = puntajes[2] + respuestas[i]

    max_value = max(puntajes)
    estilo = ""
    if max_value == 0:
        estilo = "No tienes ningun estilo predominante, intenta volver a hacer el test respondiendo con sinceridad"
    else:
        for i in range(0, 3):
            if puntajes[i] == max_value:
                if i == 0:
                    estilo = estilo + "Visual"
                if i == 1:
                    estilo = estilo + " Auditivo"
                if i == 2:
                    estilo = estilo + " Kinestesico"
    return estilo


class SubmitEstiloForm(Action):
    def name(self) -> Text:
        return "submit_estilo_form"

    async def run(
            self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        respuestas = []
        r1 = int(tracker.get_slot("r1"))
        r2 = int(tracker.get_slot("r2"))
        r3 = int(tracker.get_slot("r3"))
        r4 = int(tracker.get_slot("r4"))
        r5 = int(tracker.get_slot("r5"))
        r6 = int(tracker.get_slot("r6"))
        r7 = int(tracker.get_slot("r7"))
        r8 = int(tracker.get_slot("r8"))
        r9 = int(tracker.get_slot("r9"))
        r10 = int(tracker.get_slot("r10"))
        r11 = int(tracker.get_slot("r11"))
        r12 = int(tracker.get_slot("r12"))
        r13 = int(tracker.get_slot("r13"))
        r14 = int(tracker.get_slot("r14"))
        r15 = int(tracker.get_slot("r15"))
        respuestas.append(r1)
        respuestas.append(r2)
        respuestas.append(r3)
        respuestas.append(r4)
        respuestas.append(r5)
        respuestas.append(r6)
        respuestas.append(r7)
        respuestas.append(r8)
        respuestas.append(r9)
        respuestas.append(r10)
        respuestas.append(r11)
        respuestas.append(r12)
        respuestas.append(r13)
        respuestas.append(r14)
        respuestas.append(r15)

        estilo = calcular_estilo(respuestas)
        estilo = "Tu estilo es "+estilo
        dispatcher.utter_message(estilo)

        return []
