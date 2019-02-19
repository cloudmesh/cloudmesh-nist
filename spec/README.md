# Create the NIST Spec

The specification will be written into a file called `.spec.yaml`. For now 
the period before the file name is important so it can be ignored in 
consecutive calles to `cms openapi`

Hence a good example on how to use it is:

```bash
git clone https://github.com/cloudmesh-community/nist.git
cd nist/spec
rm spec.yaml; cms openapi merge > /tmp/.spec.yaml; cp /tmp/.spec.yaml .
cms openapi codegen
python server.py 
```

In your web browser now put in 

* <http://127.0.0.1:8080/ui>