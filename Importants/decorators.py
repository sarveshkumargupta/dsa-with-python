
import time
import random


def note_time(func):
    def wrapper(*args, **kwargs):

        start = time.time()

        print("Pre-processing the args -> ", args, kwargs)

        res = func(*args, **kwargs)

        print("Total time taken -> ", time.time() - start)

        return res

    return wrapper


@note_time
def file_uploader(file_path, url=None):
    time.sleep(random.randint(2, 3))
    return f"Uploaded a file to {file_path} and {url}"


file_uploader("file_path", url="AWS S3")



