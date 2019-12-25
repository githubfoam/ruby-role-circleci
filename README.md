# ruby-role-circleci


=========

Circleci branch:
[![](https://img.shields.io/circleci/project/github/githubfoam/ruby-role-circleci/circleci.svg?style=plastic)](https://circleci.com/gh/githubfoam/ruby-role-circleci)  

~~~~

----------------

Playbook
----------------

molecule testinfra/goss travisci:

        - MOLECULE_SCENARIO=centos74-goss
        - MOLECULE_SCENARIO=centos74-testinfra
        - MOLECULE_SCENARIO=ubuntu1804-goss
        - MOLECULE_SCENARIO=ubuntu1804-testinfra

        Entrypoint case #1
        ```
        /vagrant/ruby-role$ sudo molecule list
        --> Validating schema /vagrant/ruby-role/molecule/default/molecule.yml.
        Validation completed successfully.
        Instance Name    Driver Name    Provisioner Name    Scenario Name    Created    Converged
        ---------------  -------------  ------------------  ---------------  ---------  -----------
        centos7          docker         ansible             sc-centos7-goss  false      false

        vagrant@control02:/vagrant/ruby-role$ sudo docker container ls
        CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

        (venv1) vagrant@control02:/vagrant/ruby-role$ sudo molecule create -s sc-centos7-goss

        (venv1) vagrant@control02:/vagrant/ruby-role$ sudo docker container ls
        CONTAINER ID        IMAGE                     COMMAND             CREATED             STATUS              PORTS               NAMES
        eda63d5f278f        molecule_local/centos:7   "/usr/sbin/init"    13 seconds ago      Up 10 seconds                           centos7

        (venv1) vagrant@control02:/vagrant/ruby-role$ sudo dgoss edit --entrypoint=/usr/sbin/init  molecule_local/centos:7
        INFO: Starting docker container
        INFO: Container ID: 847364f2
        INFO: Run goss add/autoadd to add resources
        sh-4.2#
        ```

        Entrypoint case #2
        ```
        sudo molecule create -s sc-ubuntu1804-goss
        (venv) vagrant@control01:/vagrant/ruby-role/molecule/ubuntu1804-goss/tests$ sudo docker container ls
        CONTAINER ID        IMAGE                          COMMAND                  CREATED             STATUS              PORTS               NAMES
        c406b4b7e5bd        molecule_local/ubuntu:bionic   "bash -c 'while true…"   38 minutes ago      Up 38 minutes                           bionic

        (venv) vagrant@control01:/vagrant/ruby-role/molecule/ubuntu1804-goss/tests$ sudo docker inspect molecule_local/ubuntu:bionic | grep Entrypoint
                    "Entrypoint": null,
                    "Entrypoint": null,

        sudo dgoss edit -it --entrypoint="" molecule_local/ubuntu:bionic bash
        ```
        Experimental
        ```
        sudo molecule login -s sc-ubuntu1804-goss
        sudo docker inspect molecule_local/ubuntu:bionic | grep Entrypoint
                    "Entrypoint": null,
                    "Entrypoint": null,

        sudo dgoss edit -it --entrypoint="" molecule_local/ubuntu:bionic bash
        ```


License
-------

GNU General Public License v3.0

Author Information
------------------

An optional section for the role authors

~~~~
