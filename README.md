# docker_test

### Build image
```shell
sudo docker build -t dt . 
```

### Start container
```shell
sudo docker run --rm -p 8080:8080 -v <Your_local_path_to_src_folder>:/usr/src --name <container_name> dt
```

---

## Some docker commands

### Show all containers
```shell
sudo docker ps -a
```

### Show images
```shell
sudo docker images
```

### Remove container
```shell
sudo docker rm <container_ID>
```

### Remove image
```shell
sudo docker rmi <image_ID>
```

### Execution command in container
```shell
sudo docker exec -it <container_ID> <command>
```
or
```shell
sudo docker exec <container_ID> <command>
```
