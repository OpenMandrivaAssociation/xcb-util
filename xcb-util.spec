%define _pkgconfigdir	%{_libdir}/pkgconfig
%define _disable_ld_no_undefined 1
%define major 0
%define libname %mklibname xcb-util %major
%define major1 1
%define libname1 %mklibname xcb-util %major1
%define develname %mklibname -d xcb-util
%define staticdevelname %mklibname -s -d xcb-util

Name: xcb-util
Summary: A number of libraries which sit on top of libxcb
Version: 0.3.4
Release: %mkrel 2
Group: System/X11
License: MIT
URL: http://xcb.freedesktop.org
Source: http://xcb.freedesktop.org/dist/%name-%{version}.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 7.3-2mdv
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

%package -n %libname
Summary: A number of libraries which sit on top of libxcb
Conflicts: libxcb-util-devel < 0.3.4-2mdv
Group: System/Libraries

%description -n %libname
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n %libname1
Summary: A number of libraries which sit on top of libxcb
Conflicts: libxcb-util-devel < 0.3.4-2mdv
Group: System/Libraries

%description -n %libname1
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n %develname
Summary: A number of libraries which sit on top of libxcb
Group: Development/C
Obsoletes: libxcb-util-devel < 0.3.4-2mdv
Provides:  libxcb-util-devel = %version-%release
Requires:  %libname = %version-%release
Requires:  %libname1 = %version-%release

%description -n %develname
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package -n %staticdevelname
Summary: A number of libraries which sit on top of libxcb
Group: Development/C
Conflicts: libxcb-util-devel < 0.3.4-2mdv
Provides:  libxcb-util-static-devel = %version-%release
Requires:  %develname = %version-%release

%description -n %staticdevelname
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.



%prep
%setup -q
autoreconf -ifs

%build
%configure2_5x

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libxcb-aux.so.0*
%{_libdir}/libxcb-image.so.0*
%{_libdir}/libxcb-render-util.so.0*

%files -n %libname1
%defattr(-,root,root)
%{_libdir}/libxcb-atom.so.1*
%{_libdir}/libxcb-event.so.1*
%{_libdir}/libxcb-icccm.so.1*
%{_libdir}/libxcb-keysyms.so.1*
%{_libdir}/libxcb-property.so.1*
%{_libdir}/libxcb-reply.so.1*

%files -n %develname
%defattr(-,root,root)
%{_includedir}/xcb/xcb_atom.h
%{_includedir}/xcb/xcb_aux.h
%{_includedir}/xcb/xcb_bitops.h
%{_includedir}/xcb/xcb_event.h
%{_includedir}/xcb/xcb_icccm.h
%{_includedir}/xcb/xcb_image.h
%{_includedir}/xcb/xcb_keysyms.h
%{_includedir}/xcb/xcb_pixel.h
%{_includedir}/xcb/xcb_property.h
%{_includedir}/xcb/xcb_renderutil.h
%{_includedir}/xcb/xcb_reply.h
%{_libdir}/libxcb-atom.la
%{_libdir}/libxcb-atom.so
%{_libdir}/libxcb-aux.la
%{_libdir}/libxcb-aux.so
%{_libdir}/libxcb-event.la
%{_libdir}/libxcb-event.so
%{_libdir}/libxcb-icccm.la
%{_libdir}/libxcb-icccm.so
%{_libdir}/libxcb-image.la
%{_libdir}/libxcb-image.so
%{_libdir}/libxcb-keysyms.la
%{_libdir}/libxcb-keysyms.so
%{_libdir}/libxcb-property.la
%{_libdir}/libxcb-property.so
%{_libdir}/libxcb-render-util.la
%{_libdir}/libxcb-render-util.so
%{_libdir}/libxcb-reply.la
%{_libdir}/libxcb-reply.so
%{_pkgconfigdir}/xcb-atom.pc
%{_pkgconfigdir}/xcb-aux.pc
%{_pkgconfigdir}/xcb-event.pc
%{_pkgconfigdir}/xcb-icccm.pc
%{_pkgconfigdir}/xcb-image.pc
%{_pkgconfigdir}/xcb-keysyms.pc
%{_pkgconfigdir}/xcb-property.pc
%{_pkgconfigdir}/xcb-renderutil.pc
%{_pkgconfigdir}/xcb-reply.pc

%files -n %staticdevelname
%defattr(-,root,root)
%{_libdir}/libxcb-atom.a
%{_libdir}/libxcb-aux.a
%{_libdir}/libxcb-event.a
%{_libdir}/libxcb-icccm.a
%{_libdir}/libxcb-image.a
%{_libdir}/libxcb-keysyms.a
%{_libdir}/libxcb-property.a
%{_libdir}/libxcb-render-util.a
%{_libdir}/libxcb-reply.a
