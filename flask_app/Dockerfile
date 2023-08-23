# Base image
FROM alpine:3.14

# Install python and pip
RUN apk add --update python3 py3-pip

# Set the working directory
WORKDIR /usr/src/app

# Install python module needed by the app
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the files needed by the app to run
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# Tell the port number the container should expose
EXPOSE 5000

# Run the application
CMD ["python3", "app.py"]
