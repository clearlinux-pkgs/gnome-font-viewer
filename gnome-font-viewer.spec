#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-font-viewer
Version  : 3.24.0
Release  : 5
URL      : https://download.gnome.org/sources/gnome-font-viewer/3.24/gnome-font-viewer-3.24.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-font-viewer/3.24/gnome-font-viewer-3.24.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-font-viewer-bin
Requires: gnome-font-viewer-data
Requires: gnome-font-viewer-locales
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(harfbuzz)
BuildRequires : pkgconfig(libxml-2.0)

%description
No detailed description available

%package bin
Summary: bin components for the gnome-font-viewer package.
Group: Binaries
Requires: gnome-font-viewer-data

%description bin
bin components for the gnome-font-viewer package.


%package data
Summary: data components for the gnome-font-viewer package.
Group: Data

%description data
data components for the gnome-font-viewer package.


%package locales
Summary: locales components for the gnome-font-viewer package.
Group: Default

%description locales
locales components for the gnome-font-viewer package.


%prep
%setup -q -n gnome-font-viewer-3.24.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1493479825
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1493479825
rm -rf %{buildroot}
%make_install
%find_lang gnome-font-viewer

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-font-viewer
/usr/bin/gnome-thumbnail-font

%files data
%defattr(-,root,root,-)
/usr/share/appdata/org.gnome.font-viewer.appdata.xml
/usr/share/applications/org.gnome.font-viewer.desktop
/usr/share/dbus-1/services/org.gnome.font-viewer.service
/usr/share/thumbnailers/gnome-font-viewer.thumbnailer

%files locales -f gnome-font-viewer.lang
%defattr(-,root,root,-)

