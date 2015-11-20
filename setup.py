#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from distutils.core import setup

setup(
    name="python-farekart",
    description="Generate KML and CAP files from text warnings in the TED database",
    author="B�rd Fjukstad",
    author_email="b.fjukstad@met.no",
    url="http://www.met.no/",
    version="0.2.5",
    py_modules=["generatecap", "fare_common", "generatecap_fare"],
    scripts=["faremeldinger.py", "metno-publish-cap.py", "cap2kml.py","generatecap_fare.py"],
    data_files=[("share/xml/farekart",["schemas/XMLSchema.xsd","schemas/CAP-v1.2.xsd","schemas/mifare-index.xsd"])]
    )
