%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define oname  mate-image-viewer

Summary:	Eye of MATE image viewer
Name:		eom
Version:	1.8.0
Release:	1
Group:		Graphical desktop/Other
License:	GPLv2+ and LGPLv2+ 
Url:		http://mate-desktop.org 
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	mate-common
BuildRequires:	which
BuildRequires:	xml2po
BuildRequires:	yelp-tools
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(exempi-2.0)
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(mate-icon-theme)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	pkgconfig(xt)
Requires:	librsvg
Requires:	mate-icon-theme
Requires:	gsettings-desktop-schemas   
%rename %{oname}

%description
This is the Eye of MATE, an image viewer program.  It is meant to be
a fast and functional image viewer.

Eye of MATE is a fork of Eye of GNOME.

%package devel
Summary:	C headers needed to build EOM plugins
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
%rename %{oname}-devel

%description devel
The Eye of MATE image viewer (eom) is the official image viewer for the
MATE desktop. This package allows you to develop plugins that add new
functionality to eom.

%prep
%setup -q
%apply_patches
NOCONFIGURE=1 ./autogen.sh

%build
%configure2_5x \
	--disable-schemas-compile
           
%make

%install
%makeinstall_std

# remove unneeded converter
rm -fr %{buildroot}%{_datadir}/MateConf

%find_lang eom --with-gnome --all-name

%files -f eom.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/eom
%{_libdir}/eom/plugins
%{_datadir}/applications/eom.desktop
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.mate.eom.gschema.xml
%{_datadir}/gtk-doc/html/eom
%{_iconsdir}/hicolor/*/apps/eom.*
%{_mandir}/man1/*

%files devel
%{_libdir}/pkgconfig/eom.pc
%{_includedir}/eom-2.20

