#!bin/bash
set -e
cd topper
npm install
npm run build
cp ../_redirects topper/build/
