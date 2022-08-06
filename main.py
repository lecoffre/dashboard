import os, multiprocessing, time

def f1():
    time.sleep(10)
    os.system('python dashboard.py')
def f2():
    os.system('python site_dashboard_django/manage.py migrate')
    os.system('python site_dashboard_django/manage.py runserver 8080')


if __name__ == '__main__':
  p1 = multiprocessing.Process(target=f1)
  p1.start()
  p2 = multiprocessing.Process(target=f2)
  p2.start()
  p1.join()
  p2.join()