Ansible role: Git
=========

his Ansible role manages cloning, checking out branches or tags, and updating repositories from Git sources. It simplifies Git operations in automation workflows and is suitable for use in CI/CD pipelines, application builds, or configuration sync tasks.

Requirements
------------

This role depends on the following Ansible roles to be applied beforehand:

- A git role (e.g., [geerlingguy.git]) – to install and configure git

Role Variables
--------------

List of variables in ansible-role-build:

```sh
---
git_host: "github.com"
git_version: "HEAD"
git_repository: ""
git_destination: ""
git_force: true
git_depth: 1

git_user: "root"
git_token: ""

# linux related
git_linux_user: "{{ git_user }}"
```

Dependencies
------------

This role depends on the following Ansible roles:

- `git_installer`: Installs and configures git

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - geerlingguy.git
    - devetek.git
```

License
-------

GNU General Public License v3.0 or later

Author Information
------------------

[Nedya Prakasa]. Role created for [dPanel].

[dPanel]: https://cloud.terpusat.com/
[Nedya Prakasa]: https://github.com/prakasa1904
[devetek]: https://github.com/devetek
[geerlingguy.git]: https://galaxy.ansible.com/ui/standalone/roles/geerlingguy/git/