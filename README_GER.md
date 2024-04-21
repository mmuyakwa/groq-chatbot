# GROQ ChatBot

## Beschreibung

Der GROQ ChatBot ist eine Streamlit-Anwendung, die es Benutzern ermöglicht, mit einem KI-Modell zu interagieren und Antworten auf ihre Fragen zu erhalten. Die Anwendung verwendet die GROQ-API, um die Antworten des KI-Modells zu generieren, und bietet eine benutzerfreundliche Oberfläche, um den Chatbot zu verwenden.

## Installation

1. Stellen Sie sicher, dass Sie Python 3.10 oder höher installiert haben.
2. Klonen Sie das Repository:
   ```
   git clone https://github.com/mmuyakwa/groq-chatbot.git
   ```
3. Navigieren Sie in das Projektverzeichnis:
   ```
   cd groq-chatbot
   ```
4. Erstellen Sie eine virtuelle Umgebung und aktivieren Sie sie:
   ```
   python -m venv venv
   source venv/bin/activate
   ```
5. Installieren Sie die erforderlichen Pakete:
   ```
   pip install -r requirements.txt
   ```
6. Erstellen Sie eine `.env`-Datei im Projektverzeichnis und fügen Sie Ihren GROQ-API-Schlüssel hinzu:
   ```
   GROQ_API_KEY=gsk_YOUR-API-KEY-HERE
   ```
7. Starten Sie die Anwendung:
   ```
   streamlit run app.py
   ```
   Die Anwendung sollte nun in Ihrem Standardbrowser geöffnet werden.

## Verwendung

1. Geben Sie Ihre Frage oder Eingabeaufforderung in das Eingabefeld ein.
2. Drücken Sie die Eingabetaste oder klicken Sie auf den "Senden"-Button.
3. Der ChatBot wird Ihre Anfrage verarbeiten und eine Antwort in deutscher Sprache zurückgeben.
4. Der Chatverlauf wird in der Anwendung gespeichert, sodass Sie darauf zurückgreifen können.
5. Um den Chatverlauf zurückzusetzen, klicken Sie auf den "Reset Context Length"-Button.

## Lizenz

Dieses Projekt steht unter der [MIT-Lizenz](LICENSE).

## Autoren

- Michael Muyakwa

## Google-Links

> _See also:_ { 🔍 } [GROQ API](https://www.google.com/search?q=GROQ+API)
> { 🤖 } [Streamlit](https://www.google.com/search?q=Streamlit)
> { 📚 } [Python 3.10](https://www.google.com/search?q=Python+3.10)
> 
> _You may also enjoy:_ { 🌐 } [Chatbots in Python](https://www.google.com/search?q=Chatbots+in+Python)
> { 🤖 } [AI Language Models](https://www.google.com/search?q=AI+Language+Models)
> { 💬 } [Natural Language Processing](https://www.google.com/search?q=Natural+Language+Processing)