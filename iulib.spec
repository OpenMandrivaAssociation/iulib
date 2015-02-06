%global debug_package %{nil}
%define name    iulib
%define develname	%mklibname %{name} -d

Name:		%{name}
Version:	0.4
Release:	5
Summary:	A library of image understanding-related algorithms
License:	Apache
Group:		System/Libraries
URL:		http://code.google.com/p/iulib/
Source0:		http://iulib.googlecode.com/files/%{name}-%{version}.tgz
Patch0:		iulib-0.4-add-includes.patch
BuildRequires:  png-devel
BuildRequires:	jpeg-devel
BuildRequires:	tiff-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	imagemagick

%description
Iulib implements easy-to-use image and video I/O functions, as well as a
 large number of common image processing functions.  

%package -n	%{develname}
Summary: 	Header files, libraries and development documentation for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0 -b .old

%build
./build
autoreconf -fi
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/colib/*.h
%{_includedir}/iulib/*.h
%{_libdir}/*.a



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4-3mdv2011.0
+ Revision: 619684
- the mass rebuild of 2010.0 packages

* Mon Sep 28 2009 Funda Wang <fwang@mandriva.org> 0.4-2mdv2010.0
+ Revision: 450465
- fix build when using autotools

* Mon Sep 28 2009 Funda Wang <fwang@mandriva.org> 0.4-1mdv2010.0
+ Revision: 450460
- New version 0.4

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Feb 28 2009 Emmanuel Andry <eandry@mandriva.org> 0.3-1mdv2009.1
+ Revision: 346187
- import iulib


