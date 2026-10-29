# Kubernetes Project

This document describes the Kubernetes configuration and manifests used in this project. 

### 1. Objective
GHCR (GitHub Container Registry) is a container registry, similar to Docker Hub, used to store and distribute container images.

In this project, Kubernetes uses an image pull secret (`ghcr-secret`) to authenticate with GHCR and pull our private Django application image.

### 2. Requirements
Before proceeding, make sure you have the following tools installed on your computer:
- Docker
- Minikube
- kubectl
- Access to GHCR and a token with the necessary permissions.

### 3. Access Configuration

#### 1. What is `ghcr-secret`?

GHCR (GitHub Container Registry) is a container registry used to store and distribute container images. Private images require appropriate credentials and permissions to be accessed.

`ghcr-secret` is a Kubernetes Secret that stores the credentials required to authenticate with GHCR and pull private container images.

#### 2. How do we create it?

First, authenticate with GHCR and publish the container image if it has not already been uploaded:

```
docker tag image_name ghcr.io/username/repo:1.0
echo "$GHCR_TOKEN" | docker login ghcr.io -u username --password-stdin
docker push ghcr.io/username/repo:1.0
```

Next, create an environment variable containing your GitHub token:

```
read -rsp "GitHub Token: " GHCR_TOKEN
echo
export GHCR_TOKEN
```

Create the Kubernetes Secret:

```
kubectl create secret docker-registry ghcr-secret \
  --docker-server=ghcr.io \
  --docker-username=username \
  --docker-password="$GHCR_TOKEN"
```

Replace `username` and the image name placeholders with the appropriate values for your project.

#### 3. How do we verify that it exists?

Run the following command:

```
kubectl get secrets
```

Check that `ghcr-secret` appears in the list.

### 4. Security

-   Never store your GitHub token in the repository.
    
-   Never commit credentials or other sensitive information to version control.
    
-   Use a token with the minimum permissions required to access the private package.
    
-   Avoid exposing your token in logs, screenshots, or shared terminal output.