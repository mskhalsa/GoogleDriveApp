FROM python:3.11-slim
WORKDIR /app

# copy all project files -> container
COPY . .

# instal all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# open port 5002
EXPOSE 5002

# set flask env vars
ENV FLASK_APP=wsgi.py
ENV FLASK_RUN_PORT=5002
ENV FLASK_ENV=production

# run the app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5002", "wsgi:app"]
