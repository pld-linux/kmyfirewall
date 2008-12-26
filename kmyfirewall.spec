Summary:	Frontend for iptables
Summary(pl.UTF-8):	Frontend dla iptables
Name:		kmyfirewall
Version:	1.1.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/kmyfirewall/%{name}-%{version}.tar.bz2
# Source0-md5:	707afe4bb8724148986fd80485f0da03
Patch0:		%{name}-desktop.patch
URL:		http://kmyfirewall.sourceforge.net/
BuildRequires:	arts-qt-devel
BuildRequires:	artsc-devel
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMyFirewall attempts to make it easier to setup iptables based
firewalls on Linux systems.

%description -l pl.UTF-8
KMyFirewall ułatwia konfigurację firewalli opartych na Linuksie i
iptables.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/kde3/lib*.so
%{_libdir}/kde3/lib*.la
%{_datadir}/apps/* # specify excplicit dirs here (to avoid packaging kde dirs)
%{_datadir}/config/kmyfirewallrc
%{_desktopdir}/kde/*
%{_iconsdir}/*/*/*/*
%{_datadir}/mimelnk/application/kmfrs.desktop
%{_datadir}/servicetypes/*.desktop
%{_datadir}/services/*.desktop
