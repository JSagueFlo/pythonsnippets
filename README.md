# Nice scripts and mini programs with Python

- [Nice scripts and mini programs with Python](#nice-scripts-and-mini-programs-with-python)
  - [TO-DO's](#to-dos)
    - [La-paradoja-de-Monty-Hall](#la-paradoja-de-monty-hall)
    - [Random music alarm](#random-music-alarm)
    - [AI emotion predictor](#ai-emotion-predictor)
      - [Try to predict my emotional state based on](#try-to-predict-my-emotional-state-based-on)
      - [Weather APIs](#weather-apis)

## TO-DO's

### La-paradoja-de-Monty-Hall

La paradoja de Monty Hall

Simular La paradoja de Monty Hall, amb un projecte django publicar el projecte a Github Si pot ser amb interfície gràfica millor que millor Si no, doncs començar amb un script python i ja està

[https://www.youtube.com/watch?v=1BpTBzDQuRE](Vídeo de referència on s'explica)

### Random music alarm

Crear una aplicació que faci d'alarma

El so de l'alarma serà random entre una array de sons.mp3 que lusuari seleccionara al seu gust

objectiu: que no soni la mateixa alarma cada dia, evitar que el cervell sacostumi al mateix so

La música ens fa sentir emocions, i les emocions es relacionen directament amb els pensaments que tenim i les accions que portem a terme.

En dies positius, no en tenim dubte, no hi ha problema...

Però en dies negatius, oblidem per complet que tenim el poder de reconduir aquests pensaments de merda, a través de les emocions, per a accionar d'una forma més positiva. Per això és interessant aquesta alarma. per a que aixi, al menys, en assegurem que les emocions són positives, cada cop que sona!

### AI emotion predictor

Can an AI predict my emotional state?

#### Try to predict my emotional state based on

- Weather (sunny, cloudy, rainy, windy...)
- Pressure (hPa)
- Day of the year
- Day of the month
- Day of the week

- [https://www.w3schools.com/python/python_ml_getting_started.asp"](Python Machine Learning tutorial W3Schools)
- [https://realpython.com/python-ai-neural-network/"](realpython.com AI example (neural network))

The main idea is to get a prediction of my emotional state on certain days based on ML trained models as I suspect that there are some factors that impact my emotional state always.  
The day of the year, the atmosphere pressure, the weather, etc.  
The idea is to train the model "MySelf" answering the question "How do I feel today/now?"  
Meanwhile, the app is gonna track the data for the rest of the models (WeatherModel, PressureModel, DayOfTheYearModel...) from terciary APIs.

#### Weather APIs

- [https://pypi.org/project/python-aemet/](Python AEMET API)
