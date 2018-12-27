Name:           abseil-cpp
Version:		%{VERSION}
Release:        %{RELEASE}%{?dist}
Summary:        Abseil Common Libraries (C++)
License:        Apache 2
Group:          Development/Libraries/C and C++
Url:            http://abseil.io
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake

%description
TensorFlow is an open source software library for numerical computation using data flow graphs.

%package devel
Summary:    Development headers and library for %{name}
Group:      Development/Libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers and library for %{name}.

%prep
%setup -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_includedir}
cp -r absl $RPM_BUILD_ROOT%{_includedir}
find $RPM_BUILD_ROOT%{_includedir}/absl -type f  ! -name "*.h" -delete

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
%{_includedir}/absl

%changelog
