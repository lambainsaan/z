from flask import Flask, request, jsonify
from dataparser import find_branch_by_ifsc, find_branches_by_name_city

app = Flask(__name__)



@app.route("/branch", methods=['GET'])
def get_branch_by_ifsc():
    try:
        ifsc = request.args['ifsc']
    except KeyError:
        return jsonify({"err": "Key ifsc not present in params."})


    return jsonify(find_branch_by_ifsc(ifsc))


@app.route("/branchInCity", methods=['GET'])
def get_branch_by_name_city():
    try:
        name = request.args['name']
        city = request.args['city']
    except KeyError as e:
        return jsonify({"err": f"{e.args[0]} not present in params."})

    return jsonify(find_branches_by_name_city(name, city))