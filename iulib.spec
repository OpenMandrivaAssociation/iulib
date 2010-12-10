%define name    iulib
%define develname	%mklibname %{name} -d

Name:		%{name}
Version:	0.4
Release:	%mkrel 3
Summary:	A library of image understanding-related algorithms
License:	Apache
Group:		System/Libraries
URL:		http://code.google.com/p/iulib/
Source:		http://iulib.googlecode.com/files/%{name}-%{version}.tgz
Patch0:		iulib-0.4-add-includes.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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

%clean
rm -rf %{buildroot}

%files -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/colib/*.h
%{_includedir}/iulib/*.h
%{_libdir}/*.a

