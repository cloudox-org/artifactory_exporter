%global debug_package %{nil}
%global user prometheus
%global group prometheus

Name: alertmanager
Version: 0.31.1
Release: 1%{?dist}
Summary: Prometheus Alertmanager.
License: ASL 2.0
URL:     https://github.com/prometheus/alertmanager

Source0: https://github.com/prometheus/alertmanager/releases/download/v%{version}/%{name}-%{version}.linux-amd64.tar.gz
Source1: %{name}.unit
Source2: %{name}.default

%{?systemd_requires}
Requires(pre): shadow-utils

%description
The Alertmanager handles alerts sent by client applications such as the
Prometheus server. It takes care of deduplicating, grouping, and routing them to
the correct receiver integration such as email, PagerDuty, or OpsGenie. It also
takes care of silencing and inhibition of alerts.

%prep
%setup -q -n %{name}-%{version}.linux-amd64

%build
/bin/true

%install
mkdir -vp %{buildroot}%{_sharedstatedir}/prometheus
install -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/default/%{name}
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 755 amtool %{buildroot}%{_bindir}/amtool
install -D -m 640 alertmanager.yml %{buildroot}%{_sysconfdir}/prometheus/alertmanager.yml

%pre
getent group prometheus >/dev/null || groupadd -r prometheus
getent passwd prometheus >/dev/null || \
useradd -r -g prometheus -d %{_sharedstatedir}/prometheus -s /sbin/nologin -c "Prometheus services" prometheus
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/default/%{name}
%dir %attr(755, %{user}, %{group}) %{_sharedstatedir}/prometheus
%{_unitdir}/%{name}.service
%attr(755, -, -)%{_bindir}/amtool
%config(noreplace) %attr(640, -, %{group})%{_sysconfdir}/prometheus/alertmanager.yml

%changelog
* Wed Feb 18 2026 Ivan Garcia <igarcia@cloudox.org> - 0.31.1
- Update to Alertmanager 0.31.1
- Initial packaging for the 0.31.1 branch
