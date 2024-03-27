
## Step 1:
### install jukeboxAI from official github
[Official github](https://github.com/openai/jukebox)

### INSTALL COMMANDS

```
conda create --name jukebox python=3.7.5
conda activate jukebox
conda install mpi4py=3.0.3 # if this fails, try: pip install mpi4py==3.0.3
conda install pytorch=1.4 torchvision=0.5 cudatoolkit=10.0 -c pytorch
git clone https://github.com/openai/jukebox.git
cd jukebox
pip install -r requirements.txt
pip install -e .

conda install av=7.0.01 -c conda-forge 
pip install ./tensorboardX
pip install apex
```
### Install trouble shoot

**UnicodeEncodeError: 'ascii' codec can't encode character '\xe9' in position 13: ordinal not in range(128)**
PYTHONIOENCODING=UTF-8
https://github.com/pypa/pip/issues/10219
SOLUTIONS:
- reduce sample_length_in_seconds
- reduce n_samples


**torchvision=0.5.0 is not available through conda:**
__Option 1: use pip__
[Can not install torchvision 0.5.0 using conda](https://discuss.pytorch.org/t/can-not-install-torchvision-0-5-0-using-conda/176542)
Used [pip install torchvision\==0.5.0](https://pypi.org/project/torchvision/0.5.0/) instead of conda

**torchvision=0.3 is available**
__Option 2: use torchvision=0.3__

**ImportError: libffi.so.7: cannot open shared object file: No such file or directory**
`sudo apt install libffi7`
https://askubuntu.com/questions/1286772/libffi-so-7-cannot-open-shared-object-file-no-such-file-or-directory
#libffi

**RuntimeError: cublas runtime error : the GPU program failed to execute at /tmp/pip-req-build-pb3z3zl3/aten/src/THC/THCBlas.cu:315**
Install newest versions 

## Step 2: 
## install local_jukeboxAI 
[Official github](https://github.com/xiscoding/local_jukeboxAI.git)
``` bash
git clone https://github.com/xiscoding/local_jukeboxAI.git
```

## Step 3:
### copy files from jukeboxAI into local_jukeboxAI

## RUNNING THE CODE
### runprompted.py 
    - Generates a continuation from sample audio file(s)
    - uses a file selector gui 
    - run and follow prompts