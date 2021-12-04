# Installation Instructions

## For Speech2Text Interface

1. Ensure you have a python-enabled environment through either Terminal or WSL2 or downloading Python3 from the Windows store
2. Ensure that [pip3](https://vgkits.org/blog/pip3-windows-howto/) is installed
3. Clone the git repository with `git clone https://github.com/muellerzr/capstone-2021/`
4. Perform the following in your bash terminal from the root directory of the repository:
```bash
pip3 install -r requirements.txt
```
5. You can verify that everything is installed correctly by performing `pip3 show transformers`. It should return a stable version