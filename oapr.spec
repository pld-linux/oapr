Summary:	C++ wrapper on apr
Summary(pl):	Wrapper C++ na apr
Name:		oapr
Version:	0.1
Release:	0.1
Epoch:		0
License:	GPL
Group:		Libraries
Source0:	http://www.openaether.org/builds/%{name}-%{version}.tar.gz
# Source0-md5:	8a8ceacd948a7613b233c86ef8f07ca8
URL:		http://www.openaether.org/
BuildRequires:	apr-util-devel
BuildRequires:	xerces-c-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
oapr is C++ wrapper on C library: apr. This package contains shared
libraries.

%description -l pl
oapr jest wrapperem C++ dla biblioteki C apr. Ten pakiet zawiera
biblioteki dzielone.

%package devel
Summary:	Header files for oapr library
Summary(pl):	Pliki nag³ówkowe biblioteki oapr
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for oapr library.

%description devel -l pl
Pliki nag³ówkowe biblioteki oapr.

%package static
Summary:	Static oapr library
Summary(pl):	Statyczna biblioteka oapr
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static oapr library.

%description static -l pl
Statyczna biblioteka oapr.

%prep
%setup -q

%build
%configure \
	--with-apr=%{_bindir} \
	--with-apu=%{_bindir}
%{__make}

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
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/oapr
%{_includedir}/oapu
%{_includedir}/oapx

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
