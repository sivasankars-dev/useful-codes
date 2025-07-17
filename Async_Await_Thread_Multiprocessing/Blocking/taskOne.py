import time

def task(name):
    print(f'{name} started')
    time.sleep(2)
    print(f'{name} finished')

def main():
    task('task1')
    task('task2')

print(main())