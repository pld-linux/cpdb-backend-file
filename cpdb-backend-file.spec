Summary:	File Common Print Dialog Backend
Summary(pl.UTF-8):	Backend plikowy dla CPDB (wspólnych okien dialogowych drukowania)
Name:		cpdb-backend-file
Version:	1.0.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/OpenPrinting/cpdb-backend-file/releases
Source0:	https://github.com/OpenPrinting/cpdb-backend-file/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c397d593e4415b9dd5b2f9866488ce0f
URL:		https://github.com/OpenPrinting/cpdb-backend-file
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
# pkgconfig(cpdb-libs-backend)
BuildRequires:	cpdb-libs-devel >= 1.2.0
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	pkgconfig
Requires:	cpdb-libs >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the File Common Print Dialog Backend. This
backend manages and provides information about printing to a file
via the printing dialog.

%description -l pl.UTF-8
Ten pakiet zawiera backend plikowy dla CPDB (Common Printing Dialog
Backends - wspólnych backendów okien dialogowych drukowania). Ten
backend zarządza i dostarcza informacje o drukowaniu do pliku.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%attr(755,root,root) %{_libdir}/print-backends/file
%{_datadir}/dbus-1/services/org.openprinting.Backend.FILE.service
%{_datadir}/print-backends/org.openprinting.Backend.FILE
