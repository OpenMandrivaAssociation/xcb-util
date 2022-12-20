# xcb-util is used by vkd3d, which is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define major 1
%define libname %mklibname xcb-util %{major}
%define develname %mklibname xcb-util -d
%define lib32name %mklib32name xcb-util %{major}
%define devel32name %mklib32name xcb-util -d

%global optflags %{optflags} -O3

Name:		xcb-util
Summary:	A number of libraries which sit on top of libxcb
Version:	0.4.1
Release:	1
Group:		System/X11
License:	MIT
URL:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	gperf
%if %{with compat32}
BuildRequires:	libc6
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
%endif

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n %{develname}
Summary:	A number of libraries which sit on top of libxcb
Group:		Development/C
Provides:	xcb-util-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{_lib}xcb-static-devel < 0.3.9

%description -n %{develname}
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%files -n %{develname}
%{_includedir}/xcb/xcb_atom.h
%{_includedir}/xcb/xcb_aux.h
%{_includedir}/xcb/xcb_event.h
%{_includedir}/xcb/xcb_util.h
%{_libdir}/libxcb-util.so
%{_libdir}/pkgconfig/xcb-atom.pc
%{_libdir}/pkgconfig/xcb-aux.pc
%{_libdir}/pkgconfig/xcb-event.pc
%{_libdir}/pkgconfig/xcb-util.pc

%package -n %{libname}
Summary:	xcb-util library package
Group:		System/X11
Conflicts:	%{_lib}xcb-xvmc0 < 1.7-2
Conflicts:	%{_lib}xcb-xtest0 < 1.7-2
Conflicts:	%{_lib}xcb-xprint0 < 1.7-2
Conflicts:	%{_lib}xcb-xfixes0 < 1.7-2
Conflicts:	%{_lib}xcb-shm0 < 1.7-2
Conflicts:	%{_lib}xcb-xevie0 < 1.7-2
Conflicts:	%{_lib}xcb-shape0 < 1.7-2
Conflicts:	%{_lib}xcb-composite0 < 1.7-2
Conflicts:	%{_lib}xcb-xv0 < 1.7-2
Conflicts:	%{_lib}xcb-xf86dri0 < 1.7-2
Conflicts:	%{_lib}xcb-damage0 < 1.7-2
Conflicts:	%{_lib}xcb-record0 < 1.7-2
Conflicts:	%{_lib}xcb-res0 < 1.7-2
Conflicts:	%{_lib}xcb-screensaver0 < 1.7-2
Conflicts:	%{_lib}xcb-glx0 < 1.7-2
Conflicts:	%{_lib}xcb-dri2_0 < 1.7-2
Conflicts:	%{_lib}xcb-xinerama0 < 1.7-2
Conflicts:	%{_lib}xcb1 < 1.7-2
Conflicts:	%{_lib}xcb-sync0 < 1.7-2
Conflicts:	%{_lib}xcb-render0 < 1.7-2
Conflicts:	%{_lib}xcb-dpms0 < 1.7-2
Conflicts:	%{_lib}xcb-randr0 < 1.7-2

%description -n %{libname}
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%files -n %{libname}
%{_libdir}/libxcb-util.so.%{major}*

%if %{with compat32}
%package -n %{devel32name}
Summary:	A number of libraries which sit on top of libxcb (32-bit)
Group:		Development/C
Requires:	%{lib32name} = %{version}-%{release}
Requires:	%{develname} = %{version}-%{release}

%description -n %{devel32name}
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%files -n %{devel32name}
%{_prefix}/lib/libxcb-util.so
%{_prefix}/lib/pkgconfig/xcb-atom.pc
%{_prefix}/lib/pkgconfig/xcb-aux.pc
%{_prefix}/lib/pkgconfig/xcb-event.pc
%{_prefix}/lib/pkgconfig/xcb-util.pc

%package -n %{lib32name}
Summary:	xcb-util library package (32-bit)
Group:		System/X11

%description -n %{lib32name}
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%files -n %{lib32name}
%{_prefix}/lib/libxcb-util.so.%{major}*
%endif

%prep
%autosetup -p1

export CONFIGURE_TOP="$(pwd)"

%if %{with compat32}
mkdir build32
cd build32
%configure32 --disable-static --with-pic
cd ..
%endif

mkdir build
cd build
%configure \
	--disable-static \
	--with-pic

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build
