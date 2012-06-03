%define major		0
%define libname		%mklibname xcb-util %{major}
%define develname	%mklibname xcb-util -d

Name: xcb-util
Summary: A number of libraries which sit on top of libxcb
Version: 0.3.9
Release: 1
Group: System/X11
License: MIT
URL: http://xcb.freedesktop.org
Source0: http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
BuildRequires: x11-proto-devel
BuildRequires: x11-util-macros >= 1.1.5
BuildRequires: xcb-devel
BuildRequires: gperf

%description
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

#--------------------------------------------------------------------

%package -n %{develname}
Summary: A number of libraries which sit on top of libxcb
Group: Development/C
Provides:  xcb-util-devel = %{version}-%{release}
Requires:  %{libname} = %{version}-%{release}
Obsoletes: %{_lib}xcb-static-devel

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
%{_includedir}/xcb/xcb_bitops.h
%{_includedir}/xcb/xcb_event.h
%{_includedir}/xcb/xcb_util.h
%{_libdir}/libxcb-util.so
%{_libdir}/pkgconfig/xcb-atom.pc
%{_libdir}/pkgconfig/xcb-aux.pc
%{_libdir}/pkgconfig/xcb-event.pc
%{_libdir}/pkgconfig/xcb-util.pc

#--------------------------------------------------------------------

%package -n %{libname}
Summary: xcb-util library package
Group: System/X11
Conflicts: %{_lib}xcb-xvmc0 < 1.7-2
Conflicts: %{_lib}xcb-xtest0 < 1.7-2
Conflicts: %{_lib}xcb-xprint0 < 1.7-2
Conflicts: %{_lib}xcb-xfixes0 < 1.7-2
Conflicts: %{_lib}xcb-shm0 < 1.7-2
Conflicts: %{_lib}xcb-xevie0 < 1.7-2
Conflicts: %{_lib}xcb-shape0 < 1.7-2
Conflicts: %{_lib}xcb-composite0 < 1.7-2
Conflicts: %{_lib}xcb-xv0 < 1.7-2
Conflicts: %{_lib}xcb-xf86dri0 < 1.7-2
Conflicts: %{_lib}xcb-damage0 < 1.7-2
Conflicts: %{_lib}xcb-record0 < 1.7-2
Conflicts: %{_lib}xcb-res0 < 1.7-2
Conflicts: %{_lib}xcb-screensaver0 < 1.7-2
Conflicts: %{_lib}xcb-glx0 < 1.7-2
Conflicts: %{_lib}xcb-dri2_0 < 1.7-2
Conflicts: %{_lib}xcb-xinerama0 < 1.7-2
Conflicts: %{_lib}xcb1 < 1.7-2
Conflicts: %{_lib}xcb-sync0 < 1.7-2
Conflicts: %{_lib}xcb-render0 < 1.7-2
Conflicts: %{_lib}xcb-dpms0 < 1.7-2
Conflicts: %{_lib}xcb-randr0 < 1.7-2

%description -n %{libname}
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%files -n %{libname}
%{_libdir}/libxcb-util.so.%{major}*

#--------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std

