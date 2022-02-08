[![build-test](https://github.com/darkwizard242/ansible-role-jq/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-jq/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-jq/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-jq/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/49017?color=dark%20green) ![Ansible Role](https://img.shields.io/ansible/role/d/49017?color=dark&style=flat-square) ![Ansible Quality Score](https://img.shields.io/ansible/quality/49017?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-jq&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-jq) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-jq&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-jq) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-jq&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-jq) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-jq&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-jq) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-jq?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-jq?color=orange&style=flat-square)

# Ansible Role: jq

Role to install (_by default_) [jq](https://github.com/stedolan/jq) package or uninstall (_if passed as var_) on **Debian** family and **EL** family systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
jq_app: jq
jq_desired_state: present
```

### Variables table:

Variable         | Description
---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------
jq_app           | Defines the app to install i.e. **jq**
jq_desired_state | Defined to dynamically chose whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Defaults to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **jq** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.jq
```

For customizing behavior of role (i.e. installation of latest **jq** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.jq
  vars:
    jq_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **jq** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.jq
  vars:
    jq_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-jq/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
