import os


def set(path=None):
    if not path:
        path = get()

    resolved_path = os.path.abspath(path)
    os.environ['HF_HOME'] = resolved_path

def set_project(name):
    path = '~/.cache/shruggingface'
    set(path + '/' + name)


def create():
    path = get()
    os.makedirs(path, exist_ok=True)


def get():
    path = os.getenv("HF_HOME", "~/.cache/huggingface/")
    if not path.endswith('/'):
        path = path + '/'
    return os.path.expanduser(path)


def exists():
    path = get()
    return os.path.isdir(path)

