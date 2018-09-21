#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-font-viewer
Version  : 3.30.0
Release  : 16
URL      : https://download.gnome.org/sources/gnome-font-viewer/3.30/gnome-font-viewer-3.30.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-font-viewer/3.30/gnome-font-viewer-3.30.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-font-viewer-bin
Requires: gnome-font-viewer-data
Requires: gnome-font-viewer-license
Requires: gnome-font-viewer-locales
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gtk+-3.0)

%description
No detailed description available

%package bin
Summary: bin components for the gnome-font-viewer package.
Group: Binaries
Requires: gnome-font-viewer-data
Requires: gnome-font-viewer-license

%description bin
bin components for the gnome-font-viewer package.


%package data
Summary: data components for the gnome-font-viewer package.
Group: Data

%description data
data components for the gnome-font-viewer package.


%package license
Summary: license components for the gnome-font-viewer package.
Group: Default

%description license
license components for the gnome-font-viewer package.


%package locales
Summary: locales components for the gnome-font-viewer package.
Group: Default

%description locales
locales components for the gnome-font-viewer package.


%prep
%setup -q -n gnome-font-viewer-3.30.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535824615
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/doc/gnome-font-viewer
cp COPYING %{buildroot}/usr/share/doc/gnome-font-viewer/COPYING
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-font-viewer

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-font-viewer
/usr/bin/gnome-thumbnail-font

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.font-viewer.desktop
/usr/share/dbus-1/services/org.gnome.font-viewer.service
/usr/share/metainfo/org.gnome.font-viewer.appdata.xml
/usr/share/thumbnailers/gnome-font-viewer.thumbnailer

%files license
%defattr(-,root,root,-)
/usr/share/doc/gnome-font-viewer/COPYING

%files locales -f gnome-font-viewer.lang
%defattr(-,root,root,-)

