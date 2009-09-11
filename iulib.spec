%define name    iulib
%define develname	%mklibname %{name} -d

Name:		%{name}
Version:	0.3
Release:	%mkrel 2
Summary:	A library of image understanding-related algorithms
License:	Apache
Group:		System/Libraries
URL:		http://code.google.com/p/iulib/
Source:		http://iulib.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  scons
BuildRequires:  png-devel
BuildRequires:	jpeg-devel
BuildRequires:	tiff-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel


%description
Iulib implements easy-to-use image and video I/O functions, as well as a
 large number of common image processing functions.  

%package -n	%{develname}
Summary: 	Header files, libraries and development documentation for %{name}
Group:		Development/C
#Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n %{name}

%build
%configure2_5x --prefix=%{_prefix}
%make

%install
rm -rf %{buildroot}
%makeinstall

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

#%files -n %{libname}
#%defattr(-,root,root)
#%{_libdir}/*.so.%{major}
#%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/colib/*.h
%{_includedir}/*.h
%{_libdir}/*.a

