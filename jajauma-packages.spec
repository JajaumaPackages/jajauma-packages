Name:           jajauma-packages
Version:        1.0.0
Release:        1%{?dist}
Summary:        JajaumaPackages Yum Configuration

License:        MIT
URL:            packages.jajauma.exnet.su
Source0:        RPM-GPG-KEY-JajaumaPackages
Source1:        everything.repo

BuildArch:      noarch

%description
%{summary}.


%package        everything
Summary:        JajaumaPackages Yum Configuration (Everything)

%description    everything
%{summary}.


%prep


%build


%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}/etc/pki/rpm-gpg/
install -m644 %{SOURCE0} %{buildroot}/etc/pki/rpm-gpg/
install -d -m755 %{buildroot}/etc/yum.repos.d/
install -m644 %{SOURCE1} %{buildroot}/etc/yum.repos.d/jajauma-packages-everything.repo


%files everything
/etc/pki/rpm-gpg/RPM-GPG-KEY-JajaumaPackages
%config /etc/yum.repos.d/jajauma-packages-everything.repo


%changelog
* Thu Aug 10 2017 Jajauma's Packages <jajauma@yandex.ru> - 1.0.0-1
- Initial releas
