FROM alpine:latest

RUN apk update && apk add zip

WORKDIR /publish

# This image expects the generated images to be mounted/copied here
# Then it zips them
CMD ["zip", "-r", "broken_glass.zip", "."]
