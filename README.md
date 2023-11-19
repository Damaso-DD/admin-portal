# Files required for Flask API portal

## Instructions:

Build the new image:

1. Change to `flask-api` directory: `cd flask-api`
2. Edit `requirements.txt`, `Dockerfile`, `flask-api.py`, and `vcluster-template.yaml` to suit your needs.
3. Build the image: `docker build -t YOUR_DOCKER_HUB_USERNAME/flask-api .`
4. Push the new image to Docker Hub: `docker push YOUR_DOCKER_HUB_USERNAME/flask-api`

Install the app in Kubernetes:

1. Go back to the root directory: `cd ..`
2. Edit `secrets.yaml` and add the values corresponding to: `LOFT_DOMAIN` and `ACCESS_KEY`.
3. Deploy the application: `kubectl apply -k ./` 