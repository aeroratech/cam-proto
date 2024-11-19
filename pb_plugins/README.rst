======================================
Autogenerator for the MAVCam
======================================

Install instructions
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    pip install -r requirements.txt
    pip install -e .


How to use it
~~~~~~~~~~~~~

.. code-block:: bash

    export TEMPLATE_PATH="$(pwd)/templates/swift"
    protoc --plugin=protoc-gen-custom=$(which protoc-gen-mavcam) \
            -I../protos \
            --custom_out=. \
            --custom_opt="file_ext=swift,template_path=${TEMPLATE_PATH}" \
            ../protos/action/action.proto

