FROM python:3.9
WORKDIR /app
RUN PYTHONDONTWRITEBYTECODE=1
COPY requirement.txt /app/ 
RUN apt-get update && apt-get install libgl1 -y
RUN pip3 install --no-compile --no-cache-dir -r requirement.txt
Copy ./ /app/
CMD ["python3","flask_server.py"]
EXPOSE 5000
