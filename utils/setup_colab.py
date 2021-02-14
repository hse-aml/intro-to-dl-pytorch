import os


def download_github_code(path):
    filename = path.rsplit('/')[-1]
    os.system('shred -u {}'.format(filename))
    os.system('wget https://raw.githubusercontent.com/hse-aml/intro-to-dl-pytorch/main/{} -O {}'.format(path, filename))


def setup_week01():
    download_github_code('utils/grading.py')
    download_github_code('week01/data/train.npy')
    download_github_code('week01/data/target.npy')


def setup_week02():
    download_github_code('utils/grading.py')
