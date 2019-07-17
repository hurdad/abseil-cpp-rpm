Name:           abseil-cpp
Version:	%{VERSION}
Release:        %{RELEASE}%{?dist}
Summary:        Abseil Common Libraries (C++)
License:        Apache 2
Group:          Development/Libraries/C and C++
Url:            http://abseil.io
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake3

%description
TensorFlow is an open source software library for numerical computation using data flow graphs.

%package devel
Summary:    Development headers and library for %{name}
Group:      Development/Libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers and library for %{name}.

%prep
%setup -n %{name}-daf381e8535a1f1f1b8a75966a74e7cca63dee89

%build
cmake3 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr .

%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md AUTHORS

%files devel
%defattr(-,root,root,-)
%{_includedir}
%{_libdir}/*.a
%{_libdir}/cmake/*

%changelog
