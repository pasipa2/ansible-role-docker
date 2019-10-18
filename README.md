hukuru-ansible-role-docker
=========

This role installs and configure docker daemon.

Requirements
------------

None

Role Variables
--------------

Available variables are listed in default values (see `defaults/main.yml`):

Dependencies
------------

Tested on Centos 7 only

Example Playbook
----------------

```yaml
- hosts: all

  vars:
    docker_users: ['test']

  roles:
    - hukuru-ansible-role-docker
```

License
-------

BSD

Author Information
------------------

This role was created in by [hukuruIO](https://www.hukuru.io/)
