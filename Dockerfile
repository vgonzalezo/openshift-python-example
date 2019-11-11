#FROM python:rc-alpine
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
#RUN apk add firefox-esr

#RUN apt update && apt-get install -y libxss1 libappindicator1 libindicator7 xvfb 
#RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#RUN apt install -y ./google-chrome*.deb
#RUN Xvfb :99 -ac && export DISPLAY=:99

RUN apt update
RUN apt-get install -y build-essential chrpath libssl-dev libxft-dev
RUN apt-get install -y libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/share/
RUN ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin
#RUN phantomjs --version

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080
CMD [ "python", "./base_flask.py"]
