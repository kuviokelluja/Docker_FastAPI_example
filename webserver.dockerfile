FROM ubuntu:20.04 as development
EXPOSE 9999
RUN apt update && apt upgrade -y
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install python3.10 python3-pip -y
RUN apt-get install python3.10-distutils -y
COPY main.py /app/main.py
COPY api/ /app/api/
COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install --upgrade pip 
WORKDIR /app/
RUN python3 -m pip install -r ./requirements.txt
CMD ["python3", "./main.py"]

FROM development as builder
RUN python3 -m pip install pyinstaller
RUN python3 -m PyInstaller --onefile --name FastapiServer main.py
WORKDIR /app/dist/
CMD ["./FastapiServer"]

FROM frolvlad/alpine-glibc as production
COPY --from=builder /app/dist/FastapiServer /app/FastapiServer
WORKDIR /app
ENTRYPOINT ["./FastapiServer"]