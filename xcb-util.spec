%define _pkgconfigdir	%{_libdir}/pkgconfig
%define _disable_ld_no_undefined 1
%define develname %mklibname -d xcb-util
%define staticdevelname %mklibname -s -d xcb-util

Name: xcb-util
Summary: A number of libraries which sit on top of libxcb
Version: 0.3.5
Release: %mkrel 5
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

%define aux_major 0
%define atom_major 1
%define event_major 1
%define icccm_major 1
%define image_major 0
%define keysyms_major 1
%define property_major 1
%define render_util_major 0
%define reply_major 1

%define libaux         %mklibname xcb-aux         %aux_major
%define libatom        %mklibname xcb-atom        %atom_major
%define libevent       %mklibname xcb-event       %event_major
%define libicccm       %mklibname xcb-icccm       %icccm_major
%define libimage       %mklibname xcb-image       %image_major
%define libkeysyms     %mklibname xcb-keysyms     %keysyms_major
%define libproperty    %mklibname xcb-property    %property_major
%define librender_util %mklibname xcb-render-util %render_util_major
%define libreply       %mklibname xcb-reply       %reply_major

# Require Obsoletes
%define libxcb_util0   %mklibname xcb-util        0
%define libxcb_util1   %mklibname xcb-util        1

#--------------------------------------------------------------------

%package -n %develname
Summary: A number of libraries which sit on top of libxcb
Group: Development/C
Obsoletes: libxcb-util-devel < 0.3.4-2mdv
Provides:  libxcb-util-devel = %version-%release
Provides:  xcb-util-devel = %version-%release
Requires:  %libaux = %version-%release
Requires:  %libatom = %version-%release
Requires:  %libevent = %version-%release
Requires:  %libicccm = %version-%release
Requires:  %libimage = %version-%release
Requires:  %libkeysyms = %version-%release
Requires:  %libproperty = %version-%release
Requires:  %librender_util = %version-%release
Requires:  %libreply = %version-%release

%description -n %develname
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

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

#--------------------------------------------------------------------

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

#--------------------------------------------------------------------

%package -n %libaux
Summary: xcb-util's libxcb-aux
Group: System/X11
Conflicts: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: %{libxcb_util0}
Obsoletes: %{libxcb_util1}

%description -n %libaux
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%files -n %libaux
%defattr(-,root,root)
%{_libdir}/libxcb-aux.so.%{aux_major}*

#--------------------------------------------------------------------

%package -n %libatom
Summary: xcb-util's libxcb-atom
Group: System/X11
Conflicts: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: %{libxcb_util0}
Obsoletes: %{libxcb_util1}

%description -n %libatom
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%files -n %libatom
%defattr(-,root,root)
%{_libdir}/libxcb-atom.so.%{atom_major}*

#--------------------------------------------------------------------

%package -n %libevent
Summary: xcb-util's libxcb-event
Group: System/X11
Conflicts: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: %{libxcb_util0}
Obsoletes: %{libxcb_util1}

%description -n %libevent
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%files -n %libevent
%defattr(-,root,root)
%{_libdir}/libxcb-event.so.%{event_major}*

#--------------------------------------------------------------------

%package -n %libicccm
Summary: xcb-util's libxcb-icccm
Group: System/X11
Conflicts: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: %{libxcb_util0}
Obsoletes: %{libxcb_util1}

%description -n %libicccm
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%files -n %libicccm
%defattr(-,root,root)
%{_libdir}/libxcb-icccm.so.%{icccm_major}*

#--------------------------------------------------------------------

%package -n %libimage
Summary: xcb-util's libxcb-image
Group: System/X11
Conflicts: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: %{libxcb_util0}
Obsoletes: %{libxcb_util1}

%description -n %libimage
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%files -n %libimage
%defattr(-,root,root)
%{_libdir}/libxcb-image.so.%{image_major}*

#--------------------------------------------------------------------

%package -n %libkeysyms
Summary: xcb-util's libxcb-keysyms
Group: System/X11
Conflicts: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: %{libxcb_util0}
Obsoletes: %{libxcb_util1}

%description -n %libkeysyms
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%files -n %libkeysyms
%defattr(-,root,root)
%{_libdir}/libxcb-keysyms.so.%{keysyms_major}*

#--------------------------------------------------------------------

%package -n %libproperty
Summary: xcb-util's libxcb-property
Group: System/X11
Conflicts: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: %{libxcb_util0}
Obsoletes: %{libxcb_util1}

%description -n %libproperty
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%files -n %libproperty
%defattr(-,root,root)
%{_libdir}/libxcb-property.so.%{property_major}*

#--------------------------------------------------------------------

%package -n %librender_util
Summary: xcb-util's libxcb-render-util
Group: System/X11
Conflicts: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: %{libxcb_util0}
Obsoletes: %{libxcb_util1}

%description -n %librender_util
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%files -n %librender_util
%defattr(-,root,root)
%{_libdir}/libxcb-render-util.so.%{render_util_major}*

#--------------------------------------------------------------------

%package -n %libreply
Summary: xcb-util's libxcb-reply
Group: System/X11
Conflicts: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: libxcb-util-devel < 0.3.4-2mdv
Obsoletes: %{libxcb_util0}
Obsoletes: %{libxcb_util1}

%description -n %libreply
The xcb-util module provides a number of libraries which sit on top of
libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%files -n %libreply
%defattr(-,root,root)
%{_libdir}/libxcb-reply.so.%{reply_major}*

#--------------------------------------------------------------------

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

