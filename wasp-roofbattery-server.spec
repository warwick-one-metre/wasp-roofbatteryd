Name:      wasp-roofbattery-server
Version:   1.1.0
Release:   0
Url:       https://github.com/warwick-one-metre/wasp-roofbatteryd
Summary:   Roof battery voltage monitor for the SuperWASP telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python36, python36-Pyro4, python36-pyserial, python36-warwick-observatory-common
Requires:  observatory-log-client, %{?systemd_requires}

%description
Roof battery voltage monitor for the SuperWASP telescope.

roofbatteryd recieves data from a custom voltmeter board and
makes the latest measurement available for other services via Pyro.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/roofbatteryd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/wasp_roofbattery.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/10-wasp-roofbattery.rules %{buildroot}%{_udevrulesdir}

%post
%systemd_post wasp_roofbattery.service

%preun
%systemd_preun wasp_roofbattery.service

%postun
%systemd_postun_with_restart wasp_roofbattery.service

%files
%defattr(0755,root,root,-)
%{_bindir}/roofbatteryd
%defattr(0644,root,root,-)
%{_udevrulesdir}/10-wasp-roofbattery.rules
%{_unitdir}/wasp_roofbattery.service

%changelog
