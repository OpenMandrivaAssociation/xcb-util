%define _pkgconfigdir	%{_libdir}/pkgconfig
%define _disable_ld_no_undefined 1

Name: libxcb-util-devel
Summary: A number of libraries which sit on top of libxcb
Version: 0.3.4
Release: %mkrel 1
Group: System/X11
License: MIT
URL: http://xcb.freedesktop.org
Source: http://xcb.freedesktop.org/dist/xcb-util-%{version}.tar.bz2
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

%prep
%setup -q -n xcb-util-%{version}

%build
autoreconf -ifs
%configure

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
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
%{_libdir}/libxcb-atom.a
%{_libdir}/libxcb-atom.la
%{_libdir}/libxcb-atom.so
%{_libdir}/libxcb-atom.so.1
%{_libdir}/libxcb-atom.so.1.0.0
%{_libdir}/libxcb-aux.a
%{_libdir}/libxcb-aux.la
%{_libdir}/libxcb-aux.so
%{_libdir}/libxcb-aux.so.0
%{_libdir}/libxcb-aux.so.0.0.0
%{_libdir}/libxcb-event.a
%{_libdir}/libxcb-event.la
%{_libdir}/libxcb-event.so
%{_libdir}/libxcb-event.so.1
%{_libdir}/libxcb-event.so.1.0.0
%{_libdir}/libxcb-icccm.a
%{_libdir}/libxcb-icccm.la
%{_libdir}/libxcb-icccm.so
%{_libdir}/libxcb-icccm.so.1
%{_libdir}/libxcb-icccm.so.1.0.0
%{_libdir}/libxcb-image.a
%{_libdir}/libxcb-image.la
%{_libdir}/libxcb-image.so
%{_libdir}/libxcb-image.so.0
%{_libdir}/libxcb-image.so.0.0.0
%{_libdir}/libxcb-keysyms.a
%{_libdir}/libxcb-keysyms.la
%{_libdir}/libxcb-keysyms.so
%{_libdir}/libxcb-keysyms.so.1
%{_libdir}/libxcb-keysyms.so.1.0.0
%{_libdir}/libxcb-property.a
%{_libdir}/libxcb-property.la
%{_libdir}/libxcb-property.so
%{_libdir}/libxcb-property.so.1
%{_libdir}/libxcb-property.so.1.0.0
%{_libdir}/libxcb-render-util.a
%{_libdir}/libxcb-render-util.la
%{_libdir}/libxcb-render-util.so
%{_libdir}/libxcb-render-util.so.0
%{_libdir}/libxcb-render-util.so.0.0.0
%{_libdir}/libxcb-reply.a
%{_libdir}/libxcb-reply.la
%{_libdir}/libxcb-reply.so
%{_libdir}/libxcb-reply.so.1
%{_libdir}/libxcb-reply.so.1.0.0
%{_pkgconfigdir}/xcb-atom.pc
%{_pkgconfigdir}/xcb-aux.pc
%{_pkgconfigdir}/xcb-event.pc
%{_pkgconfigdir}/xcb-icccm.pc
%{_pkgconfigdir}/xcb-image.pc
%{_pkgconfigdir}/xcb-keysyms.pc
%{_pkgconfigdir}/xcb-property.pc
%{_pkgconfigdir}/xcb-renderutil.pc
%{_pkgconfigdir}/xcb-reply.pc
