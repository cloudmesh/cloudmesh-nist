# macOS

On macOS you can run the example simply by saying

```bash
$ make
```

This will open up one terminal, run the servoer in it. Then it will wait for 3 seconds and issue a curl call agoinst the server.

# Other OS

In case you have another OS you can open two terminals and go to the source directory.

IN the first terminal you run 

```bash
$ python server.py
```

In the second terminal you run the curl call 

```bash
curl http://localhost:8080/cloudmesh/cpu
```

# Tips

Make sure you have python properly configured and run it on a moder OS such as Ubuntu 18.04 or 18.10. We recommend using pyenv to be able to run it easily on differnt versions of python. The code has been tested by many undergraduate and graduate studenst as well as our research collaborators. If you run into issues, make first sure your environment is properly set up. Please note that we do require that python is set to python 3. If you run it with python3 instead of python you may need to change things. To avoid any such issues, just use pyenv. IT is trivial to install on macOS and Ubuntu following our notes in our cloud handbook. 
