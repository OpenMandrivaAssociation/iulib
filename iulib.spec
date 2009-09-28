%define name    iulib
%define develname	%mklibname %{name} -d

Name:		%{name}
Version:	0.4
Release:	%mkrel 1
Summary:	A library of image understanding-related algorithms
License:	Apache
Group:		System/Libraries
URL:		http://code.google.com/p/iulib/
Source:		http://iulib.googlecode.com/files/%{name}-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  scons
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

%build
%scons prefix=%{_prefix} opt="%{optflags}"

%install
rm -rf %{buildroot}
%scons_install opt="%{optflags}" prefix=%{buildroot}/%{_prefix}
%if "%{_lib}" != "lib"
mkdir -p %{buildroot}/%{_libdir}
mv %{buildroot}/%{_prefix}/lib/*.a %{buildroot}/%{_libdir}
%endif

%clean
rm -rf %{buildroot}

%files -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/colib/*.h
%{_includedir}/iulib/*.h
%{_libdir}/*.a

