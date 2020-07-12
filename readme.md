# Long running process coding task
This project is on response of the given task

Solutions: I have build the on top of a Django a python framework. The long running task is managed by Celery a python package for running long running process in baground. you can find the code for the long running task on /src/monitor/apps/lrp/task.py. Thes task result is logged in to a databse table. The process runs on every 10th minute on clock time by celery beat.

### Installation
Put the csv file on the csv directory. The file must be on the given formate as on the instruction. Now open your terminal and go inside the project directory. 

Build docker image:

```
docker build -t monitor .
```
Run the test cases.

```
docker run -it monitor python /opt/app/src/manage.py test monitor --settings=monitor.settings.test
```
The following command run the project on port 8000

```
docker run --rm -it -p 8000:8000 monitor
```

### End points for summary result

Get summary
Url: http://127.0.0.1:8000/
```
    {
    "total_verified": 3, 
    "total_up": 2, 
    "total_down": 1, 
    "unique_sites": 3, 
    "unique_up_sites": 2, 
    "unique_down_sites": 1
    }
```
### CI/CD
I have added configeration file for CircleCi. Install circle ci on you local PC and run the test using CircleCI by the following command.

```
circleci local execute
```
The command will run the test with tox and also verify the coding style guidline. This script can be ferther improved adding ansible for automated deployment after test and verification of code.
