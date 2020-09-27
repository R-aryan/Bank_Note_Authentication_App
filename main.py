from src.inference.app_swager import app

# http://127.0.0.1:5000/apidocs/ url for running swagger
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=8000, debug=True)
