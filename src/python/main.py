import logging

from flask import Flask, request, jsonify

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)


@app.route('/userinfo')
def userinfo():
    role = request.headers.get('x-role')   

    if role == "anonym":
        return "user not logged in", 403
     
    return jsonify({
        "id": request.headers.get('x-mail'),
        "username": request.headers.get('x-given_name')+" "+request.headers.get('x-family_name')   ,
        "email": request.headers.get('x-mail'),
        "displayName": request.headers.get('x-given_name'),
        "role": role
    })

if __name__ == '__main__':
    print("AuthZ Server Up and running")
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=False)


