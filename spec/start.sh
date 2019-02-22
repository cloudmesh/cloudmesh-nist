#!/bin/sh
rm -rf .spec.yaml; cms openapi merge > /tmp/.spec.yaml; cp /tmp/.spec.yaml .; cms openapi codegen; python server.py
