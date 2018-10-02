Add a FaaS example for implementation idea. We already had this more or less previously, but due to teh switch to OpenAPI this is less obvious. We need to implement two different backends. One for FaaS and one for a bigger footprint for REST service hosting.

cm generate -in function.yaml

This is an interface and not an API!

function.yaml:
---
function:
    name: k-means
  - parameters:
    - x-list
    - y-list
  - output:
    - map-list
  - implementation:
    - runtime: python3.7
    - kmeans.py
  - resources:
    - memory: 1KB
    - time: <10s
  - provider: AWSlamda



can generate rest call


serverless computing example
- go to AWS lambda
- go to others openwhisk
- go to Azure

