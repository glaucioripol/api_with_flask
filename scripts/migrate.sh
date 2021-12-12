export IS_DEV="1"
export FLASK_APP=app 
flask db upgrade 
flask db migrate