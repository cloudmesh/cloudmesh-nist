

cm generate -in function.yaml

function.yaml:
---
function: 
    name: k-means
  - parameters:
    - x-list
    - y-list
  - oupput:
    - map-list
  - implementation:
    - runtime: python3.7
    - a.py
  - resources:
    - memory: 1KB
    - time: <10s
  

can generate rest call


serverless computing example
- go to AWS lambda
- go to others openwhisk
- go to Azure

