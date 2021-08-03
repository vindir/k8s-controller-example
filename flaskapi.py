"""Code for a flask API to Create, Read, Update, Delete users"""
import os
from time import sleep
from pprint import pprint
from flask import jsonify, request, Flask

import kubernetes.client
import kubernetes.config
from kubernetes.client.rest import ApiException
from k8s_job_handlers import *

app = Flask(__name__)

app.config["SAMPLE_ENV_CONFIG"] = os.getenv("env_config_sample")

@app.route("/")
def index():
    """Function to test the functionality of the API"""
    return "Hello, world!"


@app.route("/list_jobs", methods=["POST"])
def list_jobs():
    configuration = kubernetes.client.Configuration()
    with kubernetes.client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = kubernetes.client.BatchV1Api(api_client)
        pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
        timeout_seconds = 30 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
        try:
            api_response = api_instance.list_job_for_all_namespaces( pretty=pretty, timeout_seconds=timeout_seconds )
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling BatchV1Api->list_job_for_all_namespaces: %s\n" % e)


@app.route("/create/<job_name>", methods=["POST"])
def add_job(job_name = "GenericJob"):
    """Function to create a job"""
    json = request.json
    try:
        config.load_kube_config()
        batch_v1 = kubernetes.client.BatchV1Api()
        job = create_job_object(job_name)
        create_job(batch_v1, job, job_name)
        resp = jsonify("Job created successfully!")
        resp.status_code = 200
        return resp
    except Exception as exception:
        return jsonify(str(exception))


@app.route("/update/<job_name>", methods=["POST"])
def update_job(job_name = "GenericJob"):
    """Function to update a job"""
    json = request.json
    try:
        config.load_kube_config()
        batch_v1 = kubernetes.client.BatchV1Api()
        job = create_job_object(job_name)
        update_job(batch_v1, job, job_name)
        resp = jsonify("Job updated successfully!")
        resp.status_code = 200
        return resp
    except Exception as exception:
        return jsonify(str(exception))


@app.route("/delete/<job_name>")
def delete_job(job_name = "GenericJob"):
    """Function to delete a job"""
    json = request.json
    try:
        config.load_kube_config()
        batch_v1 = kubernetes.client.BatchV1Api()
        delete_job(batch_v1, job_name)
        resp = jsonify("Job deleted successfully!")
        resp.status_code = 200
        return resp
    except Exception as exception:
        return jsonify(str(exception))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
