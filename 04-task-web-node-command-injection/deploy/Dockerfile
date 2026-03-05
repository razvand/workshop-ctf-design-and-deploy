FROM node:14-alpine

WORKDIR /app

# Copy source code
COPY ./src/index.js .

# Copy flag to root
COPY ./flag /flag

# Set permissions
RUN chown root:root /flag && chmod 644 /flag

# Expose port
EXPOSE 3000

# Run the app
CMD ["node", "index.js"]
