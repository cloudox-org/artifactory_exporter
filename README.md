# Artifactory Exporter

[![RPM builds for EL8, EL9 and EL10](https://github.com/cloudox-org/artifactory_exporter/actions/workflows/rpm-build.yml/badge.svg?branch=main)](https://github.com/cloudox-org/artifactory_exporter/actions/workflows/rpm-build.yml)

Artifactory Exporter RPM builds for EL8,EL9 and EL10

RPM repo available here:

<https://rpms.cloudox.org/prometheus/>

This repo prioritizes LTS releases and overall stability for EL releases

Setup:

* Add the following to `/etc/yum.repos.d/prometheus.repo` for the desired platform.
example:

```bash
[prometheus-10]
name=prometheus 10
baseurl=https://rpms.cloudox.org/prometheus/el10/
gpgcheck=1
enabled=1
gpgkey=https://rpms.cloudox.org/prometheus/gpgkeys/RPM-GPG-KEY-prometheus-rpm
```
