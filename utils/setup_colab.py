import os


def download_github_code(path):
    filename = path.rsplit('/')[-1]
    os.system('shred -u {}'.format(filename))
    os.system('wget -q https://raw.githubusercontent.com/hse-aml/intro-to-dl-pytorch/main/{} -O {}'.format(path, filename))


def setup_week01():
    download_github_code('utils/grading.py')
    download_github_code('week01/data/train.npy')
    download_github_code('week01/data/target.npy')


def setup_week02():
    download_github_code('utils/grading.py')


def setup_week02_honor():
    download_github_code('utils/tqdm_utils.py')
    download_github_code('utils/util.py')


def setup_week03_1():
    download_github_code('utils/grading.py')


def setup_week03_2():
    download_github_code('utils/tqdm_utils.py')
    download_github_code('utils/download_utils.py')
    download_github_code('utils/grading.py')


def setup_week04():
    download_github_code('week04/lfw_dataset.py')
    download_github_code('utils/tqdm_utils.py')
    download_github_code('utils/download_utils.py')
    download_github_code('utils/grading.py')


def setup_week05():
    download_github_code('utils/grading.py')
    download_github_code('week05/names.txt')


def setup_week06():
    download_github_code('utils/grading.py')
    download_github_code('week06/beheaded_inception3.py')
    download_github_code('week06/grading_utils.py')
    os.system('wget -qO- https://github.com/hse-aml/intro-to-dl-pytorch/releases/download/final_project/handout.tar.gz | tar -xzvf - -C .')

    for i in range(30):
        os.system(f'wget -q https://raw.githubusercontent.com/hse-aml/intro-to-dl-pytorch/main/week06/data/img_{i}.jpg -O data/img_{i}')
