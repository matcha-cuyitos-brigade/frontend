# Frontend for a CPU simulator
***
## What is this?
an interactive frontend for a cpu simulator, created using HTML, Flask and NGINX, it runs on a docker container

## Folder structure
```bash
.
└── frontend_cpu
    ├── Dockerfile
    ├── nginx
    │   ├── mime.types
    │   └── nginx.conf
    └── templates
        ├── ALU_cuyo.jpg
        ├── CLOCK_cuyo.jpg
        ├── RAM_CUYO.jpg
        ├── REGIST_cuyo.jpg
        ├── addr_register.png
        ├── background.jpg
        ├── clock.png
        ├── controlunit.png
        ├── index.html
        ├── input1.png
        ├── input2.png
        ├── output.png
        ├── ram.png
        └── register.png
```
 ## Run Docker container
   clone the repo to your computer using: 
   ```bash
git clone <git link>
```
then go to the project directory using the following command:
```bash
cd <user>/frontend/frontend_cpu/
```
now it's really important that you already have docker on your computer, if you don't please stop here and go to https://docs.docker.com/docker-for-mac/install/ to install it

if you already have it installed, run the following commands:
```bash
docker build --rm -f "frontend_cpu/Dockerfile" -t webapp:0.1 frontend_cpu
docker run -d -p 5001:80 webapp:0.1
```
done! now click this link http://localhost:5001 to go to the frontend

