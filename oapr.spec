Summary:	C++ wrapper on nspr
Summary(pl.UTF-8):	Wrapper C++ na nspr
Name:		oapr
Version:	0.2.1
Release:	0.1
Epoch:		0
License:	Apache Software License v1.1
Group:		Libraries
#Source0Download: http://www.openaether.org/oapr.html
Source0:	http://www.openaether.org/builds/%{name}-%{version}.tar.gz
# Source0-md5:	8fd9e8607c7574d2943f437877c0a8a0
URL:		http://www.openaether.org/oapr.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	libtool >= 2:1.4d-3
BuildRequires:	nspr-devel
BuildRequires:	ossp-uuid-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
oapr is wrapper on nspr libraries. This package contains shared
libraries.

%description -l pl.UTF-8
oapr jest wrapperem bibliotek nspr. Ten pakiet zawiera biblioteki
współdzielone.

%package devel
Summary:	Header files for oapr libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek oapr
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	boost-devel
Requires:	nspr-devel

%description devel
Header files for oapr libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek oapr.

%package static
Summary:	Static oapr libraries
Summary(pl.UTF-8):	Statyczne biblioteki oapr
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static oapr libraries.

%description static -l pl.UTF-8
Statyczne biblioteki oapr.

%prep
%setup -q

%build
# need libtoolize (C++ linking)
mkdir -p config
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-nspr-include=%{_includedir}/nspr

%{__make} \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/oapr
%{_includedir}/oapu
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
