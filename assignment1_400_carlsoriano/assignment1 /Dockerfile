# Use an official Python 3.7 image as the base image
FROM python:3.7

# Set the working directory inside the container
WORKDIR /app


# Create a volume named servervol
VOLUME /serverdata

# Copy your application files into the container
COPY . /app

# Set the command to run your application by default
CMD ["python", "app/text_gen.py"]
