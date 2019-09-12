# Docker pull base image
FROM python:3.7-slim

# Run Update
RUN apt-get update -y && apt-get clean

#Create Directories
RUN mkdir -p /opt/query_rest_api/query_api

# Working Directory
WORKDIR /opt/query_rest_api/

# Copy files
COPY requirements.txt /opt/query_rest_api/
COPY query_api/*.py /opt/query_rest_api/query_api/
COPY app.py /opt/query_rest_api/

# Install python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Export variables
ENV PYTHONPATH=${PYTHONPATH}:"/opt/query_rest_api/query_api"
ENV API_DOMAIN=http://localhost:5000
ENV FLASK_DEBUG=0
ENV FLASK_RUN_PORT=5000

# Enable Port
EXPOSE ${FLASK_RUN_PORT}

#
ENTRYPOINT [ "python", "-u", "/opt/query_rest_api/app.py" ] 

#
CMD ["/bin/bash"]