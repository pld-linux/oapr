Summary:	C++ wrapper on apr
Summary(pl):	Wrapper C++ na apr
Name:		oapr
Version:	0.1.3
Release:	0.1
Epoch:		0
License:	Apache Software License v1.1
Group:		Libraries
#Source0Download: http://www.openaether.org/download.html
Source0:	http://www.openaether.org/builds/%{name}-%{version}.tar.gz
# Source0-md5:	c74b89e733ec33a65369ec020b4f16ba
URL:		http://www.openaether.org/
BuildRequires:	apr-util-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	libtool >= 2:1.4d-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
oapr is C++ wrapper on C library: apr. This package contains shared
libraries.

%description -l pl
oapr jest wrapperem C++ dla biblioteki C apr. Ten pakiet zawiera
biblioteki dzielone.

%package devel
Summary:	Header files for oapr libraries
Summary(pl):	Pliki nagłówkowe bibliotek oapr
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	apr-devel
Requires:	boost-devel

%description devel
Header files for oapr libraries.

%description devel -l pl
Pliki nagłówkowe bibliotek oapr.

%package static
Summary:	Static oapr libraries
Summary(pl):	Statyczne biblioteki oapr
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static oapr libraries.

%description static -l pl
Statyczne biblioteki oapr.

%prep
%setup -q

%build
# need libtoolize (C++ linking)
mkdir -p config
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-apr=%{_bindir} \
	--with-apr-util=%{_bindir}

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
%{_includedir}/oapx

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
