Sample of a k8s controller kicking off a job

## Kubernetes Client Documentation
The kubernetes client is in a bunch of languages. These links point to the python versions for getting
jobs dynamically specced and loaded.

* API Docs: https://k8s-python.readthedocs.io/en/latest/README.html
* API Job Spec: https://github.com/kubernetes-client/python/blob/master/kubernetes/client/models/v1_job_spec.py#L21
* API BatchV1Api Spec: https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/BatchV1Api.md#list_job_for_all_namespaces
* Job Sample: https://github.com/kubernetes-client/python/blob/master/examples/job_crud.py
* General Samples: https://github.com/kubernetes-client/python/tree/master/examples

### Source:
Initial template for flask API borrowed from https://github.com/RikKraanVantage/kubernetes-flask-mysql
