Name:       bigger-spacebar
Version:    0.1
Release:    1%{?dist}
Summary:    Patch to increase spacebar size in Jolla keyboard
License:    LGPLv2
Source:     %{name}.tar.gz
URL:        https://github.com/toxip/bigger-spacebar
BuildArch:  noarch
Packager:   toxip
Requires:   patchmanager
Requires:   sailfish-version >= 2.1.4

%description
Improves keyboard usability by increasing the size of spacebar in Jolla keyboard

%define debug_package %{nil}

%prep
%setup -q -n %{name}

%build
%qmake5

%install
rm -rf %{buildroot}
%qmake5_install

%files
/usr/share/patchmanager/patches/%{name}/

%pre
if [ -d /usr/share/patchmanager/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%preun
/usr/sbin/patchmanager -u %{name} || true

%changelog

* Sat May 26 2018 Topias Vainio <toxip@disroot.org> 0.1-1
- Initial release
