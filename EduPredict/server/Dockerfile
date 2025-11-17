# Use a base image that supports both Node.js and Python
FROM node:18-alpine

# Install Python and pip
RUN apk add --no-cache python3 py3-pip

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install Node.js dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Install Python dependencies
RUN python3 -m pip install --no-cache-dir -r microservice/requirements.txt

# Expose the port
EXPOSE 5000

# Start the application
CMD ["npm", "start"]