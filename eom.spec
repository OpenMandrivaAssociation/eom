%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define oname  mate-image-viewer

Name:          eom
Version:       1.6.1
Release:       1
Summary:       Eye of MATE image viewer
Group:         Graphical desktop/Other
License:       GPLv2+ and LGPLv2+ 
URL:           http://mate-desktop.org 
Source0:       http://pub.mate-desktop.org/releases/%{url_ver}/%{oname}-%{version}.tar.xz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gtk-doc)
BuildRequires: pkgconfig(libglade-2.0)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(exempi-2.0)
BuildRequires: pkgconfig(libart-2.0)
BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(mate-doc-utils)
BuildRequires: pkgconfig(mate-desktop-2.0)
BuildRequires: pkgconfig(lcms)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(mate-icon-theme)
BuildRequires: pkgconfig(pygtk-2.0)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: pkgconfig(pygobject-2.0)
BuildRequires: jpeg-devel
BuildRequires: intltool
BuildRequires: which
BuildRequires: xml2po
BuildRequires: mate-common
BuildRequires: yelp-tools

Requires:      mate-icon-theme
Requires:      gsettings-desktop-schemas   

Provides:      %{oname} = %{version}-%{release}

%description
This is the Eye of MATE, an image viewer program.  It is meant to be
a fast and functional image viewer.

Eye of MATE is a fork of Eye of GNOME.

%package devel
Summary:  C headers needed to build EOM plugins
Group:    Development/C
Requires: %{name} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Provides: %{oname}-devel = %{version}-%{release}

%description devel
The Eye of MATE image viewer (eom) is the official image viewer for the
MATE desktop. This package allows you to develop plugins that add new
functionality to eom.

%prep
%setup -q -n %{oname}-%{version}
%apply_patches

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
   --disable-schemas-compile \
   --disable-scrollkeeper
           
%make LIBS='-lgmodule-2.0 -lz'


%install
%makeinstall_std

desktop-file-install                               \
  --delete-original                                \
  --dir %{buildroot}%{_datadir}/applications    \
%{buildroot}%{_datadir}/applications/eom.desktop

%find_lang eom --with-gnome

# save space by linking identical images in translated docs
helpdir=%{buildroot}%{_datadir}/mate/help/%{name}
for f in $helpdir/C/figures/*.png; do
  b="$(basename $f)"
  for d in $helpdir/*; do
    if [ -d "$d" -a "$d" != "$helpdir/C" ]; then
      g="$d/figures/$b"
      if [ -f "$g" ]; then
        if cmp -s $f $g; then
          rm "$g"; ln -s "../../C/figures/$b" "$g"
        fi
      fi
    fi
  done
done

%post
/bin/touch --no-create %{_datadir}/mate-image-viewer/icons/hicolor >&/dev/null || :


%files -f eom.lang
%doc AUTHORS COPYING NEWS README
%{_mandir}/man1/*
%{_bindir}/eom
%{_libdir}/eom/plugins
%{_datadir}/applications/eom.desktop
#%{_datadir}/eom
%{_datadir}/mate/help/eom
%{_datadir}/icons/hicolor/*/apps/eom.*
%{_datadir}/glib-2.0/schemas/org.mate.eom.gschema.xml
%{_datadir}/MateConf/gsettings/eom.convert
%{_datadir}/gtk-doc/html/eom
%{_datadir}/mate-image-viewer

%files devel
%{_libdir}/pkgconfig/eom.pc
%{_includedir}/eom-2.20

