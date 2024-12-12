# Not official release yet
%define snapshot 20271127
%define commit 07785b7576a0655660badd845f06ed286208da1a
%define shortcommit %(c=%{commit}; echo ${c:0:7})

%define libname	%mklibname %{name}
%define devname	%mklibname %{name} -d

Name:           ondselsolver
Version:        1.0.1
Release:        1
Summary:        Assembly Constraints and Multibody Dynamics code
# TBD, see https://github.com/Ondsel-Development/OndselSolver/issues/45
License:        LGPL-2.1-only
URL:            https://github.com/Ondsel-Development/OndselSolver
Source0:	https://github.com/Ondsel-Development/OndselSolver/archive/%{?snapshot:%{commit}}%{!?snapshot:v%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz
BuildRequires:  cmake
BuildRequires:  ninja

%description
Assembly Constraints and Multibody Dynamics code

#-----------------------------------------------------------------------

%package  -n %{libname}
Summary:        Assembly Constraints and Multibody Dynamics code

%description  -n %{libname}
This package contains the OndselSolver shared library.

%files  -n %{libname}
%license LICENSE
%{_libdir}/*.so.*

#-----------------------------------------------------------------------

%package -n %{devname}
Summary:        Development files for OndselSolver
Requires:       %{libname} = %{EVRD}

%description -n %{devname}
Header and other development files for OndselSolver.

%files -n %{devname}
%doc README.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#-----------------------------------------------------------------------

%prep
#autosetup -p1 -n OndselSolver-PR-11363
%autosetup -p1 -n OndselSolver-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
%cmake \
	-GNinja
%ninja_build

%install
%ninja_install -C build

# Fix pkgconfig install path
mv %{buildroot}%{_datadir}/pkgconfig %{buildroot}%{_libdir}/pkgconfig 


