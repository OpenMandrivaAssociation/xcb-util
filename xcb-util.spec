%define major 1
%define libname %mklibname xcb-util %{major}
%define develname %mklibname xcb-util -d

Name:		xcb-util
Summary:	A number of libraries which sit on top of libxcb
Version:	0.3.9
Release:	3
Group:		System/X11
License:	MIT
URL:		http://xcb.freedesktop.org
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
BuildRequires:	x11-proto-devel
BuildRequires:	x11-util-macros >= 1.1.5
BuildRequires:	xcb-devel
BuildRequires:	gperf

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
#%{_includedir}/xcb/xcb_bitops.h
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

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std



%changelog
* Mon Jun 04 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.3.9-1
+ Revision: 802190
- version update 0.3.9
- version update 0.3.9

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.3.8-2
+ Revision: 745507
- rebuild
- cleaned up spec
- disabled static build
- removed .la files

* Mon Oct 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.8-1
+ Revision: 704124
- update to new version 0.3.8
- add conflicts on libraries which no longer exists

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.6-3
+ Revision: 671281
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.6-2mdv2011.0
+ Revision: 608194
- rebuild

* Mon Nov 16 2009 Thierry Vignaud <tv@mandriva.org> 0.3.6-1mdv2010.1
+ Revision: 466574
- new release

* Mon Jul 06 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 0.3.5-5mdv2010.0
+ Revision: 392804
- Fix upgrade

* Fri Jun 12 2009 Pascal Terjan <pterjan@mandriva.org> 0.3.5-4mdv2010.0
+ Revision: 385419
- Fix upgrade

* Mon Jun 08 2009 Götz Waschk <waschk@mandriva.org> 0.3.5-3mdv2010.0
+ Revision: 383848
- add missing devel dep

* Fri Jun 05 2009 Helio Chissini de Castro <helio@mandriva.com> 0.3.5-2mdv2010.0
+ Revision: 383049
- Proper obsoletes

* Thu Jun 04 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 0.3.5-1mdv2010.0
+ Revision: 382844
- update to 0.3.5
- split libraries on their own packages

* Mon May 04 2009 Götz Waschk <waschk@mandriva.org> 0.3.4-3mdv2010.0
+ Revision: 371642
- rebuild

* Mon May 04 2009 Götz Waschk <waschk@mandriva.org> 0.3.4-2mdv2010.0
+ Revision: 371634
- libify the package (bug #50569)
- use the right source package name

* Thu Apr 30 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 0.3.4-1mdv2010.0
+ Revision: 369176
- New version 0.3.4

* Fri Feb 06 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 0.3.3-1mdv2009.1
+ Revision: 338080
- New version 0.3.3

* Thu Dec 18 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 0.3.2-2mdv2009.1
+ Revision: 315840
- Bump release
- New version 0.3.2

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1mdv2009.0
+ Revision: 193499
- xcb-util is a collection of libraries that complement xcb. From the README:
  These libraries are currently included, roughly ordered by maturity:
  render-util: Convenience functions for the Render extension.
  aux: Convenient access to connection setup and some core requests.
  atom: Standard core X atom constants and atom caching.
  property: Callback X property-change handling.
  icccm: Both client and window-manager helpers for ICCCM.
  keysyms: Standard X key constants and conversion to/from keycodes.
  event: Callback X event handling.
  image: Port of Xlib's XImage and XShmImage functions.
  wm: Framework for window manager implementation.
  If you find any of these libraries useful, please let us know what
  you're using and why you aren't in a mental hospital yet. We'd welcome
  patches/suggestions for enhancement and new libraries; Please report any
  issues you find to the freedesktop.org bug tracker, at:
        <https://bugs.freedesktop.org/enter_bug.cgi?product=XCB>
  Discussion about XCB occurs on the XCB mailing list:
        <mailto:xcb at lists.freedesktop.org>
        <http://lists.freedesktop.org/mailman/listinfo/xcb>
  You can obtain the latest development versions of XCB using GIT.
  For anonymous checkouts, use:
        git clone git://anongit.freedesktop.org/git/xcb/util
  For developers, use:
        git clone git+ssh://git.freedesktop.org/git/xcb/util
- xcb-util package.

