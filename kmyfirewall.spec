Summary:	Frontend for iptables
Summary(pl):	Frontend dla iptables
Name:		kmyfirewall
Version:	0.9.6.2
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/kmyfirewall/%{name}-%{version}.tar.bz2
# Source0-md5:	6237add44c0fe8af1f725a2e259ddba3
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

%description -l pl
KMyFirewall u³atwia konfiguracjê firewalli opartych na Linuksie i
iptables.

%prep
%setup -q

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

# FIXME (desktop file name)
mv $RPM_BUILD_ROOT%{_datadir}/applnk/System/kmyfirewall.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

# FIXME (category)
echo "Categories=Qt;KDE;System;" >> \
	$RPM_BUILD_ROOT%{_desktopdir}/kde/kmyfirewall.desktop

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
%{_datadir}/apps/*
%{_datadir}/config/kmyfirewallrc
%{_desktopdir}/kde/*
%{_iconsdir}/*/*/*/*
%{_datadir}/mimelnk/application/kmfrs.desktop
