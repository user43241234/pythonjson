from flask import Flask, jsonify, json

app = Flask('app')

x = input("what is your username?")
y = input("what is your password?")
z = input("what is your school id")
a = input("what is your email?")
user_info = {
  "username": x,
  "password": y,
  "school id": z,
  "email": a
}
with open('save.json', 'w') as f:
  json.dump(user_info, f)
with open('pass.lock', 'w') as f:
  write(y)


@app.route('/')
def hello_world():
  name = {
    "username": x,
    "password": y,
    "school id": z,
    "email": a
  }
  return jsonify(name)

app.run(host='0.0.0.0', port=8080)
