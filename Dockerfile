FROM python

RUN pip install docker-py feedparser nosexcover prometheus_client pycobertura pylint pytest pytest-cov requests setuptools sphinx

RUN wget -qO /usr/local/bin/qcoverage  https://github.com/qnib/qcoverage/releases/download/v0.1/qcoverage_v0.1_Linux \
 && chmod +x /usr/local/bin/qcoverage


COPY ./sources/ ./flask_project
RUN cd flask_project/ && ls -lrt
RUN pip install -r ./flask_project/requirements.txt

