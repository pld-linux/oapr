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
URL:		www.openaether.org
BuildRequires:	xerces-c-devel
BuildRequires:	apr-util-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
oapr is C++ wrapper on C library: apr. This package contains shared
libaries

%description -l pl
oapr jest wrapperem C++ na bibliotece C: apr. Ten pakiet zawiera
biblioteki dzielone


%package devel
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Summary:	Static libraries and headers.

%description devel
Static libraries and headers for oapr library

%description devel -l pl
Biblioteki statyczne i pliki nag³ówkowe dla biblioteki oapr

%prep
%setup -q -n %{name}-%{version}

%build
%configure --with-apr=%{_bindir} --with-apu=%{_bindir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/*.so.*


%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_includedir}/oapr/*
%{_includedir}/oapu/*
%{_includedir}/oapx/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
