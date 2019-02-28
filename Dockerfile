FROM ubuntu:18.04

RUN ln -s /usr/share/zoneinfo/Etc/GMT+7 /etc/localtime
RUN apt update \
    && apt install -y git python3 \
    python3-pip \
    libsm6 \
    libxext6 \
    libfontconfig1 \
    libxrender1 \
    python3-tk

RUN git clone https://github.com/vimentor-com/pythonbackenddemo.git
RUN cd pythonbackenddemo && \
    git checkout 6-gunicorn-flask && \
    pip3 install -r requirements.txt
RUN mkdir -p ~/.config/matplotlib/
RUN touch ~/.config/matplotlib/matplotlibrc
RUN echo "backend: Agg" > ~/.config/matplotlib/matplotlibrc

ENTRYPOINT ["/bin/bash", "/pythonbackenddemo/entrypoint.sh"]
