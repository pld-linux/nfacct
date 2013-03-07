Summary:	Userspace netfilter accounting management utility
Summary(pl.UTF-8):	Program przestrzeni użytkownika do zarządzania infrastrukturą rozliczania netfiltra
Name:		nfacct
Version:	1.0.1
Release:	1
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://www.netfilter.org/projects/nfacct/files/%{name}-%{version}.tar.bz2
# Source0-md5:	992e863409d144350dbc8f0554a0f478
URL:		http://www.netfilter.org/projects/nfacct/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6
BuildRequires:	libmnl-devel >= 1.0.0
BuildRequires:	libnetfilter_acct-devel >= 1.0.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libmnl >= 1.0.0
Requires:	libnetfilter_acct >= 1.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nfacct is the command line tool to create/retrieve/delete accounting
objects.

%description -l pl.UTF-8
nfacct to narzędzie linii poleceń do tworzenia/odczytu/usuwania
obiektów rozliczających.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/nfacct
%{_mandir}/man8/nfacct.8*
