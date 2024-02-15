%define mate_ver	%(echo %{version}|cut -d. -f1,2)

%define oname mate-image-viewer

%define gi_major 1.0
%define girname %mklibname %{name}-gir %{gi_major}

Summary:	Eye of MATE image viewer
Name:		eom
Version:	1.28.0
Release:	1
Group:		Graphical desktop/Other
License:	GPLv2+ and LGPLv2+
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{mate_ver}/%{name}-%{version}.tar.xz

BuildRequires:	autoconf-archive
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(exempi-2.0)
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libpeas-1.0)
BuildRequires:	pkgconfig(libpeas-gtk-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(MagickWand)
BuildRequires:	yelp-tools

Requires:	gsettings-desktop-schemas
Requires:	librsvg
Requires:	mate-icon-theme
Requires:	mate-desktop-schemas
Requires:	typelib(Peas)
Requires:	typelib(PeasGtk)
Requires:	typelib(Eom)

%rename %{oname}

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides Eye of MATE, an image viewer program. It is meant to
be a fast and functional image viewer.

%files -f eom.lang
%doc AUTHORS COPYING NEWS README
%{_bindir}/eom
%{_bindir}/eom-thumbnailer
%{_libdir}/eom/plugins
%{_datadir}/applications/eom.desktop
%{_datadir}/%{name}
%{_datadir}/thumbnailers/eom-thumbnailer.thumbnailer
%{_datadir}/metainfo/eom.appdata.xml
%{_datadir}/glib-2.0/schemas/org.mate.eom.enums.xml
%{_datadir}/glib-2.0/schemas/org.mate.eom.gschema.xml
%{_datadir}/gtk-doc/html/eom
%{_iconsdir}/hicolor/*/apps/eom.*
%doc %{_mandir}/man1/*

#---------------------------------------------------------------------------

%package devel
Summary:	C headers needed to build EOM plugins
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
%rename		%{oname}-devel

%description devel
This package contains includes files for developing plugins based on EoM's
API.

%files devel
%{_includedir}/eom-2.20
%{_libdir}/pkgconfig/eom.pc
%{_datadir}/gir-1.0/Eom-%{gi_major}.gir

#---------------------------------------------------------------------------

%package -n %{girname}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries
#Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
This package contains GObject Introspection interface library for %{name}.

%files -n %{girname}
%{_libdir}/girepository-1.0/Eom-%{gi_major}.typelib

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
export LDFLAGS="-L%{_libdir}/"
%configure \
	--disable-schemas-compile \
	--enable-introspection \
	--enable-thumbnailer \
	--without-gdk-pixbuf-thumbnailer

%make_build

%install
%make_install

# locales
%find_lang eom --with-gnome --all-name

