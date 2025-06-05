# MVG Connections Flask App

Dieses Projekt stellt eine einfache Flask-Webanwendung bereit, um MVG-Verbindungen abzufragen. Der Quellcode wird beim Bauen des Containers automatisch von GitHub geladen – du benötigst also nur das folgende Dockerfile.

---

## Dockerfile

```dockerfile
FROM python:3.11
WORKDIR /app
RUN git clone https://github.com/Progaros/flask-app.git .
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["python", "app.py"]
```

---

## Ausführung

1. **Dockerfile speichern**  
   Speichere den obigen Inhalt als Datei mit dem Namen `Dockerfile` in ein leeres Verzeichnis.

2. **Docker-Image bauen**  
   Öffne ein Terminal im selben Verzeichnis und führe aus:
   ```
   docker build -t mvg-connections .
   ```

3. **Container starten**  
   Starte den Container mit:
   ```
   docker run -d --name mvg-connections -p 5346:5000 mvg-connections
   ```

4. **Webanwendung aufrufen**  
   Rufe im Browser [http://localhost:5346](http://localhost:5346) auf.
