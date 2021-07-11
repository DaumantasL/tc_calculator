FROM python:3.8-alpine
COPY . /calculator_root
WORKDIR /calculator_root
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD python ./setup.py install
