import json
import jwt
from flask import Flask, request




from jwt import JWT, jwk_from_dict
from jwcrypto.jwk import JWK




SECRET_KEY = "hkBxrbZ9Td4QEwgRewV6gZSVH4q78vBia4GBYuqd09SsiMsIjH"
def generate_keys():
    jwk = JWK.generate(kty = "RSA", size = 2048, alg = "R256", use = "sig", kid = SECRET_KEY)
    return jwk.export_private(as_dict = True), jwk.export_public(as_dict = True)




flask_app = Flask(__name__)
@flask_app.route('/auth', methods=['GET', 'POST'])
def loginFunction():
    #Generate token
    private_key, public_key = generate_keys()
    #Send the client the JSON we just made
    return  flask_app.response_class(response=json.dumps(public_key), mimetype='application/json')








@flask_app.route("/", methods = ['GET', 'POST', 'PATCH'])
def jsonGrabberFunction():
    #content = decode(request.get_json, private_key)
    #print(content)
    return "This is a test of the emergency alert system"
   


if __name__ == "__main__":
    private_key_instance, public_key_instance = generate_keys()
    flask_app.run(port=8080, debug=True)















