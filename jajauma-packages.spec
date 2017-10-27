Name:           jajauma-packages
Version:        1.0.0
Release:        1%{?dist}
Summary:        JajaumaPackages Yum Configuration

License:        MIT
URL:            packages.jajauma.exnet.su
Source0:        RPM-GPG-KEY-JajaumaPackages
Source1:        jajauma-packages-everything.repo
Source2:        jajauma-packages-wine.repo
Source3:        jajauma-packages-server.repo
Source4:        jajauma-packages-development.repo
Source5:        jajauma-packages-neovim.repo
Source6:        jajauma-packages-doublecmd.repo
Source7:        jajauma-packages-ffmpeg.repo
Source8:        jajauma-packages-kernel.repo
Source9:        jajauma-packages-scientific.repo
Source10:       jajauma-packages-misc.repo

BuildArch:      noarch

%description
%{summary}.


%package        everything
Summary:        JajaumaPackages Yum Configuration (Everything)
%description    everything
%{summary}.

%package        wine
Summary:        JajaumaPackages Yum Configuration (Wine)
%description    wine
%{summary}.

%package        server
Summary:        JajaumaPackages Yum Configuration (Server)
%description    server
%{summary}.

%package        development
Summary:        JajaumaPackages Yum Configuration (Development)
%description    development
%{summary}.

%package        neovim
Summary:        JajaumaPackages Yum Configuration (Neovim)
%description    neovim
%{summary}.

%package        doublecmd
Summary:        JajaumaPackages Yum Configuration (Double Commander)
%description    doublecmd
%{summary}.

%package        ffmpeg
Summary:        JajaumaPackages Yum Configuration (FFmpeg)
%description    ffmpeg
%{summary}.

%package        kernel
Summary:        JajaumaPackages Yum Configuration (Linux Kernel)
%description    kernel
%{summary}.

%package        scientific
Summary:        JajaumaPackages Yum Configuration (Scientific)
%description    scientific
%{summary}.

%package        misc
Summary:        JajaumaPackages Yum Configuration (Miscellaneous)
%description    misc
%{summary}.

%prep


%build


%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}/etc/pki/rpm-gpg/
install -m644 %{SOURCE0} %{buildroot}/etc/pki/rpm-gpg/
install -d -m755 %{buildroot}/etc/yum.repos.d/
install -m644 %{SOURCE1} %{buildroot}/etc/yum.repos.d/jajauma-packages-everything.repo
install -m644 %{SOURCE2} %{buildroot}/etc/yum.repos.d/jajauma-packages-wine.repo
install -m644 %{SOURCE3} %{buildroot}/etc/yum.repos.d/jajauma-packages-server.repo
install -m644 %{SOURCE4} %{buildroot}/etc/yum.repos.d/jajauma-packages-development.repo
install -m644 %{SOURCE5} %{buildroot}/etc/yum.repos.d/jajauma-packages-neovim.repo
install -m644 %{SOURCE6} %{buildroot}/etc/yum.repos.d/jajauma-packages-doublecmd.repo
install -m644 %{SOURCE7} %{buildroot}/etc/yum.repos.d/jajauma-packages-ffmpeg.repo
install -m644 %{SOURCE8} %{buildroot}/etc/yum.repos.d/jajauma-packages-kernel.repo
install -m644 %{SOURCE9} %{buildroot}/etc/yum.repos.d/jajauma-packages-scientific.repo
install -m644 %{SOURCE10} %{buildroot}/etc/yum.repos.d/jajauma-packages-misc.repo


%files everything
/etc/pki/rpm-gpg/RPM-GPG-KEY-JajaumaPackages
%config /etc/yum.repos.d/jajauma-packages-everything.repo

%files wine
/etc/pki/rpm-gpg/RPM-GPG-KEY-JajaumaPackages
%config /etc/yum.repos.d/jajauma-packages-wine.repo

%files server
/etc/pki/rpm-gpg/RPM-GPG-KEY-JajaumaPackages
%config /etc/yum.repos.d/jajauma-packages-server.repo

%files development
/etc/pki/rpm-gpg/RPM-GPG-KEY-JajaumaPackages
%config /etc/yum.repos.d/jajauma-packages-development.repo

%files neovim
/etc/pki/rpm-gpg/RPM-GPG-KEY-JajaumaPackages
%config /etc/yum.repos.d/jajauma-packages-neovim.repo

%files doublecmd
/etc/pki/rpm-gpg/RPM-GPG-KEY-JajaumaPackages
%config /etc/yum.repos.d/jajauma-packages-doublecmd.repo

%files ffmpeg
/etc/pki/rpm-gpg/RPM-GPG-KEY-JajaumaPackages
%config /etc/yum.repos.d/jajauma-packages-ffmpeg.repo

%files kernel
/etc/pki/rpm-gpg/RPM-GPG-KEY-JajaumaPackages
%config /etc/yum.repos.d/jajauma-packages-kernel.repo

%files scientific
/etc/pki/rpm-gpg/RPM-GPG-KEY-JajaumaPackages
%config /etc/yum.repos.d/jajauma-packages-scientific.repo

%files misc
/etc/pki/rpm-gpg/RPM-GPG-KEY-JajaumaPackages
%config /etc/yum.repos.d/jajauma-packages-misc.repo


%changelog
* Tue Aug 22 2017 Jajauma's Packages <jajauma@yandex.ru> - 1.0.0-1
- Initial release
