# EXPORT HOST TO RUN FLASK APP
export FLASK_ENV=production
export FLASK_RUN_PORT=3333 
export FLASK_APP=app
export IS_DEV='0'
# flask run --host '0.0.0.0'
waitress-serve --call --listen=0.0.0.0:3333 'app:create_app'