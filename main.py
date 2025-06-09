respuestas = {
    "feliz" : "que bueno me alegro que te sientas asi, disfruta tu dia <3",
    "triste" : "lo siento, recuerda que despues de la tormenta sale el sol",
    "enojado" : "respira y relajate todo estara bien es cosa de tiempo <3", 
    "aburrido" : "vamos a hacer algo divertido el dia de hoy",
    "estresado" : "recuerda que la vida es corta y hay que disfrutarla",
    "ansioso" : "todo estara bien no te preocupes, todo pasa por algo", 
    }
print ("hola, ¿como te sientes el dia de hoy?")
#mostrar mensaje inicial
estado = input ("ingresa tu estado de animo: "). lower()
if estado in respuestas: 
    print (respuestas[estado])
else:
    print ("no reconozco este tipo de animo pero espero que te sientas mejor pronto")