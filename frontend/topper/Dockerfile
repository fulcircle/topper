# base image
FROM node:10.13.0

COPY package.json /frontend/
WORKDIR /frontend/
RUN npm install
ENV PATH /frontend/node_modules/.bin:$PATH

COPY . /frontend/topper/
WORKDIR /frontend/topper/

EXPOSE 3000

CMD npm start
