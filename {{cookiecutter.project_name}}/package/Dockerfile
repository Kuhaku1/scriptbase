FROM python:{{cookiecutter.version_python}}
COPY main.py /app/
COPY requirements.txt /app/requirements.txt
ADD pip.conf /root/.pip/
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY {{cookiecutter.package_name}}.tar.gz /app/
RUN pip install /app/{{cookiecutter.package_name}}.tar.gz
CMD ["python", "/app/main.py"]