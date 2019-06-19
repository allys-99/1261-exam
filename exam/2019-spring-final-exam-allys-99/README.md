# CEBD-1261 - Big Data Infrastructure / Final Exam / June 15th, 2019

To get a working project stored in your own private GitHub repo generated from https://classroom.github.com/a/Fm4TqvnO , your task is to fill all the `<TODO>` missing parts (could be part of code, some shell command, etc.) in this README.md file as well as in all available files. You might also have to create new files.

You might also have to fill some check boxes (look at the markdown code):
- [ ] No
- [x] Yes

All of your modifications & new files have to be shared at the end of this exam with your instructor through GitHub.

**I strongly suggest you to commit & push regularly your repo to GitHub**.

Some guidelines:
- 3 hours maximum (strong deadline) - **Starts at 1:45pm, Ends at 4:45pm** -
- Free Access to the Internet, including Search Engine, GCP, your own projects & the content of this course (_but absolutely no plagiarism between you, nor external help!_)

Your main goal is to create a tool to decode encrypted messages by computing letters frequency.
https://www.dcode.fr/monoalphabetic-substitution

:bulb: Have a quick look at the provided files.

## Start a Spark Cluster in Docker Swarm

```shell
docker stack deploy --compose-file=stack-spark.yml spark
```

The name of the deployed Docker Stack is: `spark`

To list all the services running on that stack:

```shell
docker stack services spark
```

## Make sure that there is 2 Spark Workers running

```shell
docker ps
```

## Count Words

Complete the [count_letters.py](count_letters.py]) Python Script that will count all the words of the [encrypted.txt](encrypted.txt) file.

Deploy & run that script in the Spark Cluster. To do so, what option do you choose?
- [x] Manual Copy of the Script
- [ ] Dockerfile
- [ ] Bind Mount
- [ ] Docker Volume

In few words, why did you choose that option?
> `It was the easiest.`

In what kind of environment it is meant to be used?
> `If we need to get something done and just recuperate the results then this is a good choice`
> `For large amounts of data, it is better to use the volume so that the data is saved when the image is no longer needed.`

The actual command(s) used:
```shell
docker cp script/count_letters.py $CONTAINER_ID:/tmp
docker cp data/encrypted.txt $CONTAINER_ID:/tmp
docker cp data/encrypted.txt $WORKER_ID:/tmp
docker exec $CONTAINER_ID   bin/spark-submit     --master spark://master:7077     --class endpoint     /tmp/count_letters.py
```

Snippet of the output of the script (_to be completed with your own output_):
```
+----+-----+
|word|count|
+----+-----+
|    |   12|
|   T|    9|
|   M|    9|
|   A|    8|
|   O|    6|
|   F|    6|
|   L|    4|
|   R|    4|
|   E|    4|
|   S|    4|
|   W|    3|
|   G|    3|
|   Z|    3|
|   K|    2|
|   B|    2|
|   Y|    2|
|   V|    1|
|   N|    1|
|   D|    1|
|   U|    1|
+----+-----+
only showing top 20 row

```

## Embedded files / DockerHub

* Define a Dockerfile that extends _the `spark` image used in the Spark Cluster_ to embed into this new image (under `/script`) the [count_letters.py](count_letters.py]) script.

* Build locally your image called `count_letter`, with `v1` as its tag.

```shell
Docker build -t count_letter:v1 .
Sending build context to Docker daemon  4.639MB
Step 1/2 : FROM mjhea0/spark:2.4.1
 ---> 15823becb013
Step 2/2 : COPY script/count_letters.py /script/
 ---> 467f33d98c11
Successfully built 467f33d98c11
Successfully tagged count_letter:v1
```

* Create a `files-volume` Docker Volume that contains the [encrypted.txt](encrypted.txt) file.

```shell
docker volume create files-volume

docker run --rm -v "$(pwd)"/data:/data -v files-volume:/volume busybox cp -r /data/ /volume

```

* Redefine the [stack-spark.yml](stack-spark.yml) file (renamed `stack-spark-volume.yml`) to make use of the new image and the `files-volume` volume.

* Redeploy the Spark Cluster using that new definition of the stack.

* Retest your script

```shell
<TODO>
```

## Jupyter & MongoDB Deployments

Deploy both [Jupyter](stack_jupyter.yml) & MongoDB + MongoDB Express on your existing Spark Cluster.

:bulb: MongoDB should use an external volume (why? `<TODO>`) called `mongo-db`, mounted as `/data/db`.

Also, the `root` & `admin` `PASSWORD`s of MongoDB & MongoDB Express should be `CEBD.1261`.

```shell
<TODO>
```

## Jupyter Notebook

Create & Run in Jupyter a notebook that will count the letters of [encrypted.txt](encrypted.txt), then saves (in "overwrite" mode) those counts into the `encrypted.count` Database / Collection of MongoDB.

- Download that Jupyter notebook and save it along this README.md file
- Export the corresponding JSon file from MongoDB Express and save it along this README.md file

## On GCP - _OPTIONAL_

To get extra points, replicate the usage of the [count_letters.py](count_letters.py]) script on your GCP environment.
- Document what you did through screenshots & notebook exports.
