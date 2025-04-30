from invoke import task

@task
def hello(c):
    print("Hello from PyInvoke!")