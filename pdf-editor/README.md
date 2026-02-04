# Configuration

Add pdf editor docker container with name pdf-editor and local port 3000 and available from whole system

## Add local docker container from image with custom name

```bash
docker run -d --name pdf-editor -p 3000:8080 ghcr.io/alam00000/bentopdf:latest
```

## add symbolic link like below to make it executable from entire system

```bash
sudo ln -s /home/rloi/Documents/repo/automation/pdf-editor/pdf-editor.sh /usr/local/bin/pdf-editor
```