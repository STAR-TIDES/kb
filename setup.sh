set -eux

cd frontend/star-tides
npm i -g @angular/cli@latest
ng build --no-verbose --deploy-url='/static/'
cd -
rm -rf star_tides/static/*
cp -r frontend/star-tides/dist/star-tides/* star_tides/static/
ls -l star_tides/static

python3 run.py